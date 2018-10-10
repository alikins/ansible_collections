# Ansible module: ansible.module_ipa_sudocmdgroup


Manage FreeIPA sudo command group

## Description

Add, modify or delete sudo command group within IPA server using IPA API.

## Requirements

TODO

## Arguments

``` json
{
    "cn": "{'description': ['Sudo Command Group.'], 'aliases': ['name'], 'required': True}",
    "description": "{'description': ['Group description.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "sudocmd": "{'description': ['List of sudo commands to assign to the group.', 'If an empty list is passed all assigned commands will be removed from the group.', 'If option is omitted sudo commands will not be checked or changed.']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure sudo command group exists
  ipa_sudocmdgroup:
    name: group01
    description: Group of important commands
    sudocmd:
    - su
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure sudo command group does not exist
  ipa_sudocmdgroup:
    name: group01
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
