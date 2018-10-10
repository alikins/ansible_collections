# Ansible module: ansible.module_ucs_ip_pool


Configures IP address pools on Cisco UCS Manager

## Description

Configures IP address pools and blocks of IP addresses on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "default_gw": "{'description': ['The default gateway associated with the IPv4 addresses in the block.'], 'default': '0.0.0.0'}",
    "descrption": "{'description': ['The user-defined description of the IP address pool.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "first_addr": "{'description': ['The first IPv4 address in the IPv4 addresses block.', 'This is the From field in the UCS Manager Add IPv4 Blocks menu.']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "ipv6_default_gw": "{'description': ['The default gateway associated with the IPv6 addresses in the block.'], 'default': '::'}",
    "ipv6_first_addr": "{'description': ['The first IPv6 address in the IPv6 addresses block.', 'This is the From field in the UCS Manager Add IPv6 Blocks menu.']}",
    "ipv6_last_addr": "{'description': ['The last IPv6 address in the IPv6 addresses block.', 'This is the To field in the UCS Manager Add IPv6 Blocks menu.']}",
    "ipv6_prefix": "{'description': ['The network address prefix associated with the IPv6 addresses in the block.'], 'default': '64'}",
    "ipv6_primary_dns": "{'description': ['The primary DNS server that this block of IPv6 addresses should access.'], 'default': '::'}",
    "ipv6_secondary_dns": "{'description': ['The secondary DNS server that this block of IPv6 addresses should access.'], 'default': '::'}",
    "last_addr": "{'description': ['The last IPv4 address in the IPv4 addresses block.', 'This is the To field in the UCS Manager Add IPv4 Blocks menu.']}",
    "name": "{'description': ['The name of the IP address pool.', 'This name can be between 1 and 32 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the IP address pool is created.'], 'required': True}",
    "order": "{'description': ['The Assignment Order field.', 'This can be one of the following:', 'default - Cisco UCS Manager selects a random identity from the pool.', 'sequential - Cisco UCS Manager selects the lowest available identity from the pool.'], 'choices': ['default', 'sequential'], 'default': 'default'}",
    "org_dn": "{'description': ['Org dn (distinguished name)'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "primary_dns": "{'description': ['The primary DNS server that this block of IPv4 addresses should access.'], 'default': '0.0.0.0'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "secondary_dns": "{'description': ['The secondary DNS server that this block of IPv4 addresses should access.'], 'default': '0.0.0.0'}",
    "state": "{'description': ['If C(present), will verify IP pool is present and will create if needed.', 'If C(absent), will verify IP pool is absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnet_mask": "{'description': ['The subnet mask associated with the IPv4 addresses in the block.'], 'default': '255.255.255.0'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure IPv4 address pools
  ucs_ip_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: ip-A
    order: sequential
    first_addr: 192.168.0.10
    last_addr: 192.168.0.19
    subnet_mask: 255.255.255.0
    default_gw: 192.168.0.1
    primary_dns: 172.16.143.136
- name: Configure IPv6 address pools
  ucs_ip_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: ipv6-B
    ipv6_first_addr: fe80::1cae:7992:d7a1:ed07
    ipv6_last_addr: fe80::1cae:7992:d7a1:edfe
    ipv6_default_gw: fe80::1cae:7992:d7a1:ecff

- name: Remove IPv4 address pools
  ucs_ip_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: ip-A
    state: absent
- name: Remove IPv6 address pools
  ucs_ip_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: ipv6-B
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
