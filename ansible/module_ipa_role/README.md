# Ansible module: ansible.module_ipa_role


Manage FreeIPA role

## Description

Add, modify and delete a role within FreeIPA server using FreeIPA API

## Requirements

TODO

## Arguments

``` json
{
    "cn": "{'description': ['Role name.', 'Can not be changed as it is the unique identifier.'], 'required': True, 'aliases': ['name']}",
    "description": "{'description': ['A description of this role-group.']}",
    "group": "{'description': ['List of group names assign to this role.', 'If an empty list is passed all assigned groups will be unassigned from the role.', 'If option is omitted groups will not be checked or changed.', 'If option is passed all assigned groups that are not passed will be unassigned from the role.']}",
    "host": "{'description': ['List of host names to assign.', 'If an empty list is passed all assigned hosts will be unassigned from the role.', 'If option is omitted hosts will not be checked or changed.', 'If option is passed all assigned hosts that are not passed will be unassigned from the role.']}",
    "hostgroup": "{'description': ['List of host group names to assign.', 'If an empty list is passed all assigned host groups will be removed from the role.', 'If option is omitted host groups will not be checked or changed.', 'If option is passed all assigned hostgroups that are not passed will be unassigned from the role.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "privilege": "{'description': ['List of privileges granted to the role.', 'If an empty list is passed all assigned privileges will be removed.', 'If option is omitted privileges will not be checked or changed.', 'If option is passed all assigned privileges that are not passed will be removed.'], 'version_added': '2.4'}",
    "service": "{'description': ['List of service names to assign.', 'If an empty list is passed all assigned services will be removed from the role.', 'If option is omitted services will not be checked or changed.', 'If option is passed all assigned services that are not passed will be removed from the role.']}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['List of user names to assign.', 'If an empty list is passed all assigned users will be removed from the role.', 'If option is omitted users will not be checked or changed.']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure role is present
- ipa_role:
    name: dba
    description: Database Administrators
    state: present
    user:
    - pinky
    - brain
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure role with certain details
- ipa_role:
    name: another-role
    description: Just another role
    group:
    - editors
    host:
    - host01.example.com
    hostgroup:
    - hostgroup01
    privilege:
    - Group Administrators
    - User Administrators
    service:
    - service01

# Ensure role is absent
- ipa_role:
    name: dba
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
