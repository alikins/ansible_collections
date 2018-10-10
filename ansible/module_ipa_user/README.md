# Ansible module: ansible.module_ipa_user


Manage FreeIPA users

## Description

Add, modify and delete user within IPA server

## Requirements

TODO

## Arguments

``` json
{
    "displayname": "{'description': ['Display name']}",
    "gidnumber": "{'description': ['Posix Group ID'], 'version_added': 2.5}",
    "givenname": "{'description': ['First name']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "krbpasswordexpiration": "{'description': ['Date at which the user password will expire', 'In the format YYYYMMddHHmmss', 'e.g. 20180121182022 will expire on 21 January 2018 at 18:20:22'], 'version_added': 2.5}",
    "loginshell": "{'description': ['Login shell']}",
    "mail": "{'description': ['List of mail addresses assigned to the user.', 'If an empty list is passed all assigned email addresses will be deleted.', 'If None is passed email addresses will not be checked or changed.']}",
    "password": "{'description': ['Password for new user']}",
    "sn": "{'description': ['Surname']}",
    "sshpubkey": "{'description': ['List of public SSH key.', 'If an empty list is passed all assigned public keys will be deleted.', 'If None is passed SSH public keys will not be checked or changed.']}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "telephonenumber": "{'description': ['List of telephone numbers assigned to the user.', 'If an empty list is passed all assigned telephone numbers will be deleted.', 'If None is passed telephone numbers will not be checked or changed.']}",
    "title": "{'description': ['Title']}",
    "uid": "{'description': ['uid of the user'], 'required': True, 'aliases': ['name']}",
    "uidnumber": "{'description': ['Account Settings UID/Posix User ID number'], 'version_added': 2.5}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure pinky is present
- ipa_user:
    name: pinky
    state: present
    krbpasswordexpiration: 20200119235959
    givenname: Pinky
    sn: Acme
    mail:
    - pinky@acme.com
    telephonenumber:
    - '+555123456'
    sshpubkey:
    - ssh-rsa ....
    - ssh-dsa ....
    uidnumber: 1001
    gidnumber: 100
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure brain is absent
- ipa_user:
    name: brain
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
