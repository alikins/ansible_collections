# Ansible module: ansible.module_aws_waf_web_acl


create and delete WAF Web ACLs

## Description

Read the AWS documentation for WAF U(https://aws.amazon.com/documentation/waf/)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "default_action": "{'description': ["The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the Rule objects that are associated with the WebACL"], 'choices': ['block', 'allow', 'count']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "metric_name": "{'description': ['A friendly name or description for the metrics for this WebACL', "The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.", "You can't change metric_name after you create the WebACL", 'Metric name will default to I(name) with disallowed characters stripped out']}",
    "name": "{'description': ['Name of the Web Application Firewall ACL to manage'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_rules": "{'description': ["Whether to remove rules that aren't passed with C(rules). Defaults to false"]}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "rules": "{'description': ['A list of rules that the Web ACL will enforce.', 'Each rule must contain I(name), I(action), I(priority) keys.', 'Priorities must be unique, but not necessarily consecutive. Lower numbered priorities are evalauted first.', 'The I(type) key can be passed as C(rate_based), it defaults to C(regular)']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['whether the Web ACL should be present or absent'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

  - name: create web ACL
    aws_waf_web_acl:
      name: my_web_acl
      rules:
        - name: my_rule
          priority: 1
          action: block
      default_action: block
      purge_rules: yes
      state: present

  - name: delete the web acl
    aws_waf_web_acl:
      name: my_web_acl
      state: absent

```

## License

TODO

## Author Information
  - ['Mike Mochan (@mmochan)', 'Will Thames (@willthames)']
  - ['Mike Mochan (@mmochan)', 'Will Thames (@willthames)']
