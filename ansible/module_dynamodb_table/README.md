# Ansible module: ansible.module_dynamodb_table


Create, update or delete AWS Dynamo DB tables

## Description

Create or delete AWS Dynamo DB tables.
Can update the provisioned throughput on existing tables.
Returns the status of the specified table.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "hash_key_name": "{'description': ['Name of the hash key.', 'Required when C(state=present).']}",
    "hash_key_type": "{'description': ['Type of the hash key.'], 'choices': ['STRING', 'NUMBER', 'BINARY'], 'default': 'STRING'}",
    "indexes": "{'description': ["list of dictionaries describing indexes to add to the table. global indexes can be updated. local indexes don't support updates or have throughput.", "required options: ['name', 'type', 'hash_key_name']", "valid types: ['all', 'global_all', 'global_include', 'global_keys_only', 'include', 'keys_only']", "other options: ['hash_key_type', 'range_key_name', 'range_key_type', 'includes', 'read_capacity', 'write_capacity']"], 'default': [], 'version_added': '2.1'}",
    "name": "{'description': ['Name of the table.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "range_key_name": "{'description': ['Name of the range key.']}",
    "range_key_type": "{'description': ['Type of the range key.'], 'choices': ['STRING', 'NUMBER', 'BINARY'], 'default': 'STRING'}",
    "read_capacity": "{'description': ['Read throughput capacity (units) to provision.'], 'default': 1}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete the table'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tags": "{'version_added': '2.4', 'description': ['a hash/dictionary of tags to add to the new instance or for starting/stopping instance by tag; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\'']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait_for_active_timeout": "{'version_added': '2.4', 'description': ['how long before wait gives up, in seconds. only used when tags is set'], 'default': 60}",
    "write_capacity": "{'description': ['Write throughput capacity (units) to provision.'], 'default': 1}",
}
```

## Examples


``` yaml

# Create dynamo table with hash and range primary key
- dynamodb_table:
    name: my-table
    region: us-east-1
    hash_key_name: id
    hash_key_type: STRING
    range_key_name: create_time
    range_key_type: NUMBER
    read_capacity: 2
    write_capacity: 2
    tags:
      tag_name: tag_value

# Update capacity on existing dynamo table
- dynamodb_table:
    name: my-table
    region: us-east-1
    read_capacity: 10
    write_capacity: 10

# set index on existing dynamo table
- dynamodb_table:
    name: my-table
    region: us-east-1
    indexes:
      - name: NamedIndex
        type: global_include
        hash_key_name: id
        range_key_name: create_time
        includes:
          - other_field
          - other_field2
        read_capacity: 10
        write_capacity: 10

# Delete dynamo table
- dynamodb_table:
    name: my-table
    region: us-east-1
    state: absent

```

## License

TODO

## Author Information
  - ['Alan Loi (@loia)']
