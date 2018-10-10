# Ansible module: ansible.module_rax_meta


Manipulate metadata for Rackspace Cloud Servers

## Description

Manipulate metadata for Rackspace Cloud Servers

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Server IP address to modify metadata for, will match any IP assigned to the server']}",
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "id": "{'description': ['Server ID to modify metadata for']}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "meta": "{'description': ['A hash of metadata to associate with the instance']}",
    "name": "{'description': ['Server name to modify metadata for']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Set metadata for a server
  hosts: all
  gather_facts: False
  tasks:
    - name: Set metadata
      local_action:
        module: rax_meta
        credentials: ~/.raxpub
        name: "{{ inventory_hostname }}"
        region: DFW
        meta:
          group: primary_group
          groups:
            - group_two
            - group_three
          app: my_app

    - name: Clear metadata
      local_action:
        module: rax_meta
        credentials: ~/.raxpub
        name: "{{ inventory_hostname }}"
        region: DFW

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
