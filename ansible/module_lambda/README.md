# Ansible module: ansible.module_lambda


Manage AWS Lambda functions

## Description

Allows for the management of Lambda functions.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "dead_letter_arn": "{'description': ['The parent object that contains the target Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.'], 'version_added': '2.3'}",
    "description": "{'description': ['A short, user-defined function description. Lambda does not use this value. Assign a meaningful description as you see fit.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "environment_variables": "{'description': ['A dictionary of environment variables the Lambda function is given.'], 'aliases': ['environment'], 'version_added': '2.3'}",
    "handler": "{'description': ['The function within your code that Lambda calls to begin execution']}",
    "memory_size": "{'description': ['The amount of memory, in MB, your Lambda function is given'], 'default': 128}",
    "name": "{'description': ['The name you want to assign to the function you are uploading. Cannot be changed.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role": "{'description': ['The Amazon Resource Name (ARN) of the IAM role that Lambda assumes when it executes your function to access any other Amazon Web Services (AWS) resources. You may use the bare ARN if the role belongs to the same AWS account.', 'Required when C(state=present)']}",
    "runtime": "{'description': ['The runtime environment for the Lambda function you are uploading. Required when creating a function. Use parameters as described in boto3 docs. Current example runtime environments are nodejs, nodejs4.3, java8 or python2.7', 'Required when C(state=present)']}",
    "s3_bucket": "{'description': ['Amazon S3 bucket name where the .zip file containing your deployment package is stored', 'If C(state=present) then either zip_file or s3_bucket must be present.', 's3_bucket and s3_key are required together']}",
    "s3_key": "{'description': ['The Amazon S3 object (the deployment package) key name you want to upload', 's3_bucket and s3_key are required together']}",
    "s3_object_version": "{'description': ['The Amazon S3 object (the deployment package) version you want to upload.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete Lambda function'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['tag dict to apply to the function (requires botocore 1.5.40 or above)'], 'version_added': '2.5'}",
    "timeout": "{'description': ['The function maximum execution time in seconds after which Lambda should terminate the function.'], 'default': 3}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_security_group_ids": "{'description': ['List of VPC security group IDs to associate with the Lambda function. Required when vpc_subnet_ids is used.']}",
    "vpc_subnet_ids": "{'description': ["List of subnet IDs to run Lambda function in. Use this option if you need to access resources in your VPC. Leave empty if you don't want to run the function in a VPC."]}",
    "zip_file": "{'description': ['A .zip file containing your deployment package', 'If C(state=present) then either zip_file or s3_bucket must be present.'], 'aliases': ['src']}",
}
```

## Examples


``` yaml

# Create Lambda functions
- name: looped creation
  lambda:
    name: '{{ item.name }}'
    state: present
    zip_file: '{{ item.zip_file }}'
    runtime: 'python2.7'
    role: 'arn:aws:iam::987654321012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    vpc_subnet_ids:
    - subnet-123abcde
    - subnet-edcba321
    vpc_security_group_ids:
    - sg-123abcde
    - sg-edcba321
    environment_variables: '{{ item.env_vars }}'
    tags:
      key1: 'value1'
  with_items:
    - name: HelloWorld
      zip_file: hello-code.zip
      env_vars:
        key1: "first"
        key2: "second"
    - name: ByeBye
      zip_file: bye-code.zip
      env_vars:
        key1: "1"
        key2: "2"

# To remove previously added tags pass a empty dict
- name: remove tags
  lambda:
    name: 'Lambda function'
    state: present
    zip_file: 'code.zip'
    runtime: 'python2.7'
    role: 'arn:aws:iam::987654321012:role/lambda_basic_execution'
    handler: 'hello_python.my_handler'
    tags: {}

# Basic Lambda function deletion
- name: Delete Lambda functions HelloWorld and ByeBye
  lambda:
    name: '{{ item }}'
    state: absent
  with_items:
    - HelloWorld
    - ByeBye

```

## License

TODO

## Author Information
  - ['Steyn Huizinga (@steynovich)']
