# Ansible module: ansible.module_nxos_igmp_interface


Manages IGMP interface configuration

## Description

Manages IGMP interface configuration settings.

## Requirements

TODO

## Arguments

``` json
{
    "group_timeout": "{'description': ["Sets the group membership timeout for IGMPv2. Values can range from 3 to 65,535 seconds or keyword 'default'. The default is 260 seconds."]}",
    "immediate_leave": "{'description': ['Enables the device to remove the group entry from the multicast routing table immediately upon receiving a leave message for the group. Use this command to minimize the leave latency of IGMPv2 group memberships on a given IGMP interface because the device does not send group-specific queries. The default is disabled.'], 'type': 'bool'}",
    "interface": "{'description': ['The full interface name for IGMP configuration. e.g. I(Ethernet1/2).'], 'required': True}",
    "last_member_qrt": "{'description': ["Sets the query interval waited after sending membership reports before the software deletes the group state. Values can range from 1 to 25 seconds or keyword 'default'. The default is 1 second."]}",
    "last_member_query_count": "{'description': ["Sets the number of times that the software sends an IGMP query in response to a host leave message. Values can range from 1 to 5 or keyword 'default'. The default is 2."]}",
    "oif_prefix": "{'description': ['This argument is deprecated, please use oif_ps instead. Configure a prefix for static outgoing interface (OIF).']}",
    "oif_ps": "{'description': ["Configure prefixes and sources for static outgoing interface (OIF). This is a list of dict where each dict has source and prefix defined or just prefix if source is not needed. The specified values will be configured on the device and if any previous prefix/sources exist, they will be removed. Keyword 'default' is also accpted which removes all existing prefix/sources."], 'version_added': 2.6}",
    "oif_routemap": "{'description': ["Configure a routemap for static outgoing interface (OIF) or keyword 'default'."]}",
    "oif_source": "{'description': ['This argument is deprecated, please use oif_ps instead. Configure a source for static outgoing interface (OIF).']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "querier_timeout": "{'description': ["Sets the querier timeout that the software uses when deciding to take over as the querier. Values can range from 1 to 65535 seconds or keyword 'default'. The default is 255 seconds."]}",
    "query_interval": "{'description': ["Sets the frequency at which the software sends IGMP host query messages. Values can range from 1 to 18000 seconds or keyword 'default'. The default is 125 seconds."]}",
    "query_mrt": "{'description': ["Sets the response time advertised in IGMP queries. Values can range from 1 to 25 seconds or keyword 'default'. The default is 10 seconds."]}",
    "report_llg": "{'description': ['Configures report-link-local-groups. Enables sending reports for groups in 224.0.0.0/24. Reports are always sent for nonlink local groups. By default, reports are not sent for link local groups.'], 'type': 'bool'}",
    "restart": "{'description': ['Restart IGMP. This is NOT idempotent as this is action only.'], 'type': 'bool', 'default': False}",
    "robustness": "{'description': ["Sets the robustness variable. Values can range from 1 to 7 or keyword 'default'. The default is 2."]}",
    "startup_query_count": "{'description': ["Query count used when the IGMP process starts up. The range is from 1 to 10 or keyword 'default'. The default is 2."]}",
    "startup_query_interval": "{'description': ["Query interval used when the IGMP process starts up. The range is from 1 to 18000 or keyword 'default'. The default is 31."]}",
    "state": "{'description': ['Manages desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent', 'default']}",
    "version": "{'description': ["IGMP version. It can be 2 or 3 or keyword 'default'."], 'choices': ['2', '3', 'default']}",
}
```

## Examples


``` yaml

- nxos_igmp_interface:
    interface: ethernet1/32
    startup_query_interval: 30
    oif_ps:
      - { 'prefix': '238.2.2.6' }
      - { 'source': '192.168.0.1', 'prefix': '238.2.2.5'}
    state: present

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
