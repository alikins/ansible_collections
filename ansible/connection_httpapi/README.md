# Ansible connection: ansible.connection_httpapi


Use httpapi to run command on network appliances

## Description

This connection plugin provides a connection to remote devices over a HTTP(S)-based api.

## Requirements

TODO

## Arguments

``` json
{
    "become": "{'type': 'boolean', 'description': ['The become option will instruct the CLI session to attempt privilege escalation on platforms that support it.  Normally this means transitioning from user mode to C(enable) mode in the CLI session. If become is set to True and the remote device does not support privilege escalation or the privilege has already been elevated, then this option is silently ignored.', 'Can be configured from the CLI via the C(--become) or C(-b) options.'], 'default': False, 'ini': [{'section': 'privilege_escalation', 'key': 'become'}], 'env': [{'name': 'ANSIBLE_BECOME'}], 'vars': [{'name': 'ansible_become'}]}",
    "become_method": "{'description': ['This option allows the become method to be specified in for handling privilege escalation.  Typically the become_method value is set to C(enable) but could be defined as other values.'], 'default': 'sudo', 'ini': [{'section': 'privilege_escalation', 'key': 'become_method'}], 'env': [{'name': 'ANSIBLE_BECOME_METHOD'}], 'vars': [{'name': 'ansible_become_method'}]}",
    "host": "{'description': ['Specifies the remote device FQDN or IP address to establish the HTTP(S) connection to.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}]}",
    "network_os": "{'description': ['Configures the device platform network operating system.  This value is used to load the correct httpapi and cliconf plugins to communicate with the remote device'], 'vars': [{'name': 'ansible_network_os'}]}",
    "password": "{'description': ['Configures the user password used to authenticate to the remote device when needed for the device API.'], 'vars': [{'name': 'ansible_password'}, {'name': 'ansible_httpapi_pass'}]}",
    "persistent_command_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait for a command to return from the remote device.  If this timer is exceeded before the command returns, the connection plugin will raise an exception and close.'], 'default': 10, 'ini': [{'section': 'persistent_connection', 'key': 'command_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_COMMAND_TIMEOUT'}], 'vars': [{'name': 'ansible_command_timeout'}]}",
    "persistent_connect_timeout": "{'type': 'int', 'description': ['Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection.  If this value expires before the connection to the remote device is completed, the connection will fail.'], 'default': 30, 'ini': [{'section': 'persistent_connection', 'key': 'connect_timeout'}], 'env': [{'name': 'ANSIBLE_PERSISTENT_CONNECT_TIMEOUT'}]}",
    "port": "{'type': 'int', 'description': ['Specifies the port on the remote device that listens for connections when establishing the HTTP(S) connection.', 'When unspecified, will pick 80 or 443 based on the value of use_ssl.'], 'ini': [{'section': 'defaults', 'key': 'remote_port'}], 'env': [{'name': 'ANSIBLE_REMOTE_PORT'}], 'vars': [{'name': 'ansible_httpapi_port'}]}",
    "remote_user": "{'description': ['The username used to authenticate to the remote device when the API connection is first established.  If the remote_user is not specified, the connection will use the username of the logged in user.', 'Can be configured from the CLI via the C(--user) or C(-u) options.'], 'ini': [{'section': 'defaults', 'key': 'remote_user'}], 'env': [{'name': 'ANSIBLE_REMOTE_USER'}], 'vars': [{'name': 'ansible_user'}]}",
    "timeout": "{'type': 'int', 'description': ['Sets the connection time, in seconds, for communicating with the remote device.  This timeout is used as the default timeout value for commands when issuing a command to the network CLI.  If the command does not return in timeout seconds, an error is generated.'], 'default': 120}",
    "use_ssl": "{'type': 'boolean', 'description': ['Whether to connect using SSL (HTTPS) or not (HTTP).'], 'default': False, 'vars': [{'name': 'ansible_httpapi_use_ssl'}]}",
    "validate_certs": "{'type': 'boolean', 'version_added': '2.7', 'description': ['Whether to validate SSL certificates'], 'default': True, 'vars': [{'name': 'ansible_httpapi_validate_certs'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Networking Team']
