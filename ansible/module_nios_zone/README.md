# Ansible module: ansible.module_nios_zone


Configure Infoblox NIOS DNS zones

## Description

Adds and/or removes instances of DNS zone objects from Infoblox NIOS servers.  This module manages NIOS C(zone_auth) objects using the Infoblox WAPI interface over REST.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "fqdn": "{'description': ['Specifies the qualified domain name to either add or remove from the NIOS instance based on the configured C(state) value.'], 'required': True, 'aliases': ['name']}",
    "grid_primary": "{'description': ['Configures the grid primary servers for this zone.'], 'suboptions': {'name': {'description': ['The name of the grid primary server']}}}",
    "grid_secondaries": "{'description': ['Configures the grid secondary servers for this zone.'], 'suboptions': {'name': {'description': ['The name of the grid secondary server']}}}",
    "ns_group": "{'version_added': '2.6', 'description': ['Configures the name server group for this zone. Name server group is mutually exclusive with grid primary and grid secondaries.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "restart_if_needed": "{'version_added': '2.6', 'description': ['If set to true, causes the NIOS DNS service to restart and load the new zone configuration'], 'type': 'bool'}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "view": "{'description': ['Configures the DNS view name for the configured resource.  The specified DNS zone must already exist on the running NIOS instance prior to configuring zones.'], 'required': True, 'default': 'default', 'aliases': ['dns_view']}",
    "zone_format": "{'version_added': '2.7', 'description': ['Create an authorative Reverse-Mapping Zone which is an area of network space for which one or more name servers-primary and secondary-have the responsibility to respond to address-to-name queries. It supports reverse-mapping zones for both IPv4 and IPv6 addresses.'], 'default': 'FORWARD'}",
}
```

## Examples


``` yaml

- name: configure a zone on the system using grid primary and secondaries
  nios_zone:
    name: ansible.com
    grid_primary:
      - name: gridprimary.grid.com
    grid_secondaries:
      - name: gridsecondary1.grid.com
      - name: gridsecondary2.grid.com
    restart_if_needed: true
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: configure a zone on the system using a name server group
  nios_zone:
    name: ansible.com
    ns_group: examplensg
    restart_if_needed: true
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: configure a reverse mapping zone on the system using IPV4 zone format
  nios_zone:
    name: 10.10.10.0/24
    zone_format: IPV4
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: configure a reverse mapping zone on the system using IPV6 zone format
  nios_zone:
    name: 100::1/128
    zone_format: IPV6
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: update the comment and ext attributes for an existing zone
  nios_zone:
    name: ansible.com
    comment: this is an example comment
    extattrs:
      Site: west-dc
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: remove the dns zone
  nios_zone:
    name: ansible.com
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: remove the reverse mapping dns zone from the system with IPV4 zone format
  nios_zone:
    name: 10.10.10.0/24
    zone_format: IPV4
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
