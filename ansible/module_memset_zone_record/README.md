# Ansible module: ansible.module_memset_zone_record


Create and delete records in Memset DNS zones

## Description

Manage DNS records in a Memset account.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'required': True, 'description': ['The address for this record (can be IP or text string depending on record type).'], 'aliases': ['ip', 'data']}",
    "api_key": "{'required': True, 'description': ['The API key obtained from the Memset control panel.']}",
    "priority": "{'description': ['C(SRV) and C(TXT) record priority, in the range 0 > 999 (inclusive).']}",
    "record": "{'required': False, 'description': ['The subdomain to create.']}",
    "relative": "{'type': 'bool', 'description': ['If set then the current domain is added onto the address field for C(CNAME), C(MX), C(NS) and C(SRV)record types.']}",
    "state": "{'default': 'present', 'description': ['Indicates desired state of resource.'], 'choices': ['absent', 'present']}",
    "ttl": "{'description': ["The record's TTL in seconds (will inherit zone's TTL if not explicitly set). This must be a valid int from U(https://www.memset.com/apidocs/methods_dns.html#dns.zone_record_create)."], 'choices': [0, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]}",
    "type": "{'required': True, 'description': ['The type of DNS record to create.'], 'choices': ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SRV', 'TXT']}",
    "zone": "{'required': True, 'description': ['The name of the zone to which to add the record to.']}",
}
```

## Examples


``` yaml

# Create DNS record for www.domain.com
- name: create DNS record
  memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    state: present
    zone: domain.com
    type: A
    record: www
    address: 1.2.3.4
    ttl: 300
    relative: false
  delegate_to: localhost

# create an SPF record for domain.com
- name: create SPF record for domain.com
  memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    state: present
    zone: domain.com
    type: TXT
    address: "v=spf1 +a +mx +ip4:a1.2.3.4 ?all"
  delegate_to: localhost

# create multiple DNS records
- name: create multiple DNS records
  memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    zone: "{{ item.zone }}"
    type: "{{ item.type }}"
    record: "{{ item.record }}"
    address: "{{ item.address }}"
  delegate_to: localhost
  with_items:
    - { 'zone': 'domain1.com', 'type': 'A', 'record': 'www', 'address': '1.2.3.4' }
    - { 'zone': 'domain2.com', 'type': 'A', 'record': 'mail', 'address': '4.3.2.1' }

```

## License

TODO

## Author Information
  - ['Simon Weald (@analbeard)']
