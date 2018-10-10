# Ansible module: ansible.module_junos_facts


Collect facts from remote devices running Juniper Junos

## Description

Collects fact information from a remote device running the Junos operating system.  By default, the module will collect basic fact information from the device to be included with the hostvars. Additional fact information can be collected based on the configured set of arguments.

## Requirements

TODO

## Arguments

``` json
{
    "config_format": "{'description': ['The I(config_format) argument specifies the format of the configuration when serializing output from the device. This argument is applicable only when C(config) value is present in I(gather_subset). The I(config_format) should be supported by the junos version running on device. This value is not applicable while fetching old style facts that is when C(ofacts) value is present in value if I(gather_subset) value.'], 'required': False, 'default': 'text', 'choices': ['xml', 'text', 'set', 'json'], 'version_added': '2.3'}",
    "gather_subset": "{'description': ["When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected. To maintain backward compatbility old style facts can be retrieved by explicilty adding C(ofacts)  to value, this reqires junos-eznc to be installed as a prerequisite. Valid value of gather_subset are default, hardware, config, interfaces, ofacts. If C(ofacts) is present in the list it fetches the old style facts (fact keys without 'ansible_' prefix) and it requires junos-eznc library to be installed on control node and the device login credentials must be given in C(provider) option."], 'required': False, 'default': ['!config', '!ofacts'], 'version_added': '2.3'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
}
```

## Examples


``` yaml

- name: collect default set of facts
  junos_facts:

- name: collect default set of facts and configuration
  junos_facts:
    gather_subset: config

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
