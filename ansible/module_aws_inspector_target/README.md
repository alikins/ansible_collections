# Ansible module: ansible.module_aws_inspector_target


Create, Update and Delete Amazon Inspector Assessment Targets

## Description

C
r
e
a
t
e
s
,
 
u
p
d
a
t
e
s
,
 
o
r
 
d
e
l
e
t
e
s
 
A
m
a
z
o
n
 
I
n
s
p
e
c
t
o
r
 
A
s
s
e
s
s
m
e
n
t
 
T
a
r
g
e
t
s
 
a
n
d
 
m
a
n
a
g
e
s
 
t
h
e
 
r
e
q
u
i
r
e
d
 
R
e
s
o
u
r
c
e
 
G
r
o
u
p
s
.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The user-defined name that identifies the assessment target.  The name must be unique within the AWS account.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The state of the assessment target.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "tags": "{'description': ['Tags of the EC2 instances to be added to the assessment target.', 'Required if C(state=present).']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Create my_target Assessment Target
  aws_inspector_target:
    name: my_target
    tags:
      role: scan_target

- name: Update Existing my_target Assessment Target with Additional Tags
  aws_inspector_target:
    name: my_target
    tags:
      env: dev
      role: scan_target

- name: Delete my_target Assessment Target
  aws_inspector_target:
    name: my_target
    state: absent

```

## License

TODO

## Author Information
  - ['Dennis Conrad (@dennisconrad)']
