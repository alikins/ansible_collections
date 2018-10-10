# Ansible module: ansible.module_junos_scp


Transfer files from or to remote devices running Junos

## Description

This module transfers files via SCP from or to remote devices running Junos.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['The C(dest) argument specifies the path in which to receive the files.'], 'default': '.'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "recursive": "{'description': ['The C(recursive) argument enables recursive transfer of files and directories.'], 'type': 'bool', 'default': False}",
    "remote_src": "{'description': ['The C(remote_src) argument enables the download of files (I(scp get)) from the remote device. The default behavior is to upload files (I(scp put)) to the remote device.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['The C(src) argument takes a single path, or a list of paths to be transfered. The argument C(recursive) must be C(true) to transfer directories.'], 'required': True}",
}
```

## Examples


``` yaml

# the required set of connection arguments have been purposely left off
# the examples for brevity
- name: upload local file to home directory on remote device
  junos_scp:
    src: test.tgz

- name: upload local file to tmp directory on remote device
  junos_scp:
    src: test.tgz
    dest: /tmp/

- name: download file from remote device
  junos_scp:
    src: test.tgz
    remote_src: true

```

## License

TODO

## Author Information
  - ['Christian Giese (@GIC-de)']
