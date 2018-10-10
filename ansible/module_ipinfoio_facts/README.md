# Ansible module: ansible.module_ipinfoio_facts


Retrieve IP geolocation facts of a host's IP address

## Description

Gather IP geolocation facts of a host's IP address using ipinfo.io API

## Requirements

TODO

## Arguments

``` json
{
    "http_agent": "{'description': ['Set http user agent'], 'required': False, 'default': 'ansible-ipinfoio-module/0.0.1'}",
    "timeout": "{'description': ['HTTP connection timeout in seconds'], 'required': False, 'default': 10}",
}
```

## Examples


``` yaml

# Retrieve geolocation data of a host's IP address
- name: get IP geolocation data
  ipinfoio_facts:

```

## License

TODO

## Author Information
  - ['Aleksei Kostiuk (@akostyuk)']
