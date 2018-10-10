# Ansible module: ansible.module_ipa_subca


Manage FreeIPA Lightweight Sub Certificate Authorities

## Description

Add, modify, enable, disable and delete an IPA Lightweight Sub Certificate Authorities using IPA API.

## Requirements

TODO

## Arguments

``` json
{
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "state": "{'description': ['State to ensure', "State 'disable' and 'enable' is available for FreeIPA 4.4.2 version and onwards"], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "subca_desc": "{'description': ["The Sub Certificate Authority's description."], 'required': True}",
    "subca_name": "{'description': ['The Sub Certificate Authority name which needs to be managed.'], 'required': True, 'aliases': ['name']}",
    "subca_subject": "{'description': ["The Sub Certificate Authority's Subject. e.g., 'CN=SampleSubCA1,O=testrelm.test'"], 'required': True}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure IPA Sub CA is present
- ipa_subca:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    subca_name: AnsibleSubCA1
    subca_subject: 'CN=AnsibleSubCA1,O=example.com'
    subca_desc: Ansible Sub CA

# Ensure that IPA Sub CA is removed
- ipa_subca:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: absent
    subca_name: AnsibleSubCA1

# Ensure that IPA Sub CA is disabled
- ipa_subca:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: disable
    subca_name: AnsibleSubCA1

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
