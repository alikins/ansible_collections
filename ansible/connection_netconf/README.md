# Ansible connection: ansible.connection_netconf


Provides a persistent connection using the netconf protocol

## Description

This connection plugin provides a connection to remote devices over the SSH NETCONF subsystem.  This connection plugin is typically used by network devices for sending and receiving RPC calls over NETCONF.
Note this connection plugin requires ncclient to be installed on the local Ansible controller.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['Specifies the remote device FQDN or IP address to establish the SSH connection to.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}]}",
    "host_key_auto_add": "{'type': 'boolean', 'description': ['By default, Ansible will prompt the user before adding SSH keys to the known hosts file. By enabling this option, unknown host keys will automatically be added to the known hosts file.', 'Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.'], 'default': False, 'ini': [{'section': 'paramiko_connection', 'key': 'host_key_auto_add'}], 'env': [{'name': 'ANSIBLE_HOST_KEY_AUTO_ADD'}]}",
    "host_key_checking": "{'description': ['Set this to "False" if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host'], 'type': 'boolean', 'default': True, 'env': [{'name': 'ANSIBLE_HOST_KEY_CHECKING'}, {'name': 'ANSIBLE_SSH_HOST_KEY_CHECKING'}, {'name': 'ANSIBLE_NETCONF_HOST_KEY_CHECKING'}], 'ini': [{'section': 'defaults', 'key': 'host_key_checking'}, {'section': 'paramiko_connection', 'key': 'host_key_checking'}], 'vars': [{'name': 'ansible_host_key_checking'}, {'name': 'ansible_ssh_host_key_checking'}, {'name': 'ansible_netconf_host_key_checking'}]}",
    "look_for_keys": "{'default': True, 'description': ['Enables looking for ssh keys in the usual locations for ssh keys (e.g. :file:`~/.ssh/id_*`).'], 'env': [{'name': 'ANSIBLE_PARAMIKO_LOOK_FOR_KEYS'}], 'ini': [{'section': 'paramiko_connection', 'key': 'look_for_keys'}], 'type': 'boolean'}",
    "netconf_ssh_config": "{'description': ['This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.'], 'ini': [{'section': 'netconf_connection', 'key': 'ssh_config', 'version_added': '2.7'}], 'env': [{'name': 'ANSIBLE_NETCONF_SSH_CONFIG'}], 'vars': [{'name': 'ansible_netconf_ssh_config', 'version_added': '2.7'}]}",
    "network_os": "{'description': ['Configures the device platform network operating system.  This value is used to load a device specific netconf plugin.  If this option is not configured, then the default netconf plugin will be used.'], 'vars': [{'name': 'ansible_network_os'}]}",
    "password": "{'description': ['Configures the user password used to authenticate to the remote device when first establishing the SSH connection.'], 'vars': [{'name': 'ansible_password'}, {'name': 'ansible_ssh_pass'}]}",
    "persistent_command_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait for a command to return from the remote device.  If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.'], 'default': 10, 'ini': [{'section': 'persistent_connection', 'key': 'command_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_COMMAND_TIMEOUT'}], 'vars': [{'name': 'ansible_command_timeout'}]}",
    "persistent_connect_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection.  If this value expires before the connection to the remote device is completed, the connection will fail.'], 'default': 30, 'ini': [{'section': 'persistent_connection', 'key': 'connect_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_CONNECT_TIMEOUT'}]}",
    "port": "{'type': 'int', 'description': ['Specifies the port on the remote device that listens for connections when establishing the SSH connection.'], 'default': 830, 'ini': [{'section': 'defaults', 'key': 'remote_port'}], 'env': [{'name': 'ANSIBLE_REMOTE_PORT'}], 'vars': [{'name': 'ansible_port'}]}",
    "private_key_file": "{'description': ['The private SSH key or certificate file used to authenticate to the remote device when first establishing the SSH connection.'], 'ini': [{'section': 'defaults', 'key': 'private_key_file'}], 'env': [{'name': 'ANSIBLE_PRIVATE_KEY_FILE'}], 'vars': [{'name': 'ansible_private_key_file'}]}",
    "remote_user": "{'description': ['The username used to authenticate to the remote device when the SSH connection is first established.  If the remote_user is not specified, the connection will use the username of the logged in user.', 'Can be configured from the CLI via the C(--user) or C(-u) options.'], 'ini': [{'section': 'defaults', 'key': 'remote_user'}], 'env': [{'name': 'ANSIBLE_REMOTE_USER'}], 'vars': [{'name': 'ansible_user'}]}",
    "timeout": "{'type': 'int', 'description': ['Sets the connection time, in seconds, for communicating with the remote device.  This timeout is used as the default timeout value when awaiting a response after issuing a call to a RPC.  If the RPC does not return in timeout seconds, an error is generated.'], 'default': 120}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Networking Team']
