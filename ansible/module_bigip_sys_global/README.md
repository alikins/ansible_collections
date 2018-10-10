# Ansible module: ansible.module_bigip_sys_global


Manage BIG-IP global settings

## Description

Manage BIG-IP global settings.

## Requirements

TODO

## Arguments

``` json
{
    "banner_text": "{'description': ['Specifies the text to present in the advisory banner.']}",
    "console_timeout": "{'description': ['Specifies the number of seconds of inactivity before the system logs off a user that is logged on.']}",
    "gui_setup": "{'description': ['C(enable) or C(disabled) the Setup utility in the browser-based Configuration utility.'], 'type': 'bool'}",
    "lcd_display": "{'description': ['Specifies, when C(enabled), that the system menu displays on the LCD screen on the front of the unit. This setting has no effect when used on the VE platform.'], 'type': 'bool'}",
    "mgmt_dhcp": "{'description': ['Specifies whether or not to enable DHCP client on the management interface'], 'type': 'bool'}",
    "net_reboot": "{'description': ['Specifies, when C(enabled), that the next time you reboot the system, the system boots to an ISO image on the network, rather than an internal media drive.'], 'type': 'bool'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "quiet_boot": "{'description': ['Specifies, when C(enabled), that the system suppresses informational text on the console during the boot cycle. When C(disabled), the system presents messages and informational text on the console during the boot cycle.'], 'type': 'bool'}",
    "security_banner": "{'description': ['Specifies whether the system displays an advisory message on the login screen.'], 'type': 'bool'}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['The state of the variable on the system. When C(present), guarantees that an existing variable is set to C(value).'], 'default': 'present', 'choices': ['present']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Disable the setup utility
  bigip_sys_global:
    gui_setup: no
    password: secret
    server: lb.mydomain.com
    user: admin
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
