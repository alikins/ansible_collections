# Ansible connection: ansible.connection_napalm


Provides persistent connection using NAPALM

## Description

This connection plugin provides connectivity to network devices using the NAPALM network device abstraction library.  This library requires certain features to be enabled on network devices depending on the destination device operating system.  The connection plugin requires C(napalm) to be installed locally on the Ansible controller.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['Specifies the remote device FQDN or IP address to establish the SSH connection to.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}]}",
    "host_key_auto_add": "{'type': 'boolean', 'description': ['By default, Ansible will prompt the user before adding SSH keys to the known hosts file. By enabling this option, unknown host keys will automatically be added to the known hosts file.', 'Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.'], 'default': False, 'ini': [{'section': 'paramiko_connection', 'key': 'host_key_auto_add'}], 'env': [{'name': 'ANSIBLE_HOST_KEY_AUTO_ADD'}]}",
    "network_os": "{'description': ['Configures the device platform network operating system.  This value is used to load a napalm device abstraction.'], 'vars': [{'name': 'ansible_network_os'}]}",
    "password": "{'description': ['Configures the user password used to authenticate to the remote device when first establishing the SSH connection.'], 'vars': [{'name': 'ansible_password'}, {'name': 'ansible_ssh_pass'}]}",
    "persistent_command_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait for a command to return from the remote device.  If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.'], 'default': 10, 'ini': [{'section': 'persistent_connection', 'key': 'command_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_COMMAND_TIMEOUT'}], 'vars': [{'name': 'ansible_command_timeout'}]}",
    "persistent_connect_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection.  If this value expires before the connection to the remote device is completed, the connection will fail.'], 'default': 30, 'ini': [{'section': 'persistent_connection', 'key': 'connect_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_CONNECT_TIMEOUT'}]}",
    "port": "{'type': 'int', 'description': ['Specifies the port on the remote device that listens for connections when establishing the SSH connection.'], 'default': 22, 'ini': [{'section': 'defaults', 'key': 'remote_port'}], 'env': [{'name': 'ANSIBLE_REMOTE_PORT'}], 'vars': [{'name': 'ansible_port'}]}",
    "private_key_file": "{'description': ['The private SSH key or certificate file used to authenticate to the remote device when first establishing the SSH connection.'], 'ini': [{'section': 'defaults', 'key': 'private_key_file'}], 'env': [{'name': 'ANSIBLE_PRIVATE_KEY_FILE'}], 'vars': [{'name': 'ansible_private_key_file'}]}",
    "remote_user": "{'description': ['The username used to authenticate to the remote device when the SSH connection is first established.  If the remote_user is not specified, the connection will use the username of the logged in user.', 'Can be configured from the CLI via the C(--user) or C(-u) options.'], 'ini': [{'section': 'defaults', 'key': 'remote_user'}], 'env': [{'name': 'ANSIBLE_REMOTE_USER'}], 'vars': [{'name': 'ansible_user'}]}",
    "timeout": "{'type': 'int', 'description': ['Sets the connection time, in seconds, for communicating with the remote device.  This timeout is used as the default timeout value for commands when issuing a command to the network CLI.  If the command does not return in timeout seconds, an error is generated.'], 'default': 120}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Networking Team']
