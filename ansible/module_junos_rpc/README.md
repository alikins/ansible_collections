# Ansible module: ansible.module_junos_rpc


Runs an arbitrary RPC over NetConf on an Juniper JUNOS device

## Description

Sends a request to the remote device running JUNOS to execute the specified RPC using the NetConf transport.  The reply is then returned to the playbook in the C(xml) key.  If an alternate output format is requested, the reply is transformed to the requested output.

## Requirements

TODO

## Arguments

``` json
{
    "args": "{'description': ['The C(args) argument provides a set of arguments for the RPC call and are encoded in the request message.  This argument accepts a set of key=value arguments.']}",
    "attrs": "{'description': ['The C(attrs) arguments defines a list of attributes and their values to set for the RPC call. This accepts a dictionary of key-values.'], 'version_added': '2.5'}",
    "output": "{'description': ['The C(output) argument specifies the desired output of the return data.  This argument accepts one of C(xml), C(text), or C(json).  For C(json), the JUNOS device must be running a version of software that supports native JSON output.'], 'default': 'xml'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "rpc": "{'description': ['The C(rpc) argument specifies the RPC call to send to the remote devices to be executed.  The RPC Reply message is parsed and the contents are returned to the playbook.'], 'required': True}",
}
```

## Examples


``` yaml

- name: collect interface information using rpc
  junos_rpc:
    rpc: get-interface-information
    args:
      interface-name: em0
      media: True

- name: get system information
  junos_rpc:
    rpc: get-system-information

- name: load configuration
  junos_rpc:
    rpc: load-configuration
    attrs:
      action: override
      url: /tmp/config.conf

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
