# Ansible module: ansible.module_udm_dns_record


Manage dns entries on a univention corporate server

## Description

This module allows to manage dns records on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'required': False, 'default': [], 'description': ["Additional data for this record, e.g. ['a': '192.0.2.1']. Required if C(state=present)."]}",
    "name": "{'required': True, 'description': ['Name of the record, this is also the DNS record. E.g. www for www.example.com.']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the dns record is present or not.']}",
    "type": "{'required': True, 'choices': ['host_record', 'alias', 'ptr_record', 'srv_record', 'txt_record'], 'description': ['Define the record type. C(host_record) is a A or AAAA record, C(alias) is a CNAME, C(ptr_record) is a PTR record, C(srv_record) is a SRV record and C(txt_record) is a TXT record.']}",
    "zone": "{'required': True, 'description': ['Corresponding DNS zone for this record, e.g. example.com.']}",
}
```

## Examples


``` yaml

# Create a DNS record on a UCS
- udm_dns_zone:
    name: www
    zone: example.com
    type: host_record
    data:
      - a: 192.0.2.1

```

## License

TODO

## Author Information
  - ['Tobias Rueetschi (@2-B)']
