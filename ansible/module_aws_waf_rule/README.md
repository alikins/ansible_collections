# Ansible module: ansible.module_aws_waf_rule


create and delete WAF Rules

## Description

Read the AWS documentation for WAF U(https://aws.amazon.com/documentation/waf/)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "conditions": "{'description': ['list of conditions used in the rule. Each condition should contain I(type): which is one of [C(byte), C(geo), C(ip), C(size), C(sql) or C(xss)] I(negated): whether the condition should be negated, and C(condition), the name of the existing condition. M(aws_waf_condition) can be used to create new conditions\n']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "metric_name": "{'description': ['A friendly name or description for the metrics for the rule', "The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.", "You can't change metric_name after you create the rule", 'Defaults to the same as name with disallowed characters removed']}",
    "name": "{'description': ['Name of the Web Application Firewall rule'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_conditions": "{'description': ['Whether or not to remove conditions that are not passed when updating `conditions`. Defaults to false.']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['whether the rule should be present or absent'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml


  - name: create WAF rule
    aws_waf_rule:
      name: my_waf_rule
      conditions:
        - name: my_regex_condition
          type: regex
          negated: no
        - name: my_geo_condition
          type: geo
          negated: no
        - name: my_byte_condition
          type: byte
          negated: yes

  - name: remove WAF rule
    aws_waf_rule:
      name: "my_waf_rule"
      state: absent


```

## License

TODO

## Author Information
  - ['Mike Mochan (@mmochan)', 'Will Thames (@willthames)']
  - ['Mike Mochan (@mmochan)', 'Will Thames (@willthames)']
