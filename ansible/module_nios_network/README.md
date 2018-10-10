# Ansible module: ansible.module_nios_network


Configure Infoblox NIOS network object

## Description

Adds and/or removes instances of network objects from Infoblox NIOS servers.  This module manages NIOS C(network) objects using the Infoblox WAPI interface over REST.
Supports both IPV4 and IPV6 internet protocols

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "network": "{'description': ['Specifies the network to add or remove from the system.  The value should use CIDR notation.'], 'required': True, 'aliases': ['name', 'cidr']}",
    "network_view": "{'description': ['Configures the name of the network view to associate with this configured instance.'], 'required': True, 'default': 'default'}",
    "options": "{'description': ['Configures the set of DHCP options to be included as part of the configured network instance.  This argument accepts a list of values (see suboptions).  When configuring suboptions at least one of C(name) or C(num) must be specified.'], 'suboptions': {'name': {'description': ['The name of the DHCP option to configure']}, 'num': {'description': ['The number of the DHCP option to configure']}, 'value': {'description': ['The value of the DHCP option specified by C(name)'], 'required': True}, 'use_option': {'description': ['Only applies to a subset of options (see NIOS API documentation)'], 'type': 'bool', 'default': 'yes'}, 'vendor_class': {'description': ['The name of the space this DHCP option is associated to'], 'default': 'DHCP'}}}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure a network ipv4
  nios_network:
    network: 192.168.10.0/24
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: configure a network ipv6
  nios_network:
    network: fe80::/64
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: set dhcp options for a network ipv4
  nios_network:
    network: 192.168.10.0/24
    comment: this is a test comment
    options:
      - name: domain-name
        value: ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: remove a network ipv4
  nios_network:
    network: 192.168.10.0/24
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
