# Ansible module: ansible.module_ec2_vol


create and attach a volume, return volume id and device map

## Description

creates an EBS volume and optionally attaches it to an instance. If both an instance ID and a device name is given and the instance has a device at the device name, then no volume is created and no attachment is made. This module has a dependency on python-boto.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "delete_on_termination": "{'description': ['When set to "yes", the volume will be deleted upon instance termination.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "device_name": "{'description': ['device id to override device mapping. Assumes /dev/sdf for Linux/UNIX and /dev/xvdf for Windows.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encrypted": "{'description': ['Enable encryption at rest for this volume.'], 'default': 'no', 'version_added': '1.8'}",
    "id": "{'description': ['volume id if you wish to attach an existing volume (requires instance) or remove an existing volume'], 'version_added': '1.6'}",
    "instance": "{'description': ['instance ID if you wish to attach the volume. Since 1.9 you can set to None to detach.']}",
    "iops": "{'description': ['the provisioned IOPs you want to associate with this volume (integer).'], 'default': 100, 'version_added': '1.3'}",
    "kms_key_id": "{'description': ['Specify the id of the KMS key to use.'], 'version_added': '2.3'}",
    "name": "{'description': ['volume Name tag if you wish to attach an existing volume (requires instance)'], 'version_added': '1.6'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "snapshot": "{'description': ['snapshot ID on which to base the volume'], 'version_added': '1.5'}",
    "state": "{'description': ['whether to ensure the volume is present or absent, or to list existing volumes (The C(list) option was added in version 1.8).'], 'default': 'present', 'choices': ['absent', 'present', 'list'], 'version_added': '1.6'}",
    "tags": "{'description': ['tag:value pairs to add to the volume after creation'], 'default': {}, 'version_added': '2.3'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volume_size": "{'description': ['size of volume (in GB) to create.']}",
    "volume_type": "{'description': ['Type of EBS volume; standard (magnetic), gp2 (SSD), io1 (Provisioned IOPS), st1 (Throughput Optimized HDD), sc1 (Cold HDD). "Standard" is the old EBS default and continues to remain the Ansible default for backwards compatibility.'], 'default': 'standard', 'version_added': '1.9'}",
    "zone": "{'description': ['zone in which to create the volume, if unset uses the zone the instance is in (if set)'], 'aliases': ['aws_zone', 'ec2_zone']}",
}
```

## Examples


``` yaml

# Simple attachment action
- ec2_vol:
    instance: XXXXXX
    volume_size: 5
    device_name: sdd

# Example using custom iops params
- ec2_vol:
    instance: XXXXXX
    volume_size: 5
    iops: 100
    device_name: sdd

# Example using snapshot id
- ec2_vol:
    instance: XXXXXX
    snapshot: "{{ snapshot }}"

# Playbook example combined with instance launch
- ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    wait: yes
    count: 3
  register: ec2
- ec2_vol:
    instance: "{{ item.id }}"
    volume_size: 5
  with_items: "{{ ec2.instances }}"
  register: ec2_vol

# Example: Launch an instance and then add a volume if not already attached
#   * Volume will be created with the given name if not already created.
#   * Nothing will happen if the volume is already attached.
#   * Requires Ansible 2.0

- ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    zone: YYYYYY
    id: my_instance
    wait: yes
    count: 1
  register: ec2

- ec2_vol:
    instance: "{{ item.id }}"
    name: my_existing_volume_Name_tag
    device_name: /dev/xvdf
  with_items: "{{ ec2.instances }}"
  register: ec2_vol

# Remove a volume
- ec2_vol:
    id: vol-XXXXXXXX
    state: absent

# Detach a volume (since 1.9)
- ec2_vol:
    id: vol-XXXXXXXX
    instance: None

# List volumes for an instance
- ec2_vol:
    instance: i-XXXXXX
    state: list

# Create new volume using SSD storage
- ec2_vol:
    instance: XXXXXX
    volume_size: 50
    volume_type: gp2
    device_name: /dev/xvdf

# Attach an existing volume to instance. The volume will be deleted upon instance termination.
- ec2_vol:
    instance: XXXXXX
    id: XXXXXX
    device_name: /dev/sdf
    delete_on_termination: yes

```

## License

TODO

## Author Information
  - ['Lester Wade (@lwade)']
