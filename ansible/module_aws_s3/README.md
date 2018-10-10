# Ansible module: ansible.module_aws_s3


manage objects in S3

## Description

This module allows the user to manage S3 buckets and the objects within them. Includes support for creating and deleting both objects and buckets, retrieving objects as files or strings and generating download links. This module has a dependency on boto3 and botocore.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key id. If not set then the value of the AWS_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bucket": "{'description': ['Bucket name.'], 'required': True}",
    "dest": "{'description': ['The destination file path when downloading an object/key with a GET operation.'], 'version_added': '1.3'}",
    "dualstack": "{'description': ['Enables Amazon S3 Dual-Stack Endpoints, allowing S3 communications using both IPv4 and IPv6.', 'Requires at least botocore version 1.4.45.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encrypt": "{'description': ['When set for PUT mode, asks for server-side encryption.'], 'default': True, 'version_added': '2.0'}",
    "encryption_kms_key_id": "{'description': ['KMS key id to use when encrypting objects using C(aws:kms) encryption. Ignored if encryption is not C(aws:kms)'], 'version_added': '2.7'}",
    "encryption_mode": "{'description': ['What encryption mode to use if C(encrypt) is set'], 'default': 'AES256', 'choices': ['AES256', 'aws:kms'], 'version_added': '2.7'}",
    "expiration": "{'description': ['Time limit (in seconds) for the URL generated and returned by S3/Walrus when performing a mode=put or mode=geturl operation.'], 'default': 600}",
    "headers": "{'description': ["Custom headers for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'."], 'version_added': '2.0'}",
    "ignore_nonexistent_bucket": "{'description': ['Overrides initial bucket lookups in case bucket or iam policies are restrictive. Example: a user may have the GetObject permission but no other permissions. In this case using the option mode: get will fail without specifying ignore_nonexistent_bucket: True.'], 'version_added': '2.3'}",
    "marker": "{'description': ['Specifies the key to start with when using list mode. Object keys are returned in alphabetical order, starting with key after the marker in order.'], 'version_added': '2.0'}",
    "max_keys": "{'description': ['Max number of results to return in list mode, set this if you want to retrieve fewer than the default 1000 keys.'], 'default': 1000, 'version_added': '2.0'}",
    "metadata": "{'description': ["Metadata for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'."], 'version_added': '1.6'}",
    "mode": "{'description': ['Switches the module behaviour between put (upload), get (download), geturl (return download url, Ansible 1.3+), getstr (download object as string (1.3+)), list (list keys, Ansible 2.0+), create (bucket), delete (bucket), and delobj (delete object, Ansible 2.0+).'], 'required': True, 'choices': ['get', 'put', 'delete', 'create', 'geturl', 'getstr', 'delobj', 'list']}",
    "object": "{'description': ['Keyname of the object inside the bucket. Can be used to create "virtual directories", see examples.']}",
    "overwrite": "{'description': ["Force overwrite either locally on the filesystem or remotely with the object/key. Used with PUT and GET operations. Boolean or one of [always, never, different], true is equal to 'always' and false is equal to 'never', new in 2.0. When this is set to 'different', the md5 sum of the local file is compared with the 'ETag' of the object/key in S3. The ETag may or may not be an MD5 digest of the object data. See the ETag response header here U(https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html)"], 'default': 'always', 'aliases': ['force']}",
    "permission": "{'description': ["This option lets the user set the canned permissions on the object/bucket that are created. The permissions that can be set are 'private', 'public-read', 'public-read-write', 'authenticated-read' for a bucket or 'private', 'public-read', 'public-read-write', 'aws-exec-read', 'authenticated-read', 'bucket-owner-read', 'bucket-owner-full-control' for an object. Multiple permissions can be specified as a list."], 'default': 'private', 'version_added': '2.0'}",
    "prefix": "{'description': ['Limits the response to keys that begin with the specified prefix for list mode'], 'default': '', 'version_added': '2.0'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['AWS region to create the bucket in. If not set then the value of the AWS_REGION and EC2_REGION environment variables are checked, followed by the aws_region and ec2_region settings in the Boto config file. If none of those are set the region defaults to the S3 Location: US Standard. Prior to ansible 1.8 this parameter could be specified but had no effect.'], 'required': False, 'aliases': ['aws_region', 'ec2_region'], 'version_added': '1.8'}",
    "retries": "{'description': ['On recoverable failure, how many times to retry before actually failing.'], 'default': 0, 'version_added': '2.0'}",
    "rgw": "{'description': ['Enable Ceph RGW S3 support. This option requires an explicit url via s3_url.'], 'default': False, 'version_added': '2.2'}",
    "s3_url": "{'description': ['S3 URL endpoint for usage with Ceph, Eucalyptus and fakes3 etc. Otherwise assumes AWS.'], 'aliases': ['S3_URL']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "src": "{'description': ['The source file path when performing a PUT operation.'], 'version_added': '1.3'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "version": "{'description': ['Version ID of the object inside the bucket. Can be used to get a specific version of a file if versioning is enabled in the target bucket.'], 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Simple PUT operation
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put

- name: Simple PUT operation in Ceph RGW S3
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    rgw: true
    s3_url: "http://localhost:8000"

- name: Simple GET operation
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get

- name: Get a specific version of an object.
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    version: 48c9ee5131af7a716edc22df9772aa6f
    dest: /usr/local/myfile.txt
    mode: get

- name: PUT/upload with metadata
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    metadata: 'Content-Encoding=gzip,Cache-Control=no-cache'

- name: PUT/upload with custom headers
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    src: /usr/local/myfile.txt
    mode: put
    headers: 'x-amz-grant-full-control=emailAddress=owner@example.com'

- name: List keys simple
  aws_s3:
    bucket: mybucket
    mode: list

- name: List keys all options
  aws_s3:
    bucket: mybucket
    mode: list
    prefix: /my/desired/
    marker: /my/desired/0023.txt
    max_keys: 472

- name: Create an empty bucket
  aws_s3:
    bucket: mybucket
    mode: create
    permission: public-read

- name: Create a bucket with key as directory, in the EU region
  aws_s3:
    bucket: mybucket
    object: /my/directory/path
    mode: create
    region: eu-west-1

- name: Delete a bucket and all contents
  aws_s3:
    bucket: mybucket
    mode: delete

- name: GET an object but don't download if the file checksums match. New in 2.0
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    dest: /usr/local/myfile.txt
    mode: get
    overwrite: different

- name: Delete an object from a bucket
  aws_s3:
    bucket: mybucket
    object: /my/desired/key.txt
    mode: delobj

```

## License

TODO

## Author Information
  - ['Lester Wade (@lwade)', 'Sloane Hertel (@s-hertel)']
  - ['Lester Wade (@lwade)', 'Sloane Hertel (@s-hertel)']
