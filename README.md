# Azure -proposed

## Python tool

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

Example output:

```
$ ubuntu-azure-proposed
building index for bionic...
scanning bionic from http://cloud-images.ubuntu.com/releases/bionic/release/ubuntu-18.04-server-cloudimg-amd64-azure.vhd.manifest...
building index for focal...
scanning focal from http://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64-azure.vhd.manifest...
building index for jammy...
scanning jammy from http://cloud-images.ubuntu.com/releases/jammy/release/ubuntu-22.04-server-cloudimg-amd64-azure.vhd.manifest...
+---------------------------+--------+----------------------------------+----------------------------------+
| package                   | series | current                          | proposed                         |
+---------------------------+--------+----------------------------------+----------------------------------+
| apt                       | bionic | 1.6.14                           | 1.6.17                           |
| apt-utils                 | bionic | 1.6.14                           | 1.6.17                           |
| cloud-init                | bionic | 22.2-0ubuntu1~18.04.3            | 22.3.3-0ubuntu1~18.04.1          |
| grub-efi-amd64-bin        | bionic | 2.04-1ubuntu44.1.2               | 2.04-1ubuntu47.4                 |
| grub-efi-amd64-signed     | bionic | 1.167~18.04.5+2.04-1ubuntu44.1.2 | 1.173.2~18.04.1+2.04-1ubuntu47.4 |
| libx11-data               | bionic | 2:1.6.4-3ubuntu0.4               | 2:1.6.4-3ubuntu0.5               |
| linux-azure               | bionic | 5.4.0.1091.68                    | 5.4.0.1092.69                    |
| linux-cloud-tools-azure   | bionic | 5.4.0.1091.68                    | 5.4.0.1092.69                    |
| linux-cloud-tools-common  | bionic | 4.15.0-99.100                    | 4.15.0-194.205                   |
| linux-headers-azure       | bionic | 5.4.0.1091.68                    | 5.4.0.1092.69                    |
| linux-image-azure         | bionic | 5.4.0.1091.68                    | 5.4.0.1092.69                    |
| linux-tools-azure         | bionic | 5.4.0.1091.68                    | 5.4.0.1092.69                    |
| linux-tools-common        | bionic | 4.15.0-99.100                    | 4.15.0-194.205                   |
| parted                    | bionic | 3.2-20ubuntu0.2                  | 3.2-20ubuntu0.3                  |
| python3-update-manager    | bionic | 1:18.04.11.13                    | 1:18.04.11.14                    |
| secureboot-db             | bionic | 1.4~ubuntu0.18.04.1              | 1.4.1                            |
| ubuntu-advantage-tools    | bionic | 27.10.1~18.04.1                  | 27.11.1~18.04.1                  |
| unattended-upgrades       | bionic | 1.1ubuntu1.18.04.14              | 1.1ubuntu1.18.04.15              |
| update-manager-core       | bionic | 1:18.04.11.13                    | 1:18.04.11.14                    |
| update-notifier-common    | bionic | 3.192.1.12                       | 3.192.1.14                       |
| cloud-init                | focal  | 22.2-0ubuntu1~20.04.3            | 22.3.3-0ubuntu1~20.04.1          |
| dmeventd                  | focal  | 2:1.02.167-1ubuntu1              | 2:1.02.167-1ubuntu1.1            |
| dmsetup                   | focal  | 2:1.02.167-1ubuntu1              | 2:1.02.167-1ubuntu1.1            |
| grub-efi-amd64-bin        | focal  | 2.04-1ubuntu44.2                 | 2.04-1ubuntu47.4                 |
| grub-efi-amd64-signed     | focal  | 1.167.2+2.04-1ubuntu44.2         | 1.173.2~20.04.1+2.04-1ubuntu47.4 |
| libdrm-common             | focal  | 2.4.107-8ubuntu1~20.04.2         | 2.4.110-1ubuntu1~20.04.1         |
| libx11-data               | focal  | 2:1.6.9-2ubuntu1.2               | 2:1.6.9-2ubuntu1.3               |
| linux-azure               | focal  | 5.15.0.1020.25~20.04.13          | 5.15.0.1021.26~20.04.14          |
| linux-cloud-tools-azure   | focal  | 5.15.0.1020.25~20.04.13          | 5.15.0.1021.26~20.04.14          |
| linux-cloud-tools-common  | focal  | 5.4.0-99.112                     | 5.4.0-128.144                    |
| linux-headers-azure       | focal  | 5.15.0.1020.25~20.04.13          | 5.15.0.1021.26~20.04.14          |
| linux-image-azure         | focal  | 5.15.0.1020.25~20.04.13          | 5.15.0.1021.26~20.04.14          |
| linux-tools-azure         | focal  | 5.15.0.1020.25~20.04.13          | 5.15.0.1021.26~20.04.14          |
| linux-tools-common        | focal  | 5.4.0-99.112                     | 5.4.0-128.144                    |
| lvm2                      | focal  | 2.03.07-1ubuntu1                 | 2.03.07-1ubuntu1.1               |
| openssh-client            | focal  | 1:8.2p1-4ubuntu0.5               | 1:8.2p1-4ubuntu0.6               |
| openssh-server            | focal  | 1:8.2p1-4ubuntu0.5               | 1:8.2p1-4ubuntu0.6               |
| openssh-sftp-server       | focal  | 1:8.2p1-4ubuntu0.5               | 1:8.2p1-4ubuntu0.6               |
| secureboot-db             | focal  | 1.5                              | 1.6~20.04.1                      |
| ubuntu-advantage-tools    | focal  | 27.10.1~20.04.1                  | 27.11.1~20.04.1                  |
| update-notifier-common    | focal  | 3.192.30.11                      | 3.192.30.13                      |
| apt                       | jammy  | 2.4.7                            | 2.4.8                            |
| apt-utils                 | jammy  | 2.4.7                            | 2.4.8                            |
| binutils                  | jammy  | 2.38-3ubuntu1                    | 2.38-4ubuntu2                    |
| binutils-x86-64-linux-gnu | jammy  | 2.38-3ubuntu1                    | 2.38-4ubuntu2                    |
| cloud-init                | jammy  | 22.2-0ubuntu1~22.04.3            | 22.3.3-0ubuntu1~22.04.1          |
| grub-efi-amd64-bin        | jammy  | 2.06-2ubuntu7                    | 2.06-2ubuntu10                   |
| grub-efi-amd64-signed     | jammy  | 1.180+2.06-2ubuntu7              | 1.182~22.04.1+2.06-2ubuntu10     |
| linux-azure               | jammy  | 5.15.0.1020.19                   | 5.15.0.1021.20                   |
| linux-cloud-tools-azure   | jammy  | 5.15.0.1020.19                   | 5.15.0.1021.20                   |
| linux-cloud-tools-common  | jammy  | 5.15.0-48.54                     | 5.15.0-50.56                     |
| linux-headers-azure       | jammy  | 5.15.0.1020.19                   | 5.15.0.1021.20                   |
| linux-image-azure         | jammy  | 5.15.0.1020.19                   | 5.15.0.1021.20                   |
| linux-tools-azure         | jammy  | 5.15.0.1020.19                   | 5.15.0.1021.20                   |
| linux-tools-common        | jammy  | 5.15.0-48.54                     | 5.15.0-50.56                     |
| sudo                      | jammy  | 1.9.9-1ubuntu2                   | 1.9.9-1ubuntu2.1                 |
| ubuntu-advantage-tools    | jammy  | 27.10.1~22.04.1                  | 27.11.1~22.04.1                  |
| update-notifier-common    | jammy  | 3.192.54                         | 3.192.54.2                       |
+---------------------------+--------+----------------------------------+----------------------------------+
```

## Helper script

`./script/create_vms.sh` is able to parse a JSON file produced by `azure-ubuntu-proposed` and to create one VM per package. Each VM is created from the provided image, updated (using apt-get upgrade) and get a given package from -proposed installed on it. A CSV formated list of strings is returned to let the user run tests on the VMs.

Usage:
```
SSH_KEY=PATH_TO_PUBLIC_KEY ./scripts/create_vm.sh IMAGE_URN PATH_TO_JSON_FILE
```

Example:
```
azure-ubuntu-proposed -s jammy -F json > packages.json
SSH_KEY=~/.ssh/id_rsa.pub ./scripts/create_vm.sh 'Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest' packages.json
```
