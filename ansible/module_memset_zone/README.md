# Ansible module: ansible.module_memset_zone


Creates and deletes Memset DNS zones

## Description

Manage DNS zones in a Memset account.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'required': True, 'description': ['The API key obtained from the Memset control panel.']}",
    "force": "{'required': False, 'default': False, 'type': 'bool', 'description': ['Forces deletion of a zone and all zone domains/zone records it contains.']}",
    "name": "{'required': True, 'description': ['The zone nickname; usually the same as the main domain. Ensure this value has at most 250 characters.'], 'aliases': ['nickname']}",
    "state": "{'required': True, 'description': ['Indicates desired state of resource.'], 'choices': ['absent', 'present']}",
    "ttl": "{'description': ['The default TTL for all records created in the zone. This must be a valid int from U(https://www.memset.com/apidocs/methods_dns.html#dns.zone_create).'], 'choices': [0, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]}",
}
```

## Examples


``` yaml

# Create the zone 'test'
- name: create zone
  memset_zone:
    name: test
    state: present
    api_key: 5eb86c9196ab03919abcf03857163741
    ttl: 300
  delegate_to: localhost

# Force zone deletion
- name: force delete zone
  memset_zone:
    name: test
    state: absent
    api_key: 5eb86c9196ab03919abcf03857163741
    force: true
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Simon Weald (@analbeard)']
