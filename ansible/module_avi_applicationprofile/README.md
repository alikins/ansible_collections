# Ansible module: ansible.module_avi_applicationprofile


Module for setup of ApplicationProfile Avi RESTful Object

## Description

This module is used to configure ApplicationProfile object
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
    "description": "{'description': ['User defined description for the object.']}",
    "dns_service_profile": "{'description': ['Specifies various dns service related controls for virtual service.']}",
    "dos_rl_profile": "{'description': ['Specifies various security related controls for virtual service.']}",
    "http_profile": "{'description': ['Specifies the http application proxy profile parameters.']}",
    "name": "{'description': ['The name of the application profile.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "preserve_client_ip": "{'description': ['Specifies if client ip needs to be preserved for backend connection.', 'Not compatible with connection multiplexing.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "preserve_client_port": "{'description': ['Specifies if we need to preserve client port while preseving client ip for backend connections.', 'Field introduced in 17.2.7.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.6', 'type': 'bool'}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tcp_app_profile": "{'description': ['Specifies the tcp application proxy profile parameters.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Specifies which application layer proxy is enabled for the virtual service.', 'Enum options - APPLICATION_PROFILE_TYPE_L4, APPLICATION_PROFILE_TYPE_HTTP, APPLICATION_PROFILE_TYPE_SYSLOG, APPLICATION_PROFILE_TYPE_DNS,', 'APPLICATION_PROFILE_TYPE_SSL.'], 'required': True}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the application profile.']}",
}
```

## Examples


``` yaml

  - name: Create an Application Profile for HTTP application enabled for SSL traffic
    avi_applicationprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      http_profile:
        cache_config:
          age_header: true
          aggressive: false
          date_header: true
          default_expire: 600
          enabled: false
          heuristic_expire: false
          max_cache_size: 0
          max_object_size: 4194304
          mime_types_group_refs:
          - admin:System-Cacheable-Resource-Types
          min_object_size: 100
          query_cacheable: false
          xcache_header: true
        client_body_timeout: 0
        client_header_timeout: 10000
        client_max_body_size: 0
        client_max_header_size: 12
        client_max_request_size: 48
        compression_profile:
          compressible_content_ref: admin:System-Compressible-Content-Types
          compression: false
          remove_accept_encoding_header: true
          type: AUTO_COMPRESSION
        connection_multiplexing_enabled: true
        hsts_enabled: false
        hsts_max_age: 365
        http_to_https: false
        httponly_enabled: false
        keepalive_header: false
        keepalive_timeout: 30000
        max_bad_rps_cip: 0
        max_bad_rps_cip_uri: 0
        max_bad_rps_uri: 0
        max_rps_cip: 0
        max_rps_cip_uri: 0
        max_rps_unknown_cip: 0
        max_rps_unknown_uri: 0
        max_rps_uri: 0
        post_accept_timeout: 30000
        secure_cookie_enabled: false
        server_side_redirect_to_https: false
        spdy_enabled: false
        spdy_fwd_proxy_mode: false
        ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
        ssl_everywhere_enabled: false
        websockets_enabled: true
        x_forwarded_proto_enabled: false
        xff_alternate_name: X-Forwarded-For
        xff_enabled: true
      name: System-HTTP
      tenant_ref: admin
      type: APPLICATION_PROFILE_TYPE_HTTP

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
