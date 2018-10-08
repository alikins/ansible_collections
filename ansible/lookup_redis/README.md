# Ansible lookup: ansible.lookup_redis


fetch data from Redis

## Description

This lookup returns a list of results from a Redis DB corresponding to a list of items given to it

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['list of keys to query']}",
    "host": "{'description': ['location of Redis host'], 'default': '127.0.0.1', 'env': [{'name': 'ANSIBLE_REDIS_HOST'}], 'ini': [{'section': 'lookup_redis', 'key': 'host'}]}",
    "port": "{'description': ['port on which Redis is listening on'], 'default': '6379A', 'type': 'int', 'env': [{'name': 'ANSIBLE_REDIS_PORT'}], 'ini': [{'section': 'lookup_redis', 'key': 'port'}]}",
    "socket": "{'description': ['path to socket on which to query Redis, this option overrides host and port options when set.'], 'type': 'path', 'env': [{'name': 'ANSIBLE_REDIS_SOCKET'}], 'ini': [{'section': 'lookup_redis', 'key': 'socket'}]}",
}
```

## Examples


``` yaml

- name: query redis for somekey (default or configured settings used)
  debug: msg="{{ lookup('redis', 'somekey'}}"

- name: query redis for list of keys and non-default host and port
  debug: msg="{{ lookup('redis', item, host='myredis.internal.com', port=2121) }}"
  loop: '{{list_of_redis_keys}}'

- name: use list directly
  debug: msg="{{ lookup('redis', 'key1', 'key2', 'key3') }}"

- name: use list directly with a socket
  debug: msg="{{ lookup('redis', 'key1', 'key2', socket='/var/tmp/redis.sock') }}"


```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>', 'Ansible Core']
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>', 'Ansible Core']
