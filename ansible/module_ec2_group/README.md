# Ansible module: ansible.module_ec2_group


maintain an ec2 VPC security group

## Description

maintains ec2 security groups. This module has a dependency on python-boto >= 2.5

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['Description of the security group. Required when C(state) is C(present).'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "group_id": "{'description': ['Id of group to delete (works only with absent).', 'One of and only one of I(name) or I(group_id) is required.'], 'required': False, 'version_added': '2.4'}",
    "name": "{'description': ['Name of the security group.', 'One of and only one of I(name) or I(group_id) is required.', 'Required if I(state=present).'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_rules": "{'version_added': '1.8', 'description': ['Purge existing rules on security group that are not found in rules'], 'required': False, 'default': 'true', 'aliases': []}",
    "purge_rules_egress": "{'version_added': '1.8', 'description': ['Purge existing rules_egress on security group that are not found in rules_egress'], 'required': False, 'default': 'true', 'aliases': []}",
    "purge_tags": "{'version_added': '2.4', 'description': ['If yes, existing tags will be purged from the resource to match exactly what is defined by I(tags) parameter. If the I(tags) parameter is not set then tags will not be modified.'], 'required': False, 'default': True, 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "rules": "{'description': ['List of firewall inbound rules to enforce in this group (see example). If none are supplied, no inbound rules will be enabled. Rules list may include its own name in `group_name`. This allows idempotent loopback additions (e.g. allow group to access itself). Rule sources list support was added in version 2.4. This allows to define multiple sources per source type as well as multiple source types per rule. Prior to 2.4 an individual source is allowed. In version 2.5 support for rule descriptions was added.'], 'required': False}",
    "rules_egress": "{'description': ['List of firewall outbound rules to enforce in this group (see example). If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no outbound rules will be enabled. Rule Egress sources list support was added in version 2.4. In version 2.5 support for rule descriptions was added.'], 'required': False, 'version_added': '1.6'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'version_added': '1.4', 'description': ['Create or delete a security group'], 'required': False, 'default': 'present', 'choices': ['present', 'absent'], 'aliases': []}",
    "tags": "{'version_added': '2.4', 'description': ['A dictionary of one or more tags to assign to the security group.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['ID of the VPC to create the group in.'], 'required': False}",
}
```

## Examples


``` yaml

- name: example using security group rule descriptions
  ec2_group:
    name: "{{ name }}"
    description: sg with rule descriptions
    vpc_id: vpc-xxxxxxxx
    profile: "{{ aws_profile }}"
    region: us-east-1
    rules:
      - proto: tcp
        ports:
        - 80
        cidr_ip: 0.0.0.0/0
        rule_desc: allow all on port 80

- name: example ec2 group
  ec2_group:
    name: example
    description: an example EC2 group
    vpc_id: 12345
    region: eu-west-1
    aws_secret_key: SECRET
    aws_access_key: ACCESS
    rules:
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 22
        to_port: 22
        cidr_ip: 10.0.0.0/8
      - proto: tcp
        from_port: 443
        to_port: 443
        # this should only be needed for EC2 Classic security group rules
        # because in a VPC an ELB will use a user-account security group
        group_id: amazon-elb/sg-87654321/amazon-elb-sg
      - proto: tcp
        from_port: 3306
        to_port: 3306
        group_id: 123412341234/sg-87654321/exact-name-of-sg
      - proto: udp
        from_port: 10050
        to_port: 10050
        cidr_ip: 10.0.0.0/8
      - proto: udp
        from_port: 10051
        to_port: 10051
        group_id: sg-12345678
      - proto: icmp
        from_port: 8 # icmp type, -1 = any type
        to_port:  -1 # icmp subtype, -1 = any subtype
        cidr_ip: 10.0.0.0/8
      - proto: all
        # the containing group name may be specified here
        group_name: example
      - proto: all
        # in the 'proto' attribute, if you specify -1, all, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6),
        # traffic on all ports is allowed, regardless of any ports you specify
        from_port: 10050 # this value is ignored
        to_port: 10050 # this value is ignored
        cidr_ip: 10.0.0.0/8

    rules_egress:
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
        cidr_ipv6: 64:ff9b::/96
        group_name: example-other
        # description to use if example-other needs to be created
        group_desc: other example EC2 group

- name: example2 ec2 group
  ec2_group:
    name: example2
    description: an example2 EC2 group
    vpc_id: 12345
    region: eu-west-1
    rules:
      # 'ports' rule keyword was introduced in version 2.4. It accepts a single port value or a list of values including ranges (from_port-to_port).
      - proto: tcp
        ports: 22
        group_name: example-vpn
      - proto: tcp
        ports:
          - 80
          - 443
          - 8080-8099
        cidr_ip: 0.0.0.0/0
      # Rule sources list support was added in version 2.4. This allows to define multiple sources per source type as well as multiple source types per rule.
      - proto: tcp
        ports:
          - 6379
          - 26379
        group_name:
          - example-vpn
          - example-redis
      - proto: tcp
        ports: 5665
        group_name: example-vpn
        cidr_ip:
          - 172.16.1.0/24
          - 172.16.17.0/24
        cidr_ipv6:
          - 2607:F8B0::/32
          - 64:ff9b::/96
        group_id:
          - sg-edcd9784
  diff: True

- name: "Delete group by its id"
  ec2_group:
    group_id: sg-33b4ee5b
    state: absent

```

## License

TODO

## Author Information
  - ['Andrew de Quincey (@adq)']
