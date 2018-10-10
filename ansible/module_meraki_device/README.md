# Ansible module: ansible.module_meraki_device


Manage devices in the Meraki cloud

## Description

Visibility into devices associated to a Meraki environment.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ["Postal address of device's location."]}",
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "hostname": "{'description': ['Hostname of network device to search for.'], 'aliases': ['name']}",
    "lat": "{'description': ["Latitude of device's geographic location.", 'Use negative number for southern hemisphere.'], 'aliases': ['latitude']}",
    "lldp_cdp_timespan": "{'description': ['Timespan, in seconds, used to query LLDP and CDP information.', 'Must be less than 1 month.']}",
    "lng": "{'description': ["Longitude of device's geographic location.", 'Use negative number for western hemisphere.'], 'aliases': ['longitude']}",
    "model": "{'description': ['Model of network device to search for.']}",
    "move_map_marker": "{'description': ['Whether or not to set the latitude and longitude of a device based on the new address.', 'Only applies when C(lat) and C(lng) are not specified.'], 'type': 'bool'}",
    "net_id": "{'description': ['ID of a network.']}",
    "net_name": "{'description': ['Name of a network.'], 'aliases': ['network']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.', 'If C(clone) is specified, C(org_name) is the name of the new organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "serial": "{'description': ['Serial number of a device to query.']}",
    "serial_lldp_cdp": "{'description': ['Serial number of device to query LLDP/CDP information from.']}",
    "serial_uplink": "{'description': ['Serial number of device to query uplink information from.']}",
    "state": "{'description': ['Query an organization.'], 'choices': ['absent', 'present', 'query'], 'default': 'query'}",
    "tags": "{'description': ['Space delimited list of tags to assign to device.']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query all devices in an organization.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query all devices in a network.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Query a device by serial number.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup uplink information about a device.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial_uplink: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup LLDP and CDP information about devices connected to specified device.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    serial_lldp_cdp: ABC-123
    state: query
  delegate_to: localhost

- name: Lookup a device by hostname.
  meraki_device:
    auth_key: abc12345
    org_name: YourOrg
    net_name: YourNet
    hostname: main-switch
    state: query
  delegate_to: localhost

- name: Query all devices of a specific model.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    model: MR26
    state: query
  delegate_to: localhost

- name: Update information about a device.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    serial: '{{serial}}'
    name: mr26
    address: 1060 W. Addison St., Chicago, IL
    lat: 41.948038
    lng: -87.65568
    tags: recently-added
  delegate_to: localhost

- name: Claim a deivce into a network.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: present
  delegate_to: localhost

- name: Remove a device from a network.
  meraki_device:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    serial: ABC-123
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
