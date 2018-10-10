# Ansible module: ansible.module_profitbricks_volume


Create or destroy a volume

## Description

Allows you to create or remove a volume from a ProfitBricks datacenter. This module has a dependency on profitbricks >= 1.0.0

## Requirements

TODO

## Arguments

``` json
{
    "auto_increment": "{'description': ['Whether or not to increment a single number in the name for created virtual machines.'], 'default': True, 'type': 'bool'}",
    "bus": "{'description': ['The bus type.'], 'required': False, 'default': 'VIRTIO', 'choices': ['IDE', 'VIRTIO']}",
    "count": "{'description': ['The number of volumes you wish to create.'], 'required': False, 'default': 1}",
    "datacenter": "{'description': ['The datacenter in which to create the volumes.'], 'required': True}",
    "disk_type": "{'description': ['The disk type of the volume.'], 'required': False, 'default': 'HDD', 'choices': ['HDD', 'SSD']}",
    "image": "{'description': ['The system image ID for the volume, e.g. a3eae284-a2fe-11e4-b187-5f1f641608c8. This can also be a snapshot image ID.'], 'required': True}",
    "image_password": "{'description': ['Password set for the administrative user.'], 'required': False, 'version_added': '2.2'}",
    "instance_ids": "{'description': ["list of instance ids, currently only used when state='absent' to remove instances."], 'required': False}",
    "licence_type": "{'description': ['The licence type for the volume. This is used when the image is non-standard.'], 'required': False, 'default': 'UNKNOWN', 'choices': ['LINUX', 'WINDOWS', 'UNKNOWN', 'OTHER']}",
    "name": "{'description': ['The name of the volumes. You can enumerate the names using auto_increment.'], 'required': True}",
    "size": "{'description': ['The size of the volume.'], 'required': False, 'default': 10}",
    "ssh_keys": "{'description': ['Public SSH keys allowing access to the virtual machine.'], 'required': False, 'version_added': '2.2'}",
    "state": "{'description': ['create or terminate datacenters'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription_password": "{'description': ['THe ProfitBricks password. Overrides the PB_PASSWORD environment variable.'], 'required': False}",
    "subscription_user": "{'description': ['The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable.'], 'required': False}",
    "wait": "{'description': ['wait for the datacenter to be created before returning'], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Create Multiple Volumes

- profitbricks_volume:
    datacenter: Tardis One
    name: vol%02d
    count: 5
    auto_increment: yes
    wait_timeout: 500
    state: present

# Remove Volumes

- profitbricks_volume:
    datacenter: Tardis One
    instance_ids:
      - 'vol01'
      - 'vol02'
    wait_timeout: 500
    state: absent


```

## License

TODO

## Author Information
  - ['Matt Baldwin (baldwin@stackpointcloud.com)']
