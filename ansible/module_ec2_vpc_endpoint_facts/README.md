# Ansible module: ansible.module_ec2_vpc_endpoint_facts


Retrieves AWS VPC endpoints details using AWS methods

## Description

Gets various details related to AWS VPC Endpoints

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html) for possible filters.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "query": "{'description': ['Specifies the query action to take. Services returns the supported AWS services that can be specified when creating an endpoint.'], 'required': True, 'choices': ['services', 'endpoints']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_endpoint_ids": "{'description': ['Get details of specific endpoint IDs', 'Provide this value as a list']}",
}
```

## Examples


``` yaml

# Simple example of listing all support AWS services for VPC endpoints
- name: List supported AWS endpoint services
  ec2_vpc_endpoint_facts:
    query: services
    region: ap-southeast-2
  register: supported_endpoint_services

- name: Get all endpoints in ap-southeast-2 region
  ec2_vpc_endpoint_facts:
    query: endpoints
    region: ap-southeast-2
  register: existing_endpoints

- name: Get all endpoints with specific filters
  ec2_vpc_endpoint_facts:
    query: endpoints
    region: ap-southeast-2
    filters:
      vpc-id:
        - vpc-12345678
        - vpc-87654321
      vpc-endpoint-state:
        - available
        - pending
  register: existing_endpoints

- name: Get details on specific endpoint
  ec2_vpc_endpoint_facts:
    query: endpoints
    region: ap-southeast-2
    vpc_endpoint_ids:
      - vpce-12345678
  register: endpoint_details

```

## License

TODO

## Author Information
  - ['Karen Cheng (@Etherdaemon)']
