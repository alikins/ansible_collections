# Ansible module: ansible.module_sqs_queue


Creates or deletes AWS SQS queues

## Description

Create or delete AWS SQS queues.
Update attributes on existing queues.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "default_visibility_timeout": "{'description': ['The default visibility timeout in seconds.']}",
    "delivery_delay": "{'description': ['The delivery delay in seconds.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "maximum_message_size": "{'description': ['The maximum message size in bytes.']}",
    "message_retention_period": "{'description': ['The message retention period in seconds.']}",
    "name": "{'description': ['Name of the queue.'], 'required': True}",
    "policy": "{'description': ['The json dict policy to attach to queue'], 'version_added': '2.1'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "receive_message_wait_time": "{'description': ['The receive message wait time in seconds.']}",
    "redrive_policy": "{'description': ['json dict with the redrive_policy (see example)'], 'version_added': '2.2'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete the queue'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create SQS queue with redrive policy
- sqs_queue:
    name: my-queue
    region: ap-southeast-2
    default_visibility_timeout: 120
    message_retention_period: 86400
    maximum_message_size: 1024
    delivery_delay: 30
    receive_message_wait_time: 20
    policy: "{{ json_dict }}"
    redrive_policy:
      maxReceiveCount: 5
      deadLetterTargetArn: arn:aws:sqs:eu-west-1:123456789012:my-dead-queue

# Delete SQS queue
- sqs_queue:
    name: my-queue
    region: ap-southeast-2
    state: absent

```

## License

TODO

## Author Information
  - ['Alan Loi (@loia)', 'Fernando Jose Pando (@nand0p)', 'Nadir Lloret (@nadirollo)']
  - ['Alan Loi (@loia)', 'Fernando Jose Pando (@nand0p)', 'Nadir Lloret (@nadirollo)']
  - ['Alan Loi (@loia)', 'Fernando Jose Pando (@nand0p)', 'Nadir Lloret (@nadirollo)']
