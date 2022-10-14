import argparse
import gzip
import sys
from enum import Enum
from typing import Tuple

import requests
from prettytable import PrettyTable


def parse_package_file(file: str) -> dict[str, str]:
    result = dict()
    lines = file.splitlines(keepends=False)
    for line in lines:
        try:
            key, value = line.split(": ")
        except ValueError:
            continue

        if key == "Package":
            current_package_name = value
        if key == "Version":
            result[current_package_name] = value

    return result


def download_package_file(suite: str, component: str, pocket: str) -> str:
    formated_pocket = ""
    if pocket != "Release":
        formated_pocket = "-" + pocket.lower()

    url = f"http://archive.ubuntu.com/ubuntu/dists/{suite}{formated_pocket}/{component}/binary-amd64/Packages.gz"
    resp = requests.get(url)
    resp.raise_for_status()

    return gzip.decompress(resp.content).decode("utf-8")


def get_package_index_for_suite(suite: str) -> dict[str, dict[str, str]]:
    components = ["main", "universe"]
    pockets = ["Release", "Proposed", "Updates"]
    index: dict[str, dict[str, str]] = {"Release": {}, "Proposed": {}, "Updates": {}}

    for pocket in pockets:
        for component in components:
            package_file = download_package_file(suite, component, pocket)
            component_index = parse_package_file(package_file)
            index[pocket].update(component_index)

    return index


def download_manifest(url: str) -> str:
    resp = requests.get(url)

    resp.raise_for_status()
    return resp.text


def parse_manifest(manifest: str) -> dict[str, str]:
    packages = {}
    for line in manifest.splitlines():
        try:
            name, version = line.split()
        except ValueError:
            # this is a snap, we don't care for now
            continue
        packages[name] = version
    return packages


def get_suites() -> list[Tuple[str, str]]:
    return [("bionic", "18.04"), ("focal", "20.04"), ("jammy", "22.04")]


def get_manifest_urls() -> dict[Tuple[str, str], str]:
    urls: dict[Tuple[str, str], str] = dict()
    for suite in get_suites():
        urls[
            suite
        ] = f"http://cloud-images.ubuntu.com/releases/{suite[0]}/release/ubuntu-{suite[1]}-server-cloudimg-amd64-azure.vhd.manifest"  # noqa: E501

    return urls


def get_package_version(index: dict[str, dict[str, str]], package: str, pocket: str) -> str:

    return index[pocket].get(package, "")


def get_current_version(index: dict[str, dict[str, str]], package: str, arch: str = "amd64") -> str:
    updates_version = get_package_version(index, package, "Updates")

    if len(updates_version) > 0:
        return updates_version

    release_version = get_package_version(index, package, "Release")
    return release_version


def compare_package_versions(index: dict[str, dict[str, str]], package: str, suite: str) -> list[str]:
    current_version = get_current_version(index, package)
    proposed_version = get_package_version(index, package, "Proposed")

    if proposed_version != "" and current_version != proposed_version:
        return [package, suite, current_version, proposed_version]

    return []


class Format(str, Enum):
    TABLE = ("table",)
    JSON = "json"


def print_results(results, fmt: Format = Format.TABLE) -> None:
    table = PrettyTable()
    table.align = "l"
    table.field_names = ["package", "series", "current", "proposed"]

    for result in results:
        table.add_row(result)

    if fmt == Format.TABLE:
        print(table)
    elif fmt == Format.JSON:
        table.header = False
        print(table.get_json_string())


def main() -> None:
    parser = argparse.ArgumentParser(description="Finds which package from Ubuntu Azure images are in -proposed")
    parser.add_argument("--series", "-s", dest="series", help="Restrict to a given series")
    parser.add_argument("--format", "-F", choices=[f.value for f in Format], dest="format", help="Output format")
    args = parser.parse_args()

    results: list[list[str]] = list()

    for (suite, _), url in get_manifest_urls().items():
        if args.series is not None and suite != args.series:
            continue

        manifest = download_manifest(url)
        packages = parse_manifest(manifest)

        print(f"building index for {suite}...", file=sys.stderr)
        index = get_package_index_for_suite(suite)

        print(f"scanning {suite} from {url}...", file=sys.stderr)
        for package in packages:
            diff = compare_package_versions(index, package, suite)
            if len(diff) != 0:
                results.append(diff)

    print_results(results, args.format)


if __name__ == "__main__":
    main()
