# Ansible module: ansible.module_stacki_host


Add or remove host to stacki front-end

## Description

Use this module to add or remove hosts to a stacki front-end via API.
U(https://github.com/StackIQ/stacki)

## Requirements

TODO

## Arguments

``` json
{
    "force_install": "{'description': ['Set value to True to force node into install state if it already exists in stacki.']}",
    "name": "{'description': ['Name of the host to be added to Stacki.'], 'required': True}",
    "prim_intf": "{'description': ['Name of the primary network interface.']}",
    "prim_intf_ip": "{'description': ['IP Address for the primary network interface.']}",
    "prim_intf_mac": "{'description': ['MAC Address for the primary PXE boot network interface.']}",
    "stacki_endpoint": "{'description': ['URL for the Stacki API Endpoint.'], 'required': True}",
    "stacki_password": "{'description': ['Password for authenticating with Stacki API, but if not specified, the environment variable C(stacki_password) is used instead.'], 'required': True}",
    "stacki_user": "{'description': ['Username for authenticating with Stacki API, but if not specified, the environment variable C(stacki_user) is used instead.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Add a host named test-1
  stacki_host:
    name: test-1
    stacki_user: usr
    stacki_password: pwd
    stacki_endpoint: url
    prim_intf_mac: mac_addr
    prim_intf_ip: x.x.x.x
    prim_intf: eth0

- name: Remove a host named test-1
  stacki_host:
    name: test-1
    stacki_user: usr
    stacki_password: pwd
    stacki_endpoint: url
    state: absent

```

## License

TODO

## Author Information
  - ['Hugh Ma <Hugh.Ma@flextronics.com>']
