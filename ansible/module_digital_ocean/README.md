# Ansible module: ansible.module_digital_ocean


Create/delete a droplet/SSH_key in DigitalOcean

## Description

Create/delete a droplet in DigitalOcean and optionally wait for it to be 'running', or deploy an SSH key.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['DigitalOcean api token.'], 'version_added': '1.9.5'}",
    "backups_enabled": "{'description': ['Optional, Boolean, enables backups for your droplet.'], 'type': 'bool', 'default': False, 'version_added': '1.6'}",
    "command": "{'description': ['Which target you want to operate on.'], 'default': 'droplet', 'choices': ['droplet', 'ssh']}",
    "id": "{'description': ['Numeric, the droplet id you want to operate on.'], 'aliases': ['droplet_id']}",
    "image_id": "{'description': ['This is the slug of the image you would like the droplet created with.']}",
    "ipv6": "{'description': ['Optional, Boolean, enable IPv6 for your droplet.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "name": "{'description': ['String, this is the name of the droplet - must be formatted by hostname rules, or the name of a SSH key.']}",
    "private_networking": "{'description': ['Bool, add an additional, private network interface to droplet for inter-droplet communication.'], 'type': 'bool', 'default': False, 'version_added': '1.4'}",
    "region_id": "{'description': ['This is the slug of the region you would like your server to be created in.']}",
    "size_id": "{'description': ['This is the slug of the size you would like the droplet created with.']}",
    "ssh_key_ids": "{'description': ['Optional, array of SSH key (numeric) ID that you would like to be added to the server.']}",
    "ssh_pub_key": "{'description': ['The public SSH key you want to add to your account.']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'active', 'absent', 'deleted']}",
    "unique_name": "{'description': ['Bool, require unique hostnames.  By default, DigitalOcean allows multiple hosts with the same name.  Setting this to "yes" allows only one host per name.  Useful for idempotence.'], 'type': 'bool', 'default': False, 'version_added': '1.4'}",
    "user_data": "{'description': ['opaque blob of data which is made available to the droplet'], 'version_added': '2.0'}",
    "virtio": "{'description': ['Bool, turn on virtio driver in droplet for improved network and storage I/O.'], 'type': 'bool', 'default': True, 'version_added': '1.4'}",
    "wait": "{'description': ['Wait for the droplet to be in state \'running\' before returning.  If wait is "no" an ip_address may not be returned.'], 'type': 'bool', 'default': True}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds.'], 'default': 300}",
}
```

## Examples


``` yaml

# Ensure a SSH key is present
# If a key matches this name, will return the ssh key id and changed = False
# If no existing key matches this name, a new key is created, the ssh key id is returned and changed = False

- digital_ocean:
    state: present
    command: ssh
    name: my_ssh_key
    ssh_pub_key: 'ssh-rsa AAAA...'
    api_token: XXX

# Create a new Droplet
# Will return the droplet details including the droplet id (used for idempotence)

- digital_ocean:
    state: present
    command: droplet
    name: mydroplet
    api_token: XXX
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64
    wait_timeout: 500
  register: my_droplet

- debug:
    msg: "ID is {{ my_droplet.droplet.id }}"

- debug:
    msg: "IP is {{ my_droplet.droplet.ip_address }}"

# Ensure a droplet is present
# If droplet id already exist, will return the droplet details and changed = False
# If no droplet matches the id, a new droplet will be created and the droplet details (including the new id) are returned, changed = True.

- digital_ocean:
    state: present
    command: droplet
    id: 123
    name: mydroplet
    api_token: XXX
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64
    wait_timeout: 500

# Create a droplet with ssh key
# The ssh key id can be passed as argument at the creation of a droplet (see ssh_key_ids).
# Several keys can be added to ssh_key_ids as id1,id2,id3
# The keys are used to connect as root to the droplet.

- digital_ocean:
    state: present
    ssh_key_ids: 123,456
    name: mydroplet
    api_token: XXX
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64


```

## License

TODO

## Author Information
  - ['Vincent Viallet (@zbal)']
