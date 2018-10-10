# Ansible module: ansible.module_nxos_gir


Trigger a graceful removal or insertion (GIR) of the switch

## Description

Trigger a graceful removal or insertion (GIR) of the switch.

## Requirements

TODO

## Arguments

``` json
{
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "state": "{'description': ['Specify desired state of the resource.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "system_mode_maintenance": "{'description': ['When C(system_mode_maintenance=true) it puts all enabled protocols in maintenance mode (using the isolate command). When C(system_mode_maintenance=false) it puts all enabled protocols in normal mode (using the no isolate command).'], 'type': 'bool'}",
    "system_mode_maintenance_dont_generate_profile": "{'description': ['When C(system_mode_maintenance_dont_generate_profile=true) it prevents the dynamic searching of enabled protocols and executes commands configured in a maintenance-mode profile. Use this option if you want the system to use a maintenance-mode profile that you have created. When C(system_mode_maintenance_dont_generate_profile=false) it prevents the dynamic searching of enabled protocols and executes commands configured in a normal-mode profile. Use this option if you want the system to use a normal-mode profile that you have created.'], 'type': 'bool'}",
    "system_mode_maintenance_on_reload_reset_reason": "{'description': ['Boots the switch into maintenance mode automatically in the event of a specified system crash. Note that not all reset reasons are applicable for all platforms. Also if reset reason is set to match_any, it is not idempotent as it turns on all reset reasons. If reset reason is match_any and state is absent, it turns off all the reset reasons.'], 'choices': ['hw_error', 'svc_failure', 'kern_failure', 'wdog_timeout', 'fatal_error', 'lc_failure', 'match_any', 'manual_reload', 'any_other', 'maintenance']}",
    "system_mode_maintenance_shutdown": "{'description': ['Shuts down all protocols, vPC domains, and interfaces except the management interface (using the shutdown command). This option is disruptive while C(system_mode_maintenance) (which uses the isolate command) is not.'], 'type': 'bool'}",
    "system_mode_maintenance_timeout": "{'description': ['Keeps the switch in maintenance mode for a specified number of minutes. Range is 5-65535.']}",
}
```

## Examples


``` yaml

# Trigger system maintenance mode
- nxos_gir:
    system_mode_maintenance: true
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Trigger system normal mode
- nxos_gir:
    system_mode_maintenance: false
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Configure on-reload reset-reason for maintenance mode
- nxos_gir:
    system_mode_maintenance_on_reload_reset_reason: manual_reload
    state: present
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Add on-reload reset-reason for maintenance mode
- nxos_gir:
    system_mode_maintenance_on_reload_reset_reason: hw_error
    state: present
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Remove on-reload reset-reason for maintenance mode
- nxos_gir:
    system_mode_maintenance_on_reload_reset_reason: manual_reload
    state: absent
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Set timeout for maintenance mode
- nxos_gir:
    system_mode_maintenance_timeout: 30
    state: present
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"
# Remove timeout for maintenance mode
- nxos_gir:
    system_mode_maintenance_timeout: 30
    state: absent
    host: "{{ inventory_hostname }}"
    username: "{{ un }}"
    password: "{{ pwd }}"

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
