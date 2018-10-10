# Ansible module: ansible.module_aws_direct_connect_gateway


Manage AWS Direct Connect Gateway

## Description

Creates AWS Direct Connect Gateway
Deletes AWS Direct Connect Gateway
Attaches Virtual Gateways to Direct Connect Gateway
Detaches Virtual Gateways to Direct Connect Gateway

## Requirements

TODO

## Arguments

``` json
{
    "amazon_asn": "{'description': ['amazon side asn'], 'required': True}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "direct_connect_gateway_id": "{'description': ['id of an existing direct connect gateway'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['name of the dxgw to be created or deleted'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['present to ensure resource is created.', 'absent to remove resource'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "virtual_gateway_id": "{'description': ['vpn gateway id of an existing virtual gateway'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create a new direct connect gateway attached to virtual private gateway
  dxgw:
    state: present
    name: my-dx-gateway
    amazon_asn: 7224
    virtual_gateway_id: vpg-12345
  register: created_dxgw

- name: Create a new unattached dxgw
  dxgw:
    state: present
    name: my-dx-gateway
    amazon_asn: 7224
  register: created_dxgw


```

## License

TODO

## Author Information
  - ['Gobin Sougrakpam (gobins@github)']
