# Ansible module: ansible.module_iam


Manage IAM users, groups, roles and keys

## Description

Allows for the management of IAM users, user API keys, groups, roles.

## Requirements

TODO

## Arguments

``` json
{
    "access_key_ids": "{'description': ['A list of the keys that you want impacted by the access_key_state parameter.']}",
    "access_key_state": "{'description': ["When type is user, it creates, removes, deactivates or activates a user's access key(s). Note that actions apply only to keys specified."], 'choices': ['create', 'remove', 'active', 'inactive']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "groups": "{'description': ['A list of groups the user should belong to. When update, will gracefully remove groups not listed.']}",
    "iam_type": "{'description': ['Type of IAM resource'], 'choices': ['user', 'group', 'role']}",
    "key_count": "{'description': ['When access_key_state is create it will ensure this quantity of keys are present. Defaults to 1.'], 'default': '1'}",
    "name": "{'description': ['Name of IAM resource to create or identify'], 'required': True}",
    "new_name": "{'description': ['When state is update, will replace name with new_name on IAM resource']}",
    "new_path": "{'description': ['When state is update, will replace the path with new_path on the IAM resource']}",
    "password": "{'description': ['When type is user and state is present, define the users login password. Also works with update. Note that always returns changed.']}",
    "path": "{'description': ['When creating or updating, specify the desired path of the resource. If state is present, it will replace the current path to match what is passed in when they do not match.'], 'default': '/'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether to create, delete or update the IAM resource. Note, roles cannot be updated.'], 'required': True, 'choices': ['present', 'absent', 'update']}",
    "trust_policy": "{'description': ['The inline (JSON or YAML) trust policy document that grants an entity permission to assume the role. Mutually exclusive with C(trust_policy_filepath).'], 'version_added': '2.2'}",
    "trust_policy_filepath": "{'description': ['The path to the trust policy document that grants an entity permission to assume the role. Mutually exclusive with C(trust_policy).'], 'version_added': '2.2'}",
    "update_password": "{'default': 'always', 'choices': ['always', 'on_create'], 'description': ['C(always) will update passwords if they differ.  C(on_create) will only set the password for newly created users.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Basic user creation example
tasks:
- name: Create two new IAM users with API keys
  iam:
    iam_type: user
    name: "{{ item }}"
    state: present
    password: "{{ temp_pass }}"
    access_key_state: create
  with_items:
    - jcleese
    - mpython

# Advanced example, create two new groups and add the pre-existing user
# jdavila to both groups.
task:
- name: Create Two Groups, Mario and Luigi
  iam:
    iam_type: group
    name: "{{ item }}"
    state: present
  with_items:
     - Mario
     - Luigi
  register: new_groups

- name:
  iam:
    iam_type: user
    name: jdavila
    state: update
    groups: "{{ item.created_group.group_name }}"
  with_items: "{{ new_groups.results }}"

# Example of role with custom trust policy for Lambda service
- name: Create IAM role with custom trust relationship
  iam:
    iam_type: role
    name: AAALambdaTestRole
    state: present
    trust_policy:
      Version: '2012-10-17'
      Statement:
      - Action: sts:AssumeRole
        Effect: Allow
        Principal:
          Service: lambda.amazonaws.com


```

## License

TODO

## Author Information
  - ['Jonathan I. Davila (@defionscode)', 'Paul Seiffert (@seiffert)']
  - ['Jonathan I. Davila (@defionscode)', 'Paul Seiffert (@seiffert)']
