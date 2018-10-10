# Ansible module: ansible.module_dnsimple


Interface with dnsimple.com (a DNS hosting service)

## Description

Manages domains and records via the DNSimple API, see the docs: U(http://developer.dnsimple.com/).

## Requirements

TODO

## Arguments

``` json
{
    "account_api_token": "{'description': ['Account API token. See I(account_email) for more information.']}",
    "account_email": "{'description': ['Account email. If omitted, the environment variables C(DNSIMPLE_EMAIL) and C(DNSIMPLE_API_TOKEN) will be looked for.', "If those aren't found, a C(.dnsimple) file will be looked for, see: U(https://github.com/mikemaccana/dnsimple-python#getting-started)."]}",
    "domain": "{'description': ['Domain to work with. Can be the domain name (e.g. "mydomain.com") or the numeric ID of the domain in DNSimple.', 'If omitted, a list of domains will be returned.', "If domain is present but the domain doesn't exist, it will be created."]}",
    "priority": "{'description': ['Record priority.']}",
    "record": "{'description': ['Record to add, if blank a record for the domain will be created, supports the wildcard (*).']}",
    "record_ids": "{'description': ['List of records to ensure they either exist or do not exist.']}",
    "solo": "{'description': ['Whether the record should be the only one for that record type and record name.', 'Only use with C(state) is set to C(present) on a record.'], 'type': 'bool'}",
    "state": "{'description': ['whether the record should exist or not.'], 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['The TTL to give the new record in seconds.'], 'default': 3600}",
    "type": "{'description': ['The type of DNS record to create.'], 'choices': ['A', 'ALIAS', 'CNAME', 'MX', 'SPF', 'URL', 'TXT', 'NS', 'SRV', 'NAPTR', 'PTR', 'AAAA', 'SSHFP', 'HINFO', 'POOL']}",
    "value": "{'description': ['Record value.', 'Must be specified when trying to ensure a record exists.']}",
}
```

## Examples


``` yaml

- name: Authenticate using email and API token and fetch all domains
  dnsimple:
    account_email: test@example.com
    account_api_token: dummyapitoken
  delegate_to: localhost

- name: Fetch my.com domain records
  dnsimple:
    domain: my.com
    state: present
  delegate_to: localhost
  register: records

- name: Delete a domain
  dnsimple:
    domain: my.com
    state: absent
  delegate_to: localhost

- name: Create a test.my.com A record to point to 127.0.0.1
  dnsimple:
    domain: my.com
    record: test
    type: A
    value: 127.0.0.1
  delegate_to: localhost
  register: record

- name: Delete record using record_ids
  dnsimple:
    domain: my.com
    record_ids: '{{ record["id"] }}'
    state: absent
  delegate_to: localhost

- name: Create a my.com CNAME record to example.com
  dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    state: present
  delegate_to: localhost

- name: change TTL value for a record
  dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    ttl: 600
    state: present
  delegate_to: localhost

- name: Delete the record
  dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Alex Coomans (@drcapulet)']
