# Ansible callback: ansible.callback_mail


Sends failure events via email

## Description

This callback will report failures via email

## Requirements

TODO

## Arguments

``` json
{
    "bcc": "{'description': ["BCC'd recipient"], 'ini': [{'section': 'callback_mail', 'key': 'bcc', 'version_added': '2.5'}]}",
    "cc": "{'description': ["CC'd recipient"], 'ini': [{'section': 'callback_mail', 'key': 'cc', 'version_added': '2.5'}]}",
    "mta": "{'description': ['Mail Transfer Agent, server that accepts SMTP'], 'env': [{'name': 'SMTPHOST'}], 'ini': [{'section': 'callback_mail', 'key': 'smtphost', 'version_added': '2.5'}], 'default': 'localhost'}",
    "mtaport": "{'description': ['Mail Transfer Agent Port, port at which server SMTP'], 'ini': [{'section': 'callback_mail', 'key': 'smtpport', 'version_added': '2.5'}], 'default': 25}",
    "sender": "{'description': ['Mail sender'], 'ini': [{'section': 'callback_mail', 'key': 'sender', 'version_added': '2.5'}]}",
    "to": "{'description': ['Mail recipient'], 'ini': [{'section': 'callback_mail', 'key': 'to', 'version_added': '2.5'}], 'default': 'root'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
