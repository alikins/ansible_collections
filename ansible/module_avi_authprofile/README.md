# Ansible module: ansible.module_avi_authprofile


Module for setup of AuthProfile Avi RESTful Object

## Description

This module is used to configure AuthProfile object
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
    "http": "{'description': ['Http user authentication params.']}",
    "ldap": "{'description': ['Ldap server and directory settings.']}",
    "name": "{'description': ['Name of the auth profile.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "saml": "{'description': ['Saml settings.', 'Field introduced in 17.2.3.'], 'version_added': '2.5'}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tacacs_plus": "{'description': ['Tacacs+ settings.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Type of the auth profile.', 'Enum options - AUTH_PROFILE_LDAP, AUTH_PROFILE_TACACS_PLUS, AUTH_PROFILE_SAML.'], 'required': True}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the auth profile.']}",
}
```

## Examples


``` yaml

  - name: Create user authorization profile based on the LDAP
    avi_authprofile:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      http:
        cache_expiration_time: 5
        group_member_is_full_dn: false
      ldap:
        base_dn: dc=avi,dc=local
        bind_as_administrator: true
        port: 389
        security_mode: AUTH_LDAP_SECURE_NONE
        server:
        - 10.10.0.100
        settings:
          admin_bind_dn: user@avi.local
          group_filter: (objectClass=*)
          group_member_attribute: member
          group_member_is_full_dn: true
          group_search_dn: dc=avi,dc=local
          group_search_scope: AUTH_LDAP_SCOPE_SUBTREE
          ignore_referrals: true
          password: password
          user_id_attribute: samAccountname
          user_search_dn: dc=avi,dc=local
          user_search_scope: AUTH_LDAP_SCOPE_ONE
      name: ProdAuth
      tenant_ref: admin
      type: AUTH_PROFILE_LDAP

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
