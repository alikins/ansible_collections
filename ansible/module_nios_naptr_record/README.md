# Ansible module: ansible.module_nios_naptr_record


Configure Infoblox NIOS NAPTR records

## Description

Adds and/or removes instances of NAPTR record objects from Infoblox NIOS servers.  This module manages NIOS C(record:naptr) objects using the Infoblox WAPI interface over REST.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "flags": "{'description': ['Configures the flags field for this NAPTR record. These control the interpretation of the fields for an NAPTR record object. Supported values for the flags field are "U", "S", "P" and "A".'], 'required': False}",
    "name": "{'description': ['Specifies the fully qualified hostname to add or remove from the system'], 'required': True}",
    "order": "{'description': ['Configures the order (0-65535) for this NAPTR record. This parameter specifies the order in which the NAPTR rules are applied when multiple rules are present.'], 'required': True}",
    "preference": "{'description': ['Configures the preference (0-65535) for this NAPTR record. The preference field determines the order NAPTR records are processed when multiple records with the same order parameter are present.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "regexp": "{'description': ['Configures the regexp field for this NAPTR record. This is the regular expression-based rewriting rule of the NAPTR record. This should be a POSIX compliant regular expression, including the substitution rule and flags. Refer to RFC 2915 for the field syntax details.'], 'required': False}",
    "replacement": "{'description': ['Configures the replacement field for this NAPTR record. For nonterminal NAPTR records, this field specifies the next domain name to look up.'], 'required': True}",
    "services": "{'description': ['Configures the services field (128 characters maximum) for this NAPTR record. The services field contains protocol and service identifiers, such as "http+E2U" or "SIPS+D2T".'], 'required': False}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "ttl": "{'description': ['Configures the TTL to be associated with this NAPTR record']}",
    "view": "{'description': ['Sets the DNS view to associate this a record with. The DNS view must already be configured on the system'], 'required': True, 'default': 'default', 'aliases': ['dns_view']}",
}
```

## Examples


``` yaml

- name: configure a NAPTR record
  nios_naptr_record:
    name: '*.subscriber-100.ansiblezone.com'
    order: 1000
    preference: 10
    replacement: replacement1.network.ansiblezone.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: add a comment to an existing NAPTR record
  nios_naptr_record:
    name: '*.subscriber-100.ansiblezone.com'
    order: 1000
    preference: 10
    replacement: replacement1.network.ansiblezone.com
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: remove a NAPTR record from the system
  nios_naptr_record:
    name: '*.subscriber-100.ansiblezone.com'
    order: 1000
    preference: 10
    replacement: replacement1.network.ansiblezone.com
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
