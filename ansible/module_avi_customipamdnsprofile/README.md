# Ansible module: ansible.module_avi_customipamdnsprofile


Module for setup of CustomIpamDnsProfile Avi RESTful Object

## Description

This module is used to configure CustomIpamDnsProfile object
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
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "name": "{'description': ['Name of the custom ipam dns profile.', 'Field introduced in 17.1.1.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "script_params": "{'description': ['Parameters that are always passed to the ipam/dns script.', 'Field introduced in 17.1.1.']}",
    "script_uri": "{'description': ['Script uri of form controller //ipamdnsscripts/<file-name>.', 'Field introduced in 17.1.1.'], 'required': True}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.', 'Field introduced in 17.1.1.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Field introduced in 17.1.1.']}",
}
```

## Examples


``` yaml

- name: Example to create CustomIpamDnsProfile object
  avi_customipamdnsprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_customipamdnsprofile

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
