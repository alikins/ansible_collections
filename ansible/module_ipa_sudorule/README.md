# Ansible module: ansible.module_ipa_sudorule


Manage FreeIPA sudo rule

## Description

Add, modify or delete sudo rule within IPA server using IPA API.

## Requirements

TODO

## Arguments

``` json
{
    "cmd": "{'description': ['List of commands assigned to the rule.', 'If an empty list is passed all commands will be removed from the rule.', 'If option is omitted commands will not be checked or changed.']}",
    "cmdcategory": "{'description': ['Command category the rule applies to.'], 'choices': ['all']}",
    "cn": "{'description': ['Canonical name.', 'Can not be changed as it is the unique identifier.'], 'required': True, 'aliases': ['name']}",
    "description": "{'description': ['Description of the sudo rule.']}",
    "host": "{'description': ['List of hosts assigned to the rule.', 'If an empty list is passed all hosts will be removed from the rule.', 'If option is omitted hosts will not be checked or changed.', 'Option C(hostcategory) must be omitted to assign hosts.']}",
    "hostcategory": "{'description': ['Host category the rule applies to.', "If 'all' is passed one must omit C(host) and C(hostgroup).", "Option C(host) and C(hostgroup) must be omitted to assign 'all'."], 'choices': ['all']}",
    "hostgroup": "{'description': ['List of host groups assigned to the rule.', 'If an empty list is passed all host groups will be removed from the rule.', 'If option is omitted host groups will not be checked or changed.', 'Option C(hostcategory) must be omitted to assign host groups.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "runasgroupcategory": "{'description': ['RunAs Group category the rule applies to.'], 'choices': ['all'], 'version_added': '2.5'}",
    "runasusercategory": "{'description': ['RunAs User category the rule applies to.'], 'choices': ['all'], 'version_added': '2.5'}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "sudoopt": "{'description': ['List of options to add to the sudo rule.']}",
    "user": "{'description': ['List of users assigned to the rule.', 'If an empty list is passed all users will be removed from the rule.', 'If option is omitted users will not be checked or changed.']}",
    "usercategory": "{'description': ['User category the rule applies to.'], 'choices': ['all']}",
    "usergroup": "{'description': ['List of user groups assigned to the rule.', 'If an empty list is passed all user groups will be removed from the rule.', 'If option is omitted user groups will not be checked or changed.']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure sudo rule is present that's allows all every body to execute any command on any host without being asked for a password.
- ipa_sudorule:
    name: sudo_all_nopasswd
    cmdcategory: all
    description: Allow to run every command with sudo without password
    hostcategory: all
    sudoopt:
    - '!authenticate'
    usercategory: all
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
# Ensure user group developers can run every command on host group db-server as well as on host db01.example.com.
- ipa_sudorule:
    name: sudo_dev_dbserver
    description: Allow developers to run every command with sudo on all database server
    cmdcategory: all
    host:
    - db01.example.com
    hostgroup:
    - db-server
    sudoopt:
    - '!authenticate'
    usergroup:
    - developers
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
