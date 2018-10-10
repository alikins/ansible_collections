# Ansible module: ansible.module_nxos_snapshot


Manage snapshots of the running states of selected features

## Description

Create snapshots of the running states of selected features, add new show commands for snapshot creation, delete and compare existing snapshots.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Define what snapshot action the module would perform.'], 'required': True, 'choices': ['add', 'compare', 'create', 'delete', 'delete_all']}",
    "compare_option": "{'description': ['Snapshot options to be used when C(action=compare).'], 'choices': ['summary', 'ipv4routes', 'ipv6routes']}",
    "comparison_results_file": "{'description': ['Name of the file where snapshots comparison will be stored when C(action=compare).']}",
    "description": "{'description': ['Snapshot description to be used when C(action=create).']}",
    "element_key1": "{'description': ['Specify the tags used to distinguish among row entries, to be used when C(action=add).']}",
    "element_key2": "{'description': ['Specify the tags used to distinguish among row entries, to be used when C(action=add).']}",
    "path": "{'description': ['Specify the path of the file where new created snapshot or snapshots comparison will be stored, to be used when C(action=create) and C(save_snapshot_locally=true) or C(action=compare).'], 'default': './'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "row_id": "{'description': ["Specifies the tag of each row entry of the show command's XML output, to be used when C(action=add)."]}",
    "save_snapshot_locally": "{'description': ['Specify to locally store a new created snapshot, to be used when C(action=create).'], 'type': 'bool', 'default': False}",
    "section": "{'description': ['Used to name the show command output, to be used when C(action=add).']}",
    "show_command": "{'description': ['Specify a new show command, to be used when C(action=add).']}",
    "snapshot1": "{'description': ['First snapshot to be used when C(action=compare).']}",
    "snapshot2": "{'description': ['Second snapshot to be used when C(action=compare).']}",
    "snapshot_name": "{'description': ['Snapshot name, to be used when C(action=create) or C(action=delete).']}",
}
```

## Examples


``` yaml

# Create a snapshot and store it locally
- nxos_snapshot:
    action: create
    snapshot_name: test_snapshot
    description: Done with Ansible
    save_snapshot_locally: true
    path: /home/user/snapshots/

# Delete a snapshot
- nxos_snapshot:
    action: delete
    snapshot_name: test_snapshot

# Delete all existing snapshots
- nxos_snapshot:
    action: delete_all

# Add a show command for snapshots creation
- nxos_snapshot:
    section: myshow
    show_command: show ip interface brief
    row_id: ROW_intf
    element_key1: intf-name

# Compare two snapshots
- nxos_snapshot:
    action: compare
    snapshot1: pre_snapshot
    snapshot2: post_snapshot
    comparison_results_file: compare_snapshots.txt
    compare_option: summary
    path: '../snapshot_reports/'

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
