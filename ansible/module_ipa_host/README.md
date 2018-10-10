# Ansible module: ansible.module_ipa_host


Manage FreeIPA host

## Description

Add, modify and delete an IPA host using IPA API

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A description of this host.']}",
    "force": "{'description': ['Force host name even if not in DNS.'], 'required': False, 'type': 'bool'}",
    "fqdn": "{'description': ['Full qualified domain name.', 'Can not be changed as it is the unique identifier.'], 'required': True, 'aliases': ['name']}",
    "ip_address": "{'description': ['Add the host to DNS with this IP address.']}",
    "ipa_host": "{'description': ['IP or hostname of IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_HOST) will be used instead.', 'If both the environment variable C(IPA_HOST) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'ipa.example.com'}",
    "ipa_pass": "{'description': ['Password of administrative user.', 'If the value is not specified in the task, the value of environment variable C(IPA_PASS) will be used instead.', 'If both the environment variable C(IPA_PASS) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'required': True}",
    "ipa_port": "{'description': ['Port of FreeIPA / IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PORT) will be used instead.', 'If both the environment variable C(IPA_PORT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 443}",
    "ipa_prot": "{'description': ['Protocol used by IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_PROT) will be used instead.', 'If both the environment variable C(IPA_PROT) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'https', 'choices': ['http', 'https']}",
    "ipa_timeout": "{'description': ['Specifies idle timeout (in seconds) for the connection.', 'For bulk operations, you may want to increase this in order to avoid timeout from IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_TIMEOUT) will be used instead.', 'If both the environment variable C(IPA_TIMEOUT) and the value are not specified in the task, then default value is set.'], 'default': 10, 'version_added': 2.7}",
    "ipa_user": "{'description': ['Administrative account used on IPA server.', 'If the value is not specified in the task, the value of environment variable C(IPA_USER) will be used instead.', 'If both the environment variable C(IPA_USER) and the value are not specified in the task, then default value is set.', 'Environment variable fallback mechanism is added in version 2.5.'], 'default': 'admin'}",
    "mac_address": "{'description': ['List of Hardware MAC address(es) off this host.', 'If option is omitted MAC addresses will not be checked or changed.', 'If an empty list is passed all assigned MAC addresses will be removed.', 'MAC addresses that are already assigned but not passed will be removed.'], 'aliases': ['macaddress']}",
    "ns_hardware_platform": "{'description': ['Host hardware platform (e.g. "Lenovo T61")'], 'aliases': ['nshardwareplatform']}",
    "ns_host_location": "{'description': ['Host location (e.g. "Lab 2")'], 'aliases': ['nshostlocation']}",
    "ns_os_version": "{'description': ['Host operating system and version (e.g. "Fedora 9")'], 'aliases': ['nsosversion']}",
    "random_password": "{'description': ['Generate a random password to be used in bulk enrollment'], 'default': False, 'type': 'bool', 'version_added': '2.5'}",
    "state": "{'description': ['State to ensure'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "update_dns": "{'description': ['If set C("True") with state as C("absent"), then removes DNS records of the host managed by FreeIPA DNS.', 'This option has no effect for states other than "absent".'], 'default': False, 'type': 'bool', 'version_added': '2.5'}",
    "user_certificate": "{'description': ['List of Base-64 encoded server certificates.', 'If option is omitted certificates will not be checked or changed.', 'If an empty list is passed all assigned certificates will be removed.', 'Certificates already assigned but not passed will be removed.'], 'aliases': ['usercertificate']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Ensure host is present
- ipa_host:
    name: host01.example.com
    description: Example host
    ip_address: 192.168.0.123
    ns_host_location: Lab
    ns_os_version: CentOS 7
    ns_hardware_platform: Lenovo T61
    mac_address:
    - "08:00:27:E3:B1:2D"
    - "52:54:00:BD:97:1E"
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Generate a random password for bulk enrolment
- ipa_host:
    name: host01.example.com
    description: Example host
    ip_address: 192.168.0.123
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    validate_certs: False
    random_password: True

# Ensure host is disabled
- ipa_host:
    name: host01.example.com
    state: disabled
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure that all user certificates are removed
- ipa_host:
    name: host01.example.com
    user_certificate: []
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure host is absent
- ipa_host:
    name: host01.example.com
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

# Ensure host and its DNS record is absent
- ipa_host:
    name: host01.example.com
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    update_dns: True

```

## License

TODO

## Author Information
  - ['Thomas Krahn (@Nosmoht)']
