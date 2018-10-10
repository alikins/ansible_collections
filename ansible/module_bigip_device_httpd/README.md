# Ansible module: ansible.module_bigip_device_httpd


Manage HTTPD related settings on BIG-IP

## Description

Manages HTTPD related settings on the BIG-IP. These settings are interesting to change when you want to set GUI timeouts and other TMUI related settings.

## Requirements

TODO

## Arguments

``` json
{
    "allow": "{'description': ['Specifies, if you have enabled HTTPD access, the IP address or address range for other systems that can communicate with this system.', 'To specify all addresses, use the value C(all).', 'IP address can be specified, such as 172.27.1.10.', 'IP rangees can be specified, such as 172.27.*.* or 172.27.0.0/255.255.0.0.']}",
    "auth_name": "{'description': ['Sets the BIG-IP authentication realm name.']}",
    "auth_pam_dashboard_timeout": "{'description': ['Sets whether or not the BIG-IP dashboard will timeout.'], 'type': 'bool'}",
    "auth_pam_idle_timeout": "{'description': ['Sets the GUI timeout for automatic logout, in seconds.']}",
    "auth_pam_validate_ip": "{'description': ['Sets the authPamValidateIp setting.'], 'type': 'bool'}",
    "fast_cgi_timeout": "{'description': ['Sets the timeout of FastCGI.']}",
    "hostname_lookup": "{'description': ['Sets whether or not to display the hostname, if possible.'], 'type': 'bool'}",
    "log_level": "{'description': ['Sets the minimum httpd log level.'], 'choices': ['alert', 'crit', 'debug', 'emerg', 'error', 'info', 'notice', 'warn']}",
    "max_clients": "{'description': ['Sets the maximum number of clients that can connect to the GUI at once.']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "redirect_http_to_https": "{'description': ['Whether or not to redirect http requests to the GUI to https.'], 'type': 'bool'}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "ssl_cipher_suite": "{'description': ['Specifies the ciphers that the system uses.', 'The values in the suite are separated by colons (:).', 'Can be specified in either a string or list form. The list form is the recommended way to provide the cipher suite. See examples for usage.', 'Use the value C(default) to set the cipher suite to the system default. This value is equivalent to specifying a list of C(ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-RSA-AES128-SHA256,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA,ECDHE-ECDSA-AES256-SHA, ECDHE-ECDSA-AES128-SHA256,ECDHE-ECDSA-AES256-SHA384,AES128-GCM-SHA256, AES256-GCM-SHA384,AES128-SHA,AES256-SHA,AES128-SHA256,AES256-SHA256, ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-DES-CBC3-SHA,DES-CBC3-SHA).'], 'version_added': 2.6}",
    "ssl_port": "{'description': ['The HTTPS port to listen on.']}",
    "ssl_protocols": "{'description': ['The list of SSL protocols to accept on the management console.', 'A space-separated list of tokens in the format accepted by the Apache mod_ssl SSLProtocol directive.', 'Can be specified in either a string or list form. The list form is the recommended way to provide the cipher suite. See examples for usage.', 'Use the value C(default) to set the SSL protocols to the system default. This value is equivalent to specifying a list of C(all,-SSLv2,-SSLv3).'], 'version_added': 2.6}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Set the BIG-IP authentication realm name
  bigip_device_httpd:
    auth_name: BIG-IP
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set the auth pam timeout to 3600 seconds
  bigip_device_httpd:
    auth_pam_idle_timeout: 1200
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set the validate IP settings
  bigip_device_httpd:
    auth_pam_validate_ip: on
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set SSL cipher suite by list
  bigip_device_httpd:
    password: secret
    server: lb.mydomain.com
    user: admin
    ssl_cipher_suite:
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-RSA-AES256-GCM-SHA384
      - ECDHE-RSA-AES128-SHA
      - AES256-SHA256
  delegate_to: localhost

- name: Set SSL cipher suite by string
  bigip_device_httpd:
    password: secret
    server: lb.mydomain.com
    user: admin
    ssl_cipher_suite: ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:AES256-SHA256
  delegate_to: localhost

- name: Set SSL protocols by list
  bigip_device_httpd:
    password: secret
    server: lb.mydomain.com
    user: admin
    ssl_protocols:
      - all
      - -SSLv2
      - -SSLv3
  delegate_to: localhost

- name: Set SSL protocols by string
  bigip_device_httpd:
    password: secret
    server: lb.mydomain.com
    user: admin
    ssl_cipher_suite: all -SSLv2 -SSLv3
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joe Reifel (@JoeReifel)', 'Tim Rupp (@caphrim007)']
  - ['Joe Reifel (@JoeReifel)', 'Tim Rupp (@caphrim007)']
