# Ansible module: ansible.module_panos_object


create/read/update/delete object in PAN-OS or Panorama

## Description

Policy objects form the match criteria for policy rules and many other functions in PAN-OS. These may include address object, address groups, service objects, service groups, and tag.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The IP address of the host or network in CIDR notation.']}",
    "address_type": "{'description': ['The type of address object definition.  Valid types are I(ip-netmask) and I(ip-range).']}",
    "addressgroup": "{'description': ['A static group of address objects or dynamic address group.']}",
    "addressobject": "{'description': ['The name of the address object.']}",
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "color": "{'description': ['- The color of the tag object.  Valid values are I(red, green, blue, yellow, copper, orange, purple, gray, light green, cyan, light gray, blue gray, lime, black, gold, and brown).\n']}",
    "description": "{'description': ['The description of the object.']}",
    "destination_port": "{'description': ['The destination port to be used in a service object definition.']}",
    "devicegroup": "{'description': ['- The name of the Panorama device group. The group must exist on Panorama. If device group is not defined it is assumed that we are contacting a firewall.\n']}",
    "dynamic_value": "{'description': ['The filter match criteria to be used in a dynamic addressgroup definition.']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device or Panorama management console being configured.'], 'required': True}",
    "operation": "{'description': ['The operation to be performed.  Supported values are I(add)/I(delete)/I(find).'], 'required': True}",
    "password": "{'description': ['Password credentials to use for authentication.'], 'required': True}",
    "protocol": "{'description': ['The IP protocol to be used in a service object definition.  Valid values are I(tcp) or I(udp).']}",
    "servicegroup": "{'description': ['A group of service objects.']}",
    "serviceobject": "{'description': ['The name of the service object.']}",
    "services": "{'description': ['The group of service objects used in a servicegroup definition.']}",
    "source_port": "{'description': ['The source port to be used in a service object definition.']}",
    "static_value": "{'description': ['A group of address objects to be used in an addressgroup definition.']}",
    "tag_name": "{'description': ['The name of an object or rule tag.']}",
    "username": "{'description': ['Username credentials to use for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: search for shared address object
  panos_object:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    operation: 'find'
    address: 'DevNet'

- name: create an address group in devicegroup using API key
  panos_object:
    ip_address: '{{ ip_address }}'
    api_key: '{{ api_key }}'
    operation: 'add'
    addressgroup: 'Prod_DB_Svrs'
    static_value: ['prod-db1', 'prod-db2', 'prod-db3']
    description: 'Production DMZ database servers'
    tag_name: 'DMZ'
    devicegroup: 'DMZ Firewalls'

- name: create a global service for TCP 3306
  panos_object:
    ip_address: '{{ ip_address }}'
    api_key: '{{ api_key }}'
    operation: 'add'
    serviceobject: 'mysql-3306'
    destination_port: '3306'
    protocol: 'tcp'
    description: 'MySQL on tcp/3306'

- name: create a global tag
  panos_object:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    operation: 'add'
    tag_name: 'ProjectX'
    color: 'yellow'
    description: 'Associated with Project X'

- name: delete an address object from a devicegroup using API key
  panos_object:
    ip_address: '{{ ip_address }}'
    api_key: '{{ api_key }}'
    operation: 'delete'
    addressobject: 'Win2K test'

```

## License

TODO

## Author Information
  - ['Bob Hagen (@rnh556)']
