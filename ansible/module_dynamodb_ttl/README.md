# Ansible module: ansible.module_dynamodb_ttl


set TTL for a given DynamoDB table

## Description

Uses boto3 to set TTL.
requires botocore version 1.5.24 or higher.

## Requirements

TODO

## Arguments

``` json
{
    "attribute_name": "{'description': ['the name of the Time to Live attribute used to store the expiration time for items in the table', 'this appears to be required by the API even when disabling TTL.'], 'required': True}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['state to set DynamoDB table to'], 'choices': ['enable', 'disable'], 'required': False, 'default': 'enable'}",
    "table_name": "{'description': ['name of the DynamoDB table to work on'], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: enable TTL on my cowfacts table
  dynamodb_ttl:
    state: enable
    table_name: cowfacts
    attribute_name: cow_deleted_date

- name: disable TTL on my cowfacts table
  dynamodb_ttl:
    state: disable
    table_name: cowfacts
    attribute_name: cow_deleted_date

```

## License

TODO

## Author Information
  - ['Ted Timmons (@tedder)']
