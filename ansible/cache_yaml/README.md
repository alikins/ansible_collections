# Ansible cache: ansible.cache_yaml


YAML formatted files

## Description

This cache uses YAML formatted, per host, files saved to the filesystem.

## Requirements

TODO

## Arguments

``` json
{
    "_prefix": "{'description': ['User defined prefix to use when creating the files'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_PREFIX'}], 'ini': [{'key': 'fact_caching_prefix', 'section': 'defaults'}]}",
    "_timeout": "{'default': 86400, 'description': ['Expiration timeout for the cache plugin data'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_TIMEOUT'}], 'ini': [{'key': 'fact_caching_timeout', 'section': 'defaults'}], 'type': 'integer'}",
    "_uri": "{'required': True, 'description': ['Path in which the cache plugin will save the files'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_CONNECTION'}], 'ini': [{'key': 'fact_caching_connection', 'section': 'defaults'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
