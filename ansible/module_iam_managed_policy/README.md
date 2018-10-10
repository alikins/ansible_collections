# Ansible module: ansible.module_iam_managed_policy


Manage User Managed IAM policies

## Description

Allows creating and removing managed IAM policies

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "make_default": "{'description': ['Make this revision the default revision.'], 'default': True}",
    "only_version": "{'description': ['Remove all other non default revisions, if this is used with C(make_default) it will result in all other versions of this policy being deleted.'], 'type': 'bool', 'default': False}",
    "policy": "{'description': ['A properly json formatted policy']}",
    "policy_description": "{'description': ['A helpful description of this policy, this value is immuteable and only set when creating a new policy.'], 'default': ''}",
    "policy_name": "{'description': ['The name of the managed policy.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Should this managed policy be present or absent. Set to absent to detach all entities from this policy and remove it if found.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create Policy ex nihilo
- name: Create IAM Managed Policy
  iam_managed_policy:
    policy_name: "ManagedPolicy"
    policy_description: "A Helpful managed policy"
    policy: "{{ lookup('template', 'managed_policy.json.j2') }}"
    state: present

# Update a policy with a new default version
- name: Create IAM Managed Policy
  iam_managed_policy:
    policy_name: "ManagedPolicy"
    policy: "{{ lookup('file', 'managed_policy_update.json') }}"
    state: present

# Update a policy with a new non default version
- name: Create IAM Managed Policy
  iam_managed_policy:
    policy_name: "ManagedPolicy"
    policy: "{{ lookup('file', 'managed_policy_update.json') }}"
    make_default: false
    state: present

# Update a policy and make it the only version and the default version
- name: Create IAM Managed Policy
  iam_managed_policy:
    policy_name: "ManagedPolicy"
    policy: "{ 'Version': '2012-10-17', 'Statement':[{'Effect': 'Allow','Action': '*','Resource': '*'}]}"
    only_version: true
    state: present

# Remove a policy
- name: Create IAM Managed Policy
  iam_managed_policy:
    policy_name: "ManagedPolicy"
    state: absent

```

## License

TODO

## Author Information
  - ['Dan Kozlowski (@dkhenry)']
