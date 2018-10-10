# Ansible module: ansible.module_ec2_ami_find


Searches for AMIs to obtain the AMI ID and other information

## Description

Returns list of matching AMIs with AMI ID, along with other useful information
Can search AMIs with different owners
Can search by matching tag(s), by AMI name and/or other criteria
Results can be sorted and sliced

## Requirements

TODO

## Arguments

``` json
{
    "ami_id": "{'description': ['An AMI ID to match.']}",
    "ami_tags": "{'description': ['A hash/dictionary of tags to match for the AMI.']}",
    "architecture": "{'description': ['An architecture type to match (e.g. x86_64).']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "hypervisor": "{'description': ['A hypervisor type type to match (e.g. xen).']}",
    "is_public": "{'description': ['Whether or not the image(s) are public.'], 'type': 'bool'}",
    "name": "{'description': ['An AMI name to match.']}",
    "no_result_action": "{'description': ['What to do when no results are found.', "'success' reports success and returns an empty array", "'fail' causes the module to report failure"], 'choices': ['success', 'fail'], 'default': 'success'}",
    "owner": "{'description': ['Search AMIs owned by the specified owner', "Can specify an AWS account ID, or one of the special IDs 'self', 'amazon' or 'aws-marketplace'", 'If not specified, all EC2 AMIs in the specified region will be searched.', 'You can include wildcards in many of the search options. An asterisk (*) matches zero or more characters, and a question mark (?) matches exactly one character. You can escape special characters using a backslash (\\) before the character. For example, a value of \\*amazon\\?\\\\ searches for the literal string *amazon?\\.']}",
    "platform": "{'description': ['Platform type to match.']}",
    "product_code": "{'description': ['Marketplace product code to match.'], 'version_added': '2.3'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use.'], 'required': True, 'aliases': ['aws_region', 'ec2_region']}",
    "root_device_type": "{'description': ['Root device type to match (e.g. ebs, instance-store).'], 'version_added': '2.5'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sort": "{'description': ['Optional attribute which with to sort the results.', "If specifying 'tag', the 'tag_name' parameter is required.", 'Starting at version 2.1, additional sort choices of architecture, block_device_mapping, creationDate, hypervisor, is_public, location, owner_id, platform, root_device_name, root_device_type, state, and virtualization_type are supported.'], 'choices': ['name', 'description', 'tag', 'architecture', 'block_device_mapping', 'creationDate', 'hypervisor', 'is_public', 'location', 'owner_id', 'platform', 'root_device_name', 'root_device_type', 'state', 'virtualization_type']}",
    "sort_end": "{'description': ['Which result to end with (when sorting).', 'Corresponds to Python slice notation.']}",
    "sort_order": "{'description': ['Order in which to sort results.', "Only used when the 'sort' parameter is specified."], 'choices': ['ascending', 'descending'], 'default': 'ascending'}",
    "sort_start": "{'description': ['Which result to start with (when sorting).', 'Corresponds to Python slice notation.']}",
    "sort_tag": "{'description': ['Tag name with which to sort results.', "Required when specifying 'sort=tag'."]}",
    "state": "{'description': ['AMI state to match.'], 'default': 'available'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "virtualization_type": "{'description': ['Virtualization type to match (e.g. hvm).']}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Search for the AMI tagged "project:website"
- ec2_ami_find:
    owner: self
    ami_tags:
      project: website
    no_result_action: fail
  register: ami_find

# Search for the latest Ubuntu 14.04 AMI
- ec2_ami_find:
    name: "ubuntu/images/ebs/ubuntu-trusty-14.04-amd64-server-*"
    owner: 099720109477
    sort: name
    sort_order: descending
    sort_end: 1
  register: ami_find

# Launch an EC2 instance
- ec2:
    image: "{{ ami_find.results[0].ami_id }}"
    instance_type: m3.medium
    key_name: mykey
    wait: yes

```

## License

TODO

## Author Information
  - ['Tom Bamford (@tombamford)']
