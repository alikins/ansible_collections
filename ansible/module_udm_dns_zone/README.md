# Ansible module: ansible.module_udm_dns_zone


Manage dns zones on a univention corporate server

## Description

This module allows to manage dns zones on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## Requirements

TODO

## Arguments

``` json
{
    "contact": "{'required': False, 'default': '', 'description': ['Contact person in the SOA record.']}",
    "expire": "{'required': False, 'default': 604800, 'description': ['Specifies the upper limit on the time interval that can elapse before the zone is no longer authoritative.']}",
    "interfaces": "{'required': False, 'description': ['List of interface IP addresses, on which the server should response this zone. Required if C(state=present).']}",
    "mx": "{'required': False, 'default': [], 'description': ['List of MX servers. (Must declared as A or AAAA records).']}",
    "nameserver": "{'required': False, 'description': ['List of appropriate name servers. Required if C(state=present).']}",
    "refresh": "{'required': False, 'default': 3600, 'description': ['Interval before the zone should be refreshed.']}",
    "retry": "{'required': False, 'default': 1800, 'description': ['Interval that should elapse before a failed refresh should be retried.']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the dns zone is present or not.']}",
    "ttl": "{'required': False, 'default': 600, 'description': ['Minimum TTL field that should be exported with any RR from this zone.']}",
    "type": "{'required': True, 'choices': ['forward_zone', 'reverse_zone'], 'description': ['Define if the zone is a forward or reverse DNS zone.']}",
    "zone": "{'required': True, 'description': ['DNS zone name, e.g. C(example.com).']}",
}
```

## Examples


``` yaml

# Create a DNS zone on a UCS
- udm_dns_zone:
    zone: example.com
    type: forward_zone
    nameserver:
      - ucs.example.com
    interfaces:
      - 192.0.2.1

```

## License

TODO

## Author Information
  - ['Tobias Rueetschi (@2-B)']
