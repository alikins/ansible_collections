# Ansible callback: ansible.callback_foreman


Sends events to Foreman

## Description

This callback will report facts and task events to Foreman https://theforeman.org/
Before 2.4, if you wanted to use an ini configuration, the file must be placed in the same directory as this plugin and named foreman.ini
In 2.4 and above you can just put it in the main Ansible configuration file.

## Requirements

TODO

## Arguments

``` json
{
    "ssl_cert": "{'description': ['X509 certificate to authenticate to Foreman if https is used'], 'env': [{'name': 'FOREMAN_SSL_CERT'}], 'default': '/etc/foreman/client_cert.pem', 'ini': [{'section': 'callback_foreman', 'key': 'ssl_cert'}]}",
    "ssl_key": "{'description': ['the corresponding private key'], 'env': [{'name': 'FOREMAN_SSL_KEY'}], 'default': '/etc/foreman/client_key.pem', 'ini': [{'section': 'callback_foreman', 'key': 'ssl_key'}]}",
    "url": "{'description': ['URL to the Foreman server'], 'env': [{'name': 'FOREMAN_URL'}], 'required': True, 'default': 'http://localhost:3000', 'ini': [{'section': 'callback_foreman', 'key': 'url'}]}",
    "verify_certs": "{'description': ['Toggle to decidewhether to verify the Foreman certificate.', "It can be set to '1' to verify SSL certificates using the installed CAs or to a path pointing to a CA bundle.", "Set to '0' to disable certificate checking."], 'env': [{'name': 'FOREMAN_SSL_VERIFY'}], 'default': 1, 'ini': [{'section': 'callback_foreman', 'key': 'verify_certs'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
