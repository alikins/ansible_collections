# Ansible module: ansible.module_avi_poolgroup


Module for setup of PoolGroup Avi RESTful Object

## Description

This module is used to configure PoolGroup object
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
    "cloud_config_cksum": "{'description': ['Checksum of cloud configuration for poolgroup.', 'Internally set by cloud connector.']}",
    "cloud_ref": "{'description': ['It is a reference to an object of type cloud.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "created_by": "{'description': ['Name of the user who created the object.']}",
    "deployment_policy_ref": "{'description': ['When setup autoscale manager will automatically promote new pools into production when deployment goals are met.', 'It is a reference to an object of type poolgroupdeploymentpolicy.']}",
    "description": "{'description': ['Description of pool group.']}",
    "fail_action": "{'description': ['Enable an action - close connection, http redirect, or local http response - when a pool group failure happens.', 'By default, a connection will be closed, in case the pool group experiences a failure.']}",
    "implicit_priority_labels": "{'description': ['Whether an implicit set of priority labels is generated.', 'Field introduced in 17.1.9,17.2.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.5', 'type': 'bool'}",
    "members": "{'description': ['List of pool group members object of type poolgroupmember.']}",
    "min_servers": "{'description': ['The minimum number of servers to distribute traffic to.', 'Allowed values are 1-65535.', "Special values are 0 - 'disable'.", 'Default value when not specified in API or module is interpreted by Avi Controller as 0.']}",
    "name": "{'description': ['The name of the pool group.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "priority_labels_ref": "{'description': ['Uuid of the priority labels.', 'If not provided, pool group member priority label will be interpreted as a number with a larger number considered higher priority.', 'It is a reference to an object of type prioritylabels.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the pool group.']}",
}
```

## Examples


``` yaml

- name: Example to create PoolGroup object
  avi_poolgroup:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_poolgroup

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
