# Ansible module: ansible.module_nxos_interface_ospf


Manages configuration of an OSPF interface instance

## Description

Manages configuration of an OSPF interface instance.

## Requirements

TODO

## Arguments

``` json
{
    "area": "{'description': ['Ospf area associated with this cisco_interface_ospf instance. Valid values are a string, formatted as an IP address (i.e. "0.0.0.0") or as an integer.'], 'required': True}",
    "cost": "{'description': ['The cost associated with this cisco_interface_ospf instance.']}",
    "dead_interval": "{'description': ["Time interval an ospf neighbor waits for a hello packet before tearing down adjacencies. Valid values are an integer or the keyword 'default'."]}",
    "hello_interval": "{'description': ["Time between sending successive hello packets. Valid values are an integer or the keyword 'default'."]}",
    "interface": "{'description': ['Name of this cisco_interface resource. Valid value is a string.'], 'required': True}",
    "message_digest": "{'description': ['Enables or disables the usage of message digest authentication.'], 'type': 'bool'}",
    "message_digest_algorithm_type": "{'description': ["Algorithm used for authentication among neighboring routers within an area. Valid values are 'md5' and 'default'."], 'choices': ['md5', 'default']}",
    "message_digest_encryption_type": "{'description': ["Specifies the scheme used for encrypting message_digest_password. Valid values are '3des' or 'cisco_type_7' encryption or 'default'."], 'choices': ['cisco_type_7', '3des', 'default']}",
    "message_digest_key_id": "{'description': ["Md5 authentication key-id associated with the ospf instance. If this is present, message_digest_encryption_type, message_digest_algorithm_type and message_digest_password are mandatory. Valid value is an integer and 'default'."]}",
    "message_digest_password": "{'description': ['Specifies the message_digest password. Valid value is a string.']}",
    "network": "{'description': ["Specifies interface ospf network type. Valid values are 'point-to-point' or 'broadcast'."], 'choices': ['point-to-point', 'broadcast'], 'version_added': '2.8'}",
    "ospf": "{'description': ['Name of the ospf instance.'], 'required': True}",
    "passive_interface": "{'description': ['Setting to true will prevent this interface from receiving HELLO packets.'], 'type': 'bool'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- nxos_interface_ospf:
    interface: ethernet1/32
    ospf: 1
    area: 1
    cost: default

- nxos_interface_ospf:
    interface: loopback0
    ospf: prod
    area: 0.0.0.0
    network: point-to-point
    state: present

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
