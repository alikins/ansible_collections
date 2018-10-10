# Ansible module: ansible.module_ec2_snapshot


creates a snapshot from an existing volume

## Description

creates an EC2 snapshot from an existing EBS volume

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['description to be applied to the snapshot'], 'required': False}",
    "device_name": "{'description': ['device name of a mounted volume to be snapshotted'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "instance_id": "{'description': ['instance that has the required volume to snapshot mounted'], 'required': False}",
    "last_snapshot_min_age": "{'description': ["If the volume's most recent snapshot has started less than `last_snapshot_min_age' minutes ago, a new snapshot will not be created."], 'required': False, 'default': 0, 'version_added': '2.0'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "snapshot_id": "{'description': ['snapshot id to remove'], 'required': False, 'version_added': '1.9'}",
    "snapshot_tags": "{'description': ['a hash/dictionary of tags to add to the snapshot'], 'required': False, 'version_added': '1.6'}",
    "state": "{'description': ['whether to add or create a snapshot'], 'required': False, 'default': 'present', 'choices': ['absent', 'present'], 'version_added': '1.9'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volume_id": "{'description': ['volume from which to take the snapshot'], 'required': False}",
    "wait": "{'description': ['wait for the snapshot to be ready'], 'type': 'bool', 'required': False, 'default': True, 'version_added': '1.5.1'}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds', 'specify 0 to wait forever'], 'required': False, 'default': 0, 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

# Simple snapshot of volume using volume_id
- ec2_snapshot:
    volume_id: vol-abcdef12
    description: snapshot of /data from DB123 taken 2013/11/28 12:18:32

# Snapshot of volume mounted on device_name attached to instance_id
- ec2_snapshot:
    instance_id: i-12345678
    device_name: /dev/sdb1
    description: snapshot of /data from DB123 taken 2013/11/28 12:18:32

# Snapshot of volume with tagging
- ec2_snapshot:
    instance_id: i-12345678
    device_name: /dev/sdb1
    snapshot_tags:
        frequency: hourly
        source: /data

# Remove a snapshot
- local_action:
    module: ec2_snapshot
    snapshot_id: snap-abcd1234
    state: absent

# Create a snapshot only if the most recent one is older than 1 hour
- local_action:
    module: ec2_snapshot
    volume_id: vol-abcdef12
    last_snapshot_min_age: 60

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)']
