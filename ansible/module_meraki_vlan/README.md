# Ansible module: ansible.module_meraki_vlan


Manage VLANs in the Meraki cloud

## Description

Create, edit, query, or delete VLANs in a Meraki environment.

## Requirements

TODO

## Arguments

``` json
{
    "appliance_ip": "{'description': ['IP address of appliance.', 'Address must be within subnet specified in C(subnet) parameter.']}",
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "dns_nameservers": "{'description': ['Semi-colon delimited list of DNS IP addresses.', 'Specify one of the following options for preprogrammed DNS entries opendns, google_dns, upstream_dns']}",
    "fixed_ip_assignments": "{'description': ['Static IP address assignements to be distributed via DHCP by MAC address.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "name": "{'description': ['Name of VLAN.'], 'aliases': ['vlan_name']}",
    "net_id": "{'description': ['ID of network which VLAN is in or should be in.']}",
    "net_name": "{'description': ['Name of network which VLAN is in or should be in.'], 'aliases': ['network']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "reserved_ip_range": "{'description': ['IP address ranges which should be reserve and not distributed via DHCP.']}",
    "state": "{'description': ['Specifies whether object should be queried, created/modified, or removed.'], 'choices': ['absent', 'present', 'query'], 'default': 'query'}",
    "subnet": "{'description': ['CIDR notation of network subnet.']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
    "vlan_id": "{'description': ['ID number of VLAN.', 'ID should be between 1-4096.']}",
    "vpn_nat_subnet": "{'description': ['The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN.']}",
}
```

## Examples


``` yaml

- name: Query all VLANs in a network.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query information about a single VLAN by ID.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    vlan_id: 2
    state: query
  delegate_to: localhost

- name: Create a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: present
    vlan_id: 2
    name: TestVLAN
    subnet: 192.0.1.0/24
    appliance_ip: 192.0.1.1
  delegate_to: localhost

- name: Update a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: present
    vlan_id: 2
    name: TestVLAN
    subnet: 192.0.1.0/24
    appliance_ip: 192.168.250.2
    fixed_ip_assignments:
      - mac: "13:37:de:ad:be:ef"
        ip: 192.168.250.10
        name: fixed_ip
    reserved_ip_range:
      - start: 192.168.250.10
        end: 192.168.250.20
        comment: reserved_range
    dns_nameservers: opendns
  delegate_to: localhost

- name: Delete a VLAN.
  meraki_vlan:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: absent
    vlan_id: 2
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
