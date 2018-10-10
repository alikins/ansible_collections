# Ansible module: ansible.module_eos_eapi


Manage and configure Arista EOS eAPI

## Description

Use to enable or disable eAPI access, and set the port and state of http, https, local_http and unix-socket servers.
When enabling eAPI access the default is to enable HTTP on port 80, enable HTTPS on port 443, disable local HTTP, and disable Unix socket server. Use the options listed below to override the default configuration.
Requires EOS v4.12 or greater.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "config": "{'description': ['The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source.  There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The I(config) argument allows the implementer to pass in the configuration to use as the base config for comparison.'], 'version_added': '2.2'}",
    "http": "{'description': ['The C(http) argument controls the operating state of the HTTP transport protocol when eAPI is present in the running-config. When the value is set to True, the HTTP protocol is enabled and when the value is set to False, the HTTP protocol is disabled. By default, when eAPI is first configured, the HTTP protocol is disabled.'], 'type': 'bool', 'default': False, 'aliases': ['enable_http']}",
    "http_port": "{'description': ['Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled.  This argument accepts integer values in the valid range of 1 to 65535.'], 'default': 80}",
    "https": "{'description': ['The C(https) argument controls the operating state of the HTTPS transport protocol when eAPI is present in the running-config. When the value is set to True, the HTTPS protocol is enabled and when the value is set to False, the HTTPS protocol is disabled. By default, when eAPI is first configured, the HTTPS protocol is enabled.'], 'type': 'bool', 'default': True, 'aliases': ['enable_https']}",
    "https_port": "{'description': ['Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled.  This argument accepts integer values in the valid range of 1 to 65535.'], 'default': 443}",
    "local_http": "{'description': ['The C(local_http) argument controls the operating state of the local HTTP transport protocol when eAPI is present in the running-config.  When the value is set to True, the HTTP protocol is enabled and restricted to connections from localhost only.  When the value is set to False, the HTTP local protocol is disabled.', 'Note is value is independent of the C(http) argument'], 'type': 'bool', 'default': False, 'aliases': ['enable_local_http']}",
    "local_http_port": "{'description': ['Configures the HTTP port that will listen for connections when the HTTP transport protocol is enabled.  This argument accepts integer values in the valid range of 1 to 65535.'], 'default': 8080}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(eapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(eapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['eapi', 'cli'], 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=eapi).  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool', 'default': 'yes'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "socket": "{'description': ['The C(socket) argument controls the operating state of the UNIX Domain Socket used to receive eAPI requests.  When the value of this argument is set to True, the UDS will listen for eAPI requests.  When the value is set to False, the UDS will not be available to handle requests.  By default when eAPI is first configured, the UDS is disabled.'], 'type': 'bool', 'default': False, 'aliases': ['enable_socket']}",
    "state": "{'description': ['The C(state) argument controls the operational state of eAPI on the remote device.  When this argument is set to C(started), eAPI is enabled to receive requests and when this argument is C(stopped), eAPI is disabled and will not receive requests.'], 'default': 'started', 'choices': ['started', 'stopped']}",
    "vrf": "{'description': ['The C(vrf) argument will configure eAPI to listen for connections in the specified VRF.  By default, eAPI transports will listen for connections in the global table.  This value requires the VRF to already be created otherwise the task will fail.'], 'default': 'default', 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: Enable eAPI access with default configuration
  eos_eapi:
    state: started

- name: Enable eAPI with no HTTP, HTTPS at port 9443, local HTTP at port 80, and socket enabled
  eos_eapi:
    state: started
    http: false
    https_port: 9443
    local_http: yes
    local_http_port: 80
    socket: yes

- name: Shutdown eAPI access
  eos_eapi:
    state: stopped

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
