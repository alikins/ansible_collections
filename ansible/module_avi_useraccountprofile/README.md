# Ansible module: ansible.module_avi_useraccountprofile


Module for setup of UserAccountProfile Avi RESTful Object

## Description

This module is used to configure UserAccountProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "account_lock_timeout": "{'description': ['Lock timeout period (in minutes).', 'Default is 30 minutes.', 'Default value when not specified in API or module is interpreted by Avi Controller as 30.', 'Units(MIN).']}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "credentials_timeout_threshold": "{'description': ['The time period after which credentials expire.', 'Default is 180 days.', 'Default value when not specified in API or module is interpreted by Avi Controller as 180.', 'Units(DAYS).']}",
    "max_concurrent_sessions": "{'description': ['Maximum number of concurrent sessions allowed.', 'There are unlimited sessions by default.', 'Default value when not specified in API or module is interpreted by Avi Controller as 0.']}",
    "max_login_failure_count": "{'description': ['Number of login attempts before lockout.', 'Default is 3 attempts.', 'Default value when not specified in API or module is interpreted by Avi Controller as 3.']}",
    "max_password_history_count": "{'description': ['Maximum number of passwords to be maintained in the password history.', 'Default is 4 passwords.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.']}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

- name: Example to create UserAccountProfile object
  avi_useraccountprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_useraccountprofile

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
