# Ansible module: ansible.module_kinesis_stream


Manage a Kinesis Stream

## Description

Create or Delete a Kinesis Stream.
Update the retention period of a Kinesis Stream.
Update Tags on a Kinesis Stream.
Enable/disable server side encryption on a Kinesis Stream.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encryption_state": "{'description': ['Enable or Disable encryption on the Kinesis Stream.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.5'}",
    "encryption_type": "{'description': ['The type of encryption.'], 'default': 'KMS', 'version_added': '2.5'}",
    "key_id": "{'description': ['The GUID or alias for the KMS key.'], 'version_added': '2.5'}",
    "name": "{'description': ['The name of the Kinesis Stream you are managing.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "retention_period": "{'description': ['The default retention period is 24 hours and can not be less than 24 hours.', 'The retention period can be modified during any point in time.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "shards": "{'description': ['The number of shards you want to have with this stream.', 'This is required when state == present']}",
    "state": "{'description': ['Create or Delete the Kinesis Stream.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['A dictionary of resource tags of the form: { tag1: value1, tag2: value2 }.'], 'aliases': ['resource_tags']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Wait for operation to complete before returning.'], 'default': True}",
    "wait_timeout": "{'description': ['How many seconds to wait for an operation to complete before timing out.'], 'default': 300}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic creation example:
- name: Set up Kinesis Stream with 10 shards and wait for the stream to become ACTIVE
  kinesis_stream:
    name: test-stream
    shards: 10
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic creation example with tags:
- name: Set up Kinesis Stream with 10 shards, tag the environment, and wait for the stream to become ACTIVE
  kinesis_stream:
    name: test-stream
    shards: 10
    tags:
      Env: development
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic creation example with tags and increase the retention period from the default 24 hours to 48 hours:
- name: Set up Kinesis Stream with 10 shards, tag the environment, increase the retention period and wait for the stream to become ACTIVE
  kinesis_stream:
    name: test-stream
    retention_period: 48
    shards: 10
    tags:
      Env: development
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic delete example:
- name: Delete Kinesis Stream test-stream and wait for it to finish deleting.
  kinesis_stream:
    name: test-stream
    state: absent
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic enable encryption example:
- name: Encrypt Kinesis Stream test-stream.
  kinesis_stream:
    name: test-stream
    state: present
    encryption_state: enabled
    encryption_type: KMS
    key_id: alias/aws/kinesis
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic disable encryption example:
- name: Encrypt Kinesis Stream test-stream.
  kinesis_stream:
    name: test-stream
    state: present
    encryption_state: disabled
    encryption_type: KMS
    key_id: alias/aws/kinesis
    wait: yes
    wait_timeout: 600
  register: test_stream

```

## License

TODO

## Author Information
  - ['Allen Sanabria (@linuxdynasty)']
