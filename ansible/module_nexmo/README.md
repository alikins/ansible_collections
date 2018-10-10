# Ansible module: ansible.module_nexmo


Send a SMS via nexmo

## Description

Send a SMS message via nexmo

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Nexmo API Key'], 'required': True}",
    "api_secret": "{'description': ['Nexmo API Secret'], 'required': True}",
    "client_cert": "{'description': ['PEM formatted certificate chain file to be used for SSL client authentication. This file can also include the key as well, and if the key is included, C(client_key) is not required.']}",
    "client_key": "{'description': ['PEM formatted file that contains your private key to be used for SSL client authentication. If C(client_cert) contains both the certificate and key, this option is not required.']}",
    "dest": "{'description': ['Phone number(s) to send SMS message to'], 'required': True}",
    "force": "{'description': ['If C(yes) do not get a cached copy.'], 'aliases': ['thirsty'], 'type': 'bool', 'default': False}",
    "force_basic_auth": "{'description': ['Credentials specified with I(url_username) and I(url_password) should be passed in HTTP Header.'], 'default': False, 'type': 'bool'}",
    "http_agent": "{'description': ['Header to identify as, generally appears in web server logs.'], 'default': 'ansible-httpget'}",
    "msg": "{'description': ['Message to text to send. Messages longer than 160 characters will be split into multiple messages'], 'required': True}",
    "src": "{'description': ['Nexmo Number to send from'], 'required': True}",
    "url": "{'description': ['HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path']}",
    "url_password": "{'description': ['The password for use in HTTP basic authentication.', 'If the I(url_username) parameter is not specified, the I(url_password) parameter will not be used.']}",
    "url_username": "{'description': ['The username for use in HTTP basic authentication.', 'This parameter can be used without I(url_password) for sites that allow empty passwords']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Send notification message via Nexmo
  nexmo:
    api_key: 640c8a53
    api_secret: 0ce239a6
    src: 12345678901
    dest:
      - 10987654321
      - 16789012345
    msg: '{{ inventory_hostname }} completed'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
