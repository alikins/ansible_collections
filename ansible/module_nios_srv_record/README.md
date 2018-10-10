# Ansible module: ansible.module_nios_srv_record


Configure Infoblox NIOS SRV records

## Description

Adds and/or removes instances of SRV record objects from Infoblox NIOS servers.  This module manages NIOS C(record:srv) objects using the Infoblox WAPI interface over REST.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "name": "{'description': ['Specifies the fully qualified hostname to add or remove from the system'], 'required': True}",
    "port": "{'description': ['Configures the port (0-65535) of this SRV record.'], 'required': True}",
    "priority": "{'description': ['Configures the priority (0-65535) for this SRV record.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "target": "{'description': ['Configures the target FQDN for this SRV record.'], 'required': True}",
    "ttl": "{'description': ['Configures the TTL to be associated with this host record']}",
    "view": "{'description': ['Sets the DNS view to associate this a record with.  The DNS view must already be configured on the system'], 'required': True, 'default': 'default', 'aliases': ['dns_view']}",
    "weight": "{'description': ['Configures the weight (0-65535) for this SRV record.'], 'required': True}",
}
```

## Examples


``` yaml

- name: configure an SRV record
  nios_srv_record:
    name: _sip._tcp.service.ansible.com
    port: 5080
    priority: 10
    target: service1.ansible.com
    weight: 10
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: add a comment to an existing SRV record
  nios_srv_record:
    name: _sip._tcp.service.ansible.com
    port: 5080
    priority: 10
    target: service1.ansible.com
    weight: 10
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: remove an SRV record from the system
  nios_srv_record:
    name: _sip._tcp.service.ansible.com
    port: 5080
    priority: 10
    target: service1.ansible.com
    weight: 10
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
  - ['Blair Rampling (@brampling)']
