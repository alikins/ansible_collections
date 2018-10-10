# Ansible module: ansible.module_rax_identity


Load Rackspace Cloud Identity

## Description

Verifies Rackspace Cloud credentials and returns identity information

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present', 'required': False}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Load Rackspace Cloud Identity
  gather_facts: False
  hosts: local
  connection: local
  tasks:
    - name: Load Identity
      local_action:
        module: rax_identity
        credentials: ~/.raxpub
        region: DFW
      register: rackspace_identity

```

## License

TODO

## Author Information
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
