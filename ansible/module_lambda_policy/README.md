# Ansible module: ansible.module_lambda_policy


Creates, updates or deletes AWS Lambda policy statements

## Description

This module allows the management of AWS Lambda policy statements. It is idempotent and supports "Check" mode.  Use module M(lambda) to manage the lambda function itself, M(lambda_alias) to manage function aliases, M(lambda_event) to manage event source mappings such as Kinesis streams, M(execute_lambda) to execute a lambda function and M(lambda_facts) to gather facts relating to one or more lambda functions.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with lambda: followed by the API name (see Operations ). For example, lambda:CreateFunction . You can use wildcard (lambda:* ) to grant permission for all AWS Lambda actions.'], 'required': True}",
    "alias": "{'description': ['Name of the function alias. Mutually exclusive with C(version).']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "event_source_token": "{'description': ['Token string representing source ARN or account. Mutually exclusive with C(source_arn) or C(source_account).']}",
    "function_name": "{'description': ['Name of the Lambda function whose resource policy you are updating by adding a new permission.', 'You can specify a function name (for example, Thumbnail ) or you can specify Amazon Resource Name (ARN) of the', 'function (for example, arn:aws:lambda:us-west-2:account-id:function:ThumbNail ). AWS Lambda also allows you to', 'specify partial ARN (for example, account-id:Thumbnail ). Note that the length constraint applies only to the', 'ARN. If you specify only the function name, it is limited to 64 character in length.'], 'required': True, 'aliases': ['lambda_function_arn', 'function_arn']}",
    "principal": "{'description': ['The principal who is getting this permission. It can be Amazon S3 service Principal (s3.amazonaws.com ) if you want Amazon S3 to invoke the function, an AWS account ID if you are granting cross-account permission, or any valid AWS service principal such as sns.amazonaws.com . For example, you might want to allow a custom application in another AWS account to push events to AWS Lambda by invoking your function.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_account": "{'description': ["The AWS account ID (without a hyphen) of the source owner. For example, if the SourceArn identifies a bucket, then this is the bucket owner's account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don't specify the SourceArn ) owned by a specific account."]}",
    "source_arn": "{'description': ['This is optional; however, when granting Amazon S3 permission to invoke your function, you should specify this field with the bucket Amazon Resource Name (ARN) as its value. This ensures that only events generated from the specified bucket can invoke the function.']}",
    "state": "{'description': ['Describes the desired state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "statement_id": "{'description': ['A unique statement identifier.'], 'required': True, 'aliases': ['sid']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "version": "{'description': ['Version of the Lambda function. Mutually exclusive with C(alias).']}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  - name: Lambda S3 event notification
    lambda_policy:
      state: "{{ state | default('present') }}"
      function_name: functionName
      alias: Dev
      statement_id: lambda-s3-myBucket-create-data-log
      action: lambda:InvokeFunction
      principal: s3.amazonaws.com
      source_arn: arn:aws:s3:eu-central-1:123456789012:bucketName
      source_account: 123456789012

  - name: show results
    debug: var=lambda_policy_action


```

## License

TODO

## Author Information
  - ['Pierre Jodouin (@pjodouin)', 'Michael De La Rue (@mikedlr)']
  - ['Pierre Jodouin (@pjodouin)', 'Michael De La Rue (@mikedlr)']
