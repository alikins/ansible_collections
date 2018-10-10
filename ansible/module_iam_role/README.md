# Ansible module: ansible.module_iam_role


Manage AWS IAM roles

## Description

Manage AWS IAM roles

## Requirements

TODO

## Arguments

``` json
{
    "assume_role_policy_document": "{'description': ['The trust relationship policy document that grants an entity permission to assume the role.', 'This parameter is required when C(state=present).']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "boundary": "{'description': ['Add the ARN of an IAM managed policy to restrict the permissions this role can pass on to IAM roles/users that it creates.', 'Boundaries cannot be set on Instance Profiles, so if this option is specified then C(create_instance_profile) must be false.', 'This is intended for roles/users that have permissions to create new IAM objects.', 'For more information on boundaries, see U(https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)'], 'aliases': ['boundary_policy_arn'], 'version_added': '2.7'}",
    "create_instance_profile": "{'description': ['Creates an IAM instance profile along with the role'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
    "description": "{'description': ['Provide a description of the new role'], 'version_added': '2.5'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "managed_policy": "{'description': ['A list of managed policy ARNs or, since Ansible 2.4, a list of either managed policy ARNs or friendly names. To embed an inline policy, use M(iam_policy). To remove existing policies, use an empty list item.'], 'aliases': ['managed_policies']}",
    "name": "{'description': ['The name of the role to create.'], 'required': True}",
    "path": "{'description': ['The path to the role. For more information about paths, see U(http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html).'], 'default': '/'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_policies": "{'description': ['Detaches any managed policies not listed in the "managed_policy" option. Set to false if you want to attach policies elsewhere.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or remove the IAM role'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create a role with description
  iam_role:
    name: mynewrole
    assume_role_policy_document: "{{ lookup('file','policy.json') }}"
    description: This is My New Role

- name: "Create a role and attach a managed policy called 'PowerUserAccess'"
  iam_role:
    name: mynewrole
    assume_role_policy_document: "{{ lookup('file','policy.json') }}"
    managed_policy:
      - arn:aws:iam::aws:policy/PowerUserAccess

- name: Keep the role created above but remove all managed policies
  iam_role:
    name: mynewrole
    assume_role_policy_document: "{{ lookup('file','policy.json') }}"
    managed_policy: []

- name: Delete the role
  iam_role:
    name: mynewrole
    assume_role_policy_document: "{{ lookup('file', 'policy.json') }}"
    state: absent


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
