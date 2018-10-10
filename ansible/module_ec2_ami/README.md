# Ansible module: ansible.module_ec2_ami


create or destroy an image in ec2

## Description

Registers or deregisters ec2 images.

## Requirements

TODO

## Arguments

``` json
{
    "architecture": "{'version_added': '2.3', 'description': ['The target architecture of the image to register']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "billing_products": "{'description': ['A list of valid billing codes. To be used with valid accounts by aws marketplace vendors.'], 'version_added': '2.5'}",
    "delete_snapshot": "{'description': ['Delete snapshots when deregistering the AMI.'], 'default': False, 'type': 'bool'}",
    "description": "{'description': ['Human-readable string describing the contents and purpose of the AMI.']}",
    "device_mapping": "{'version_added': '2.0', 'description': ['List of device hashes/dictionaries with custom configurations (same block-device-mapping parameters).', 'Valid properties include: device_name, volume_type, size/volume_size (in GB), delete_on_termination (boolean), no_device (boolean), snapshot_id, iops (for io1 volume_type), encrypted\n']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "enhanced_networking": "{'description': ['A boolean representing whether enhanced networking with ENA is enabled or not.'], 'version_added': '2.5'}",
    "image_id": "{'description': ['Image ID to be deregistered.']}",
    "image_location": "{'description': ['The s3 location of an image to use for the AMI.'], 'version_added': '2.5'}",
    "instance_id": "{'description': ['Instance ID to create the AMI from.']}",
    "kernel_id": "{'version_added': '2.3', 'description': ['The target kernel id of the image to register.']}",
    "launch_permissions": "{'description': ['Users and groups that should be able to launch the AMI. Expects dictionary with a key of user_ids and/or group_names. user_ids should be a list of account ids. group_name should be a list of groups, "all" is the only acceptable value currently.', 'You must pass all desired launch permissions if you wish to modify existing launch permissions (passing just groups will remove all users)'], 'version_added': '2.0'}",
    "name": "{'description': ['The name of the new AMI.']}",
    "no_reboot": "{'description': ['Flag indicating that the bundling process should not attempt to shutdown the instance before bundling. If this flag is True, the responsibility of maintaining file system integrity is left to the owner of the instance.'], 'default': False, 'type': 'bool'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_tags": "{'description': ["Whether to remove existing tags that aren't passed in the C(tags) parameter"], 'version_added': '2.5', 'default': 'no'}",
    "ramdisk_id": "{'description': ['The ID of the RAM disk.'], 'version_added': '2.5'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "root_device_name": "{'version_added': '2.3', 'description': ['The root device name of the image to register.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sriov_net_support": "{'description': ['Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.'], 'version_added': '2.5'}",
    "state": "{'description': ['Register or deregister an AMI.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tags": "{'description': ['A dictionary of tags to add to the new image; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\''], 'version_added': '2.0'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "virtualization_type": "{'version_added': '2.3', 'description': ['The virtualization type of the image to register.']}",
    "wait": "{'description': ["Wait for the AMI to be in state 'available' before returning."], 'default': False, 'type': 'bool'}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds.'], 'default': 900}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic AMI Creation
- ec2_ami:
    instance_id: i-xxxxxx
    wait: yes
    name: newtest
    tags:
      Name: newtest
      Service: TestService

# Basic AMI Creation, without waiting
- ec2_ami:
    instance_id: i-xxxxxx
    wait: no
    name: newtest

# AMI Registration from EBS Snapshot
- ec2_ami:
    name: newtest
    state: present
    architecture: x86_64
    virtualization_type: hvm
    root_device_name: /dev/xvda
    device_mapping:
      - device_name: /dev/xvda
        volume_size: 8
        snapshot_id: snap-xxxxxxxx
        delete_on_termination: true
        volume_type: gp2

# AMI Creation, with a custom root-device size and another EBS attached
- ec2_ami:
    instance_id: i-xxxxxx
    name: newtest
    device_mapping:
        - device_name: /dev/sda1
          size: XXX
          delete_on_termination: true
          volume_type: gp2
        - device_name: /dev/sdb
          size: YYY
          delete_on_termination: false
          volume_type: gp2

# AMI Creation, excluding a volume attached at /dev/sdb
- ec2_ami:
    instance_id: i-xxxxxx
    name: newtest
    device_mapping:
        - device_name: /dev/sda1
          size: XXX
          delete_on_termination: true
          volume_type: gp2
        - device_name: /dev/sdb
          no_device: yes

# Deregister/Delete AMI (keep associated snapshots)
- ec2_ami:
    image_id: "{{ instance.image_id }}"
    delete_snapshot: False
    state: absent

# Deregister AMI (delete associated snapshots too)
- ec2_ami:
    image_id: "{{ instance.image_id }}"
    delete_snapshot: True
    state: absent

# Update AMI Launch Permissions, making it public
- ec2_ami:
    image_id: "{{ instance.image_id }}"
    state: present
    launch_permissions:
      group_names: ['all']

# Allow AMI to be launched by another account
- ec2_ami:
    image_id: "{{ instance.image_id }}"
    state: present
    launch_permissions:
      user_ids: ['123456789012']

```

## License

TODO

## Author Information
  - ['Evan Duffield (@scicoin-project) <eduffield@iacquire.com>', 'Constantin Bugneac (@Constantin07) <constantin.bugneac@endava.com>', 'Ross Williams (@gunzy83) <gunzy83au@gmail.com>', 'Willem van Ketwich (@wilvk) <willvk@gmail.com>']
  - ['Evan Duffield (@scicoin-project) <eduffield@iacquire.com>', 'Constantin Bugneac (@Constantin07) <constantin.bugneac@endava.com>', 'Ross Williams (@gunzy83) <gunzy83au@gmail.com>', 'Willem van Ketwich (@wilvk) <willvk@gmail.com>']
  - ['Evan Duffield (@scicoin-project) <eduffield@iacquire.com>', 'Constantin Bugneac (@Constantin07) <constantin.bugneac@endava.com>', 'Ross Williams (@gunzy83) <gunzy83au@gmail.com>', 'Willem van Ketwich (@wilvk) <willvk@gmail.com>']
  - ['Evan Duffield (@scicoin-project) <eduffield@iacquire.com>', 'Constantin Bugneac (@Constantin07) <constantin.bugneac@endava.com>', 'Ross Williams (@gunzy83) <gunzy83au@gmail.com>', 'Willem van Ketwich (@wilvk) <willvk@gmail.com>']
