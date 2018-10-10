# Ansible module: ansible.module_cloudformation


Create or delete an AWS CloudFormation stack

## Description

Launches or updates an AWS CloudFormation stack and waits for it complete.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "changeset_name": "{'description': ['Name given to the changeset when creating a changeset, only used when create_changeset is true. By default a name prefixed with Ansible-STACKNAME is generated based on input parameters. See the AWS Change Sets docs U(http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)'], 'version_added': '2.4'}",
    "create_changeset": "{'description': ['If stack already exists create a changeset instead of directly applying changes. See the AWS Change Sets docs U(http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html). WARNING: if the stack does not exist, it will be created without changeset. If the state is absent, the stack will be deleted immediately with no changeset.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "create_timeout": "{'description': ['The amount of time (in minutes) that can pass before the stack status becomes CREATE_FAILED'], 'version_added': '2.6'}",
    "disable_rollback": "{'description': ['If a stacks fails to form, rollback will remove the stack'], 'type': 'bool', 'default': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "events_limit": "{'description': ['Maximum number of CloudFormation events to fetch from a stack when creating or updating it.'], 'default': 200, 'version_added': '2.7'}",
    "notification_arns": "{'description': ['The Simple Notification Service (SNS) topic ARNs to publish stack related events.'], 'version_added': '2.0'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['The role that AWS CloudFormation assumes to create the stack. See the AWS CloudFormation Service Role docs U(http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)'], 'version_added': '2.3'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "stack_name": "{'description': ['name of the cloudformation stack'], 'required': True}",
    "stack_policy": "{'description': ['the path of the cloudformation stack policy. A policy cannot be removed once placed, but it can be modified. (for instance, [allow all updates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html#d0e9051)'], 'version_added': '1.9'}",
    "state": "{'description': ['If state is "present", stack will be created.  If state is "present" and if stack exists and template has changed, it will be updated. If state is "absent", stack will be removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['Dictionary of tags to associate with stack and its resources during stack creation. Can be updated later, updating tags removes previous entries.'], 'version_added': '1.4'}",
    "template": "{'description': ['The local path of the cloudformation template.', 'This must be the full path to the file, relative to the working directory. If using roles this may look like "roles/cloudformation/files/cloudformation-example.json".', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' is 'present', the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."]}",
    "template_body": "{'description': ['Template body. Use this to pass in the actual body of the Cloudformation template.', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' ispresent, the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."], 'version_added': '2.5'}",
    "template_format": "{'description': ['(deprecated) For local templates, allows specification of json or yaml format. Templates are now passed raw to CloudFormation regardless of format. This parameter is ignored since Ansible 2.3.'], 'default': 'json', 'choices': ['json', 'yaml'], 'version_added': '2.0'}",
    "template_parameters": "{'description': ['A list of hashes of all the template variables for the stack. The value can be a string or a dict.', 'Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).'], 'default': {}}",
    "template_url": "{'description': ['Location of file containing the template body. The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' ispresent, the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."], 'version_added': '2.0'}",
    "termination_protection": "{'description': ['enable or disable termination protection on the stack. Only works with botocore >= 1.7.18.'], 'version_added': '2.5'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: create a cloudformation stack
  cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    disable_rollback: true
    template: "files/cloudformation-example.json"
    template_parameters:
      KeyName: "jmartin"
      DiskType: "ephemeral"
      InstanceType: "m1.small"
      ClusterSize: 3
    tags:
      Stack: "ansible-cloudformation"

# Basic role example
- name: create a stack, specify role that cloudformation assumes
  cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    disable_rollback: true
    template: "roles/cloudformation/files/cloudformation-example.json"
    role_arn: 'arn:aws:iam::123456789012:role/cloudformation-iam-role'

- name: delete a stack
  cloudformation:
    stack_name: "ansible-cloudformation-old"
    state: "absent"

# Create a stack, pass in template from a URL, disable rollback if stack creation fails,
# pass in some parameters to the template, provide tags for resources created
- name: create a stack, pass in the template via an URL
  cloudformation:
    stack_name: "ansible-cloudformation"
    state: present
    region: us-east-1
    disable_rollback: true
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    template_parameters:
      KeyName: jmartin
      DiskType: ephemeral
      InstanceType: m1.small
      ClusterSize: 3
    tags:
      Stack: ansible-cloudformation

# Create a stack, passing in template body using lookup of Jinja2 template, disable rollback if stack creation fails,
# pass in some parameters to the template, provide tags for resources created
- name: create a stack, pass in the template body via lookup template
  cloudformation:
    stack_name: "ansible-cloudformation"
    state: present
    region: us-east-1
    disable_rollback: true
    template_body: "{{ lookup('template', 'cloudformation.j2') }}"
    template_parameters:
      KeyName: jmartin
      DiskType: ephemeral
      InstanceType: m1.small
      ClusterSize: 3
    tags:
      Stack: ansible-cloudformation

# Pass a template parameter which uses Cloudformation's UsePreviousValue attribute
# When use_previous_value is set to True, the given value will be ignored and
# Cloudformation will use the value from a previously submitted template.
# If use_previous_value is set to False (default) the given value is used.
- cloudformation:
    stack_name: "ansible-cloudformation"
    state: "present"
    region: "us-east-1"
    template: "files/cloudformation-example.json"
    template_parameters:
      DBSnapshotIdentifier:
        use_previous_value: True
        value: arn:aws:rds:es-east-1:000000000000:snapshot:rds:my-db-snapshot
      DBName:
        use_previous_value: True
    tags:
      Stack: "ansible-cloudformation"

# Enable termination protection on a stack.
# If the stack already exists, this will update its termination protection
- name: enable termination protection during stack creation
  cloudformation:
    stack_name: my_stack
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    termination_protection: yes

# Configure TimeoutInMinutes before the stack status becomes CREATE_FAILED
# In this case, if disable_rollback is not set or is set to false, the stack will be rolled back.
- name: enable termination protection during stack creation
  cloudformation:
    stack_name: my_stack
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    create_timeout: 5


```

## License

TODO

## Author Information
  - ['James S. Martin (@jsmartin)']
