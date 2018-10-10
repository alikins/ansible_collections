# Ansible module: ansible.module_memset_zone_domain


Create and delete domains in Memset DNS zones

## Description

Manage DNS zone domains in a Memset account.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'required': True, 'description': ['The API key obtained from the Memset control panel.']}",
    "domain": "{'required': True, 'description': ['The zone domain name. Ensure this value has at most 250 characters.'], 'aliases': ['name']}",
    "state": "{'default': 'present', 'description': ['Indicates desired state of resource.'], 'choices': ['absent', 'present']}",
    "zone": "{'required': True, 'description': ['The zone to add the domain to (this must already exist).']}",
}
```

## Examples


``` yaml

# Create the zone domain 'test.com'
- name: create zone domain
  memset_zone_domain:
    domain: test.com
    zone: testzone
    state: present
    api_key: 5eb86c9196ab03919abcf03857163741
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Simon Weald (@analbeard)']
