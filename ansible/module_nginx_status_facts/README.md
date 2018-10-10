# Ansible module: ansible.module_nginx_status_facts


Retrieve nginx status facts

## Description

Gathers facts from nginx from an URL having C(stub_status) enabled.

## Requirements

TODO

## Arguments

``` json
{
    "timeout": "{'description': ['HTTP connection timeout in seconds.'], 'required': False, 'default': 10}",
    "url": "{'description': ['URL of the nginx status.'], 'required': True}",
}
```

## Examples


``` yaml

# Gather status facts from nginx on localhost
- name: get current http stats
  nginx_status_facts:
    url: http://localhost/nginx_status

# Gather status facts from nginx on localhost with a custom timeout of 20 seconds
- name: get current http stats
  nginx_status_facts:
    url: http://localhost/nginx_status
    timeout: 20

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
