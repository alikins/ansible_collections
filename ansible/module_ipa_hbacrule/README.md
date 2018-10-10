# Ansible module: ansible.module_ipa_hbacrule


Manage FreeIPA HBAC rule

## Description

Add, modify or delete an IPA HBAC rule using IPA API.

## Requirements

TODO

## Arguments

``` json
{
    "cn": "{'description': ['Canonical name.', 'Can not be changed as it is the unique identifier.'], 'required': True, 'aliases': ['name']}",
    "description": "{'description': ['Description']}",
    "host": "{'description': ['List of host names to assign.', 'If an empty list is passed all hosts will be removed from the rule.', 'If option is omitted hosts will not be checked or changed.'], 'required': False}",
    "hostcategory": "{'description': ['Host category'], 'choices': ['all']}",
    "hostgroup": "{'description': ['List of hostgroup names to assign.', 'If an empty list is passed all hostgroups will be removed. from the rule', 'If option is omitted hostgroups will not be checked or changed.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "service": "{'description': ['List of service names to assign.', 'If an empty list is passed all services will be removed from the rule.', 'If option is omitted services will not be checked or changed.']}",
    "servicecategory": "{'description': ['Service category'], 'choices': ['all']}",
    "servicegroup": "{'description': ['List of service group names to assign.', 'If an empty list is passed all assigned service groups will be removed from the rule.', 'If option is omitted service groups will not be checked or changed.']}",
    "sourcehost": "{'description': ['List of source host names to assign.', 'If an empty list if passed all assigned source hosts will be removed from the rule.', 'If option is omitted source hosts will not be checked or changed.']}",
    "sourcehostcategory": "{'description': ['Source host category'], 'choices': ['all']}",
    "sourcehostgroup": "{'description': ['List of source host group names to assign.', 'If an empty list if passed all assigned source host groups will be removed from the rule.', 'If option is omitted source host groups will not be checked or changed.']}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "user": "{'description': ['List of user names to assign.', 'If an empty list if passed all assigned users will be removed from the rule.', 'If option is omitted users will not be checked or changed.']}",
    "usercategory": "{'description': ['User category'], 'choices': ['all']}",
    "usergroup": "{'description': ['List of user group names to assign.', 'If an empty list if passed all assigned user groups will be removed from the rule.', 'If option is omitted user groups will not be checked or changed.']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure rule to allow all users to access any host from any host
- ipa_hbacrule:
    name: allow_all
    description: Allow all users to access any host from any host
    hostcategory: all
    servicecategory: all
    usercategory: all
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure rule with certain limitations
- ipa_hbacrule:
    name: allow_all_developers_access_to_db
    description: Allow all developers to access any database from any host
    hostgroup:
    - db-server
    usergroup:
    - developers
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure rule is absent
- ipa_hbacrule:
    name: rule_to_be_deleted
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
