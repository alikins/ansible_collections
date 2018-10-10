# Ansible module: ansible.module_rax_scaling_group


Manipulate Rackspace Cloud Autoscale Groups

## Description

Manipulate Rackspace Cloud Autoscale Groups

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "config_drive": "{'description': ['Attach read-only configuration drive to server as label config-2'], 'type': 'bool', 'default': False, 'version_added': 1.8}",
    "cooldown": "{'description': ['The period of time, in seconds, that must pass before any scaling can occur after the previous scaling. Must be an integer between 0 and 86400 (24 hrs).']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "disk_config": "{'description': ['Disk partitioning strategy'], 'choices': ['auto', 'manual'], 'default': 'auto'}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "files": "{'description': ['Files to insert into the instance. Hash of C(remotepath: localpath)']}",
    "flavor": "{'description': ['flavor to use for the instance'], 'required': True}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "image": "{'description': ['image to use for the instance. Can be an C(id), C(human_id) or C(name)'], 'required': True}",
    "key_name": "{'description': ['key pair to use on the instance']}",
    "loadbalancers": "{'description': ['List of load balancer C(id) and C(port) hashes']}",
    "max_entities": "{'description': ['The maximum number of entities that are allowed in the scaling group. Must be an integer between 0 and 1000.'], 'required': True}",
    "meta": "{'description': ['A hash of metadata to associate with the instance']}",
    "min_entities": "{'description': ['The minimum number of entities that are allowed in the scaling group. Must be an integer between 0 and 1000.'], 'required': True}",
    "name": "{'description': ['Name to give the scaling group'], 'required': True}",
    "networks": "{'description': ['The network to attach to the instances. If specified, you must include ALL networks including the public and private interfaces. Can be C(id) or C(label).'], 'default': ['public', 'private']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "server_name": "{'description': ['The base name for servers created by Autoscale'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "user_data": "{'description': ['Data to be uploaded to the servers config drive. This option implies I(config_drive). Can be a file path or a string'], 'version_added': 1.8}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "wait": "{'description': ['wait for the scaling group to finish provisioning the minimum amount of servers'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - rax_scaling_group:
        credentials: ~/.raxpub
        region: ORD
        cooldown: 300
        flavor: performance1-1
        image: bb02b1a3-bc77-4d17-ab5b-421d89850fca
        min_entities: 5
        max_entities: 10
        name: ASG Test
        server_name: asgtest
        loadbalancers:
            - id: 228385
              port: 80
      register: asg

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
