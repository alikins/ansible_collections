# Ansible module: ansible.module_aws_ses_identity


Manages SES email and domain identity

## Description

This module allows the user to manage verified email and domain identity for SES.
This covers verifying and removing identities as well as setting up complaint, bounce and delivery notification settings.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bounce_notifications": "{'description': ['Setup the SNS topic used to report bounce notifications.', 'If omitted, bounce notifications will not be delivered to a SNS topic.', 'If bounce notifications are not delivered to a SNS topic, I(feedback_forwarding) must be enabled.'], 'suboptions': {'topic': {'description': ['The ARN of the topic to send notifications to.', 'If omitted, notifications will not be delivered to a SNS topic.']}, 'include_headers': {'description': ['Whether or not to include headers when delivering to the SNS topic.', 'If I(topic) is not specified this will have no impact, but the SES setting is updated even if there is no topic.'], 'type': 'bool', 'default': False}}}",
    "complaint_notifications": "{'description': ['Setup the SNS topic used to report complaint notifications.', 'If omitted, complaint notifications will not be delivered to a SNS topic.', 'If complaint notifications are not delivered to a SNS topic, I(feedback_forwarding) must be enabled.'], 'suboptions': {'topic': {'description': ['The ARN of the topic to send notifications to.', 'If omitted, notifications will not be delivered to a SNS topic.']}, 'include_headers': {'description': ['Whether or not to include headers when delivering to the SNS topic.', 'If I(topic) is not specified this will have no impact, but the SES setting is updated even if there is no topic.'], 'type': 'bool', 'default': False}}}",
    "delivery_notifications": "{'description': ['Setup the SNS topic used to report delivery notifications.', 'If omitted, delivery notifications will not be delivered to a SNS topic.'], 'suboptions': {'topic': {'description': ['The ARN of the topic to send notifications to.', 'If omitted, notifications will not be delivered to a SNS topic.']}, 'include_headers': {'description': ['Whether or not to include headers when delivering to the SNS topic.', 'If I(topic) is not specified this will have no impact, but the SES setting is updated even if there is no topic.'], 'type': 'bool', 'default': False}}}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "feedback_forwarding": "{'description': ['Whether or not to enable feedback forwarding.', 'This can only be false if both I(bounce_notifications) and I(complaint_notifications) specify SNS topics.'], 'type': 'bool', 'default': True}",
    "identity": "{'description': ['This is the email address or domain to verify / delete.', "If this contains an '@' then it will be considered an email. Otherwise it will be considered a domain."], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether to create(or update) or delete the identity.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Ensure example@example.com email identity exists
  aws_ses_identity:
    identity: example@example.com
    state: present

- name: Delete example@example.com email identity
  aws_ses_identity:
    email: example@example.com
    state: absent

- name: Ensure example.com domain identity exists
  aws_ses_identity:
    identity: example.com
    state: present

# Create an SNS topic and send bounce and complaint notifications to it
# instead of emailing the identity owner
- name: Ensure complaints-topic exists
  sns_topic:
    name: "complaints-topic"
    state: present
    purge_subscriptions: False
  register: topic_info

- name: Deliver feedback to topic instead of owner email
  aws_ses_identity:
    identity: example@example.com
    state: present
    complaint_notifications:
      topic: "{{ topic_info.sns_arn }}"
      include_headers: True
    bounce_notifications:
      topic: "{{ topic_info.sns_arn }}"
      include_headers: False
    feedback_forwarding: False

# Create an SNS topic for delivery notifications and leave complaints
# Being forwarded to the identity owner email
- name: Ensure delivery-notifications-topic exists
  sns_topic:
    name: "delivery-notifications-topic"
    state: present
    purge_subscriptions: False
  register: topic_info

- name: Delivery notifications to topic
  aws_ses_identity:
    identity: example@example.com
    state: present
    delivery_notifications:
      topic: "{{ topic_info.sns_arn }}"

```

## License

TODO

## Author Information
  - ['Ed Costello    (@orthanc)']
