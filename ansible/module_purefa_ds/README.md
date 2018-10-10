# Ansible module: ansible.module_purefa_ds


Configure FlashArray Directory Service

## Description

Set or erase configuration for the directory service. There is no facility to SSL certificates at this time. Use the FlashArray GUI for this additional configuration work.
To modify an existing directory service configuration you must first delete an exisitng configuration and then recreate with new settings.

## Requirements

TODO

## Arguments

``` json
{
    "aa_group": "{'description': ['Sets the common Name (CN) of the directory service group containing administrators with full privileges when managing the FlashArray. The name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.']}",
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "base_dn": "{'description': ['Sets the base of the Distinguished Name (DN) of the directory service groups. The base should consist of only Domain Components (DCs). The base_dn will populate with a default value when a URI is entered by parsing domain components from the URI. The base DN should specify DC= for each domain component and multiple DCs should be separated by commas.'], 'required': True}",
    "bind_password": "{'description': ['Sets the password of the bind_user user name account.']}",
    "bind_user": "{'description': ['Sets the user name that can be used to bind to and query the directory.', 'For Active Directory, enter the username - often referred to as sAMAccountName or User Logon Name - of the account that is used to perform directory lookups.', 'For OpenLDAP, enter the full DN of the user.']}",
    "enable": "{'description': ['Whether to enable or disable directory service support.'], 'default': False, 'type': 'bool'}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "group_base": "{'description': ['Specifies where the configured groups are located in the directory tree. This field consists of Organizational Units (OUs) that combine with the base DN attribute and the configured group CNs to complete the full Distinguished Name of the groups. The group base should specify OU= for each OU and multiple OUs should be separated by commas. The order of OUs is important and should get larger in scope from left to right. Each OU should not exceed 64 characters in length.']}",
    "ro_group": "{'description': ['Sets the common Name (CN) of the configured directory service group containing users with read-only privileges on the FlashArray. This name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.']}",
    "sa_group": "{'description': ['Sets the common Name (CN) of the configured directory service group containing administrators with storage-related privileges on the FlashArray. This name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.']}",
    "state": "{'description': ['Create or delete directory service configuration'], 'default': 'present', 'choices': ['absent', 'present']}",
    "uri": "{'description': ['A list of up to 30 URIs of the directory servers. Each URI must include the scheme ldap:// or ldaps:// (for LDAP over SSL), a hostname, and a domain name or IP address. For example, ldap://ad.company.com configures the directory service with the hostname "ad" in the domain "company.com" while specifying the unencrypted LDAP protocol.']}",
}
```

## Examples


``` yaml

- name: Delete exisitng directory service
  purefa_ds:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (disabled)
  purefa_ds:
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    group_base: "OU=Pure-Admin"
    ro_group: PureReadOnly
    sa_group: PureStorage
    aa_group: PureAdmin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Enable exisitng directory service
  purefa_ds:
    enable: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable exisitng directory service
  purefa_ds:
    enable: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (enabled)
  purefa_ds:
    enable: true
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    group_base: "OU=Pure-Admin"
    ro_group: PureReadOnly
    sa_group: PureStorage
    aa_group: PureAdmin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
