# Ansible module: ansible.module_redshift_facts


Gather facts about Redshift cluster(s)

## Description

Gather facts about Redshift cluster(s)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cluster_identifier": "{'description': ['The prefix of cluster identifier of the Redshift cluster you are searching for.', "This is a regular expression match with implicit '^'. Append '$' for a complete match."], 'required': False, 'aliases': ['name', 'identifier']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "tags": "{'description': ["A dictionary/hash of tags in the format { tag1_name: 'tag1_value', tag2_name: 'tag2_value' } to match against the security group(s) you are searching for."], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do net set authentication details, see the AWS guide for details.

# Find all clusters
- redshift_facts:
  register: redshift

# Find cluster(s) with matching tags
- redshift_facts:
    tags:
      env: prd
      stack: monitoring
  register: redshift_tags

# Find cluster(s) with matching name/prefix and tags
- redshift_facts:
    tags:
      env: dev
      stack: web
    name: user-
  register: redshift_web

# Fail if no cluster(s) is/are found
- redshift_facts:
    tags:
      env: stg
      stack: db
  register: redshift_user
  failed_when: "{{ redshift_user.results | length == 0 }}"

```

## License

TODO

## Author Information
  - ['Jens Carl (@j-carl)']
