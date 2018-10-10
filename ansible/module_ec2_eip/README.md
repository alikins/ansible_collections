# Ansible module: ansible.module_ec2_eip


manages EC2 elastic IP (EIP) addresses

## Description

This module can allocate or release an EIP.
This module can associate/disassociate an EIP with instances or network interfaces.

## Requirements

TODO

## Arguments

``` json
{
    "allow_reassociation": "{'description': ['Specify this option to allow an Elastic IP address that is already associated with another network interface or instance to be re-associated with the specified instance or interface.'], 'default': 'no', 'version_added': '2.5'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "device_id": "{'description': ['The id of the device for the EIP. Can be an EC2 Instance id or Elastic Network Interface (ENI) id.'], 'required': False, 'aliases': ['instance_id'], 'version_added': '2.0'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "in_vpc": "{'description': ['Allocate an EIP inside a VPC or not. Required if specifying an ENI.'], 'default': 'no', 'version_added': '1.4'}",
    "private_ip_address": "{'description': ['The primary or secondary private IP address to associate with the Elastic IP address.'], 'version_added': '2.3'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "public_ip": "{'description': ['The IP address of a previously allocated EIP.', 'If present and device is specified, the EIP is associated with the device.', 'If absent and device is specified, the EIP is disassociated from the device.'], 'aliases': ['ip']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "release_on_disassociation": "{'description': ['whether or not to automatically release the EIP when it is disassociated'], 'default': 'no', 'version_added': '2.0'}",
    "reuse_existing_ip_allowed": "{'description': ['Reuse an EIP that is not associated to a device (when available), instead of allocating a new one.'], 'default': 'no', 'version_added': '1.6'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['If present, allocate an EIP or associate an existing EIP with a device.', 'If absent, disassociate the EIP from the device and optionally release it.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: associate an elastic IP with an instance
  ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119

- name: associate an elastic IP with a device
  ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119

- name: associate an elastic IP with a device and allow reassociation
  ec2_eip:
    device_id: eni-c8ad70f3
    public_ip: 93.184.216.119
    allow_reassociation: yes

- name: disassociate an elastic IP from an instance
  ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119
    state: absent

- name: disassociate an elastic IP with a device
  ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119
    state: absent

- name: allocate a new elastic IP and associate it with an instance
  ec2_eip:
    device_id: i-1212f003

- name: allocate a new elastic IP without associating it to anything
  ec2_eip:
    state: present
  register: eip

- name: output the IP
  debug:
    msg: "Allocated IP is {{ eip.public_ip }}"

- name: provision new instances with ec2
  ec2:
    keypair: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    count: 3
  register: ec2

- name: associate new elastic IPs with each of the instances
  ec2_eip:
    device_id: "{{ item }}"
  with_items: "{{ ec2.instance_ids }}"

- name: allocate a new elastic IP inside a VPC in us-west-2
  ec2_eip:
    region: us-west-2
    in_vpc: yes
  register: eip

- name: output the IP
  debug:
    msg: "Allocated IP inside a VPC is {{ eip.public_ip }}"

```

## License

TODO

## Author Information
  - ['Rick Mendes (@rickmendes) <rmendes@illumina.com>']
