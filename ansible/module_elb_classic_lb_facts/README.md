# Ansible module: ansible.module_elb_classic_lb_facts


Gather facts about EC2 Elastic Load Balancers in AWS

## Description

Gather facts about EC2 Elastic Load Balancers in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "names": "{'description': ['List of ELB names to gather facts about. Pass this option to gather facts about a set of ELBs, otherwise, all ELBs are returned.'], 'aliases': ['elb_ids', 'ec2_elbs']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.
# Output format tries to match ec2_elb_lb module input parameters

# Gather facts about all ELBs
- elb_classic_lb_facts:
  register: elb_facts

- debug:
    msg: "{{ item.dns_name }}"
  with_items: "{{ elb_facts.elbs }}"

# Gather facts about a particular ELB
- elb_classic_lb_facts:
    names: frontend-prod-elb
  register: elb_facts

- debug:
    msg: "{{ elb_facts.elbs.0.dns_name }}"

# Gather facts about a set of ELBs
- elb_classic_lb_facts:
    names:
    - frontend-prod-elb
    - backend-prod-elb
  register: elb_facts

- debug:
    msg: "{{ item.dns_name }}"
  with_items: "{{ elb_facts.elbs }}"


```

## License

TODO

## Author Information
  - ['Michael Schultz (github.com/mjschultz)', 'Fernando Jose Pando (@nand0p)']
  - ['Michael Schultz (github.com/mjschultz)', 'Fernando Jose Pando (@nand0p)']
