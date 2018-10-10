# Ansible module: ansible.module_iam_policy


Manage IAM policies for users, groups, and roles

## Description

Allows uploading or removing IAM policies for IAM users, groups or roles.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "iam_name": "{'description': ['Name of IAM resource you wish to target for policy actions. In other words, the user name, group name or role name.'], 'required': True}",
    "iam_type": "{'description': ['Type of IAM resource'], 'required': True, 'choices': ['user', 'group', 'role']}",
    "policy_document": "{'description': ['The path to the properly json formatted policy file (mutually exclusive with C(policy_json))']}",
    "policy_json": "{'description': ['A properly json formatted policy as string (mutually exclusive with C(policy_document), see https://github.com/ansible/ansible/issues/7005#issuecomment-42894813 on how to use it properly)']}",
    "policy_name": "{'description': ['The name label for the policy to create or remove.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "skip_duplicates": "{'description': ['By default the module looks for any policies that match the document you pass in, if there is a match it will not make a new policy object with the same rules. You can override this by specifying false which would allow for two policy objects with different names but same rules.'], 'default': '/'}",
    "state": "{'description': ['Whether to create or delete the IAM policy.'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create a policy with the name of 'Admin' to the group 'administrators'
- name: Assign a policy called Admin to the administrators group
  iam_policy:
    iam_type: group
    iam_name: administrators
    policy_name: Admin
    state: present
    policy_document: admin_policy.json

# Advanced example, create two new groups and add a READ-ONLY policy to both
# groups.
- name: Create Two Groups, Mario and Luigi
  iam:
    iam_type: group
    name: "{{ item }}"
    state: present
  with_items:
     - Mario
     - Luigi
  register: new_groups

- name: Apply READ-ONLY policy to new groups that have been recently created
  iam_policy:
    iam_type: group
    iam_name: "{{ item.created_group.group_name }}"
    policy_name: "READ-ONLY"
    policy_document: readonlypolicy.json
    state: present
  with_items: "{{ new_groups.results }}"

# Create a new S3 policy with prefix per user
- name: Create S3 policy from template
  iam_policy:
    iam_type: user
    iam_name: "{{ item.user }}"
    policy_name: "s3_limited_access_{{ item.prefix }}"
    state: present
    policy_json: " {{ lookup( 'template', 's3_policy.json.j2') }} "
    with_items:
      - user: s3_user
        prefix: s3_user_prefix


```

## License

TODO

## Author Information
  - ['Jonathan I. Davila (@defionscode)']
