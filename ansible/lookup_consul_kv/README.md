# Ansible lookup: ansible.lookup_consul_kv


Fetch metadata from a Consul key value store

## Description

Lookup metadata for a playbook from the key value store in a Consul cluster. Values can be easily set in the kv store with simple rest commands
C(curl -X PUT -d 'some-value' http://localhost:8500/v1/kv/ansible/somedata)

## Requirements

TODO

## Arguments

``` json
{
    "_raw": "{'description': ['List of key(s) to retrieve.'], 'type': 'list', 'required': True}",
    "client_cert": "{'default': 'None', 'description': ['The client cert to verify the ssl connection.'], 'env': [{'name': 'ANSIBLE_CONSUL_CLIENT_CERT'}], 'ini': [{'section': 'lookup_consul', 'key': 'client_cert'}], 'version_added': '2.8'}",
    "host": "{'default': 'localhost', 'description': ['The target to connect to, must be a resolvable address. Will be determined from C(ANSIBLE_CONSUL_URL) if that is set.', 'C(ANSIBLE_CONSUL_URL) should look like this: C(https://my.consul.server:8500)'], 'env': [{'name': 'ANSIBLE_CONSUL_URL'}], 'ini': [{'section': 'lookup_consul', 'key': 'host'}], 'version_added': '2.8'}",
    "index": "{'description': ['If the key has a value with the specified index then this is returned allowing access to historical values.']}",
    "port": "{'description': ['The port of the target host to connect to.', 'If you use C(ANSIBLE_CONSUL_URL) this value will be used from there.'], 'default': 8500}",
    "recurse": "{'type': 'boolean', 'description': ['If true, will retrieve all the values that have the given key as prefix.'], 'default': False}",
    "scheme": "{'default': 'http', 'description': ['Whether to use http or https.', 'If you use C(ANSIBLE_CONSUL_URL) this value will be used from there.'], 'version_added': '2.8'}",
    "token": "{'description': ['The acl token to allow access to restricted values.']}",
    "validate_certs": "{'default': True, 'description': ['Whether to verify the ssl connection or not.'], 'env': [{'name': 'ANSIBLE_CONSUL_VALIDATE_CERTS'}], 'ini': [{'section': 'lookup_consul', 'key': 'validate_certs'}], 'version_added': '2.8'}",
}
```

## Examples


``` yaml

  - debug:
      msg: 'key contains {{item}}'
    with_consul_kv:
      - 'key/to/retrieve'

  - name: Parameters can be provided after the key be more specific about what to retrieve
    debug:
      msg: 'key contains {{item}}'
    with_consul_kv:
      - 'key/to recurse=true token=E6C060A9-26FB-407A-B83E-12DDAFCB4D98'

  - name: retrieving a KV from a remote cluster on non default port
    debug:
      msg: "{{ lookup('consul_kv', 'my/key', host='10.10.10.10', port='2000') }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
