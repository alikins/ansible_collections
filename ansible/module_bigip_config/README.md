# Ansible module: ansible.module_bigip_config


Manage BIG-IP configuration sections

## Description

Manages a BIG-IP configuration by allowing TMSH commands that modify running configuration, or merge SCF formatted files into the running configuration. Additionally, this module is of significant importance because it allows you to save your running configuration to disk. Since the F5 module only manipulate running configuration, it is important that you utilize this module to save that running config.

## Requirements

TODO

## Arguments

``` json
{
    "merge_content": "{'description': ['Loads the specified configuration that you want to merge into the running configuration. This is equivalent to using the C(tmsh) command C(load sys config from-terminal merge).', "If you need to read configuration from a file or template, use Ansible's C(file) or C(template) lookup plugins respectively."]}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "reset": "{'description': ['Loads the default configuration on the device.', 'If this option is specified, the default configuration will be loaded before any commands or other provided configuration is run.'], 'type': 'bool', 'default': False}",
    "save": "{'description': ['The C(save) argument instructs the module to save the running-config to startup-config.', 'This operation is performed after any changes are made to the current running config. If no changes are made, the configuration is still saved to the startup config.', 'This option will always cause the module to return changed.'], 'type': 'bool', 'default': True}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "verify": "{'description': ['Validates the specified configuration to see whether they are valid to replace the running configuration.', 'The running configuration will not be changed.', 'When this parameter is set to C(yes), no change will be reported by the module.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Save the running configuration of the BIG-IP
  bigip_config:
    save: yes
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: Reset the BIG-IP configuration, for example, to RMA the device
  bigip_config:
    reset: yes
    save: yes
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: Load an SCF configuration
  bigip_config:
    merge_content: "{{ lookup('file', '/path/to/config.scf') }}"
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
