# Ansible module: ansible.module_avi_vsdatascriptset


Module for setup of VSDataScriptSet Avi RESTful Object

## Description

This module is used to configure VSDataScriptSet object
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
    "created_by": "{'description': ['Creator name.', 'Field introduced in 17.1.11,17.2.4.'], 'version_added': '2.5'}",
    "datascript": "{'description': ['Datascripts to execute.']}",
    "description": "{'description': ['User defined description for the object.']}",
    "ipgroup_refs": "{'description': ['Uuid of ip groups that could be referred by vsdatascriptset objects.', 'It is a reference to an object of type ipaddrgroup.']}",
    "name": "{'description': ['Name for the virtual service datascript collection.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "pool_group_refs": "{'description': ['Uuid of pool groups that could be referred by vsdatascriptset objects.', 'It is a reference to an object of type poolgroup.']}",
    "pool_refs": "{'description': ['Uuid of pools that could be referred by vsdatascriptset objects.', 'It is a reference to an object of type pool.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "string_group_refs": "{'description': ['Uuid of string groups that could be referred by vsdatascriptset objects.', 'It is a reference to an object of type stringgroup.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the virtual service datascript collection.']}",
}
```

## Examples


``` yaml

- name: Example to create VSDataScriptSet object
  avi_vsdatascriptset:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vsdatascriptset

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
