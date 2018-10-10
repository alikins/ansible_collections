# Ansible module: ansible.module_rax_keypair


Create a keypair for use with Rackspace Cloud Servers

## Description

Create a keypair for use with Rackspace Cloud Servers

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
    "name": "{'description': ['Name of keypair'], 'required': True}",
    "public_key": "{'description': ['Public Key string to upload. Can be a file path or string']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Create a keypair
  hosts: localhost
  gather_facts: False
  tasks:
    - name: keypair request
      local_action:
        module: rax_keypair
        credentials: ~/.raxpub
        name: my_keypair
        region: DFW
      register: keypair
    - name: Create local public key
      local_action:
        module: copy
        content: "{{ keypair.keypair.public_key }}"
        dest: "{{ inventory_dir }}/{{ keypair.keypair.name }}.pub"
    - name: Create local private key
      local_action:
        module: copy
        content: "{{ keypair.keypair.private_key }}"
        dest: "{{ inventory_dir }}/{{ keypair.keypair.name }}"

- name: Create a keypair
  hosts: localhost
  gather_facts: False
  tasks:
    - name: keypair request
      local_action:
        module: rax_keypair
        credentials: ~/.raxpub
        name: my_keypair
        public_key: "{{ lookup('file', 'authorized_keys/id_rsa.pub') }}"
        region: DFW
      register: keypair

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
