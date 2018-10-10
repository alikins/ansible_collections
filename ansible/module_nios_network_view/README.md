# Ansible module: ansible.module_nios_network_view


Configure Infoblox NIOS network views

## Description

Adds and/or removes instances of network view objects from Infoblox NIOS servers.  This module manages NIOS C(networkview) objects using the Infoblox WAPI interface over REST.
Updates instances of network view object from Infoblox NIOS servers.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Configures a text string comment to be associated with the instance of this object.  The provided text string will be configured on the object instance.']}",
    "extattrs": "{'description': ['Allows for the configuration of Extensible Attributes on the instance of the object.  This argument accepts a set of key / value pairs for configuration.']}",
    "name": "{'description': ['Specifies the fully qualified hostname to add or remove from the system. User can also update the hostname as it is possible to pass a dict containing I(new_name), I(old_name). See examples.'], 'required': True, 'aliases': ['network_view']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "state": "{'description': ['Configures the intended state of the instance of the object on the NIOS server.  When this value is set to C(present), the object is configured on the device and when this value is set to C(absent) the value is removed (if necessary) from the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure a new network view
  nios_network_view:
    name: ansible
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: update the comment for network view
  nios_network_view:
    name: ansible
    comment: this is an example comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: remove the network view
  nios_network_view:
    name: ansible
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
- name: update a existing network view
  nios_network_view:
    name: {new_name: ansible-new, old_name: ansible}
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
