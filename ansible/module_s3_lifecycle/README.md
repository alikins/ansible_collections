# Ansible module: ansible.module_s3_lifecycle


Manage s3 bucket lifecycle rules in AWS

## Description

Manage s3 bucket lifecycle rules in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "expiration_date": "{'description': ['Indicates the lifetime of the objects that are subject to the rule by the date they will expire. The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified.\n']}",
    "expiration_days": "{'description': ['Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.']}",
    "name": "{'description': ['Name of the s3 bucket'], 'required': True}",
    "noncurrent_version_expiration_days": "{'description': ['Delete noncurrent versions this many days after they become noncurrent'], 'required': False, 'version_added': 2.6}",
    "noncurrent_version_storage_class": "{'description': ['Transition noncurrent versions to this storage class'], 'default': 'glacier', 'choices': ['glacier', 'onezone_ia', 'standard_ia'], 'required': False, 'version_added': 2.6}",
    "noncurrent_version_transition_days": "{'description': ['Transition noncurrent versions this many days after they become noncurrent'], 'required': False, 'version_added': 2.6}",
    "noncurrent_version_transitions": "{'description': ['A list of transition behaviors to be applied to noncurrent versions for the rule. Each storage class may be used only once. Each transition behavior contains these elements\n  I(transition_days)\n  I(storage_class)\n'], 'version_added': 2.6}",
    "prefix": "{'description': ['Prefix identifying one or more objects to which the rule applies.  If no prefix is specified, the rule will apply to the whole bucket.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_transitions": "{'description': ['"Whether to replace all the current transition(s) with the new transition(s). When false, the provided transition(s) will be added, replacing transitions with the same storage_class. When true, existing transitions will be removed and replaced with the new transition(s)\n'], 'default': True, 'type': 'bool', 'version_added': 2.6}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "rule_id": "{'description': ['Unique identifier for the rule. The value cannot be longer than 255 characters. A unique value for the rule will be generated if no value is provided.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or remove the lifecycle rule'], 'default': 'present', 'choices': ['present', 'absent']}",
    "status": "{'description': ["If 'enabled', the rule is currently being applied. If 'disabled', the rule is not currently being applied."], 'default': 'enabled', 'choices': ['enabled', 'disabled']}",
    "storage_class": "{'description': ["The storage class to transition to. Currently there are two supported values - 'glacier',  'onezone_ia', or 'standard_ia'.", "The 'standard_ia' class is only being available from Ansible version 2.2."], 'default': 'glacier', 'choices': ['glacier', 'onezone_ia', 'standard_ia']}",
    "transition_date": "{'description': ['Indicates the lifetime of the objects that are subject to the rule by the date they will transition to a different storage class. The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified. If transition_days is not specified, this parameter is required."\n']}",
    "transition_days": "{'description': ['Indicates when, in days, an object transitions to a different storage class. If transition_date is not specified, this parameter is required.']}",
    "transitions": "{'description': ['A list of transition behaviors to be applied to the rule. Each storage class may be used only once. Each transition behavior may contain these elements I(transition_days) I(transition_date) I(storage_class)'], 'version_added': 2.6}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Configure a lifecycle rule on a bucket to expire (delete) items with a prefix of /logs/ after 30 days
- s3_lifecycle:
    name: mybucket
    expiration_days: 30
    prefix: /logs/
    status: enabled
    state: present

# Configure a lifecycle rule to transition all items with a prefix of /logs/ to glacier after 7 days and then delete after 90 days
- s3_lifecycle:
    name: mybucket
    transition_days: 7
    expiration_days: 90
    prefix: /logs/
    status: enabled
    state: present

# Configure a lifecycle rule to transition all items with a prefix of /logs/ to glacier on 31 Dec 2020 and then delete on 31 Dec 2030.
# Note that midnight GMT must be specified.
# Be sure to quote your date strings
- s3_lifecycle:
    name: mybucket
    transition_date: "2020-12-30T00:00:00.000Z"
    expiration_date: "2030-12-30T00:00:00.000Z"
    prefix: /logs/
    status: enabled
    state: present

# Disable the rule created above
- s3_lifecycle:
    name: mybucket
    prefix: /logs/
    status: disabled
    state: present

# Delete the lifecycle rule created above
- s3_lifecycle:
    name: mybucket
    prefix: /logs/
    state: absent

# Configure a lifecycle rule to transition all backup files older than 31 days in /backups/ to standard infrequent access class.
- s3_lifecycle:
    name: mybucket
    prefix: /backups/
    storage_class: standard_ia
    transition_days: 31
    state: present
    status: enabled

# Configure a lifecycle rule to transition files to infrequent access after 30 days and glacier after 90
- s3_lifecycle:
    name: mybucket
    prefix: /logs/
    state: present
    status: enabled
    transitions:
      - transition_days: 30
        storage_class: standard_ia
      - transition_days: 90
        storage_class: glacier

```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
