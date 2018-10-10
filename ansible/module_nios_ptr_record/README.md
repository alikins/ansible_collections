# Ansible module: ansible.module_nios_ptr_record


Configure Infoblox NIOS PTR records

## Description

Adds and/or removes instances of PTR record objects from Infoblox NIOS servers.  This module manages NIOS C(record:ptr) objects using the Infoblox WAPI interface over REST.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance. Maximum 256 characters.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "ipv4addr": "{'description': ['The IPv4 Address of the record. Mutually exclusive with the ipv6addr.'], 'required': True, 'aliases': ['ipv4']}",
    "ipv6addr": "{'description': ['The IPv6 Address of the record. Mutually exclusive with the ipv4addr.'], 'required': True, 'aliases': ['ipv6']}",
    "name": "{'description': ['The name of the DNS PTR record in FQDN format to add or remove from the system. The field is required only for an PTR object in Forward Mapping Zone.'], 'required': False}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "ptrdname": "{'description': ['The domain name of the DNS PTR record in FQDN format.'], 'required': True}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['Time To Live (TTL) value for the record. A 32-bit unsigned integer that represents the duration, in seconds, that the record is valid (cached). Zero indicates that the record should not be cached.']}",
    "view": "{'description': ['Sets the DNS view to associate this a record with. The DNS view must already be configured on the system'], 'required': False, 'aliases': ['dns_view']}",
}
```

## Examples


``` yaml

- name: Create a PTR Record
  nios_ptr_record:
    ipv4: 192.168.10.1
    ptrdname: host.ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Delete a PTR Record
  nios_ptr_record:
    ipv4: 192.168.10.1
    ptrdname: host.ansible.com
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
  - ['Trebuchet Clement']
