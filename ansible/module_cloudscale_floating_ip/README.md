# Ansible module: ansible.module_cloudscale_floating_ip


Manages floating IPs on the cloudscale.ch IaaS service

## Description

Create, assign and delete floating IPs on the cloudscale.ch IaaS service.
All operations are performed using the cloudscale.ch public API v1.
For details consult the full API documentation: U(https://www.cloudscale.ch/en/api/v1).
A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at U(https://control.cloudscale.ch).

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['Timeout in seconds for calls to the cloudscale.ch API.'], 'default': 30}",
    "api_token": "{'description': ['cloudscale.ch API token.', 'This can also be passed in the CLOUDSCALE_API_TOKEN environment variable.']}",
    "ip": "{'description': ['Floating IP address to change.', 'Required to assign the IP to a different server or if I(state) is absent.'], 'aliases': ['network']}",
    "ip_version": "{'description': ['IP protocol version of the floating IP.'], 'choices': [4, 6]}",
    "prefix_length": "{'description': ['Only valid if I(ip_version) is 6.', 'Prefix length for the IPv6 network. Currently only a prefix of /56 can be requested. If no I(prefix_length) is present, a single address is created.'], 'choices': [56]}",
    "reverse_ptr": "{'description': ['Reverse PTR entry for this address.', 'You cannot set a reverse PTR entry for IPv6 floating networks. Reverse PTR entries are only allowed for single addresses.']}",
    "server": "{'description': ['UUID of the server assigned to this floating IP.', 'Required unless I(state) is absent.']}",
    "state": "{'description': ['State of the floating IP.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Request a new floating IP
- name: Request a floating IP
  cloudscale_floating_ip:
    ip_version: 4
    server: 47cec963-fcd2-482f-bdb6-24461b2d47b1
    reverse_ptr: my-server.example.com
    api_token: xxxxxx
  register: floating_ip

# Assign an existing floating IP to a different server
- name: Move floating IP to backup server
  cloudscale_floating_ip:
    ip: 192.0.2.123
    server: ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Request a new floating IPv6 network
- name: Request a floating IP
  cloudscale_floating_ip:
    ip_version: 6
    prefix_length: 56
    server: 47cec963-fcd2-482f-bdb6-24461b2d47b1
    api_token: xxxxxx
  register: floating_ip

# Assign an existing floating network to a different server
- name: Move floating IP to backup server
  cloudscale_floating_ip:
    ip: '{{ floating_ip.network | ip }}'
    server: ea3b39a3-77a8-4d0b-881d-0bb00a1e7f48
    api_token: xxxxxx

# Release a floating IP
- name: Release floating IP
  cloudscale_floating_ip:
    ip: 192.0.2.123
    state: absent
    api_token: xxxxxx

```

## License

TODO

## Author Information
  - ['Gaudenz Steinlin (@gaudenz) <gaudenz.steinlin@cloudscale.ch>']
