# Ansible module: ansible.module_rax_cbs


Manipulate Rackspace Cloud Block Storage Volumes

## Description

Manipulate Rackspace Cloud Block Storage Volumes

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "description": "{'description': ['Description to give the volume being created']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "image": "{'description': ['image to use for bootable volumes. Can be an C(id), C(human_id) or C(name). This option requires C(pyrax>=1.9.3)'], 'version_added': 1.9}",
    "meta": "{'description': ['A hash of metadata to associate with the volume']}",
    "name": "{'description': ['Name to give the volume being created'], 'required': True}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "size": "{'description': ['Size of the volume to create in Gigabytes'], 'default': 100, 'required': True}",
    "snapshot_id": "{'description': ['The id of the snapshot to create the volume from']}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present', 'required': True}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "volume_type": "{'description': ['Type of the volume being created'], 'choices': ['SATA', 'SSD'], 'default': 'SATA', 'required': True}",
    "wait": "{'description': ["wait for the volume to be in state 'available' before returning"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Build a Block Storage Volume
  gather_facts: False
  hosts: local
  connection: local
  tasks:
    - name: Storage volume create request
      local_action:
        module: rax_cbs
        credentials: ~/.raxpub
        name: my-volume
        description: My Volume
        volume_type: SSD
        size: 150
        region: DFW
        wait: yes
        state: present
        meta:
          app: my-cool-app
      register: my_volume

```

## License

TODO

## Author Information
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
