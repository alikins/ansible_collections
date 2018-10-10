# Ansible module: ansible.module_panos_dag_tags


Create tags for DAG's on PAN-OS devices

## Description

Create the ip address to tag associations. Tags will in turn be used to create DAG's

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "commit": "{'description': ['commit if changed'], 'default': True}",
    "description": "{'description': ['The purpose / objective of the static Address Group']}",
    "devicegroup": "{'description': ['- Device groups are used for the Panorama interaction with Firewall(s). The group must exists on Panorama. If device group is not define we assume that we are contacting Firewall.\n']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "ip_to_register": "{'description': ['IP that will be registered with the given tag names.']}",
    "operation": "{'description': ['The action to be taken. Supported values are I(add)/I(update)/I(find)/I(delete).']}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "tag_names": "{'description': ['The list of the tags that will be added or removed from the IP address.']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Create the tags to map IP addresses
  panos_dag_tags:
    ip_address: "{{ ip_address }}"
    password: "{{ password }}"
    ip_to_register: "{{ ip_to_register }}"
    tag_names: "{{ tag_names }}"
    description: "Tags to allow certain IP's to access various SaaS Applications"
    operation: 'add'
  tags: "adddagip"

- name: List the IP address to tag mapping
  panos_dag_tags:
    ip_address: "{{ ip_address }}"
    password: "{{ password }}"
    tag_names: "{{ tag_names }}"
    description: "List the IP address to tag mapping"
    operation: 'list'
  tags: "listdagip"

- name: Unregister an IP address from a tag mapping
  panos_dag_tags:
    ip_address: "{{ ip_address }}"
    password: "{{ password }}"
    ip_to_register: "{{ ip_to_register }}"
    tag_names: "{{ tag_names }}"
    description: "Unregister IP address from tag mappings"
    operation: 'delete'
  tags: "deletedagip"

```

## License

TODO

## Author Information
  - ['Vinay Venkataraghavan (@vinayvenkat)']
