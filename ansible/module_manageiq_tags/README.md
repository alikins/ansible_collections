# Ansible module: ansible.module_manageiq_tags


Management of resource tags in ManageIQ

## Description

The manageiq_tags module supports adding, updating and deleting tags in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "resource_name": "{'description': ['the relevant resource name in manageiq'], 'required': True}",
    "resource_type": "{'description': ['the relevant resource type in manageiq'], 'required': True, 'choices': ['provider', 'host', 'vm', 'blueprint', 'category', 'cluster', 'data store', 'group', 'resource pool', 'service', 'service template', 'template', 'tenant', 'user']}",
    "state": "{'description': ['absent - tags should not exist,', 'present - tags should exist,', 'list - list current tags.'], 'choices': ['absent', 'present', 'list'], 'default': 'present'}",
    "tags": "{'description': ["tags - list of dictionaries, each includes 'name' and 'category' keys.", 'required if state is present or absent.']}",
}
```

## Examples


``` yaml

- name: Create new tags for a provider in ManageIQ
  manageiq_tags:
    resource_name: 'EngLab'
    resource_type: 'provider'
    tags:
    - category: environment
      name: prod
    - category: owner
      name: prod_ops
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Remove tags for a provider in ManageIQ
  manageiq_tags:
    state: absent
    resource_name: 'EngLab'
    resource_type: 'provider'
    tags:
    - category: environment
      name: prod
    - category: owner
      name: prod_ops
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: List current tags for a provider in ManageIQ
  manageiq_tags:
    state: list
    resource_name: 'EngLab'
    resource_type: 'provider'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

```

## License

TODO

## Author Information
  - ['Daniel Korn (@dkorn)']
