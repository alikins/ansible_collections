# Ansible module: ansible.module_rax_cbs_attachments


Manipulate Rackspace Cloud Block Storage Volume Attachments

## Description

Manipulate Rackspace Cloud Block Storage Volume Attachments

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "device": "{'description': ['The device path to attach the volume to, e.g. /dev/xvde.', 'Before 2.4 this was a required field. Now it can be left to null to auto assign the device name.']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "server": "{'description': ['Name or id of the server to attach/detach'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present', 'required': True}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "volume": "{'description': ['Name or id of the volume to attach/detach'], 'required': True}",
    "wait": "{'description': ["wait for the volume to be in 'in-use'/'available' state before returning"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Attach a Block Storage Volume
  gather_facts: False
  hosts: local
  connection: local
  tasks:
    - name: Storage volume attach request
      local_action:
        module: rax_cbs_attachments
        credentials: ~/.raxpub
        volume: my-volume
        server: my-server
        device: /dev/xvdd
        region: DFW
        wait: yes
        state: present
      register: my_volume

```

## License

TODO

## Author Information
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
