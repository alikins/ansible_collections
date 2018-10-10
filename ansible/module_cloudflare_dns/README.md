# Ansible module: ansible.module_cloudflare_dns


manage Cloudflare DNS records

## Description

Manages dns records via the Cloudflare API, see the docs: U(https://api.cloudflare.com/)

## Requirements

TODO

## Arguments

``` json
{
    "account_api_token": "{'description': ["Account API token. You can obtain your API key from the bottom of the Cloudflare 'My Account' page, found here: U(https://dash.cloudflare.com/)\n"], 'required': True}",
    "account_email": "{'description': ['Account email.'], 'required': True}",
    "algorithm": "{'description': ['Algorithm number. Required for C(type=DS) and C(type=SSHFP) when C(state=present).'], 'type': 'int', 'version_added': 2.7}",
    "cert_usage": "{'description': ['Certificate usage number. Required for C(type=TLSA) when C(state=present).'], 'choices': [0, 1, 2, 3], 'type': 'int', 'version_added': 2.7}",
    "hash_type": "{'description': ['Hash type number. Required for C(type=DS), C(type=SSHFP) and C(type=TLSA) when C(state=present).'], 'choices': [1, 2], 'type': 'int', 'version_added': 2.7}",
    "key_tag": "{'description': ['DNSSEC key tag. Needed for C(type=DS) when C(state=present).'], 'type': 'int', 'version_added': 2.7}",
    "port": "{'description': ['Service port. Required for C(type=SRV) and C(type=TLSA).']}",
    "priority": "{'description': ['Record priority. Required for C(type=MX) and C(type=SRV)'], 'default': '1'}",
    "proto": "{'description': ['Service protocol. Required for C(type=SRV) and C(type=TLSA).', 'Common values are tcp and udp.', 'Before Ansible 2.6 only tcp and udp were available.']}",
    "proxied": "{'description': ['Proxy through cloudflare network or just use DNS'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "record": "{'description': ['Record to add. Required if C(state=present). Default is C(@) (e.g. the zone name)'], 'default': '@', 'aliases': ['name']}",
    "selector": "{'description': ['Selector number. Required for C(type=TLSA) when C(state=present).'], 'choices': [0, 1], 'type': 'int', 'version_added': 2.7}",
    "service": "{'description': ['Record service. Required for C(type=SRV)']}",
    "solo": "{'description': ['Whether the record should be the only one for that record type and record name. Only use with C(state=present)', 'This will delete all other records with the same record name and type.']}",
    "state": "{'description': ['Whether the record(s) should exist or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Timeout for Cloudflare API calls'], 'default': 30}",
    "ttl": "{'description': ['The TTL to give the new record. Must be between 120 and 2,147,483,647 seconds, or 1 for automatic.'], 'default': '1 (automatic)'}",
    "type": "{'description': ['The type of DNS record to create. Required if C(state=present)', 'C(type=DS), C(type=SSHFP) and C(type=TLSA) added in Ansible 2.7.'], 'choices': ['A', 'AAAA', 'CNAME', 'TXT', 'SRV', 'MX', 'NS', 'DS', 'SPF', 'SSHFP', 'TLSA']}",
    "value": "{'description': ['The record value. Required for C(state=present)'], 'aliases': ['content']}",
    "weight": "{'description': ['Service weight. Required for C(type=SRV)'], 'default': '1'}",
    "zone": "{'description': ['The name of the Zone to work with (e.g. "example.com"). The Zone must already exist.'], 'required': True, 'aliases': ['domain']}",
}
```

## Examples


``` yaml

# create a test.my.com A record to point to 127.0.0.1
- cloudflare_dns:
    zone: my.com
    record: test
    type: A
    value: 127.0.0.1
    account_email: test@example.com
    account_api_token: dummyapitoken
  register: record

# create a my.com CNAME record to example.com
- cloudflare_dns:
    zone: my.com
    type: CNAME
    value: example.com
    state: present
    account_email: test@example.com
    account_api_token: dummyapitoken

# change it's ttl
- cloudflare_dns:
    zone: my.com
    type: CNAME
    value: example.com
    ttl: 600
    state: present
    account_email: test@example.com
    account_api_token: dummyapitoken

# and delete the record
- cloudflare_dns:
    zone: my.com
    type: CNAME
    value: example.com
    state: absent
    account_email: test@example.com
    account_api_token: dummyapitoken

# create a my.com CNAME record to example.com and proxy through cloudflare's network
- cloudflare_dns:
    zone: my.com
    type: CNAME
    value: example.com
    state: present
    proxied: yes
    account_email: test@example.com
    account_api_token: dummyapitoken

# create TXT record "test.my.com" with value "unique value"
# delete all other TXT records named "test.my.com"
- cloudflare_dns:
    domain: my.com
    record: test
    type: TXT
    value: unique value
    state: present
    solo: true
    account_email: test@example.com
    account_api_token: dummyapitoken

# create a SRV record _foo._tcp.my.com
- cloudflare_dns:
    domain: my.com
    service: foo
    proto: tcp
    port: 3500
    priority: 10
    weight: 20
    type: SRV
    value: fooserver.my.com

# create a SSHFP record login.example.com
- cloudflare_dns:
    zone: example.com
    record: login
    type: SSHFP
    algorithm: 4
    hash_type: 2
    value: 9dc1d6742696d2f51ca1f1a78b3d16a840f7d111eb9454239e70db31363f33e1

# create a TLSA record _25._tcp.mail.example.com
- cloudflare_dns:
    zone: example.com
    record: mail
    port: 25
    proto: tcp
    type: TLSA
    cert_usage: 3
    selector: 1
    hash_type: 1
    value: 6b76d034492b493e15a7376fccd08e63befdad0edab8e442562f532338364bf3

# Create a DS record for subdomain.example.com
- cloudflare_dns:
    zone: example.com
    record: subdomain
    type: DS
    key_tag: 5464
    algorithm: 8
    hash_type: 2
    value: B4EB5AC4467D2DFB3BAF9FB9961DC1B6FED54A58CDFAA3E465081EC86F89BFAB

```

## License

TODO

## Author Information
  - ['Michael Gruener (@mgruener)']
