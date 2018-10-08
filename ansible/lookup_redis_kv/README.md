# Ansible lookup: ansible.lookup_redis_kv


fetch data from Redis

## Description

this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['Two element comma separated strings composed of url of the Redis server and key to query'], 'options': {'_url': {'description': 'location of redis host in url format', 'default': 'redis://localhost:6379'}, '_key': {'description': 'key to query', 'required': True}}}",
}
```

## Examples


``` yaml

- name: query redis for somekey
  debug: msg="{{ lookup('redis_kv', 'redis://localhost:6379,somekey') }} is value in Redis for somekey"

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens <jpmens(at)gmail.com>']
