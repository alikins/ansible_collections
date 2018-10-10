# Ansible module: ansible.module_na_elementsw_vlan


NetApp Element Software Manage VLAN

## Description

Create, delete, modify VLAN

## Requirements

TODO

## Arguments

``` json
{
    "address_blocks": "{'description': ['List of address blocks for the VLAN', 'Each address block contains the starting IP address and size for the block', 'Required for create']}",
    "attributes": "{'description': ['Dictionary of attributes with name and value for each attribute']}",
    "gateway": "{'description': ['Gateway for the VLAN']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['User defined name for the new VLAN', 'Name of the vlan is unique', 'Required for create']}",
    "namespace": "{'description': ['Enable or disable namespaces'], 'type': 'bool'}",
    "netmask": "{'description': ['Netmask for the VLAN', 'Required for create']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified vlan should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "svip": "{'description': ['Storage virtual IP which is unique', 'Required for create']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "vlan_tag": "{'description': ['Virtual Network Tag'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create vlan
  na_elementsw_vlan:
    state: present
    name: test
    vlan_tag: 1
    svip: "{{ ip address }}"
    netmask: "{{ netmask }}"
    address_blocks:
      - start: "{{ starting ip_address }}"
        size: 5
      - start: "{{ starting ip_address }}"
        size: 5
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete Lun
  na_elementsw_vlan:
    state: present
    vlan_tag: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
