# Ansible module: ansible.module_cloudwatchlogs_log_group_facts


get facts about log_group in CloudWatchLogs

## Description

L
i
s
t
s
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
o
g
 
g
r
o
u
p
s
.
 
Y
o
u
 
c
a
n
 
l
i
s
t
 
a
l
l
 
y
o
u
r
 
l
o
g
 
g
r
o
u
p
s
 
o
r
 
f
i
l
t
e
r
 
t
h
e
 
r
e
s
u
l
t
s
 
b
y
 
p
r
e
f
i
x
.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "log_group_name": "{'description': ['The name or prefix of the log group to filter by.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.
- cloudwatchlogs_log_group_facts:
    log_group_name: test-log-group

```

## License

TODO

## Author Information
  - ['Willian Ricardo(@willricardo) <willricardo@gmail.com>']
