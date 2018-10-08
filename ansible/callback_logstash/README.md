# Ansible callback: ansible.callback_logstash


Sends events to Logstash

## Description

This callback will report facts and task events to Logstash https://www.elastic.co/products/logstash

## Requirements

TODO

## Arguments

``` json
{
    "port": "{'description': ['Port on which logstash is listening'], 'env': [{'name': 'LOGSTASH_PORT'}], 'default': 5000}",
    "server": "{'description': ['Address of the Logstash server'], 'env': [{'name': 'LOGSTASH_SERVER'}], 'default': 'localhost'}",
    "type": "{'description': ['Message type'], 'env': [{'name': 'LOGSTASH_TYPE'}], 'default': 'ansible'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
