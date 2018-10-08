# Ansible connection: ansible.connection_winrm


Run tasks over Microsoft's WinRM

## Description

Run commands or put/fetch on a target via WinRM
This plugin allows extra arguments to be passed that are supported by the protocol but not explicitly defined here. They should take the form of variables declared with the following pattern `ansible_winrm_<option>`.

## Requirements

TODO

## Arguments

``` json
{
    "connection_timeout": "{'description': ['Sets the operation and read timeout settings for the WinRM connection.', 'Corresponds to the C(operation_timeout_sec) and C(read_timeout_sec) args in pywinrm so avoid setting these vars with this one.', 'The default value is whatever is set in the installed version of pywinrm.'], 'vars': [{'name': 'ansible_winrm_connection_timeout'}]}",
    "kerberos_command": "{'description': ['kerberos command to use to request a authentication ticket'], 'default': 'kinit', 'vars': [{'name': 'ansible_winrm_kinit_cmd'}]}",
    "kerberos_mode": "{'description': ['kerberos usage mode.', 'The managed option means Ansible will obtain kerberos ticket.', 'While the manual one means a ticket must already have been obtained by the user.', 'If having issues with Ansible freezing when trying to obtain the Kerberos ticket, you can either set this to C(manual) and obtain it outside Ansible or install C(pexpect) through pip and try again.'], 'choices': ['managed', 'manual'], 'vars': [{'name': 'ansible_winrm_kinit_mode'}]}",
    "path": "{'description': ['URI path to connect to'], 'default': '/wsman', 'vars': [{'name': 'ansible_winrm_path'}]}",
    "port": "{'description': ['port for winrm to connect on remote target', 'The default is the https (5986) port, if using http it should be 5985'], 'vars': [{'name': 'ansible_port'}, {'name': 'ansible_winrm_port'}], 'default': 5986, 'keywords': [{'name': 'port'}], 'type': 'integer'}",
    "remote_addr": "{'description': ['Address of the windows machine'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_winrm_host'}]}",
    "remote_user": "{'keywords': [{'name': 'user'}, {'name': 'remote_user'}], 'description': ['The user to log in as to the Windows machine'], 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_winrm_user'}]}",
    "scheme": "{'description': ['URI scheme to use', 'If not set, then will default to C(https) or C(http) if I(port) is C(5985).'], 'choices': ['http', 'https'], 'vars': [{'name': 'ansible_winrm_scheme'}]}",
    "transport": "{'description': ['List of winrm transports to attempt to to use (ssl, plaintext, kerberos, etc)', 'If None (the default) the plugin will try to automatically guess the correct list', 'The choices avialable depend on your version of pywinrm'], 'type': 'list', 'vars': [{'name': 'ansible_winrm_transport'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
