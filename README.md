# Azure -proposed

Check which of the packages included in Azure images currently have a version in RELEASE-proposed that differs from the one in RELEASE-updates (or RELEASE).

How to install:

```
pip install git+https://github.com/gjolly/ubuntu-azure-proposed.git
```

How to use it:

```
usage: ubuntu-azure-proposed [-h] [--series SERIES]

Finds which package from Ubuntu Azure images are in -proposed

options:
  -h, --help            show this help message and exit
  --series SERIES, -s SERIES
                        Restrict to a given series
```
