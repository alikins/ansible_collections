# Ansible module: ansible.module_panos_interface


configure data-port network interface for DHCP

## Description

Configure data-port (DP) network interface for DHCP. By default DP interfaces are static.

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['Commit if changed'], 'default': True}",
    "create_default_route": "{'description': ['Whether or not to add default route with router learned via DHCP.'], 'default': 'false'}",
    "if_name": "{'description': ['Name of the interface to configure.'], 'required': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
    "zone_name": "{'description': ['Name of the zone for the interface. If the zone does not exist it is created but if the zone exists and it is not of the layer3 type the operation will fail.\n'], 'required': True}",
}
```

## Examples


``` yaml

- name: enable DHCP client on ethernet1/1 in zone public
  interface:
    password: "admin"
    ip_address: "192.168.1.1"
    if_name: "ethernet1/1"
    zone_name: "public"
    create_default_route: "yes"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
