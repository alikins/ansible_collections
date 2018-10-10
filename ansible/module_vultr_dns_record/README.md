# Ansible module: ansible.module_vultr_dns_record


Manages DNS records on Vultr

## Description

Create, update and remove DNS records.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "data": "{'description': ['Data of the record.', 'Required if C(state=present) or C(multiple=yes).']}",
    "domain": "{'description': ['The domain the record is related to.'], 'required': True}",
    "multiple": "{'description': ['Whether to use more than one record with similar C(name) including no name and C(record_type).', 'Only allowed for a few record types, e.g. C(record_type=A), C(record_type=NS) or C(record_type=MX).', 'C(data) will not be updated, instead it is used as a key to find existing records.'], 'default': False, 'type': 'bool'}",
    "name": "{'description': ['The record name (subrecord).'], 'default': '', 'aliases': ['subrecord']}",
    "priority": "{'description': ['Priority of the record.'], 'default': 0}",
    "record_type": "{'description': ['Type of the record.'], 'default': 'A', 'choices': ['A', 'AAAA', 'CNAME', 'MX', 'SRV', 'CAA', 'TXT', 'NS', 'SSHFP'], 'aliases': ['type']}",
    "state": "{'description': ['State of the DNS record.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['TTL of the record.'], 'default': 300}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure an A record exists
  vultr_dns_record:
    name: www
    domain: example.com
    data: 10.10.10.10
    ttl: 3600

- name: Ensure a second A record exists for round robin LB
  vultr_dns_record:
    name: www
    domain: example.com
    data: 10.10.10.11
    ttl: 60
    multiple: yes

- name: Ensure a CNAME record exists
  vultr_dns_record:
    name: web
    record_type: CNAME
    domain: example.com
    data: www.example.com

- name: Ensure MX record exists
  vultr_dns_record:
    record_type: MX
    domain: example.com
    data: "{{ item.data }}"
    priority: "{{ item.priority }}"
    multiple: yes
  with_items:
  - { data: mx1.example.com, priority: 10 }
  - { data: mx2.example.com, priority: 10 }
  - { data: mx3.example.com, priority: 20 }

- name: Ensure a record is absent
  local_action:
    module: vultr_dns_record
    name: www
    domain: example.com
    state: absent

- name: Ensure MX record is absent in case multiple exists
  vultr_dns_record:
    record_type: MX
    domain: example.com
    data: mx1.example.com
    multiple: yes
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
