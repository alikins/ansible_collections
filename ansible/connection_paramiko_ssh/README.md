# Ansible connection: ansible.connection_paramiko_ssh


Run tasks via python ssh (paramiko)

## Description

Use the python ssh implementation (Paramiko) to connect to targets
The paramiko transport is provided because many distributions, in particular EL6 and before do not support ControlPersist in their SSH implementations.
This is needed on the Ansible control machine to be reasonably efficient with connections. Thus paramiko is faster for most users on these platforms. Users with ControlPersist capability can consider using -c ssh or configuring the transport in the configuration file.
This plugin also borrows a lot of settings from the ssh plugin as they both cover the same protocol.

## Requirements

TODO

## Arguments

``` json
{
    "host_key_auto_add": "{'description': ['TODO: write it'], 'env': [{'name': 'ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD'}], 'ini': [{'key': 'host_key_auto_add', 'section': 'paramiko_connection'}], 'type': 'boolean'}",
    "host_key_checking": "{'description': ['Set this to "False" if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host'], 'type': 'boolean', 'default': True, 'env': [{'name': 'ANSIBLE_HOST_KEY_CHECKING'}, {'name': 'ANSIBLE_SSH_HOST_KEY_CHECKING', 'version_added': '2.5'}, {'name': 'ANSIBLE_PARAMIKO_HOST_KEY_CHECKING', 'version_added': '2.5'}], 'ini': [{'section': 'defaults', 'key': 'host_key_checking'}, {'section': 'paramiko_connection', 'key': 'host_key_checking', 'version_added': '2.5'}], 'vars': [{'name': 'ansible_host_key_checking', 'version_added': '2.5'}, {'name': 'ansible_ssh_host_key_checking', 'version_added': '2.5'}, {'name': 'ansible_paramiko_host_key_checking', 'version_added': '2.5'}]}",
    "look_for_keys": "{'default': True, 'description': ['TODO: write it'], 'env': [{'name': 'ANSIBLE_PARAMIKO_LOOK_FOR_KEYS'}], 'ini': [{'key': 'look_for_keys', 'section': 'paramiko_connection'}], 'type': 'boolean'}",
    "password": "{'description': ['Secret used to either login the ssh server or as a passphrase for ssh keys that require it', 'Can be set from the CLI via the C(--ask-pass) option.'], 'vars': [{'name': 'ansible_password'}, {'name': 'ansible_ssh_pass'}, {'name': 'ansible_paramiko_pass', 'version_added': '2.5'}]}",
    "proxy_command": "{'default': '', 'description': ['Proxy information for running the connection via a jumphost', "Also this plugin will scan 'ssh_args', 'ssh_extra_args' and 'ssh_common_args' from the 'ssh' plugin settings for proxy information if set."], 'env': [{'name': 'ANSIBLE_PARAMIKO_PROXY_COMMAND'}], 'ini': [{'key': 'proxy_command', 'section': 'paramiko_connection'}]}",
    "pty": "{'default': True, 'description': ['TODO: write it'], 'env': [{'name': 'ANSIBLE_PARAMIKO_PTY'}], 'ini': [{'section': 'paramiko_connection', 'key': 'pty'}], 'type': 'boolean'}",
    "record_host_keys": "{'default': True, 'description': ['TODO: write it'], 'env': [{'name': 'ANSIBLE_PARAMIKO_RECORD_HOST_KEYS'}], 'ini': [{'section': 'paramiko_connection', 'key': 'record_host_keys'}], 'type': 'boolean'}",
    "remote_addr": "{'description': ['Address of the remote target'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_ssh_host'}, {'name': 'ansible_paramiko_host'}]}",
    "remote_user": "{'description': ['User to login/authenticate as', 'Can be set from the CLI via the C(--user) or C(-u) options.'], 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_ssh_user'}, {'name': 'ansible_paramiko_user'}], 'env': [{'name': 'ANSIBLE_REMOTE_USER'}, {'name': 'ANSIBLE_PARAMIKO_REMOTE_USER', 'version_added': '2.5'}], 'ini': [{'section': 'defaults', 'key': 'remote_user'}, {'section': 'paramiko_connection', 'key': 'remote_user', 'version_added': '2.5'}]}",
    "use_persistent_connections": "{'description': ['Toggles the use of persistence for connections'], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_USE_PERSISTENT_CONNECTIONS'}], 'ini': [{'section': 'defaults', 'key': 'use_persistent_connections'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
