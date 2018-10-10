# Ansible module: ansible.module_ec2_vpc_endpoint


Create and delete AWS VPC Endpoints

## Description

Creates AWS VPC endpoints.
Deletes AWS VPC endpoints.
This module support check mode.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "client_token": "{'description': ['Optional client token to ensure idempotency'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "policy": "{'description': ['A properly formatted json policy as string, see U(https://github.com/ansible/ansible/issues/7005#issuecomment-42894813). Cannot be used with I(policy_file).', 'Option when creating an endpoint. If not provided AWS will utilise a default policy which provides full access to the service.'], 'required': False}",
    "policy_file": "{'description': ['The path to the properly json formatted policy file, see U(https://github.com/ansible/ansible/issues/7005#issuecomment-42894813) on how to use it properly. Cannot be used with I(policy).', 'Option when creating an endpoint. If not provided AWS will utilise a default policy which provides full access to the service.'], 'required': False, 'aliases': ['policy_path']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "route_table_ids": "{'description': ['List of one or more route table ids to attach to the endpoint. A route is added to the route table with the destination of the endpoint if provided.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "service": "{'description': ['An AWS supported vpc endpoint service. Use the ec2_vpc_endpoint_facts module to describe the supported endpoint services.', 'Required when creating an endpoint.'], 'required': False}",
    "state": "{'description': ['present to ensure resource is created.', 'absent to remove resource'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_endpoint_id": "{'description': ['One or more vpc endpoint ids to remove from the AWS account'], 'required': False}",
    "vpc_id": "{'description': ['Required when creating a VPC endpoint.'], 'required': False}",
    "wait": "{'description': ['When specified, will wait for either available status for state present. Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.'], 'required': False, 'default': False, 'type': 'bool'}",
    "wait_timeout": "{'description': ['Used in conjunction with wait. Number of seconds to wait for status. Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.'], 'required': False, 'default': 320}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create new vpc endpoint with a json template for policy
  ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    policy: " {{ lookup( 'template', 'endpoint_policy.json.j2') }} "
    route_table_ids:
      - rtb-12345678
      - rtb-87654321
  register: new_vpc_endpoint

- name: Create new vpc endpoint the default policy
  ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    route_table_ids:
      - rtb-12345678
      - rtb-87654321
  register: new_vpc_endpoint

- name: Create new vpc endpoint with json file
  ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    policy_file: "{{ role_path }}/files/endpoint_policy.json"
    route_table_ids:
      - rtb-12345678
      - rtb-87654321
  register: new_vpc_endpoint

- name: Delete newly created vpc endpoint
  ec2_vpc_endpoint:
    state: absent
    nat_gateway_id: "{{ new_vpc_endpoint.result['VpcEndpointId'] }}"
    region: ap-southeast-2

```

## License

TODO

## Author Information
  - ['Karen Cheng (@Etherdaemon)']
