# Ansible module: ansible.module_zabbix_proxy


Zabbix proxy creates/deletes/gets/updates

## Description

This module allows you to create, modify, get and delete Zabbix proxy entries.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the proxy..'], 'required': False}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "interface": "{'description': ['Dictionary with params for the interface when proxy is in passive mode', 'Available values are: dns, ip, main, port, type and useip.', 'Please review the interface documentation for more information on the supported properties', 'U(https://www.zabbix.com/documentation/3.2/manual/api/reference/proxy/object#proxy_interface)'], 'required': False, 'default': {}}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "proxy_name": "{'description': ['Name of the proxy in Zabbix.'], 'required': True}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['State of the proxy.', 'On C(present), it will create if proxy does not exist or update the proxy if the associated data is different.', 'On C(absent) will remove a proxy if it exists.'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "status": "{'description': ['Type of proxy. (4 - active, 5 - passive)'], 'required': False, 'choices': ['active', 'passive'], 'default': 'active'}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "tls_accept": "{'description': ['Connections from proxy.'], 'required': False, 'choices': ['no_encryption', 'PSK', 'certificate'], 'default': 'no_encryption'}",
    "tls_connect": "{'description': ['Connections to proxy.'], 'required': False, 'choices': ['no_encryption', 'PSK', 'certificate'], 'default': 'no_encryption'}",
    "tls_issuer": "{'description': ['Certificate issuer.'], 'required': False}",
    "tls_psk": "{'description': ['The preshared key, at least 32 hex digits. Required if either I(tls_connect) or I(tls_accept) has PSK enabled.'], 'required': False}",
    "tls_psk_identity": "{'description': ['PSK identity. Required if either I(tls_connect) or I(tls_accept) has PSK enabled.'], 'required': False}",
    "tls_subject": "{'description': ['Certificate subject.'], 'required': False}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Create a new proxy or update an existing proxies info
  local_action:
    module: zabbix_proxy
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    proxy_name: ExampleProxy
    description: ExampleProxy
    status: active
    state: present
    interface:
        type: 0
        main: 1
        useip: 1
        ip: 10.xx.xx.xx
        dns: ""
        port: 10050

```

## License

TODO

## Author Information
  - ['Alen Komic']
