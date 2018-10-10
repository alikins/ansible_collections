# Ansible module: ansible.module_aws_elasticbeanstalk_app


create, update, and delete an elastic beanstalk application

## Description

creates, updates, deletes beanstalk applications if app_name is provided

## Requirements

TODO

## Arguments

``` json
{
    "app_name": "{'description': ['name of the beanstalk application you wish to manage'], 'aliases': ['name']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['the description of the application']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['whether to ensure the application is present or absent'], 'default': 'present', 'choices': ['absent', 'present']}",
    "terminate_by_force": "{'description': ['when set to true, running environments will be terminated before deleting the application'], 'default': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create or update an application
- aws_elasticbeanstalk_app:
    app_name: Sample_App
    description: "Hello World App"
    state: present

# Delete application
- aws_elasticbeanstalk_app:
    app_name: Sample_App
    state: absent


```

## License

TODO

## Author Information
  - ['Harpreet Singh (@hsingh)', 'Stephen Granger (@viper233)']
  - ['Harpreet Singh (@hsingh)', 'Stephen Granger (@viper233)']
