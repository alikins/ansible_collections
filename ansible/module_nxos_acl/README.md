# Ansible module: ansible.module_nxos_acl


Manages access list entries for ACLs

## Description

Manages access list entries for ACLs.

## Requirements

TODO

## Arguments

``` json
{
    "ack": "{'description': ['Match on the ACK bit.'], 'choices': ['enable']}",
    "action": "{'description': ['Action of the ACE.'], 'choices': ['permit', 'deny', 'remark']}",
    "dest": "{'description': ["Destination ip and mask using IP/MASK notation and supports the keyword 'any'."]}",
    "dest_port1": "{'description': ['Port/protocol and also first (lower) port when using range operand.']}",
    "dest_port2": "{'description': ['Second (end) port when using range operand.']}",
    "dest_port_op": "{'description': ['Destination port operands such as eq, neq, gt, lt, range.'], 'choices': ['any', 'eq', 'gt', 'lt', 'neq', 'range']}",
    "dscp": "{'description': ['Match packets with given dscp value.'], 'choices': ['af11', 'af12', 'af13', 'af21', 'af22', 'af23', 'af31', 'af32', 'af33', 'af41', 'af42', 'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6', 'cs7', 'default', 'ef']}",
    "established": "{'description': ['Match established connections.'], 'choices': ['enable']}",
    "fin": "{'description': ['Match on the FIN bit.'], 'choices': ['enable']}",
    "fragments": "{'description': ['Check non-initial fragments.'], 'choices': ['enable']}",
    "log": "{'description': ['Log matches against this entry.'], 'choices': ['enable']}",
    "name": "{'description': ['Case sensitive name of the access list (ACL).'], 'required': True}",
    "precedence": "{'description': ['Match packets with given precedence.'], 'choices': ['critical', 'flash', 'flash-override', 'immediate', 'internet', 'network', 'priority', 'routine']}",
    "proto": "{'description': ['Port number or protocol (as supported by the switch).']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "psh": "{'description': ['Match on the PSH bit.'], 'choices': ['enable']}",
    "remark": "{'description': ['If action is set to remark, this is the description.']}",
    "rst": "{'description': ['Match on the RST bit.'], 'choices': ['enable']}",
    "seq": "{'description': ['Sequence number of the entry (ACE).']}",
    "src": "{'description': ["Source ip and mask using IP/MASK notation and supports keyword 'any'."]}",
    "src_port1": "{'description': ['Port/protocol and also first (lower) port when using range operand.']}",
    "src_port2": "{'description': ['Second (end) port when using range operand.']}",
    "src_port_op": "{'description': ['Source port operands such as eq, neq, gt, lt, range.'], 'choices': ['any', 'eq', 'gt', 'lt', 'neq', 'range']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'delete_acl']}",
    "syn": "{'description': ['Match on the SYN bit.'], 'choices': ['enable']}",
    "time_range": "{'description': ['Name of time-range to apply.']}",
    "urg": "{'description': ['Match on the URG bit.'], 'choices': ['enable']}",
}
```

## Examples


``` yaml

# configure ACL ANSIBLE
- nxos_acl:
    name: ANSIBLE
    seq: 10
    action: permit
    proto: tcp
    src: 192.0.2.1/24
    dest: any
    state: present

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
