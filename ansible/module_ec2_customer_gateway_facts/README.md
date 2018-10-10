# Ansible module: ansible.module_ec2_customer_gateway_facts


Gather facts about customer gateways in AWS

## Description

Gather facts about customer gateways in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "customer_gateway_ids": "{'description': ['Get details of a specific customer gateways using customer gateway ID/IDs. This value should be provided as a list.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html) for possible filters.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# # Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather facts about all customer gateways
  ec2_customer_gateway_facts:

- name: Gather facts about a filtered list of customer gateways, based on tags
  ec2_customer_gateway_facts:
    region: ap-southeast-2
    filters:
      "tag:Name": test-customer-gateway
      "tag:AltName": test-customer-gateway-alt
  register: cust_gw_facts

- name: Gather facts about a specific customer gateway by specifying customer gateway ID
  ec2_customer_gateway_facts:
    region: ap-southeast-2
    customer_gateway_ids:
      - 'cgw-48841a09'
      - 'cgw-fec021ce'
  register: cust_gw_facts

```

## License

TODO

## Author Information
  - ['Madhura Naniwadekar(@Madhura-CSI)']
