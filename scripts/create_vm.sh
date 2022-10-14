#!/bin/bash -eu

# This script is able to parse a JSON output produced by "azure-ubuntu-proposed -s SUITE -F json"
# it will create one VM per package in proposed, update the VM and installed the package from
# proposed.
# stderr shows logs info
# stdout is a list of CSV lines: PACKAGE,IP_ADDRESS
# more logs are available in $LOG_FILE

URN="$1"
JSON_FILE="$2"
LOCATION=${LOCATION:-'northeurope'}
SIZE="${VM_SIZE:-Standard_D4as_v5}"
RG_NAME='test-proposed'
LOG_FILE="/tmp/$RG_NAME.log"

packages=$(jq -r '.[].package' "$JSON_FILE")

function error() {
  "Failed, see logs in $LOG_FILE" >&2
}

trap error EXIT

echo "Creating resource group $RG_NAME" >&2
az group create --location "$LOCATION" --resource-group "$RG_NAME" &> "$LOG_FILE"

echo "Creating vnets" >&2
az network vnet create \
  --resource-group "$RG_NAME" \
  --name "$RG_NAME-vnet" \
  --address-prefix 10.0.0.0/16 \
  --subnet-name "$RG_NAME-subnet" \
  --subnet-prefix 10.0.0.0/24 &> "$LOG_FILE"

for package in $packages; do
  echo "Creating VM for $package" >&2

  ip_addr=$(az vm create --resource-group "$RG_NAME" \
   --name "vm-$package" \
   --image "$URN" \
   --size "$SIZE" \
   --subnet "$RG_NAME-subnet" \
   --vnet-name "$RG_NAME-vnet" \
   --admin-username ubuntu \
   --ssh-key-value "$SSH_KEY" 2> /dev/null | jq -r '.publicIpAddress')

  echo "Updating VM for $package" >&2
  ssh -o "StrictHostKeyChecking no" -i "$SSH_KEY" "ubuntu@$ip_addr" 'sudo apt-get update && sudo apt-get upgrade -y' &> "$LOG_FILE"

  echo "Enabling proposed on VM for $package" >&2
  ssh -o "StrictHostKeyChecking no" -i "$SSH_KEY" "ubuntu@$ip_addr" 'echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-proposed main restricted universe" | sudo tee /etc/apt/sources.list.d/proposed.list' &> "$LOG_FILE"
  # shellcheck disable=SC2029
  echo "Installing $package" >&2
  ssh -o "StrictHostKeyChecking no" -i "$SSH_KEY" "ubuntu@$ip_addr" "sudo apt-get update && sudo apt-get install -y $package" &> "$LOG_FILE"

  echo "$package,ubuntu@$ip_addr"
done

trap - EXIT
