# Ansible callback: ansible.callback_logdna


Sends playbook logs to LogDNA

## Description

This callback will report logs from playbook actions, tasks, and events to LogDNA (https://app.logdna.com)

## Requirements

TODO

## Arguments

``` json
{
    "conf_hostname": "{'required': False, 'description': ['Alternative Host Name; the current host name by default'], 'type': 'string', 'env': [{'name': 'LOGDNA_HOSTNAME'}], 'ini': [{'section': 'callback_logdna', 'key': 'conf_hostname'}]}",
    "conf_key": "{'required': True, 'description': ['LogDNA Ingestion Key'], 'type': 'string', 'env': [{'name': 'LOGDNA_INGESTION_KEY'}], 'ini': [{'section': 'callback_logdna', 'key': 'conf_key'}]}",
    "conf_tags": "{'required': False, 'description': ['Tags'], 'type': 'string', 'env': [{'name': 'LOGDNA_TAGS'}], 'ini': [{'section': 'callback_logdna', 'key': 'conf_tags'}], 'default': 'ansible'}",
    "plugin_ignore_errors": "{'required': False, 'description': ['Whether to ignore errors on failing or not'], 'type': 'boolean', 'env': [{'name': 'ANSIBLE_IGNORE_ERRORS'}], 'ini': [{'section': 'callback_logdna', 'key': 'plugin_ignore_errors'}], 'default': False}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
