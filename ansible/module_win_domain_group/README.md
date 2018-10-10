# Ansible module: ansible.module_win_domain_group


Creates, modifies or removes domain groups

## Description

Creates, modifies or removes groups in Active Directory.
For local groups, use the M(win_group) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['A dict of custom LDAP attributes to set on the group.', 'This can be used to set custom attributes that are not exposed as module parameters, e.g. C(mail).', 'See the examples on how to format this parameter.']}",
    "category": "{'description': ['The category of the group, this is the value to assign to the LDAP C(groupType) attribute.', 'If a new group is created then C(security) will be used by default.'], 'choices': ['distribution', 'security']}",
    "description": "{'description': ['The value to be assigned to the LDAP C(description) attribute.']}",
    "display_name": "{'description': ['The value to assign to the LDAP C(displayName) attribute.']}",
    "domain_password": "{'description': ['The password for C(username).']}",
    "domain_server": "{'description': ['Specifies the Active Directory Domain Services instance to connect to.', 'Can be in the form of an FQDN or NetBIOS name.', 'If not specified then the value is based on the domain of the computer running PowerShell.'], 'version_added': '2.5'}",
    "domain_username": "{'description': ['The username to use when interacting with AD.', 'If this is not set then the user Ansible used to log in with will be used instead.']}",
    "ignore_protection": "{'description': ['Will ignore the C(ProtectedFromAccidentalDeletion) flag when deleting or moving a group.', 'The module will fail if one of these actions need to occur and this value is set to C(no).'], 'type': 'bool', 'default': False}",
    "managed_by": "{'description': ['The value to be assigned to the LDAP C(managedBy) attribute.', 'This value can be in the forms C(Distinguished Name), C(objectGUID), C(objectSid) or C(sAMAccountName), see examples for more details.']}",
    "name": "{'description': ['The name of the group to create, modify or remove.', 'This value can be in the forms C(Distinguished Name), C(objectGUID), C(objectSid) or C(sAMAccountName), see examples for more details.'], 'required': True}",
    "organizational_unit": "{'description': ['The full LDAP path to create or move the group to.', 'This should be the path to the parent object to create or move the group to.', 'See examples for details of how this path is formed.'], 'aliases': ['ou', 'path']}",
    "protect": "{'description': ['Will set the C(ProtectedFromAccidentalDeletion) flag based on this value.', 'This flag stops a user from deleting or moving a group to a different path.'], 'type': 'bool'}",
    "scope": "{'description': ['The scope of the group.', "If C(state=present) and the group doesn't exist then this must be set."], 'choices': ['domainlocal', 'global', 'universal']}",
    "state": "{'description': ['If C(state=present) this module will ensure the group is created and is configured accordingly.', 'If C(state=absent) this module will delete the group if it exists'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Ensure the group Cow exists using sAMAccountName
  win_domain_group:
    name: Cow
    scope: global
    path: OU=groups,DC=ansible,DC=local

- name: Ensure the group Cow does't exist using the Distinguished Name
  win_domain_group:
    name: CN=Cow,OU=groups,DC=ansible,DC=local
    state: absent

- name: Delete group ignoring the protection flag
  win_domain_group:
    name: Cow
    state: absent
    ignore_protection: yes

- name: Create group with delete protection enabled and custom attributes
  win_domain_group:
    name: Ansible Users
    scope: domainlocal
    category: security
    attributes:
      mail: helpdesk@ansible.com
      wWWHomePage: www.ansible.com
    ignore_protection: yes

- name: Change the OU of a group using the SID and ignore the protection flag
  win_domain_group:
    name: S-1-5-21-2171456218-3732823212-122182344-1189
    scope: global
    organizational_unit: OU=groups,DC=ansible,DC=local
    ignore_protection: yes

- name: Add managed_by user
  win_domain_group:
    name: Group Name Here
    managed_by: Domain Admins

- name: Add group and specify the AD domain services to use for the create
  win_domain_group:
    name: Test Group
    domain_username: user@CORP.ANSIBLE.COM
    domain_password: Password01!
    domain_server: corp-DC12.corp.ansible.com
    scope: domainlocal

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
