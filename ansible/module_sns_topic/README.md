# Ansible module: ansible.module_sns_topic


Manages AWS SNS topics and subscriptions

## Description

The C(sns_topic) module allows you to create, delete, and manage subscriptions for AWS SNS topics. As of 2.6, this module can be use to subscribe and unsubscribe to topics outside of your AWS account.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "delivery_policy": "{'description': ['Delivery policy to apply to the SNS topic']}",
    "display_name": "{'description': ['Display name of the topic']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The name or ARN of the SNS topic to manage'], 'required': True}",
    "policy": "{'description': ['Policy to apply to the SNS topic']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_subscriptions": "{'description': ['Whether to purge any subscriptions not listed here. NOTE: AWS does not allow you to purge any PendingConfirmation subscriptions, so if any exist and would be purged, they are silently skipped. This means that somebody could come back later and confirm the subscription. Sorry. Blame Amazon.'], 'default': 'yes'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether to create or destroy an SNS topic'], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscriptions": "{'description': ['List of subscriptions to apply to the topic. Note that AWS requires subscriptions to be confirmed, so you will need to confirm any new subscriptions.'], 'suboptions': {'endpoint': {'description': 'Endpoint of subscription', 'required': True}, 'protocol': {'description': 'Protocol of subscription', 'required': True}}, 'default': []}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml


- name: Create alarm SNS topic
  sns_topic:
    name: "alarms"
    state: present
    display_name: "alarm SNS topic"
    delivery_policy:
      http:
        defaultHealthyRetryPolicy:
            minDelayTarget: 2
            maxDelayTarget: 4
            numRetries: 3
            numMaxDelayRetries: 5
            backoffFunction: "<linear|arithmetic|geometric|exponential>"
        disableSubscriptionOverrides: True
        defaultThrottlePolicy:
            maxReceivesPerSecond: 10
    subscriptions:
      - endpoint: "my_email_address@example.com"
        protocol: "email"
      - endpoint: "my_mobile_number"
        protocol: "sms"


```

## License

TODO

## Author Information
  - ['Joel Thompson (@joelthompson)', 'Fernando Jose Pando (@nand0p)', 'Will Thames (@willthames)']
  - ['Joel Thompson (@joelthompson)', 'Fernando Jose Pando (@nand0p)', 'Will Thames (@willthames)']
  - ['Joel Thompson (@joelthompson)', 'Fernando Jose Pando (@nand0p)', 'Will Thames (@willthames)']
