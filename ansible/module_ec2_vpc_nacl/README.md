# Ansible module: ansible.module_ec2_vpc_nacl


create and delete Network ACLs

## Description

Read the AWS documentation for Network ACLS U(http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "egress": "{'description': ["A list of rules for outgoing traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of ['tcp', 'udp', 'icmp', '-1', 'all']), the rule action ('allow' or 'deny') the CIDR of the IPv4 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples."], 'default': [], 'required': False}",
    "ingress": "{'description': ["List of rules for incoming traffic. Each rule must be specified as a list. Each rule may contain the rule number (integer 1-32766), protocol (one of ['tcp', 'udp', 'icmp', '-1', 'all']), the rule action ('allow' or 'deny') the CIDR of the IPv4 network range to allow or deny, the ICMP type (-1 means all types), the ICMP code (-1 means all codes), the last port in the range for TCP or UDP protocols, and the first port in the range for TCP or UDP protocols. See examples."], 'default': [], 'required': False}",
    "nacl_id": "{'description': ['NACL id identifying a network ACL.', 'One and only one of the I(name) or I(nacl_id) is required.'], 'required': False, 'version_added': '2.4'}",
    "name": "{'description': ['Tagged name identifying a network ACL.', 'One and only one of the I(name) or I(nacl_id) is required.'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Creates or modifies an existing NACL', 'Deletes a NACL and reassociates subnets to the default NACL'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnets": "{'description': ['The list of subnets that should be associated with the network ACL.', 'Must be specified as a list', 'Each subnet can be specified as subnet ID, or its tagged name.'], 'required': False}",
    "tags": "{'description': ['Dictionary of tags to look for and apply when creating a network ACL.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['VPC id of the requesting VPC.', 'Required when state present.'], 'required': False}",
}
```

## Examples


``` yaml


# Complete example to create and delete a network ACL
# that allows SSH, HTTP and ICMP in, and all traffic out.
- name: "Create and associate production DMZ network ACL with DMZ subnets"
  ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    region: ap-southeast-2
    subnets: ['prod-dmz-1', 'prod-dmz-2']
    tags:
      CostCode: CC1234
      Project: phoenix
      Description: production DMZ
    ingress:
        # rule no, protocol, allow/deny, cidr, icmp_type, icmp_code,
        #                                             port from, port to
        - [100, 'tcp', 'allow', '0.0.0.0/0', null, null, 22, 22]
        - [200, 'tcp', 'allow', '0.0.0.0/0', null, null, 80, 80]
        - [300, 'icmp', 'allow', '0.0.0.0/0', 0, 8]
    egress:
        - [100, 'all', 'allow', '0.0.0.0/0', null, null, null, null]
    state: 'present'

- name: "Remove the ingress and egress rules - defaults to deny all"
  ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    region: ap-southeast-2
    subnets:
      - prod-dmz-1
      - prod-dmz-2
    tags:
      CostCode: CC1234
      Project: phoenix
      Description: production DMZ
    state: present

- name: "Remove the NACL subnet associations and tags"
  ec2_vpc_nacl:
    vpc_id: 'vpc-12345678'
    name: prod-dmz-nacl
    region: ap-southeast-2
    state: present

- name: "Delete nacl and subnet associations"
  ec2_vpc_nacl:
    vpc_id: vpc-12345678
    name: prod-dmz-nacl
    state: absent

- name: "Delete nacl by its id"
  ec2_vpc_nacl:
    nacl_id: acl-33b4ee5b
    state: absent

```

## License

TODO

## Author Information
  - ['Mike Mochan (@mmochan)']
