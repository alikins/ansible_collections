# Ansible module: ansible.module_aos_blueprint_param


Manage AOS blueprint parameter values

## Description

Apstra AOS Blueprint Parameter module let you manage your Blueprint Parameter easily. You can create access, define and delete Blueprint Parameter. The list of Parameters supported is different per Blueprint. The option I(get_param_list) can help you to access the list of supported Parameters for your blueprint. This module is idempotent and support the I(check) mode. It's using the AOS REST API.

## Requirements

TODO

## Arguments

``` json
{
    "blueprint": "{'description': ['Blueprint Name or Id as defined in AOS.'], 'required': True}",
    "get_param_list": "{'description': ['Get the complete list of supported parameters for this blueprint and the description of those parameters.']}",
    "name": "{'description': ['Name of blueprint parameter, as defined by AOS design template. You can use the option I(get_param_list) to get the complete list of supported parameters for your blueprint.']}",
    "param_map": "{'description': ['Defines the aos-pyez collection that will is used to map the user-defined item name into the AOS unique ID value.  For example, if the caller provides an IP address pool I(param_value) called "Server-IpAddrs", then the aos-pyez collection is \'IpPools\'. Some I(param_map) are already defined by default like I(logical_device_maps).']}",
    "session": "{'description': ['An existing AOS session as obtained by M(aos_login) module.'], 'required': True}",
    "state": "{'description': ['Indicate what is the expected state of the Blueprint Parameter (present or not).'], 'default': 'present', 'choices': ['present', 'absent']}",
    "value": "{'description': ['Blueprint parameter value.  This value may be transformed by using the I(param_map) field; used when the blueprint parameter requires an AOS unique ID value.']}",
}
```

## Examples


``` yaml


- name: Add Logical Device Maps information in a Blueprint
  aos_blueprint_param:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    name: "logical_device_maps"
    value:
      spine_1: CumulusVX-Spine-Switch
      spine_2: CumulusVX-Spine-Switch
      leaf_1: CumulusVX-Leaf-Switch
      leaf_2: CumulusVX-Leaf-Switch
      leaf_3: CumulusVX-Leaf-Switch
    state: present

- name: Access Logical Device Maps information from a Blueprint
  aos_blueprint_param:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    name: "logical_device_maps"
    state: present

- name: Reset Logical Device Maps information in a Blueprint
  aos_blueprint_param:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    name: "logical_device_maps"
    state: absent

- name: Get list of all supported Params for a blueprint
  aos_blueprint_param:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    get_param_list: yes
  register: params_list
- debug: var=params_list

- name: Add Resource Pools information in a Blueprint, by providing a param_map
  aos_blueprint_param:
    session: "{{ aos_session }}"
    blueprint: "my-blueprint-l2"
    name: "resource_pools"
    value:
        leaf_loopback_ips: ['Switches-IpAddrs']
        spine_loopback_ips: ['Switches-IpAddrs']
        spine_leaf_link_ips: ['Switches-IpAddrs']
        spine_asns: ['Private-ASN-pool']
        leaf_asns: ['Private-ASN-pool']
        virtual_network_svi_subnets: ['Servers-IpAddrs']
    param_map:
        leaf_loopback_ips: IpPools
        spine_loopback_ips: IpPools
        spine_leaf_link_ips: IpPools
        spine_asns: AsnPools
        leaf_asns: AsnPools
        virtual_network_svi_subnets: IpPools
    state: present

```

## License

TODO

## Author Information
  - ['jeremy@apstra.com (@jeremyschulman)']
