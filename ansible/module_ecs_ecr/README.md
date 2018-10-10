# Ansible module: ansible.module_ecs_ecr


Manage Elastic Container Registry repositories

## Description

Manage Elastic Container Registry repositories

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "delete_policy": "{'description': ['if yes, remove the policy from the repository'], 'required': False, 'default': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "force_set_policy": "{'description': ['if no, prevents setting a policy that would prevent you from setting another policy in the future.'], 'required': False, 'default': False}",
    "name": "{'description': ['the name of the repository'], 'required': True}",
    "policy": "{'description': ['JSON or dict that represents the new policy'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "registry_id": "{'description': ['AWS account id associated with the registry.', 'If not specified, the default registry is assumed.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['create or destroy the repository'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# If the repository does not exist, it is created. If it does exist, would not
# affect any policies already on it.
- name: ecr-repo
  ecs_ecr: name=super/cool

- name: destroy-ecr-repo
  ecs_ecr: name=old/busted state=absent

- name: Cross account ecr-repo
  ecs_ecr: registry_id=999999999999 name=cross/account

- name: set-policy as object
  ecs_ecr:
    name: needs-policy-object
    policy:
      Version: '2008-10-17'
      Statement:
        - Sid: read-only
          Effect: Allow
          Principal:
            AWS: '{{ read_only_arn }}'
          Action:
            - ecr:GetDownloadUrlForLayer
            - ecr:BatchGetImage
            - ecr:BatchCheckLayerAvailability

- name: set-policy as string
  ecs_ecr:
    name: needs-policy-string
    policy: "{{ lookup('template', 'policy.json.j2') }}"

- name: delete-policy
  ecs_ecr:
    name: needs-no-policy
    delete_policy: yes

```

## License

TODO

## Author Information
  - ['David M. Lee (@leedm777)']
