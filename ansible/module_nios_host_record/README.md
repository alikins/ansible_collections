# Ansible module: ansible.module_nios_host_record


Configure Infoblox NIOS host records

## Description

Adds and/or removes instances of host record objects from Infoblox NIOS servers.  This module manages NIOS C(record:host) objects using the Infoblox WAPI interface over REST.
Updates instances of host record object from Infoblox NIOS servers.

## Requirements

TODO

## Arguments

``` json
{
    "aliases": "{'version_added': '2.6', 'description': ['Configures an optional list of additional aliases to add to the host record. These are equivalent to CNAMEs but held within a host record. Must be in list format.']}",
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "configure_for_dns": "{'version_added': '2.7', 'description': ['Sets the DNS to particular parent. If user needs to bypass DNS user can make the value to false.'], 'type': 'bool', 'required': False, 'default': True, 'aliases': ['dns']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "ipv4addrs": "{'description': ['Configures the IPv4 addresses for this host record.  This argument accepts a list of values (see suboptions)'], 'aliases': ['ipv4'], 'suboptions': {'ipv4addr': {'description': ['Configures the IPv4 address for the host record'], 'required': True, 'aliases': ['address']}, 'configure_for_dhcp': {'description': ['Configure the host_record over DHCP instead of DNS, if user changes it to true, user need to mention MAC address to configure'], 'required': False, 'aliases': ['dhcp']}, 'mac': {'description': ['Configures the hardware MAC address for the host record. If user makes DHCP to true, user need to mention MAC address.'], 'required': False, 'aliases': ['mac']}}}",
    "ipv6addrs": "{'description': ['Configures the IPv6 addresses for the host record.  This argument accepts a list of values (see options)'], 'aliases': ['ipv6'], 'suboptions': {'ipv6addr': {'description': ['Configures the IPv6 address for the host record'], 'required': True, 'aliases': ['address']}, 'configure_for_dhcp': {'description': ['Configure the host_record over DHCP instead of DNS, if user changes it to true, user need to mention MAC address to configure'], 'required': False, 'aliases': ['dhcp']}}}",
    "name": "{'description': ['Specifies the fully qualified hostname to add or remove from the system. User can also update the hostname as it is possible to pass a dict containing I(new_name), I(old_name). See examples.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['Configures the TTL to be associated with this host record']}",
    "view": "{'description': ['Sets the DNS view to associate this host record with.  The DNS view must already be configured on the system'], 'required': True, 'default': 'default', 'aliases': ['dns_view']}",
}
```

## Examples


``` yaml

- name: configure an ipv4 host record
  nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
    aliases:
      - cname.ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: add a comment to an existing host record
  nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: remove a host record from the system
  nios_host_record:
    name: host.ansible.com
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: update an ipv4 host record
  nios_host_record:
    name: {new_name: host-new.ansible.com, old_name: host.ansible.com}
    ipv4:
      - address: 192.168.10.1
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: create an ipv4 host record bypassing DNS
  nios_host_record:
    name: new_host
    ipv4:
      - address: 192.168.10.1
    dns: false
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: create an ipv4 host record over DHCP
  nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
        dhcp: true
        mac: 00-80-C8-E3-4C-BD
    state: present
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
