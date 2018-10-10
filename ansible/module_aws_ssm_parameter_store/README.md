# Ansible module: ansible.module_aws_ssm_parameter_store


Manage key-value pairs in aws parameter store

## Description

Manage key-value pairs in aws parameter store.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "decryption": "{'description': ['Work with SecureString type to get plain text secrets', 'Boolean'], 'required': False, 'default': True}",
    "description": "{'description': ['parameter key desciption.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "key_id": "{'description': ['aws KMS key to decrypt the secrets.'], 'required': False, 'default': 'aws/ssm (this key is automatically generated at the first parameter created).'}",
    "name": "{'description': ['parameter key name.'], 'required': True}",
    "overwrite_value": "{'description': ['Option to overwrite an existing value if it already exists.', 'String'], 'required': False, 'version_added': '2.6', 'choices': ['never', 'changed', 'always'], 'default': 'changed'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['region.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Creates or modifies an existing parameter', 'Deletes a parameter'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "string_type": "{'description': ['Parameter String type'], 'required': False, 'choices': ['String', 'StringList', 'SecureString'], 'default': 'String'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "value": "{'description': ['Parameter value.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create or update key/value pair in aws parameter store
  aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    value: "World"

- name: Delete the key
  aws_ssm_parameter_store:
    name: "Hello"
    state: absent

- name: Create or update secure key/value pair with default kms key (aws/ssm)
  aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    value: "World"

- name: Create or update secure key/value pair with nominated kms key
  aws_ssm_parameter_store:
    name: "Hello"
    description: "This is your first key"
    string_type: "SecureString"
    key_id: "alias/demo"
    value: "World"

- name: Always update a parameter store value and create a new version
  aws_ssm_parameter_store:
    name: "overwrite_example"
    description: "This example will always overwrite the value"
    string_type: "String"
    value: "Test1234"
    overwrite_value: "always"

- name: recommend to use with aws_ssm lookup plugin
  debug: msg="{{ lookup('aws_ssm', 'hello') }}"

```

## License

TODO

## Author Information
  - ['Nathan Webster (@nathanwebsterdotme)', 'Bill Wang (ozbillwang@gmail.com)', 'Michael De La Rue (@mikedlr)']
  - ['Nathan Webster (@nathanwebsterdotme)', 'Bill Wang (ozbillwang@gmail.com)', 'Michael De La Rue (@mikedlr)']
  - ['Nathan Webster (@nathanwebsterdotme)', 'Bill Wang (ozbillwang@gmail.com)', 'Michael De La Rue (@mikedlr)']
