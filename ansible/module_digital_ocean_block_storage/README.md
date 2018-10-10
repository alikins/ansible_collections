# Ansible module: ansible.module_digital_ocean_block_storage


Create/destroy or attach/detach Block Storage volumes in DigitalOcean

## Description

Create/destroy Block Storage volume in DigitalOcean, or attach/detach Block Storage volume to a droplet.

## Requirements

TODO

## Arguments

``` json
{
    "block_size": "{'description': ['The size of the Block Storage volume in gigabytes. Required when command=create and state=present. If snapshot_id is included, this will be ignored.']}",
    "command": "{'description': ['Which operation do you want to perform.'], 'choices': ['create', 'attach'], 'required': True}",
    "description": "{'description': ['Description of the Block Storage volume.']}",
    "droplet_id": "{'description': ['The droplet id you want to operate on. Required when command=attach.']}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "region": "{'description': ['The slug of the region where your Block Storage volume should be located in. If snapshot_id is included, this will be ignored.'], 'required': True}",
    "snapshot_id": "{'version_added': '2.5', 'description': ['The snapshot id you would like the Block Storage volume created with. If included, region and block_size will be ignored and changed to null.']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'choices': ['present', 'absent'], 'required': True}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "volume_name": "{'description': ['The name of the Block Storage volume.'], 'required': True}",
}
```

## Examples


``` yaml

# Create new Block Storage
- digital_ocean_block_storage:
    state: present
    command: create
    api_token: <TOKEN>
    region: nyc1
    block_size: 10
    volume_name: nyc1-block-storage
# Delete Block Storage
- digital_ocean_block_storage:
    state: absent
    command: create
    api_token: <TOKEN>
    region: nyc1
    volume_name: nyc1-block-storage
# Attach Block Storage to a Droplet
- digital_ocean_block_storage:
    state: present
    command: attach
    api_token: <TOKEN>
    volume_name: nyc1-block-storage
    region: nyc1
    droplet_id: <ID>
# Detach Block Storage from a Droplet
- digital_ocean_block_storage:
    state: absent
    command: attach
    api_token: <TOKEN>
    volume_name: nyc1-block-storage
    region: nyc1
    droplet_id: <ID>

```

## License

TODO

## Author Information
  - ['Harnek Sidhu (github: @harneksidhu)']
