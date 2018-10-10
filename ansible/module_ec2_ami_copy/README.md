# Ansible module: ansible.module_ec2_ami_copy


copies AMI between AWS regions, return new image id

## Description

Copies AMI from a source region to a destination region. B(Since version 2.3 this module depends on boto3.)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['An optional human-readable string describing the contents and purpose of the new AMI.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encrypted": "{'description': ['Whether or not the destination snapshots of the copied AMI should be encrypted.'], 'version_added': '2.2'}",
    "kms_key_id": "{'description': ['KMS key id used to encrypt image. If not specified, uses default EBS Customer Master Key (CMK) for your account.'], 'version_added': '2.2'}",
    "name": "{'description': ["The name of the new AMI to copy. (As of 2.3 the default is 'default', in prior versions it was 'null'.)"], 'default': 'default'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_image_id": "{'description': ['The ID of the AMI in source region that should be copied.'], 'required': True}",
    "source_region": "{'description': ['The source region the AMI should be copied from.'], 'required': True}",
    "tag_equality": "{'description': ['Whether to use tags if the source AMI already exists in the target region. If this is set, and all tags match in an existing AMI, the AMI will not be copied again.'], 'default': False, 'version_added': 2.6}",
    "tags": "{'description': ['A hash/dictionary of tags to add to the new copied AMI; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\'']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ["Wait for the copied AMI to be in state 'available' before returning."], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds. Prior to 2.3 the default was 1200.', 'From 2.3-2.5 this option was deprecated in favor of boto3 waiter defaults. This was reenabled in 2.6 to allow timeouts greater than 10 minutes.'], 'default': 600}",
}
```

## Examples


``` yaml

# Basic AMI Copy
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx

# AMI copy wait until available
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx
    wait: yes
    wait_timeout: 1200  # Default timeout is 600
  register: image_id

# Named AMI copy
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx
    name: My-Awesome-AMI
    description: latest patch

# Tagged AMI copy (will not copy the same AMI twice)
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx
    tags:
        Name: My-Super-AMI
        Patch: 1.2.3
    tag_equality: yes

# Encrypted AMI copy
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx
    encrypted: yes

# Encrypted AMI copy with specified key
- ec2_ami_copy:
    source_region: us-east-1
    region: eu-west-1
    source_image_id: ami-xxxxxxx
    encrypted: yes
    kms_key_id: arn:aws:kms:us-east-1:XXXXXXXXXXXX:key/746de6ea-50a4-4bcb-8fbc-e3b29f2d367b

```

## License

TODO

## Author Information
  - ['Amir Moulavi (@amir343) <amir.moulavi@gmail.com>', 'Tim C <defunct@defunct.io>']
  - ['Amir Moulavi (@amir343) <amir.moulavi@gmail.com>', 'Tim C <defunct@defunct.io>']
