# Ansible module: ansible.module_avi_vsvip


Module for setup of VsVip Avi RESTful Object

## Description

This module is used to configure VsVip object
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
    "cloud_ref": "{'description': ['It is a reference to an object of type cloud.', 'Field introduced in 17.1.1.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "dns_info": "{'description': ['Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.', 'Field introduced in 17.1.1.']}",
    "east_west_placement": "{'description': ['Force placement on all service engines in the service engine group (container clouds only).', 'Field introduced in 17.1.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "name": "{'description': ['Name for the vsvip object.', 'Field introduced in 17.1.1.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.', 'Field introduced in 17.1.1.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the vsvip object.', 'Field introduced in 17.1.1.']}",
    "vip": "{'description': ['List of virtual service ips and other shareable entities.', 'Field introduced in 17.1.1.']}",
    "vrf_context_ref": "{'description': ['Virtual routing context that the virtual service is bound to.', 'This is used to provide the isolation of the set of networks the application is attached to.', 'It is a reference to an object of type vrfcontext.', 'Field introduced in 17.1.1.']}",
}
```

## Examples


``` yaml

- name: Example to create VsVip object
  avi_vsvip:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vsvip

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
