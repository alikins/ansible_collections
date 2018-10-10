# Ansible module: ansible.module_execute_lambda


Execute an AWS Lambda function

## Description

This module executes AWS Lambda functions, allowing synchronous and asynchronous invocation.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "dry_run": "{'description': ['Do not *actually* invoke the function. A C(DryRun) call will check that the caller has permissions to call the function, especially for checking cross-account permissions.'], 'type': 'bool', 'default': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "function_arn": "{'description': ['The name of the function to be invoked']}",
    "name": "{'description': ['The name of the function to be invoked. This can only be used for invocations within the calling account. To invoke a function in another account, use I(function_arn) to specify the full ARN.']}",
    "payload": "{'description': ['A dictionary in any form to be provided as input to the Lambda function.'], 'default': {}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "tail_log": "{'description': ['If C(tail_log=yes), the result of the task will include the last 4 KB of the CloudWatch log for the function execution. Log tailing only works if you use synchronous invocation C(wait=yes). This is usually used for development or testing Lambdas.'], 'type': 'bool', 'default': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "version_qualifier": "{'description': ['Which version/alias of the function to run. This defaults to the C(LATEST) revision, but can be set to any existing version or alias. See https;//docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html for details.'], 'default': 'LATEST'}",
    "wait": "{'description': ['Whether to wait for the function results or not. If I(wait) is C(no), the task will not return any results. To wait for the Lambda function to complete, set C(wait=yes) and the result will be available in the I(output) key.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- execute_lambda:
    name: test-function
    # the payload is automatically serialized and sent to the function
    payload:
      foo: bar
      value: 8
  register: response

# Test that you have sufficient permissions to execute a Lambda function in
# another account
- execute_lambda:
    function_arn: arn:aws:lambda:us-east-1:123456789012:function/some-function
    dry_run: true

- execute_lambda:
    name: test-function
    payload:
      foo: bar
      value: 8
    wait: true
    tail_log: true
  register: response
  # the response will have a `logs` key that will contain a log (up to 4KB) of the function execution in Lambda.

- execute_lambda:
    name: test-function
    version_qualifier: PRODUCTION

```

## License

TODO

## Author Information
  - ['Ryan Scott Brown (@ryansb) <ryansb@redhat.com>']
