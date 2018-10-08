# Ansible inventory: ansible.inventory_gcp_compute


Google Cloud Compute Engine inventory source

## Description

Get inventory hosts from Google Cloud Platform GCE.
Uses a <name>.gcp.yaml (or <name>.gcp.yml) YAML configuration file.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.']}",
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "filters": "{'description': ['A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/compute/docs/reference/rest/v1/instances/list). Each additional filter in the list will act be added as an AND condition (filter1 and filter2)\n']}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "hostnames": "{'description': ["A list of options that describe the ordering for which hostnames should be assigned. Currently supported hostnames are 'public_ip', 'private_ip', or 'name'."], 'default': ['public_ip', 'private_ip', 'name']}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'gcp_compute' plugin."], 'required': True, 'choices': ['gcp_compute']}",
    "projects": "{'description': ['A list of projects in which to describe GCE instances.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
    "zones": "{'description': ['A list of regions in which to describe GCE instances.'], 'default': 'all zones available to a given project'}",
}
```

## Examples


``` yaml

plugin: gcp_compute
zones: # populate inventory with instances in these regions
  - us-east1-a
projects:
  - gcp-prod-gke-100
  - gcp-cicd-101
filters:
  - machineType = n1-standard-1
  - scheduling.automaticRestart = true AND machineType = n1-standard-1
scopes:
  - https://www.googleapis.com/auth/compute
service_account_file: /tmp/service_account.json
auth_kind: serviceaccount
keyed_groups:
  # Create groups from GCE labels
  - prefix: gcp
    key: labels
hostnames:
  # List host by name instead of the default public ip
  - name
compose:
  # Set an inventory parameter to use the Public IP address to connect to the host
  # For Private ip use "networkInterfaces[0].networkIP"
  ansible_host: networkInterfaces[0].accessConfigs[0].natIP

```

## License

TODO

## Author Information
  - ['UNKNOWN']
