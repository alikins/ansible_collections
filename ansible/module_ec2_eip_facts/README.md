# Ansible module: ansible.module_ec2_eip_facts


List EC2 EIP details

## Description

List details of EC2 Elastic IP addresses.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A set of filters to use. Each filter is a name:value pair. The value may be a list or a single element.'], 'required': False, 'default': {}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details or the AWS region,
# see the AWS Guide for details.

# List all EIP addresses in the current region.
- ec2_eip_facts:
  register: regional_eip_addresses

# List all EIP addresses for a VM.
- ec2_eip_facts:
    filters:
       instance-id: i-123456789
  register: my_vm_eips

- debug: msg="{{ my_vm_eips.addresses | json_query("[?private_ip_address=='10.0.0.5']") }}"

# List all EIP addresses for several VMs.
- ec2_eip_facts:
    filters:
       instance-id:
         - i-123456789
         - i-987654321
  register: my_vms_eips


```

## License

TODO

## Author Information
  - ['Brad Macpherson (@iiibrad)']
