# Ansible module: ansible.module_aws_glue_connection


Manage an AWS Glue connection

## Description

Manage an AWS Glue connection. See U(https://aws.amazon.com/glue/) for details.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "catalog_id": "{'description': ['The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.'], 'required': False}",
    "connection_properties": "{'description': ['A dict of key-value pairs used as parameters for this connection.'], 'required': True}",
    "connection_type": "{'description': ['The type of the connection. Currently, only JDBC is supported; SFTP is not supported.'], 'required': False, 'default': 'JDBC', 'choices': ['JDBC', 'SFTP']}",
    "description": "{'description': ['The description of the connection.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "match_criteria": "{'description': ['A list of UTF-8 strings that specify the criteria that you can use in selecting this connection.'], 'required': False}",
    "name": "{'description': ['The name of the connection.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_groups": "{'description': ['A list of security groups to be used by the connection. Use either security group name or ID.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete the AWS Glue connection.'], 'required': True, 'choices': ['present', 'absent']}",
    "subnet_id": "{'description': ['The subnet ID used by the connection.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue connection
- aws_glue_connection:
    name: my-glue-connection
    connection_properties:
      JDBC_CONNECTION_URL: jdbc:mysql://mydb:3306/databasename
      USERNAME: my-username
      PASSWORD: my-password
    state: present

# Delete an AWS Glue connection
- aws_glue_connection:
    name: my-glue-connection
    state: absent


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
