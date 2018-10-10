# Ansible module: ansible.module_avi_errorpageprofile


Module for setup of ErrorPageProfile Avi RESTful Object

## Description

This module is used to configure ErrorPageProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "app_name": "{'description': ['Name of the virtual service which generated the error page.', 'Field introduced in 17.2.4.', 'Default value when not specified in API or module is interpreted by Avi Controller as VS Name.']}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "company_name": "{'description': ['Name of the company to show in error page.', 'Field introduced in 17.2.4.', 'Default value when not specified in API or module is interpreted by Avi Controller as Avi Networks.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "error_pages": "{'description': ['Defined error pages for http status codes.', 'Field introduced in 17.2.4.']}",
    "host_name": "{'description': ['Fully qualified domain name for which the error page is generated.', 'Field introduced in 17.2.4.', 'Default value when not specified in API or module is interpreted by Avi Controller as Host Header.']}",
    "name": "{'description': ['Field introduced in 17.2.4.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.', 'Field introduced in 17.2.4.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Field introduced in 17.2.4.']}",
}
```

## Examples


``` yaml

- name: Example to create ErrorPageProfile object
  avi_errorpageprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_errorpageprofile

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
