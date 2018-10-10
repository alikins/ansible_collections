# Ansible module: ansible.module_exo_dns_record


Manages DNS records on Exoscale DNS

## Description

Create, update and delete records.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key of the Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_KEY) is used as default, when defined.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'Since 2.4, the ENV variable C(CLOUDSTACK_REGION) is used as default, when defined.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_SECRET) is used as default, when defined.']}",
    "api_timeout": "{'description': ['HTTP timeout to Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_TIMEOUT) is used as default, when defined.'], 'default': 10}",
    "content": "{'description': ['Content of the record.', 'Required if C(state=present) or C(multiple=yes).'], 'aliases': ['value', 'address']}",
    "domain": "{'description': ['Domain the record is related to.'], 'required': True}",
    "multiple": "{'description': ['Whether there are more than one records with similar C(name) and C(record_type).', 'Only allowed for a few record types, e.g. C(record_type=A), C(record_type=NS) or C(record_type=MX).', 'C(content) will not be updated, instead it is used as a key to find existing records.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the record.'], 'default': ''}",
    "prio": "{'description': ['Priority of the record.'], 'aliases': ['priority']}",
    "record_type": "{'description': ['Type of the record.'], 'default': 'A', 'choices': ['A', 'ALIAS', 'CNAME', 'MX', 'SPF', 'URL', 'TXT', 'NS', 'SRV', 'NAPTR', 'PTR', 'AAAA', 'SSHFP', 'HINFO', 'POOL'], 'aliases': ['rtype', 'type']}",
    "state": "{'description': ['State of the record.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['TTL of the record in seconds.'], 'default': 3600}",
    "validate_certs": "{'description': ['Validate SSL certs of the Exoscale DNS API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create or update an A record
  local_action:
    module: exo_dns_record
    name: web-vm-1
    domain: example.com
    content: 1.2.3.4

- name: Update an existing A record with a new IP
  local_action:
    module: exo_dns_record
    name: web-vm-1
    domain: example.com
    content: 1.2.3.5

- name: Create another A record with same name
  local_action:
    module: exo_dns_record
    name: web-vm-1
    domain: example.com
    content: 1.2.3.6
    multiple: yes

- name: Create or update a CNAME record
  local_action:
    module: exo_dns_record
    name: www
    domain: example.com
    record_type: CNAME
    content: web-vm-1

- name: Create another MX record
  local_action:
    module: exo_dns_record
    domain: example.com
    record_type: MX
    content: mx1.example.com
    prio: 10
    multiple: yes

- name: Delete one MX record out of multiple
  local_action:
    module: exo_dns_record
    domain: example.com
    record_type: MX
    content: mx1.example.com
    multiple: yes
    state: absent

- name: Remove a single A record
  local_action:
    module: exo_dns_record
    name: www
    domain: example.com
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
