# Ansible lookup: ansible.lookup_etcd


get info from an etcd server

## Description

Retrieves data from an etcd server

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['the list of keys to lookup on the etcd server'], 'type': 'list', 'elements': 'string', 'required': True}",
    "url": "{'description': ['Environment variable with the url for the etcd server'], 'default': 'http://127.0.0.1:4001', 'env': [{'name': 'ANSIBLE_ETCD_URL'}]}",
    "validate_certs": "{'description': ['toggle checking that the ssl certificates are valid, you normally only want to turn this off with self-signed certs.'], 'default': True, 'type': 'boolean'}",
    "version": "{'description': ['Environment variable with the etcd protocol version'], 'default': 'v1', 'env': [{'name': 'ANSIBLE_ETCD_VERSION'}]}",
}
```

## Examples


``` yaml

    - name: "a value from a locally running etcd"
      debug: msg={{ lookup('etcd', 'foo/bar') }}

    - name: "values from multiple folders on a locally running etcd"
      debug: msg={{ lookup('etcd', 'foo', 'bar', 'baz') }}

    - name: "since Ansible 2.5 you can set server options inline"
      debug: msg="{{ lookup('etcd', 'foo', version='v2', url='http://192.168.0.27:4001') }}"

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens)']
