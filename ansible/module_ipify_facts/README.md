# Ansible module: ansible.module_ipify_facts


Retrieve the public IP of your internet gateway

## Description

If behind NAT and need to know the public IP of your internet gateway.

## Requirements

TODO

## Arguments

``` json
{
    "api_url": "{'description': ['URL of the ipify.org API service.', 'C(?format=json) will be appended per default.'], 'required': False, 'default': 'https://api.ipify.org'}",
    "timeout": "{'description': ['HTTP connection timeout in seconds.'], 'required': False, 'default': 10, 'version_added': '2.3'}",
    "validate_certs": "{'description': ['When set to C(NO), SSL certificates will not be validated.'], 'required': False, 'default': 'yes', 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Gather IP facts from ipify.org
- name: get my public IP
  ipify_facts:

# Gather IP facts from your own ipify service endpoint with a custom timeout
- name: get my public IP
  ipify_facts:
    api_url: http://api.example.com/ipify
    timeout: 20

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
