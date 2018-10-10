# Ansible module: ansible.module_elb_target_facts


Gathers which target groups a target is associated with

## Description

This module will search through every target group in a region to find which ones have registered a given instance ID or IP.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "get_unused_target_groups": "{'description': ['Whether or not to get target groups not used by any load balancers.'], 'type': 'bool', 'default': True}",
    "instance_id": "{'description': ['What instance ID to get facts for.'], 'type': 'str', 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# practical use case - dynamically deregistering and reregistering nodes

  - name: Get EC2 Metadata
    action: ec2_metadata_facts

  - name: Get initial list of target groups
    delegate_to: localhost
    elb_target_facts:
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_facts

  - name: save fact for later
    set_fact:
      original_tgs: "{{ target_facts.instance_target_groups }}"

  - name: Deregister instance from all target groups
    delegate_to: localhost
    elb_target:
        target_group_arn: "{{ item.0.target_group_arn }}"
        target_port: "{{ item.1.target_port }}"
        target_az: "{{ item.1.target_az }}"
        target_id: "{{ item.1.target_id }}"
        state: absent
        target_status: "draining"
        region: "{{ ansible_ec2_placement_region }}"
    with_subelements:
      - "{{ original_tgs }}"
      - "targets"

    # This avoids having to wait for 'elb_target' to serially deregister each
    # target group.  An alternative would be to run all of the 'elb_target'
    # tasks async and wait for them to finish.

  - name: wait for all targets to deregister simultaneously
    delegate_to: localhost
    elb_target_facts:
      get_unused_target_groups: false
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_facts
    until: (target_facts.instance_target_groups | length) == 0
    retries: 60
    delay: 10

  - name: reregister in elbv2s
    elb_target:
      region: "{{ ansible_ec2_placement_region }}"
      target_group_arn: "{{ item.0.target_group_arn }}"
      target_port: "{{ item.1.target_port }}"
      target_az: "{{ item.1.target_az }}"
      target_id: "{{ item.1.target_id }}"
      state: present
      target_status: "initial"
    with_subelements:
      - "{{ original_tgs }}"
      - "targets"

  # wait until all groups associated with this instance are 'healthy' or
  # 'unused'
  - name: wait for registration
    elb_target_facts:
      get_unused_target_groups: false
      instance_id: "{{ ansible_ec2_instance_id }}"
      region: "{{ ansible_ec2_placement_region }}"
    register: target_facts
    until: (target_facts.instance_target_groups |
            map(attribute='targets') |
            flatten |
            map(attribute='target_health') |
            rejectattr('state', 'equalto', 'healthy') |
            rejectattr('state', 'equalto', 'unused') |
            list |
            length) == 0
    retries: 61
    delay: 10

# using the target groups to generate AWS CLI commands to reregister the
# instance - useful in case the playbook fails mid-run and manual
#            rollback is required
  - name: "reregistration commands: ELBv2s"
    debug:
      msg: >
             aws --region {{ansible_ec2_placement_region}} elbv2
             register-targets --target-group-arn {{item.target_group_arn}}
             --targets{%for target in item.targets%}
             Id={{target.target_id}},
             Port={{target.target_port}}{%if target.target_az%},AvailabilityZone={{target.target_az}}
             {%endif%}
             {%endfor%}
    with_items: "{{target_facts.instance_target_groups}}"


```

## License

TODO

## Author Information
  - ['Yaakov Kuperman (@yaakov-github)']
