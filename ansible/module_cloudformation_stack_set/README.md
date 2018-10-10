# Ansible module: ansible.module_cloudformation_stack_set


Manage groups of CloudFormation stacks

## Description

Launches/updates/deletes AWS CloudFormation Stack Sets

## Requirements

TODO

## Arguments

``` json
{
    "accounts": "{'description': ['A list of AWS accounts in which to create instance of CloudFormation stacks.', 'At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated.']}",
    "administration_role_arn": "{'description': ['ARN of the administration role, meaning the role that CloudFormation Stack Sets use to assume the roles in your child accounts.', 'This defaults to I(arn:aws:iam::{{ account ID }}:role/AWSCloudFormationStackSetAdministrationRole) where I({{ account ID }}) is replaced with the account number of the current IAM role/user/STS credentials.'], 'aliases': ['admin_role_arn', 'admin_role', 'administration_role']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "capabilities": "{'description': ['Capabilities allow stacks to create and modify IAM resources, which may include adding users or roles.', "Currently the only available values are 'CAPABILITY_IAM' and 'CAPABILITY_NAMED_IAM'. Either or both may be provided.", 'The following resources require that one or both of these parameters is specified: AWS::IAM::AccessKey, AWS::IAM::Group, AWS::IAM::InstanceProfile, AWS::IAM::Policy, AWS::IAM::Role, AWS::IAM::User, AWS::IAM::UserToGroupAddition\n'], 'choices': ['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']}",
    "description": "{'description': ['A description of what this stack set creates']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "execution_role_name": "{'description': ['ARN of the execution role, meaning the role that CloudFormation Stack Sets assumes in your child accounts.', 'This MUST NOT be an ARN, and the roles must exist in each child account specified.', 'The default name for the execution role is I(AWSCloudFormationStackSetExecutionRole)'], 'aliases': ['exec_role_name', 'exec_role', 'execution_role']}",
    "failure_tolerance": "{'description': ['Settings to change what is considered "failed" when running stack instance updates, and how many to do at a time.']}",
    "name": "{'description': ['name of the cloudformation stack set'], 'required': True}",
    "parameters": "{'description': ['A list of hashes of all the template variables for the stack. The value can be a string or a dict.', 'Dict can be used to set additional template parameter attributes like UsePreviousValue (see example).'], 'default': {}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_stacks": "{'description': ['Only applicable when I(state=absent). Sets whether, when deleting a stack set, the stack instances should also be deleted.', "By default, instances will be deleted. Set to 'no' or 'false' to keep stacks when stack set is deleted."], 'type': 'bool', 'default': True}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "regions": "{'description': ['A list of AWS regions to create instances of a stack in. The I(region) parameter chooses where the Stack Set is created, and I(regions) specifies the region for stack instances.', 'At least one region must be specified to create a stack set. On updates, if fewer regions are specified only the specified regions will have their stack instances updated.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['If state is "present", stack will be created.  If state is "present" and if stack exists and template has changed, it will be updated. If state is "absent", stack will be removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['Dictionary of tags to associate with stack and its resources during stack creation. Can be updated later, updating tags removes previous entries.']}",
    "template": "{'description': ['The local path of the cloudformation template.', 'This must be the full path to the file, relative to the working directory. If using roles this may look like "roles/cloudformation/files/cloudformation-example.json".', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' is present, the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."]}",
    "template_body": "{'description': ['Template body. Use this to pass in the actual body of the Cloudformation template.', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' is present, the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."]}",
    "template_url": "{'description': ['Location of file containing the template body. The URL must point to a template (max size 307,200 bytes) located in an S3 bucket in the same region as the stack.', "If 'state' is 'present' and the stack does not exist yet, either 'template', 'template_body' or 'template_url' must be specified (but only one of them). If 'state' is present, the stack does exist, and neither 'template', 'template_body' nor 'template_url' are specified, the previous template will be reused."]}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Whether or not to wait for stack operation to complete. This includes waiting for stack instances to reach UPDATE_COMPLETE status.', 'If you choose not to wait, this module will not notify when stack operations fail because it will not wait for them to finish.'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['How long to wait (in seconds) for stacks to complete create/update/delete operations.'], 'default': 900}",
}
```

## Examples


``` yaml

- name: Create a stack set with instances in two accounts
  cloudformation_stack_set:
    name: my-stack
    description: Test stack in two accounts
    state: present
    template_url: https://s3.amazonaws.com/my-bucket/cloudformation.template
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1

- name: on subsequent calls, templates are optional but parameters and tags can be altered
  cloudformation_stack_set:
    name: my-stack
    state: present
    parameters:
      InstanceName: my_stacked_instance
    tags:
      foo: bar
      test: stack
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1

- name: The same type of update, but wait for the update to complete in all stacks
  cloudformation_stack_set:
    name: my-stack
    state: present
    wait: true
    parameters:
      InstanceName: my_restacked_instance
    tags:
      foo: bar
      test: stack
    accounts: [1234567890, 2345678901]
    regions:
    - us-east-1

```

## License

TODO

## Author Information
  - ['Ryan Scott Brown (@ryansb)']
