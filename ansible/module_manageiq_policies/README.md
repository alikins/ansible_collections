# Ansible module: ansible.module_manageiq_policies


Management of resource policy_profiles in ManageIQ

## Description

The manageiq_policies module supports adding and deleting policy_profiles in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "policy_profiles": "{'description': ["list of dictionaries, each includes the policy_profile 'name' key.", 'required if state is present or absent.']}",
    "resource_name": "{'description': ['the name of the resource to which the profile should be [un]assigned'], 'required': True}",
    "resource_type": "{'description': ['the type of the resource to which the profile should be [un]assigned'], 'required': True, 'choices': ['provider', 'host', 'vm', 'blueprint', 'category', 'cluster', 'data store', 'group', 'resource pool', 'service', 'service template', 'template', 'tenant', 'user']}",
    "state": "{'description': ['absent - policy_profiles should not exist,', 'present - policy_profiles should exist,', 'list - list current policy_profiles and policies.'], 'choices': ['absent', 'present', 'list'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Assign new policy_profile for a provider in ManageIQ
  manageiq_policies:
    resource_name: 'EngLab'
    resource_type: 'provider'
    policy_profiles:
      - name: openscap profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Unassign a policy_profile for a provider in ManageIQ
  manageiq_policies:
    state: absent
    resource_name: 'EngLab'
    resource_type: 'provider'
    policy_profiles:
      - name: openscap profile
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: List current policy_profile and policies for a provider in ManageIQ
  manageiq_policies:
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
