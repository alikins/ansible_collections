# Ansible module: ansible.module_s3_bucket


Manage S3 buckets in AWS, Ceph, Walrus and FakeS3

## Description

Manage S3 buckets in AWS, Ceph, Walrus and FakeS3

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ceph": "{'description': ['Enable API compatibility with Ceph. It takes into account the S3 API subset working with Ceph in order to provide the same module behaviour where possible.'], 'version_added': '2.2'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "force": "{'description': ['When trying to delete a bucket, delete all keys (including versions and delete markers) in the bucket first (an s3 bucket must be empty for a successful deletion)'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the s3 bucket'], 'required': True}",
    "policy": "{'description': ['The JSON policy as a string.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "requester_pays": "{'description': ['With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket.'], 'type': 'bool', 'default': False}",
    "s3_url": "{'description': ['S3 URL endpoint for usage with Ceph, Eucalyptus and fakes3 etc. Otherwise assumes AWS.'], 'aliases': ['S3_URL']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or remove the s3 bucket'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['tags dict to apply to bucket']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "versioning": "{'description': ['Whether versioning is enabled or disabled (note that once versioning is enabled, it can only be suspended)'], 'type': 'bool'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create a simple s3 bucket
- s3_bucket:
    name: mys3bucket

# Create a simple s3 bucket on Ceph Rados Gateway
- s3_bucket:
    name: mys3bucket
    s3_url: http://your-ceph-rados-gateway-server.xxx
    ceph: true

# Remove an s3 bucket and any keys it contains
- s3_bucket:
    name: mys3bucket
    state: absent
    force: yes

# Create a bucket, add a policy from a file, enable requester pays, enable versioning and tag
- s3_bucket:
    name: mys3bucket
    policy: "{{ lookup('file','policy.json') }}"
    requester_pays: yes
    versioning: yes
    tags:
      example: tag1
      another: tag2


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
