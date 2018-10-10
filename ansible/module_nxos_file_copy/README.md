# Ansible module: ansible.module_nxos_file_copy


Copy a file to a remote NXOS device

## Description

This module supports two different workflows for copying a file to flash (or bootflash) on NXOS devices.  Files can either be (1) pushed from the Ansible controller to the device or (2) pulled from a remote SCP file server to the device.  File copies are initiated from the NXOS device to the remote SCP server.  This module only supports the use of connection C(network_cli) or C(Cli) transport with connection C(local).

## Requirements

TODO

## Arguments

``` json
{
    "connect_ssh_port": "{'description': ['SSH port to connect to server during transfer of file'], 'default': 22, 'version_added': '2.5'}",
    "file_pull": "{'description': ['When (False) file is copied from the Ansible controller to the NXOS device.', 'When (True) file is copied from a remote SCP server to the NXOS device. In this mode, the file copy is initiated from the NXOS device.', 'If the file is already present on the device it will be overwritten and therefore the operation is NOT idempotent.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "file_pull_timeout": "{'description': ['Use this parameter to set timeout in seconds, when transferring large files or when the network is slow.'], 'default': 300, 'version_added': '2.7'}",
    "file_system": "{'description': ['The remote file system of the device. If omitted, devices that support a I(file_system) parameter will use their default values.'], 'default': 'bootflash:'}",
    "local_file": "{'description': ['When (file_pull is False) this is the path to the local file on the Ansible controller. The local directory must exist.', 'When (file_pull is True) this is the file name used on the NXOS device.']}",
    "local_file_directory": "{'description': ['When (file_pull is True) file is copied from a remote SCP server to the NXOS device, and written to this directory on the NXOS device. If the directory does not exist, it will be created under the file_system. This is an optional parameter.', 'When (file_pull is False), this not used.'], 'version_added': '2.7'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "remote_file": "{'description': ['When (file_pull is False) this is the remote file path on the NXOS device. If omitted, the name of the local file will be used. The remote directory must exist.', 'When (file_pull is True) this is the full path to the file on the remote SCP server to be copied to the NXOS device.']}",
    "remote_scp_server": "{'description': ['The remote scp server address which is used to pull the file. This is required if file_pull is True.'], 'version_added': '2.7'}",
    "remote_scp_server_password": "{'description': ['The remote scp server password which is used to pull the file. This is required if file_pull is True.'], 'version_added': '2.7'}",
    "remote_scp_server_user": "{'description': ['The remote scp server username which is used to pull the file. This is required if file_pull is True.'], 'version_added': '2.7'}",
}
```

## Examples


``` yaml

# File copy from ansible controller to nxos device
  - name: "copy from server to device"
    nxos_file_copy:
      local_file: "./test_file.txt"
      remote_file: "test_file.txt"

# Initiate file copy from the nxos device to transfer file from an SCP server back to the nxos device
  - name: "initiate file copy from device"
    nxos_file_copy:
      nxos_file_copy:
      file_pull: True
      local_file: "xyz"
      local_filr_directory: "dir1/dir2/dir3"
      remote_file: "/mydir/abc"
      remote_scp_server: "192.168.0.1"
      remote_scp_server_user: "myUser"
      remote_scp_server_password: "myPassword"

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
