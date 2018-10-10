# Ansible module: ansible.module_avi_applicationpersistenceprofile


Module for setup of ApplicationPersistenceProfile Avi RESTful Object

## Description

This module is used to configure ApplicationPersistenceProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "app_cookie_persistence_profile": "{'description': ['Specifies the application cookie persistence profile parameters.']}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "hdr_persistence_profile": "{'description': ['Specifies the custom http header persistence profile parameters.']}",
    "http_cookie_persistence_profile": "{'description': ['Specifies the http cookie persistence profile parameters.']}",
    "ip_persistence_profile": "{'description': ['Specifies the client ip persistence profile parameters.']}",
    "is_federated": "{'description': ["This field describes the object's replication scope.", 'If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.', 'If the field is set to true, then the object is replicated across the federation.', 'Field introduced in 17.1.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.4', 'type': 'bool'}",
    "name": "{'description': ['A user-friendly name for the persistence profile.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "persistence_type": "{'description': ['Method used to persist clients to the same server for a duration of time or a session.', 'Enum options - PERSISTENCE_TYPE_CLIENT_IP_ADDRESS, PERSISTENCE_TYPE_HTTP_COOKIE, PERSISTENCE_TYPE_TLS, PERSISTENCE_TYPE_CLIENT_IPV6_ADDRESS,', 'PERSISTENCE_TYPE_CUSTOM_HTTP_HEADER, PERSISTENCE_TYPE_APP_COOKIE, PERSISTENCE_TYPE_GSLB_SITE.', 'Default value when not specified in API or module is interpreted by Avi Controller as PERSISTENCE_TYPE_CLIENT_IP_ADDRESS.'], 'required': True}",
    "server_hm_down_recovery": "{'description': ['Specifies behavior when a persistent server has been marked down by a health monitor.', 'Enum options - HM_DOWN_PICK_NEW_SERVER, HM_DOWN_ABORT_CONNECTION, HM_DOWN_CONTINUE_PERSISTENT_SERVER.', 'Default value when not specified in API or module is interpreted by Avi Controller as HM_DOWN_PICK_NEW_SERVER.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the persistence profile.']}",
}
```

## Examples


``` yaml

  - name: Create an Application Persistence setting using http cookie.
    avi_applicationpersistenceprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      http_cookie_persistence_profile:
        always_send_cookie: false
        cookie_name: My-HTTP
        key:
        - aes_key: ShYGZdMks8j6Bpvm2sCvaXWzvXms2Z9ob+TTjRy46lQ=
          name: c1276819-550c-4adf-912d-59efa5fd7269
        - aes_key: OGsyVk84VCtyMENFOW0rMnRXVnNrb0RzdG5mT29oamJRb0dlbHZVSjR1az0=
          name: a080de57-77c3-4580-a3ea-e7a6493c14fd
        - aes_key: UVN0cU9HWmFUM2xOUzBVcmVXaHFXbnBLVUUxMU1VSktSVU5HWjJOWmVFMTBUMUV4UmxsNk4xQmFZejA9
          name: 60478846-33c6-484d-868d-bbc324fce4a5
        timeout: 15
      name: My-HTTP-Cookie
      persistence_type: PERSISTENCE_TYPE_HTTP_COOKIE
      server_hm_down_recovery: HM_DOWN_PICK_NEW_SERVER
      tenant_ref: Demo

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
