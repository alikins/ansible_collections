# Ansible module: ansible.module_avi_network


Module for setup of Network Avi RESTful Object

## Description

This module is used to configure Network object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "cloud_ref": "{'description': ['It is a reference to an object of type cloud.']}",
    "configured_subnets": "{'description': ['List of subnet.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "dhcp_enabled": "{'description': ['Select the ip address management scheme for this network.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "exclude_discovered_subnets": "{'description': ['When selected, excludes all discovered subnets in this network from consideration for virtual service placement.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "synced_from_se": "{'description': ['Boolean flag to set synced_from_se.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
    "vcenter_dvs": "{'description': ['Boolean flag to set vcenter_dvs.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "vimgrnw_ref": "{'description': ['It is a reference to an object of type vimgrnwruntime.']}",
    "vrf_context_ref": "{'description': ['It is a reference to an object of type vrfcontext.']}",
}
```

## Examples


``` yaml

- name: Example to create Network object
  avi_network:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_network

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
