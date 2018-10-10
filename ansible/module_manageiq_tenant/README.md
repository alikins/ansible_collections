# Ansible module: ansible.module_manageiq_tenant


Management of tenants in ManageIQ

## Description

The manageiq_tenant module supports adding, updating and deleting tenants in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The tenant description.'], 'required': True, 'default': None}",
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "name": "{'description': ['The tenant name.'], 'required': True, 'default': None}",
    "parent": "{'description': ['The name of the parent tenant. If not supplied and no C(parent_id) is supplied the root tenant is used.'], 'required': False, 'default': None}",
    "parent_id": "{'description': ['The id of the parent tenant. If not supplied the root tenant is used.', 'The C(parent_id) takes president over C(parent) when supplied'], 'required': False, 'default': None}",
    "quotas": "{'description': ['The tenant quotas.', 'All parameters case sensitive.', 'Valid attributes are:', ' - C(cpu_allocated) (int): use null to remove the quota.', ' - C(mem_allocated) (GB): use null to remove the quota.', ' - C(storage_allocated) (GB): use null to remove the quota.', ' - C(vms_allocated) (int): use null to remove the quota.', ' - C(templates_allocated) (int): use null to remove the quota.'], 'required': False, 'default': None}",
    "state": "{'description': ['absent - tenant should not exist, present - tenant should be.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Update the root tenant in ManageIQ
  manageiq_tenant:
    name: 'My Company'
    description: 'My company name'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Create a tenant in ManageIQ
  manageiq_tenant:
    name: 'Dep1'
    description: 'Manufacturing department'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Delete a tenant in ManageIQ
  manageiq_tenant:
    state: 'absent'
    name: 'Dep1'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Set tenant quota for cpu_allocated, mem_allocated, remove quota for vms_allocated
  manageiq_tenant:
    name: 'Dep1'
    parent_id: 1
    quotas:
      - cpu_allocated: 100
      - mem_allocated: 50
      - vms_allocated: null
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False


- name: Delete a tenant in ManageIQ using a token
  manageiq_tenant:
    state: 'absent'
    name: 'Dep1'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      verify_ssl: False

```

## License

TODO

## Author Information
  - ['Evert Mulder']
