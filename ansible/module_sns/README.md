# Ansible module: ansible.module_sns


Send Amazon Simple Notification Service messages

## Description

Sends a notification to a topic on your Amazon SNS account.

## Requirements

TODO

## Arguments

``` json
{
    "application": "{'description': ['Message to send to application subscriptions'], 'version_added': '2.8'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "email": "{'description': ['Message to send to email subscriptions.']}",
    "email_json": "{'description': ['Message to send to email-json subscriptions'], 'version_added': '2.8'}",
    "http": "{'description': ['Message to send to HTTP subscriptions']}",
    "https": "{'description': ['Message to send to HTTPS subscriptions']}",
    "lambda": "{'description': ['Message to send to Lambda subscriptions'], 'version_added': '2.8'}",
    "message_attributes": "{'description': ['Dictionary of message attributes. These are optional structured data entries to be sent along to the endpoint.', "This is in AWS's distinct Name/Type/Value format; see example below."]}",
    "message_structure": "{'description': ['The payload format to use for the message.', "This must be 'json' to support protocol-specific messages (`http`, `https`, `email`, `sms`, `sqs`). It must be 'string' to support message_attributes."], 'default': 'json', 'choices': ['json', 'string']}",
    "msg": "{'description': ['Default message for subscriptions without a more specific message.'], 'required': True, 'aliases': ['default']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sms": "{'description': ['Message to send to SMS subscriptions']}",
    "sqs": "{'description': ['Message to send to SQS subscriptions']}",
    "subject": "{'description': ['Message subject']}",
    "topic": "{'description': ['The name or ARN of the topic to publish to.'], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Send default notification message via SNS
  sns:
    msg: '{{ inventory_hostname }} has completed the play.'
    subject: Deploy complete!
    topic: deploy
  delegate_to: localhost

- name: Send notification messages via SNS with short message for SMS
  sns:
    msg: '{{ inventory_hostname }} has completed the play.'
    sms: deployed!
    subject: Deploy complete!
    topic: deploy
  delegate_to: localhost

- name: Send message with message_attributes
  sns:
    topic: "deploy"
    msg: "message with extra details!"
    message_attributes:
      channel:
        data_type: String
        string_value: "mychannel"
      color:
        data_type: String
        string_value: "green"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Michael J. Schultz (@mjschultz)', 'Paul Arthur (@flowerysong)']
  - ['Michael J. Schultz (@mjschultz)', 'Paul Arthur (@flowerysong)']
