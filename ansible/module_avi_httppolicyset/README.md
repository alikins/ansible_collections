# Ansible module: ansible.module_avi_httppolicyset


Module for setup of HTTPPolicySet Avi RESTful Object

## Description

This module is used to configure HTTPPolicySet object
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
    "cloud_config_cksum": "{'description': ['Checksum of cloud configuration for pool.', 'Internally set by cloud connector.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "created_by": "{'description': ['Creator name.']}",
    "description": "{'description': ['User defined description for the object.']}",
    "http_request_policy": "{'description': ['Http request policy for the virtual service.']}",
    "http_response_policy": "{'description': ['Http response policy for the virtual service.']}",
    "http_security_policy": "{'description': ['Http security policy for the virtual service.']}",
    "is_internal_policy": "{'description': ['Boolean flag to set is_internal_policy.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the http policy set.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the http policy set.']}",
}
```

## Examples


``` yaml

- name: Create a HTTP Policy set two switch between testpool1 and testpool2
  avi_httppolicyset:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    name: test-HTTP-Policy-Set
    tenant_ref: admin
    http_request_policy:
    rules:
      - index: 1
        enable: true
        name: test-test1
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test1
            match_criteria: EQUALS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool1"
      - index: 2
        enable: true
        name: test-test2
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test2
            match_criteria: CONTAINS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool2"
    is_internal_policy: false

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
