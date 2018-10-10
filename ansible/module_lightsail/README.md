# Ansible module: ansible.module_lightsail


Create or delete a virtual machine instance in AWS Lightsail

## Description

Creates or instances in AWS Lightsail and optionally wait for it to be 'running'.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "blueprint_id": "{'description': ["ID of the instance blueprint image. Required when state='present'"]}",
    "bundle_id": "{'description': ["Bundle of specification info for the instance. Required when state='present'"]}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "key_pair_name": "{'description': ['Name of the key pair to use with the instance']}",
    "name": "{'description': ['Name of the instance'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'absent', 'running', 'restarted', 'stopped']}",
    "user_data": "{'description': ['Launch script that can configure the instance with additional data']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Wait for the instance to be in state \'running\' before returning.  If wait is "no" an ip_address may not be returned'], 'type': 'bool', 'default': True}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds.'], 'default': 300}",
    "zone": "{'description': ["AWS availability zone in which to launch the instance. Required when state='present'"]}",
}
```

## Examples


``` yaml

# Create a new Lightsail instance, register the instance details
- lightsail:
    state: present
    name: myinstance
    region: us-east-1
    zone: us-east-1a
    blueprint_id: ubuntu_16_04
    bundle_id: nano_1_0
    key_pair_name: id_rsa
    user_data: " echo 'hello world' > /home/ubuntu/test.txt"
    wait_timeout: 500
  register: my_instance

- debug:
    msg: "Name is {{ my_instance.instance.name }}"

- debug:
    msg: "IP is {{ my_instance.instance.public_ip_address }}"

# Delete an instance if present
- lightsail:
    state: absent
    region: us-east-1
    name: myinstance


```

## License

TODO

## Author Information
  - ['Nick Ball (@nickball)']
