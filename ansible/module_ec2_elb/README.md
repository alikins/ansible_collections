# Ansible module: ansible.module_ec2_elb


De-registers or registers instances from EC2 ELBs

## Description

This module de-registers or registers an AWS EC2 instance from the ELBs that it belongs to.
Returns fact "ec2_elbs" which is a list of elbs attached to the instance if state=absent is passed as an argument.
Will be marked changed when called only if there are ELBs found to operate on.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_elbs": "{'description': ['List of ELB names, required for registration. The ec2_elbs fact should be used if there was a previous de-register.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "enable_availability_zone": "{'description': ['Whether to enable the availability zone of the instance on the target ELB if the availability zone has not already been enabled. If set to no, the task will fail if the availability zone is not enabled on the ELB.'], 'type': 'bool', 'default': True}",
    "instance_id": "{'description': ['EC2 Instance ID'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['register or deregister the instance'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Wait for instance registration or deregistration to complete successfully before returning.'], 'type': 'bool', 'default': True}",
    "wait_timeout": "{'description': ['Number of seconds to wait for an instance to change state. If 0 then this module may return an error if a transient error occurs. If non-zero then any transient errors are ignored until the timeout is reached. Ignored when wait=no.'], 'default': 0, 'version_added': '1.6'}",
}
```

## Examples


``` yaml

# basic pre_task and post_task example
pre_tasks:
  - name: Gathering ec2 facts
    action: ec2_facts
  - name: Instance De-register
    local_action:
      module: ec2_elb
      instance_id: "{{ ansible_ec2_instance_id }}"
      state: absent
roles:
  - myrole
post_tasks:
  - name: Instance Register
    local_action:
      module: ec2_elb
      instance_id: "{{ ansible_ec2_instance_id }}"
      ec2_elbs: "{{ item }}"
      state: present
    with_items: "{{ ec2_elbs }}"

```

## License

TODO

## Author Information
  - ['John Jarvis (@jarv)']
