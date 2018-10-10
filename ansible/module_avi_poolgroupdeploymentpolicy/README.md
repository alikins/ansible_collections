# Ansible module: ansible.module_avi_poolgroupdeploymentpolicy


Module for setup of PoolGroupDeploymentPolicy Avi RESTful Object

## Description

This module is used to configure PoolGroupDeploymentPolicy object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "auto_disable_old_prod_pools": "{'description': ['It will automatically disable old production pools once there is a new production candidate.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "cloud_ref": "{'description': ['It is a reference to an object of type cloud.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "evaluation_duration": "{'description': ['Duration of evaluation period for automatic deployment.', 'Allowed values are 60-86400.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "name": "{'description': ['The name of the pool group deployment policy.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "rules": "{'description': ['List of pgdeploymentrule.']}",
    "scheme": "{'description': ['Deployment scheme.', 'Enum options - BLUE_GREEN, CANARY.', 'Default value when not specified in API or module is interpreted by Avi Controller as BLUE_GREEN.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "target_test_traffic_ratio": "{'description': ['Target traffic ratio before pool is made production.', 'Allowed values are 1-100.', 'Default value when not specified in API or module is interpreted by Avi Controller as 100.', 'Units(RATIO).']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "test_traffic_ratio_rampup": "{'description': ['Ratio of the traffic that is sent to the pool under test.', 'Test ratio of 100 means blue green.', 'Allowed values are 1-100.', 'Default value when not specified in API or module is interpreted by Avi Controller as 100.']}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the pool group deployment policy.']}",
    "webhook_ref": "{'description': ['Webhook configured with url that avi controller will pass back information about pool group, old and new pool information and current deployment', 'rule results.', 'It is a reference to an object of type webhook.', 'Field introduced in 17.1.1.']}",
}
```

## Examples


``` yaml

- name: Example to create PoolGroupDeploymentPolicy object
  avi_poolgroupdeploymentpolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_poolgroupdeploymentpolicy

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
