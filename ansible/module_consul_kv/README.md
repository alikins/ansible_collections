# Ansible module: ansible.module_consul_kv


Manipulate entries in the key/value store of a consul cluster

## Description

Allows the retrieval, addition, modification and deletion of key/value entries in a consul cluster via the agent. The entire contents of the record, including the indices, flags and session are returned as 'value'.
If the key represents a prefix then Note that when a value is removed, the existing value if any is returned as part of the results.
See http://www.consul.io/docs/agent/http.html#kv for more details.

## Requirements

TODO

## Arguments

``` json
{
    "cas": "{'description': ['Used when acquiring a lock with a session. If the C(cas) is C(0), then Consul will only put the key if it does not already exist. If the C(cas) value is non-zero, then the key is only set if the index matches the ModifyIndex of that key.']}",
    "flags": "{'description': ['Opaque integer value that can be passed when setting a value.']}",
    "host": "{'description': ['Host of the consul agent.'], 'default': 'localhost'}",
    "key": "{'description': ['The key at which the value should be stored.'], 'required': True}",
    "port": "{'description': ['The port on which the consul agent is running.'], 'default': 8500}",
    "recurse": "{'description': ['If the key represents a prefix, each entry with the prefix can be retrieved by setting this to C(yes).'], 'type': 'bool', 'default': False}",
    "scheme": "{'description': ['The protocol scheme on which the consul agent is running.'], 'default': 'http', 'version_added': '2.1'}",
    "session": "{'description': ['The session that should be used to acquire or release a lock associated with a key/value pair.']}",
    "state": "{'description': ["The action to take with the supplied key and value. If the state is 'present' and `value` is set, the key contents will be set to the value supplied and `changed` will be set to `true` only if the value was different to the current contents. If the state is 'present' and `value` is not set, the existing value associated to the key will be returned. The state 'absent' will remove the key/value pair, again 'changed' will be set to true only if the key actually existed prior to the removal. An attempt can be made to obtain or free the lock associated with a key/value pair with the states 'acquire' or 'release' respectively. a valid session must be supplied to make the attempt changed will be true if the attempt is successful, false otherwise."], 'choices': ['absent', 'acquire', 'present', 'release'], 'default': 'present'}",
    "token": "{'description': ['The token key indentifying an ACL rule set that controls access to the key value pair']}",
    "validate_certs": "{'description': ['Whether to verify the tls certificate of the consul agent.'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
    "value": "{'description': ['The value should be associated with the given key, required if C(state) is C(present).'], 'required': True}",
}
```

## Examples


``` yaml

# If the key does not exist, the value associated to the "data" property in `retrieved_key` will be `None`
# If the key value is empty string, `retrieved_key["data"]["Value"]` will be `None`
- name: retrieve a value from the key/value store
  consul_kv:
    key: somekey
  register: retrieved_key

- name: Add or update the value associated with a key in the key/value store
  consul_kv:
    key: somekey
    value: somevalue

- name: Remove a key from the store
  consul_kv:
    key: somekey
    state: absent

- name: Add a node to an arbitrary group via consul inventory (see consul.ini)
  consul_kv:
    key: ansible/groups/dc1/somenode
    value: top_secret

- name: Register a key/value pair with an associated session
  consul_kv:
    key: stg/node/server_birthday
    value: 20160509
    session: "{{ sessionid }}"
    state: acquire

```

## License

TODO

## Author Information
  - ['Steve Gargan (@sgargan)', 'Colin Nolan (@colin-nolan)']
  - ['Steve Gargan (@sgargan)', 'Colin Nolan (@colin-nolan)']
