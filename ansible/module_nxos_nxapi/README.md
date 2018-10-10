# Ansible module: ansible.module_nxos_nxapi


Manage NXAPI configuration on an NXOS device

## Description

Configures the NXAPI feature on devices running Cisco NXOS.  The NXAPI feature is absent from the configuration by default.  Since this module manages the NXAPI feature it only supports the use of the C(Cli) transport.

## Requirements

TODO

## Arguments

``` json
{
    "http": "{'description': ['Controls the operating state of the HTTP protocol as one of the underlying transports for NXAPI.  By default, NXAPI will enable the HTTP transport when the feature is first configured.  To disable the use of the HTTP transport, set the value of this argument to False.'], 'required': False, 'default': True, 'type': 'bool', 'aliases': ['enable_http']}",
    "http_port": "{'description': ['Configure the port with which the HTTP server will listen on for requests.  By default, NXAPI will bind the HTTP service to the standard HTTP port 80.  This argument accepts valid port values in the range of 1 to 65535.'], 'required': False, 'default': 80}",
    "https": "{'description': ['Controls the operating state of the HTTPS protocol as one of the underlying transports for NXAPI.  By default, NXAPI will disable the HTTPS transport when the feature is first configured.  To enable the use of the HTTPS transport, set the value of this argument to True.'], 'required': False, 'default': False, 'type': 'bool', 'aliases': ['enable_https']}",
    "https_port": "{'description': ['Configure the port with which the HTTPS server will listen on for requests.  By default, NXAPI will bind the HTTPS service to the standard HTTPS port 443.  This argument accepts valid port values in the range of 1 to 65535.'], 'required': False, 'default': 443}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "sandbox": "{'description': ['The NXAPI feature provides a web base UI for developers for entering commands.  This feature is initially disabled when the NXAPI feature is configured for the first time.  When the C(sandbox) argument is set to True, the developer sandbox URL will accept requests and when the value is set to False, the sandbox URL is unavailable. This is supported on NX-OS 7K series.'], 'required': False, 'default': False, 'type': 'bool', 'aliases': ['enable_sandbox']}",
    "ssl_strong_ciphers": "{'description': ['Controls the use of whether strong or weak ciphers are configured. By default, this feature is disabled and weak ciphers are configured.  To enable the use of strong ciphers, set the value of this argument to True.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "state": "{'description': ['The C(state) argument controls whether or not the NXAPI feature is configured on the remote device.  When the value is C(present) the NXAPI feature configuration is present in the device running-config.  When the values is C(absent) the feature configuration is removed from the running-config.'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
    "tlsv1_0": "{'description': ['Controls the use of the Transport Layer Security version 1.0 is configured.  By default, this feature is enabled.  To disable the use of TLSV1.0, set the value of this argument to True.'], 'required': False, 'default': True, 'type': 'bool', 'version_added': '2.7'}",
    "tlsv1_1": "{'description': ['Controls the use of the Transport Layer Security version 1.1 is configured.  By default, this feature is disabled.  To enable the use of TLSV1.1, set the value of this argument to True.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "tlsv1_2": "{'description': ['Controls the use of the Transport Layer Security version 1.2 is configured.  By default, this feature is disabled.  To enable the use of TLSV1.2, set the value of this argument to True.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: Enable NXAPI access with default configuration
  nxos_nxapi:
    state: present

- name: Enable NXAPI with no HTTP, HTTPS at port 9443 and sandbox disabled
  nxos_nxapi:
    enable_http: false
    https_port: 9443
    https: yes
    enable_sandbox: no

- name: remove NXAPI configuration
  nxos_nxapi:
    state: absent

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
