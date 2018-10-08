# Ansible connection: ansible.connection_psrp


Run tasks over Microsoft PowerShell Remoting Protocol

## Description

Run commands or put/fetch on a target via PSRP (WinRM plugin)
This is similar to the I(winrm) connection plugin which uses the same underlying transport but instead runs in a PowerShell interpreter.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'description': ['The authentication protocol to use when authenticating the remote user.', "The default, C(negotiate), will attempt to use C(Kerberos) if it is available and fall back to C(NTLM) if it isn't."], 'vars': [{'name': 'ansible_psrp_auth'}], 'choices': ['basic', 'certificate', 'negotiate', 'kerberos', 'ntlm', 'credssp'], 'default': 'negotiate'}",
    "cert_trust_path": "{'description': ["The path to a PEM certificate chain to use when validating the server's certificate.", 'This value is ignored if I(cert_validation) is set to C(ignore).'], 'vars': [{'name': 'ansible_psrp_cert_trust_path'}]}",
    "cert_validation": "{'description': ["Whether to validate the remote server's certificate or not.", 'Set to C(ignore) to not validate any certificates.', 'I(cert_trust_path) can be set to the path of a PEM certificate chain to use in the validation.'], 'choices': ['validate', 'ignore'], 'default': 'validate', 'vars': [{'name': 'ansible_psrp_cert_validation'}]}",
    "configuration_name": "{'description': ['The name of the PowerShell configuration endpoint to connect to.'], 'vars': [{'name': 'ansible_psrp_configuration_name'}], 'default': 'Microsoft.PowerShell'}",
    "connection_timeout": "{'description': ['The connection timeout for making the request to the remote host.', 'This is measured in seconds.'], 'vars': [{'name': 'ansible_psrp_connection_timeout'}], 'default': 30}",
    "ignore_proxy": "{'description': ['Will disable any environment proxy settings and connect directly to the remote host.', 'This option is ignored if C(proxy) is set.'], 'vars': [{'name': 'ansible_psrp_ignore_proxy'}], 'type': 'bool', 'default': False}",
    "max_envelope_size": "{'description': ['Sets the maximum size of each WSMan message sent to the remote host.', 'This is measured in bytes.', 'Defaults to C(150KiB) for compatibility with older hosts.'], 'vars': [{'name': 'ansible_psrp_max_envelope_size'}], 'default': 153600}",
    "message_encryption": "{'description': ['Controls the message encryption settings, this is different from TLS encryption when I(ansible_psrp_protocol) is C(https).', 'Only the auth protocols C(negotiate), C(kerberos), C(ntlm), and C(credssp) can do message encryption. The other authentication protocols only support encryption when C(protocol) is set to C(https).', 'C(auto) means means message encryption is only used when not using TLS/HTTPS.', 'C(always) is the same as C(auto) but message encryption is always used even when running over TLS/HTTPS.', 'C(never) disables any encryption checks that are in place when running over HTTP and disables any authentication encryption processes.'], 'vars': [{'name': 'ansible_psrp_message_encryption'}], 'choices': ['auto', 'always', 'never'], 'default': 'auto'}",
    "operation_timeout": "{'description': ['Sets the WSMan timeout for each operation.', 'This is measured in seconds.', 'This should not exceed the value for C(connection_timeout).'], 'vars': [{'name': 'ansible_psrp_operation_timeout'}], 'default': 20}",
    "path": "{'description': ['The URI path to connect to.'], 'vars': [{'name': 'ansible_psrp_path'}], 'default': 'wsman'}",
    "port": "{'description': ['The port for PSRP to connect on the remote target.', 'Default is C(5986) if I(protocol) is not defined or is C(https), otherwise the port is C(5985).'], 'vars': [{'name': 'ansible_port'}, {'name': 'ansible_psrp_port'}]}",
    "protocol": "{'description': ['Set the protocol to use for the connection.', 'Default is C(https) if I(port) is not defined or I(port) is not C(5985).'], 'choices': ['http', 'https'], 'vars': [{'name': 'ansible_psrp_protocol'}]}",
    "proxy": "{'description': ['Set the proxy URL to use when connecting to the remote host.'], 'vars': [{'name': 'ansible_psrp_proxy'}]}",
    "remote_addr": "{'description': ['The hostname or IP address of the remote host.'], 'default': 'inventory_hostname', 'vars': [{'name': 'ansible_host'}, {'name': 'ansible_psrp_host'}]}",
    "remote_user": "{'description': ['The user to log in as.'], 'vars': [{'name': 'ansible_user'}, {'name': 'ansible_psrp_user'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
