# Ansible inventory: ansible.inventory_netbox


NetBox inventory source

## Description

Get inventory hosts from NetBox

## Requirements

TODO

## Arguments

``` json
{
    "api_endpoint": "{'description': ['Endpoint of the NetBox API'], 'required': True, 'env': [{'name': 'NETBOX_API'}]}",
    "group_by": "{'description': ['Keys used to create groups.'], 'type': 'list', 'choices': ['sites', 'tenants', 'racks', 'tags', 'device_roles', 'device_types', 'manufacturers'], 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'netbox' plugin."], 'required': True, 'choices': ['netbox']}",
    "query_filters": "{'description': ['List of parameters passed to the query string (Multiple values may be separated by commas)'], 'type': 'list'}",
    "timeout": "{'description': ['Timeout for Netbox requests in seconds'], 'type': 'int', 'default': 60}",
    "token": "{'required': True, 'description': ['NetBox token.'], 'env': [{'name': 'NETBOX_TOKEN'}, {'name': 'NETBOX_API_KEY'}]}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.'], 'default': True, 'type': 'boolean'}",
}
```

## Examples


``` yaml

# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml

plugin: netbox
api_endpoint: http://localhost:8000
group_by:
  - device_roles
query_filters:
  - role: network-edge-router

# Query filters are passed directly as an argument to the fetching queries.
# You can repeat tags in the query string.

query_filters:
  - role: server
  - tag: web
  - tag: production

# See the NetBox documentation at https://netbox.readthedocs.io/en/latest/api/overview/
# the query_filters work as a logical **OR**
#
# Prefix any custom fields with cf_ and pass the field value with the regular NetBox query string

query_filters:
  - cf_foo: bar

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)', 'Anthony Ruhier (@Anthony25)']
  - ['Remy Leone (@sieben)', 'Anthony Ruhier (@Anthony25)']
