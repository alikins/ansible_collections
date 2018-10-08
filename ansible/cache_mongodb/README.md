# Ansible cache: ansible.cache_mongodb


Use MongoDB for caching

## Description

This cache uses per host records saved in MongoDB.

## Requirements

TODO

## Arguments

``` json
{
    "_prefix": "{'description': ['User defined prefix to use when creating the DB entries'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_PREFIX'}], 'ini': [{'key': 'fact_caching_prefix', 'section': 'defaults'}]}",
    "_timeout": "{'default': 86400, 'description': ['Expiration timeout in seconds for the cache plugin data'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_TIMEOUT'}], 'ini': [{'key': 'fact_caching_timeout', 'section': 'defaults'}], 'type': 'integer'}",
    "_uri": "{'description': ['MongoDB Connection String URI'], 'required': False, 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_CONNECTION'}], 'ini': [{'key': 'fact_caching_connection', 'section': 'defaults'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
