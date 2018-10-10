# Ansible module: ansible.module_ec2_snapshot_copy


copies an EC2 snapshot and returns the new Snapshot ID

## Description

Copies an EC2 Snapshot from a source region to a destination region.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['An optional human-readable string describing purpose of the new Snapshot.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encrypted": "{'description': ['Whether or not the destination Snapshot should be encrypted.'], 'type': 'bool', 'default': False}",
    "kms_key_id": "{'description': ['KMS key id used to encrypt snapshot. If not specified, defaults to EBS Customer Master Key (CMK) for that account.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_region": "{'description': ['The source region the Snapshot should be copied from.'], 'required': True}",
    "source_snapshot_id": "{'description': ['The ID of the Snapshot in source region that should be copied.'], 'required': True}",
    "tags": "{'description': ['A hash/dictionary of tags to add to the new Snapshot; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\'']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ["Wait for the copied Snapshot to be in 'Available' state before returning."], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'version_added': '2.6', 'description': ['How long before wait gives up, in seconds.'], 'default': 600}",
}
```

## Examples


``` yaml

# Basic Snapshot Copy
- ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx

# Copy Snapshot and wait until available
- ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    wait: yes
    wait_timeout: 1200   # Default timeout is 600
  register: snapshot_id

# Tagged Snapshot copy
- ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    tags:
        Name: Snapshot-Name

# Encrypted Snapshot copy
- ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    encrypted: yes

# Encrypted Snapshot copy with specified key
- ec2_snapshot_copy:
    source_region: eu-central-1
    region: eu-west-1
    source_snapshot_id: snap-xxxxxxx
    encrypted: yes
    kms_key_id: arn:aws:kms:eu-central-1:XXXXXXXXXXXX:key/746de6ea-50a4-4bcb-8fbc-e3b29f2d367b

```

## License

TODO

## Author Information
  - ['Deepak Kothandan (@Deepakkothandan) <deepak.kdy@gmail.com>']
