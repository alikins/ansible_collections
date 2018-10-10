# Ansible module: ansible.module_rds_param_group


manage RDS parameter groups

## Description

Creates, modifies, and deletes RDS parameter groups. This module has a dependency on python-boto >= 2.5.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['Database parameter group description. Only set when a new group is added.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "engine": "{'description': ['The type of database for this group. Required for state=present.'], 'choices': ['aurora5.6', 'mariadb10.0', 'mariadb10.1', 'mysql5.1', 'mysql5.5', 'mysql5.6', 'mysql5.7', 'oracle-ee-11.2', 'oracle-ee-12.1', 'oracle-se-11.2', 'oracle-se-12.1', 'oracle-se1-11.2', 'oracle-se1-12.1', 'postgres9.3', 'postgres9.4', 'postgres9.5', 'postgres9.6', 'sqlserver-ee-10.5', 'sqlserver-ee-11.0', 'sqlserver-ex-10.5', 'sqlserver-ex-11.0', 'sqlserver-ex-12.0', 'sqlserver-se-10.5', 'sqlserver-se-11.0', 'sqlserver-se-12.0', 'sqlserver-web-10.5', 'sqlserver-web-11.0', 'sqlserver-web-12.0']}",
    "immediate": "{'description': ['Whether to apply the changes immediately, or after the next reboot of any associated instances.'], 'aliases': ['apply_immediately']}",
    "name": "{'description': ['Database parameter group identifier.'], 'required': True}",
    "params": "{'description': ['Map of parameter names and values. Numeric values may be represented as K for kilo (1024), M for mega (1024^2), G for giga (1024^3), or T for tera (1024^4), and these values will be expanded into the appropriate number before being set in the parameter group.'], 'aliases': ['parameters']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_tags": "{'description': ['Whether or not to remove tags that do not appear in the I(tags) list. Defaults to false.'], 'version_added': '2.4'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Specifies whether the group should be present or absent.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['Dictionary of tags to attach to the parameter group'], 'version_added': '2.4'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Add or change a parameter group, in this case setting auto_increment_increment to 42 * 1024
- rds_param_group:
      state: present
      name: norwegian_blue
      description: 'My Fancy Ex Parrot Group'
      engine: 'mysql5.6'
      params:
          auto_increment_increment: "42K"
      tags:
          Environment: production
          Application: parrot

# Remove a parameter group
- rds_param_group:
      state: absent
      name: norwegian_blue

```

## License

TODO

## Author Information
  - ['Scott Anderson (@tastychutney)', 'Will Thames (@willthames)']
  - ['Scott Anderson (@tastychutney)', 'Will Thames (@willthames)']
