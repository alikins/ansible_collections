# Ansible module: ansible.module_netcup_dns


manage Netcup DNS records

## Description

Manages DNS records via the Netcup API, see the docs U(https://ccp.netcup.net/run/webservice/servers/endpoint.php)

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key for authentification, must be obtained via the netcup CCP (U(https://ccp.netcup.net))'], 'required': True}",
    "api_password": "{'description': ['API password for authentification, must be obtained via the netcup CCP (https://ccp.netcup.net)'], 'required': True}",
    "customer_id": "{'description': ['Netcup customer id'], 'required': True}",
    "domain": "{'description': ['Domainname the records should be added / removed'], 'required': True}",
    "priority": "{'description': ['Record priority. Required for C(type=MX)'], 'required': False}",
    "record": "{'description': ['Record to add or delete, supports wildcard (*). Default is C(@) (e.g. the zone name)'], 'default': '@', 'aliases': ['name']}",
    "solo": "{'type': 'bool', 'default': False, 'description': ['Whether the record should be the only one for that record type and record name. Only use with C(state=present)', 'This will delete all other records with the same record name and type.']}",
    "state": "{'description': ['Whether the record should exist or not'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['Record type'], 'choices': ['A', 'AAAA', 'MX', 'CNAME', 'CAA', 'SRV', 'TXT', 'TLSA', 'NS', 'DS'], 'required': True}",
    "value": "{'description': ['Record value'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a record of type A
  netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "mail"
    type: "A"
    value: "127.0.0.1"

- name: Delete that record
  netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "mail"
    type: "A"
    value: "127.0.0.1"
    state: absent

- name: Create a wildcard record
  netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    name: "*"
    type: "A"
    value: "127.0.1.1"

- name: Set the MX record for example.com
  netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    domain: "example.com"
    type: "MX"
    value: "mail.example.com"

- name: Set a record and ensure that this is the only one
  netcup_dns:
    api_key: "..."
    api_password: "..."
    customer_id: "..."
    name: "demo"
    domain: "example.com"
    type: "AAAA"
    value: "::1"
    solo: true

```

## License

TODO

## Author Information
  - ['Nicolai Buchwitz (@nbuchwitz)']
