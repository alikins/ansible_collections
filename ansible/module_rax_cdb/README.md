# Ansible module: ansible.module_rax_cdb


create/delete or resize a Rackspace Cloud Databases instance

## Description

creates / deletes or resize a Rackspace Cloud Databases instance and optionally waits for it to be 'running'. The name option needs to be unique since it's used to identify the instance.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "cdb_type": "{'description': ['type of instance (i.e. MySQL, MariaDB, Percona)'], 'default': 'MySQL', 'version_added': '2.0', 'aliases': ['type']}",
    "cdb_version": "{'description': ['version of database (MySQL supports 5.1 and 5.6, MariaDB supports 10, Percona supports 5.6)'], 'choices': ['5.1', '5.6', '10'], 'version_added': '2.0', 'aliases': ['version']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "flavor": "{'description': ['flavor to use for the instance 1 to 6 (i.e. 512MB to 16GB)'], 'default': 1}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "name": "{'description': ['Name of the databases server instance']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "volume": "{'description': ['Volume size of the database 1-150GB'], 'default': 2}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Build a Cloud Databases
  gather_facts: False
  tasks:
    - name: Server build request
      local_action:
        module: rax_cdb
        credentials: ~/.raxpub
        region: IAD
        name: db-server1
        flavor: 1
        volume: 2
        cdb_type: MySQL
        cdb_version: 5.6
        wait: yes
        state: present
      register: rax_db_server

```

## License

TODO

## Author Information
  - ['Simon JAILLET (@jails)']
