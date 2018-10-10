# Ansible module: ansible.module_ip_netns


Manage network namespaces

## Description

Create or delete network namespaces using the ip command.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'required': False, 'description': ['Name of the namespace']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the namespace should exist']}",
}
```

## Examples


``` yaml

# Create a namespace named mario
- name: Create a namespace named mario
  namespace:
    name: mario
    state: present
- name: Delete a namespace named luigi
  namespace:
    name: luigi
    state: absent

```

## License

TODO

## Author Information
  - ['Arie Bregman (@bregman-arie)']
