# Ansible module: ansible.module_rax


create / delete an instance in Rackspace Public Cloud

## Description

creates / deletes a Rackspace Public Cloud instance and optionally waits for it to be 'running'.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "auto_increment": "{'description': ['Whether or not to increment a single number with the name of the created servers. Only applicable when used with the I(group) attribute or meta key.'], 'type': 'bool', 'default': True, 'version_added': 1.5}",
    "boot_from_volume": "{'description': ['Whether or not to boot the instance from a Cloud Block Storage volume. If C(yes) and I(image) is specified a new volume will be created at boot time. I(boot_volume_size) is required with I(image) to create a new volume at boot time.'], 'type': 'bool', 'default': False, 'version_added': 1.9}",
    "boot_volume": "{'description': ['Cloud Block Storage ID or Name to use as the boot volume of the instance'], 'version_added': 1.9}",
    "boot_volume_size": "{'description': ['Size of the volume to create in Gigabytes. This is only required with I(image) and I(boot_from_volume).'], 'default': 100, 'version_added': 1.9}",
    "boot_volume_terminate": "{'description': ['Whether the I(boot_volume) or newly created volume from I(image) will be terminated when the server is terminated'], 'type': 'bool', 'default': False, 'version_added': 1.9}",
    "config_drive": "{'description': ['Attach read-only configuration drive to server as label config-2'], 'type': 'bool', 'default': False, 'version_added': 1.7}",
    "count": "{'description': ['number of instances to launch'], 'default': 1, 'version_added': 1.4}",
    "count_offset": "{'description': ['number count to start at'], 'default': 1, 'version_added': 1.4}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "disk_config": "{'description': ['Disk partitioning strategy'], 'choices': ['auto', 'manual'], 'version_added': '1.4', 'default': 'auto'}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "exact_count": "{'description': ['Explicitly ensure an exact count of instances, used with state=active/present. If specified as C(yes) and I(count) is less than the servers matched, servers will be deleted to match the count. If the number of matched servers is fewer than specified in I(count) additional servers will be added.'], 'type': 'bool', 'default': False, 'version_added': 1.4}",
    "extra_client_args": "{'description': ['A hash of key/value pairs to be used when creating the cloudservers client. This is considered an advanced option, use it wisely and with caution.'], 'version_added': 1.6}",
    "extra_create_args": "{'description': ['A hash of key/value pairs to be used when creating a new server. This is considered an advanced option, use it wisely and with caution.'], 'version_added': 1.6}",
    "files": "{'description': ['Files to insert into the instance. remotefilename:localcontent']}",
    "flavor": "{'description': ['flavor to use for the instance']}",
    "group": "{'description': ['host group to assign to server, is also used for idempotent operations to ensure a specific number of instances'], 'version_added': 1.4}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "image": "{'description': ['image to use for the instance. Can be an C(id), C(human_id) or C(name). With I(boot_from_volume), a Cloud Block Storage volume will be created with this image']}",
    "instance_ids": "{'description': ["list of instance ids, currently only used when state='absent' to remove instances"], 'version_added': 1.4}",
    "key_name": "{'description': ['key pair to use on the instance'], 'aliases': ['keypair']}",
    "meta": "{'description': ['A hash of metadata to associate with the instance']}",
    "name": "{'description': ['Name to give the instance']}",
    "networks": "{'description': ['The network to attach to the instances. If specified, you must include ALL networks including the public and private interfaces. Can be C(id) or C(label).'], 'default': ['public', 'private'], 'version_added': 1.4}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "user_data": "{'description': ['Data to be uploaded to the servers config drive. This option implies I(config_drive). Can be a file path or a string'], 'version_added': 1.7}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Build a Cloud Server
  gather_facts: False
  tasks:
    - name: Server build request
      local_action:
        module: rax
        credentials: ~/.raxpub
        name: rax-test1
        flavor: 5
        image: b11d9567-e412-4255-96b9-bd63ab23bcfe
        key_name: my_rackspace_key
        files:
          /root/test.txt: /home/localuser/test.txt
        wait: yes
        state: present
        networks:
          - private
          - public
      register: rax

- name: Build an exact count of cloud servers with incremented names
  hosts: local
  gather_facts: False
  tasks:
    - name: Server build requests
      local_action:
        module: rax
        credentials: ~/.raxpub
        name: test%03d.example.org
        flavor: performance1-1
        image: ubuntu-1204-lts-precise-pangolin
        state: present
        count: 10
        count_offset: 10
        exact_count: yes
        group: test
        wait: yes
      register: rax

```

## License

TODO

## Author Information
  - ['Jesse Keating (@omgjlk)', 'Matt Martz (@sivel)']
  - ['Jesse Keating (@omgjlk)', 'Matt Martz (@sivel)']
