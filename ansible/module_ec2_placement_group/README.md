# Ansible module: ansible.module_ec2_placement_group


Create or delete an EC2 Placement Group

## Description

Create an EC2 Placement Group; if the placement group already exists, nothing is done. Or, delete an existing placement group. If the placement group is absent, do nothing. See also http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The name for the placement group.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete placement group.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "strategy": "{'description': ['Placement group strategy. Cluster will cluster instances into a low-latency group in a single Availability Zone, while Spread spreads instances across underlying hardware.'], 'required': False, 'default': 'cluster', 'choices': ['cluster', 'spread']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide
# for details.

# Create a placement group.
- ec2_placement_group:
    name: my-cluster
    state: present

# Create a Spread placement group.
- ec2_placement_group:
    name: my-cluster
    state: present
    strategy: spread

# Delete a placement group.
- ec2_placement_group:
    name: my-cluster
    state: absent


```

## License

TODO

## Author Information
  - ['Brad Macpherson (@iiibrad)']
