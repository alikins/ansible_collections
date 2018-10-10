# Ansible module: ansible.module_avi_gslbapplicationpersistenceprofile


Module for setup of GslbApplicationPersistenceProfile Avi RESTful Object

## Description

This module is used to configure GslbApplicationPersistenceProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['Field introduced in 17.1.1.']}",
    "name": "{'description': ['A user-friendly name for the persistence profile.', 'Field introduced in 17.1.1.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.', 'Field introduced in 17.1.1.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the persistence profile.', 'Field introduced in 17.1.1.']}",
}
```

## Examples


``` yaml

- name: Example to create GslbApplicationPersistenceProfile object
  avi_gslbapplicationpersistenceprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_gslbapplicationpersistenceprofile

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
