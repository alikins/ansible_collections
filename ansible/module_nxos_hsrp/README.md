# Ansible module: ansible.module_nxos_hsrp


Manages HSRP configuration on NX-OS switches

## Description

Manages HSRP configuration on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "auth_string": "{'description': ["Authentication string. If this needs to be hidden(for md5 type), the string should be 7 followed by the key string. Otherwise, it can be 0 followed by key string or just key string (for backward compatibility). For text type, this should be just be a key string. if this is 'default', authentication is removed."]}",
    "auth_type": "{'description': ['Authentication type.'], 'choices': ['text', 'md5']}",
    "group": "{'description': ['HSRP group number.'], 'required': True}",
    "interface": "{'description': ['Full name of interface that is being managed for HSRP.'], 'required': True}",
    "preempt": "{'description': ['Enable/Disable preempt.'], 'choices': ['enabled', 'disabled']}",
    "priority": "{'description': ["HSRP priority or keyword 'default'."]}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "state": "{'description': ['Specify desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "version": "{'description': ['HSRP version.'], 'default': 1, 'choices': ['1', '2']}",
    "vip": "{'description': ["HSRP virtual IP address or keyword 'default'"]}",
}
```

## Examples


``` yaml

- name: Ensure HSRP is configured with following params on a SVI
  nxos_hsrp:
    group: 10
    vip: 10.1.1.1
    priority: 150
    interface: vlan10
    preempt: enabled
    host: 68.170.147.165

- name: Ensure HSRP is configured with following params on a SVI
        with clear text authentication
  nxos_hsrp:
    group: 10
    vip: 10.1.1.1
    priority: 150
    interface: vlan10
    preempt: enabled
    host: 68.170.147.165
    auth_type: text
    auth_string: CISCO

- name: Ensure HSRP is configured with md5 authentication and clear
        authentication string
  nxos_hsrp:
    group: 10
    vip: 10.1.1.1
    priority: 150
    interface: vlan10
    preempt: enabled
    host: 68.170.147.165
    auth_type: md5
    auth_string: "0 1234"

- name: Ensure HSRP is configured with md5 authentication and hidden
        authentication string
  nxos_hsrp:
    group: 10
    vip: 10.1.1.1
    priority: 150
    interface: vlan10
    preempt: enabled
    host: 68.170.147.165
    auth_type: md5
    auth_string: "7 1234"

- name: Remove HSRP config for given interface, group, and VIP
  nxos_hsrp:
    group: 10
    interface: vlan10
    vip: 10.1.1.1
    host: 68.170.147.165
    state: absent

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
