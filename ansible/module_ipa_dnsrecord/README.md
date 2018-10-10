# Ansible module: ansible.module_ipa_dnsrecord


Manage FreeIPA DNS records

## Description

Add, modify and delete an IPA DNS Record using IPA API.

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
    "record_name": "{'description': ['The DNS record name to manage.'], 'required': True, 'aliases': ['name']}",
    "record_ttl": "{'description': ['Set the TTL for the record.', 'Applies only when adding a new or changing the value of record_value.'], 'version_added': '2.7'}",
    "record_type": "{'description': ['The type of DNS record name.', "Currently, 'A', 'AAAA', 'A6', 'CNAME', 'DNAME', 'PTR' and 'TXT' are supported.", "'A6', 'CNAME', 'DNAME' and 'TXT' are added in version 2.5."], 'required': False, 'default': 'A', 'choices': ['A', 'AAAA', 'A6', 'CNAME', 'DNAME', 'PTR', 'TXT']}",
    "record_value": "{'description': ['Manage DNS record name with this value.', "In the case of 'A' or 'AAAA' record types, this will be the IP address.", "In the case of 'A6' record type, this will be the A6 Record data.", "In the case of 'CNAME' record type, this will be the hostname.", "In the case of 'DNAME' record type, this will be the DNAME target.", "In the case of 'PTR' record type, this will be the hostname.", "In the case of 'TXT' record type, this will be a text."], 'required': True}",
    "state": "{'description': ['State to ensure'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['This only applies if C(ipa_prot) is I(https).', 'If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "zone_name": "{'description': ['The DNS zone name to which DNS record needs to be managed.'], 'required': True}",
}
```

## Examples


``` yaml

# Ensure dns record is present
- ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: vm-001
    record_type: 'AAAA'
    record_value: '::1'

# Ensure that dns record exists with a TTL
- ipa_dnsrecord:
    name: host02
    zone_name: example.com
    record_type: 'AAAA'
    record_value: '::1'
    record_ttl: 300
    ipa_host: ipa.example.com
    ipa_pass: topsecret
    state: present

# Ensure a PTR record is present
- ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: 2.168.192.in-addr.arpa
    record_name: 5
    record_type: 'PTR'
    record_value: 'internal.ipa.example.com'

# Ensure a TXT record is present
- ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: _kerberos
    record_type: 'TXT'
    record_value: 'EXAMPLE.COM'

# Ensure that dns record is removed
- ipa_dnsrecord:
    name: host01
    zone_name: example.com
    record_type: 'AAAA'
    record_value: '::1'
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    state: absent

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
