# Ansible lookup: ansible.lookup_dnstxt


query a domain(s)'s DNS txt fields

## Description

Uses a python library to return the DNS TXT record for a domain.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['domain or list of domains to query TXT records from'], 'required': True, 'type': 'list'}",
}
```

## Examples


``` yaml

- name: show txt entry
  debug: msg="{{lookup('dnstxt', ['test.example.com'])}}"

- name: iterate over txt entries
  debug: msg="{{item}}"
  with_dnstxt:
    - 'test.example.com'
    - 'other.example.com'
    - 'last.example.com'

- name: iterate of a comma delimited DNS TXT entry
  debug: msg="{{item}}"
  with_dnstxt: "{{lookup('dnstxt', ['test.example.com']).split(',')}}"

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>']
