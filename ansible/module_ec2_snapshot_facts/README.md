# Ansible module: ansible.module_ec2_snapshot_facts


Gather facts about ec2 volume snapshots in AWS

## Description

Gather facts about ec2 volume snapshots in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value. See       U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) for possible filters. Filter       names and values are case sensitive.'], 'required': False, 'default': {}}",
    "owner_ids": "{'description': ['If you specify one or more snapshot owners, only snapshots from the specified owners and for which you have       access are returned.'], 'required': False, 'default': []}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "restorable_by_user_ids": "{'description': ['If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are       returned.'], 'required': False, 'default': []}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "snapshot_ids": "{'description': ['If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned.'], 'required': False, 'default': []}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all snapshots, including public ones
- ec2_snapshot_facts:

# Gather facts about all snapshots owned by the account 0123456789
- ec2_snapshot_facts:
    filters:
      owner-id: 0123456789

# Or alternatively...
- ec2_snapshot_facts:
    owner_ids:
      - 0123456789

# Gather facts about a particular snapshot using ID
- ec2_snapshot_facts:
    filters:
      snapshot-id: snap-00112233

# Or alternatively...
- ec2_snapshot_facts:
    snapshot_ids:
      - snap-00112233

# Gather facts about any snapshot with a tag key Name and value Example
- ec2_snapshot_facts:
    filters:
      "tag:Name": Example

# Gather facts about any snapshot with an error status
- ec2_snapshot_facts:
    filters:
      status: error


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
