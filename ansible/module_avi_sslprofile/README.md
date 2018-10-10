# Ansible module: ansible.module_avi_sslprofile


Module for setup of SSLProfile Avi RESTful Object

## Description

This module is used to configure SSLProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "accepted_ciphers": "{'description': ['Ciphers suites represented as defined by U(http://www.openssl.org/docs/apps/ciphers.html).', 'Default value when not specified in API or module is interpreted by Avi Controller as AES:3DES:RC4.']}",
    "accepted_versions": "{'description': ['Set of versions accepted by the server.']}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "cipher_enums": "{'description': ['Enum options - tls_ecdhe_ecdsa_with_aes_128_gcm_sha256, tls_ecdhe_ecdsa_with_aes_256_gcm_sha384, tls_ecdhe_rsa_with_aes_128_gcm_sha256,', 'tls_ecdhe_rsa_with_aes_256_gcm_sha384, tls_ecdhe_ecdsa_with_aes_128_cbc_sha256, tls_ecdhe_ecdsa_with_aes_256_cbc_sha384,', 'tls_ecdhe_rsa_with_aes_128_cbc_sha256, tls_ecdhe_rsa_with_aes_256_cbc_sha384, tls_rsa_with_aes_128_gcm_sha256, tls_rsa_with_aes_256_gcm_sha384,', 'tls_rsa_with_aes_128_cbc_sha256, tls_rsa_with_aes_256_cbc_sha256, tls_ecdhe_ecdsa_with_aes_128_cbc_sha, tls_ecdhe_ecdsa_with_aes_256_cbc_sha,', 'tls_ecdhe_rsa_with_aes_128_cbc_sha, tls_ecdhe_rsa_with_aes_256_cbc_sha, tls_rsa_with_aes_128_cbc_sha, tls_rsa_with_aes_256_cbc_sha,', 'tls_rsa_with_3des_ede_cbc_sha, tls_rsa_with_rc4_128_sha.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "dhparam": "{'description': ['Dh parameters used in ssl.', 'At this time, it is not configurable and is set to 2048 bits.']}",
    "enable_ssl_session_reuse": "{'description': ['Enable ssl session re-use.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "prefer_client_cipher_ordering": "{'description': ['Prefer the ssl cipher ordering presented by the client during the ssl handshake over the one specified in the ssl profile.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "send_close_notify": "{'description': ["Send 'close notify' alert message for a clean shutdown of the ssl connection.", 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "ssl_rating": "{'description': ['Sslrating settings for sslprofile.']}",
    "ssl_session_timeout": "{'description': ['The amount of time before an ssl session expires.', 'Default value when not specified in API or module is interpreted by Avi Controller as 86400.', 'Units(SEC).']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tags": "{'description': ['List of tag.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Ssl profile type.', 'Enum options - SSL_PROFILE_TYPE_APPLICATION, SSL_PROFILE_TYPE_SYSTEM.', 'Field introduced in 17.2.8.', 'Default value when not specified in API or module is interpreted by Avi Controller as SSL_PROFILE_TYPE_APPLICATION.'], 'version_added': '2.6'}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

  - name: Create SSL profile with list of allowed ciphers
    avi_sslprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      accepted_ciphers: >
        ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA:
        ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:
        AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:
        AES256-SHA:DES-CBC3-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:
        ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA
      accepted_versions:
      - type: SSL_VERSION_TLS1
      - type: SSL_VERSION_TLS1_1
      - type: SSL_VERSION_TLS1_2
      cipher_enums:
      - TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
      - TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
      - TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
      - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
      - TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
      - TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
      - TLS_RSA_WITH_AES_128_GCM_SHA256
      - TLS_RSA_WITH_AES_256_GCM_SHA384
      - TLS_RSA_WITH_AES_128_CBC_SHA256
      - TLS_RSA_WITH_AES_256_CBC_SHA256
      - TLS_RSA_WITH_AES_128_CBC_SHA
      - TLS_RSA_WITH_AES_256_CBC_SHA
      - TLS_RSA_WITH_3DES_EDE_CBC_SHA
      - TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
      - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
      - TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
      - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
      - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
      - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
      name: PFS-BOTH-RSA-EC
      send_close_notify: true
      ssl_rating:
        compatibility_rating: SSL_SCORE_EXCELLENT
        performance_rating: SSL_SCORE_EXCELLENT
        security_score: '100.0'
      tenant_ref: Demo

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
