# Ansible module: ansible.module_vdirect_file


Uploads a new or updates an existing runnable file into Radware vDirect server

## Description

Uploads a new or updates an existing configuration template or workflow template into the Radware vDirect server. All parameters may be set as environment variables.

## Requirements

TODO

## Arguments

``` json
{
    "file_name": "{'description': ['vDirect runnable file name to be uploaded.', 'May be velocity configuration template (.vm) or workflow template zip file (.zip).'], 'required': True}",
    "vdirect_http_port": "{'description': ['vDirect server HTTP port number, may be set as VDIRECT_HTTP_PORT environment variable.'], 'default': 2188}",
    "vdirect_https_port": "{'description': ['vDirect server HTTPS port number, may be set as VDIRECT_HTTPS_PORT environment variable.'], 'default': 2189}",
    "vdirect_ip": "{'description': ['Primary vDirect server IP address, may be set as VDIRECT_IP environment variable.'], 'required': True}",
    "vdirect_password": "{'description': ['vDirect server password, may be set as VDIRECT_PASSWORD environment variable.'], 'required': True}",
    "vdirect_secondary_ip": "{'description': ['Secondary vDirect server IP address, may be set as VDIRECT_SECONDARY_IP environment variable.']}",
    "vdirect_timeout": "{'description': ['Amount of time to wait for async operation completion [seconds],', 'may be set as VDIRECT_TIMEOUT environment variable.'], 'default': 60}",
    "vdirect_use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection,', 'may be set as VDIRECT_HTTPS or VDIRECT_USE_SSL environment variable.'], 'type': 'bool', 'default': True}",
    "vdirect_user": "{'description': ['vDirect server username, may be set as VDIRECT_USER environment variable.'], 'required': True}",
    "vdirect_validate_certs": "{'description': ['If C(no), SSL certificates will not be validated,', 'may be set as VDIRECT_VALIDATE_CERTS or VDIRECT_VERIFY environment variable.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vdirect_wait": "{'description': ['Wait for async operation to complete, may be set as VDIRECT_WAIT environment variable.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: vdirect_file
  vdirect_file:
      vdirect_ip: 10.10.10.10
      vdirect_user: vDirect
      vdirect_password: radware
      file_name: /tmp/get_vlans.vm

```

## License

TODO

## Author Information
  - ['Evgeny Fedoruk @ Radware LTD (@evgenyfedoruk)']
