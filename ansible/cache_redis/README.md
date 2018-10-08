# Ansible cache: ansible.cache_redis


Use Redis DB for cache

## Description

This cache uses JSON formatted, per host records saved in Redis.

## Requirements

TODO

## Arguments

``` json
{
    "_prefix": "{'description': ['User defined prefix to use when creating the DB entries'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_PREFIX'}], 'ini': [{'key': 'fact_caching_prefix', 'section': 'defaults'}]}",
    "_timeout": "{'default': 86400, 'description': ['Expiration timeout for the cache plugin data'], 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_TIMEOUT'}], 'ini': [{'key': 'fact_caching_timeout', 'section': 'defaults'}], 'type': 'integer'}",
    "_uri": "{'description': ['A colon separated string of connection information for Redis.'], 'required': True, 'env': [{'name': 'ANSIBLE_CACHE_PLUGIN_CONNECTION'}], 'ini': [{'key': 'fact_caching_connection', 'section': 'defaults'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
