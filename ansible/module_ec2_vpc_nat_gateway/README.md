# Ansible module: ansible.module_ec2_vpc_nat_gateway


Manage AWS VPC NAT Gateways

## Description

Ensure the state of AWS VPC NAT Gateways based on their id, allocation and subnet ids.

## Requirements

TODO

## Arguments

``` json
{
    "allocation_id": "{'description': ['The id of the elastic IP allocation. If this is not passed and the eip_address is not passed. An EIP is generated for this NAT Gateway.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "client_token": "{'description': ['Optional unique token to be used during create to ensure idempotency. When specifying this option, ensure you specify the eip_address parameter as well otherwise any subsequent runs will fail.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "eip_address": "{'description': ['The elastic IP address of the EIP you want attached to this NAT Gateway. If this is not passed and the allocation_id is not passed, an EIP is generated for this NAT Gateway.']}",
    "if_exist_do_not_create": "{'description': ['if a NAT Gateway exists already in the subnet_id, then do not create a new one.'], 'required': False, 'default': False}",
    "nat_gateway_id": "{'description': ['The id AWS dynamically allocates to the NAT Gateway on creation. This is required when the absent option is present.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "release_eip": "{'description': ['Deallocate the EIP from the VPC.', 'Option is only valid with the absent state.', 'You should use this with the wait option. Since you can not release an address while a delete operation is happening.'], 'default': 'yes'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Ensure NAT Gateway is present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnet_id": "{'description': ['The id of the subnet to create the NAT Gateway in. This is required with the present option.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Wait for operation to complete before returning.'], 'default': 'no'}",
    "wait_timeout": "{'description': ['How many seconds to wait for an operation to complete before timing out.'], 'default': 300}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create new nat gateway with client token.
  ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    eip_address: 52.1.1.1
    region: ap-southeast-2
    client_token: abcd-12345678
  register: new_nat_gateway

- name: Create new nat gateway using an allocation-id.
  ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    allocation_id: eipalloc-12345678
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway, using an EIP address  and wait for available status.
  ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    eip_address: 52.1.1.1
    wait: yes
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway and allocate new EIP.
  ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    wait: yes
    region: ap-southeast-2
  register: new_nat_gateway

- name: Create new nat gateway and allocate new EIP if a nat gateway does not yet exist in the subnet.
  ec2_vpc_nat_gateway:
    state: present
    subnet_id: subnet-12345678
    wait: yes
    region: ap-southeast-2
    if_exist_do_not_create: true
  register: new_nat_gateway

- name: Delete nat gateway using discovered nat gateways from facts module.
  ec2_vpc_nat_gateway:
    state: absent
    region: ap-southeast-2
    wait: yes
    nat_gateway_id: "{{ item.NatGatewayId }}"
    release_eip: yes
  register: delete_nat_gateway_result
  with_items: "{{ gateways_to_remove.result }}"

- name: Delete nat gateway and wait for deleted status.
  ec2_vpc_nat_gateway:
    state: absent
    nat_gateway_id: nat-12345678
    wait: yes
    wait_timeout: 500
    region: ap-southeast-2

- name: Delete nat gateway and release EIP.
  ec2_vpc_nat_gateway:
    state: absent
    nat_gateway_id: nat-12345678
    release_eip: yes
    wait: yes
    wait_timeout: 300
    region: ap-southeast-2

```

## License

TODO

## Author Information
  - ['Allen Sanabria (@linuxdynasty)', 'Jon Hadfield (@jonhadfield)', 'Karen Cheng (@Etherdaemon)']
  - ['Allen Sanabria (@linuxdynasty)', 'Jon Hadfield (@jonhadfield)', 'Karen Cheng (@Etherdaemon)']
  - ['Allen Sanabria (@linuxdynasty)', 'Jon Hadfield (@jonhadfield)', 'Karen Cheng (@Etherdaemon)']
