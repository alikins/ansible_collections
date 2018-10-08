# Ansible lookup: ansible.lookup_aws_account_attribute


Look up AWS account attributes

## Description

Describes attributes of your AWS account. You can specify one of the listed attribute choices or omit it to see all attributes.

## Requirements

TODO

## Arguments

``` json
{
    "attribute": "{'description': ['The attribute for which to get the value(s).'], 'choices': ['supported-platforms', 'default-vpc', 'max-instances', 'vpc-max-security-groups-per-interface', 'max-elastic-ips', 'vpc-max-elastic-ips', 'has-ec2-classic']}",
    "aws_access_key": "{'description': ['The AWS access key to use.'], 'env': [{'name': 'AWS_ACCESS_KEY_ID'}, {'name': 'AWS_ACCESS_KEY'}, {'name': 'EC2_ACCESS_KEY'}]}",
    "aws_profile": "{'description': ['The AWS profile'], 'aliases': ['boto_profile'], 'env': [{'name': 'AWS_PROFILE'}, {'name': 'AWS_DEFAULT_PROFILE'}]}",
    "aws_secret_key": "{'description': ['The AWS secret key that corresponds to the access key.'], 'env': [{'name': 'AWS_SECRET_ACCESS_KEY'}, {'name': 'AWS_SECRET_KEY'}, {'name': 'EC2_SECRET_KEY'}]}",
    "aws_security_token": "{'description': ['The AWS security token if using temporary access and secret keys.'], 'env': [{'name': 'AWS_SECURITY_TOKEN'}, {'name': 'AWS_SESSION_TOKEN'}, {'name': 'EC2_SECURITY_TOKEN'}]}",
    "region": "{'description': ['The region for which to create the connection.'], 'env': [{'name': 'AWS_REGION'}, {'name': 'EC2_REGION'}]}",
}
```

## Examples


``` yaml

vars:
  has_ec2_classic: "{{ lookup('aws_account_attribute', attribute='has-ec2-classic') }}"
  # true | false

  default_vpc_id: "{{ lookup('aws_account_attribute', attribute='default-vpc') }}"
  # vpc-xxxxxxxx | none

  account_details: "{{ lookup('aws_account_attribute', wantlist='true') }}"
  # {'default-vpc': ['vpc-xxxxxxxx'], 'max-elastic-ips': ['5'], 'max-instances': ['20'],
  #  'supported-platforms': ['VPC', 'EC2'], 'vpc-max-elastic-ips': ['5'], 'vpc-max-security-groups-per-interface': ['5']}


```

## License

TODO

## Author Information
  - ['Sloane Hertel <shertel@redhat.com>']
