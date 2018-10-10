# Ansible module: ansible.module_s3_sync


Efficiently upload multiple files to S3

## Description

The S3 module is great, but it is very slow for a large volume of files- even a dozen will be noticeable. In addition to speed, it handles globbing, inclusions/exclusions, mime types, expiration mapping, recursion, cache control and smart directory mapping.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bucket": "{'description': ['Bucket name.'], 'required': True}",
    "cache_control": "{'description': ['This is a string.', 'Cache-Control header set on uploaded objects.', 'Directives are separated by commmas.'], 'required': False, 'version_added': '2.4'}",
    "delete": "{'description': ['Remove remote files that exist in bucket but are not present in the file root.'], 'required': False, 'default': False, 'version_added': '2.4'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "exclude": "{'description': ['Shell pattern-style file matching.', 'Used after include to remove files (for instance, skip "*.txt")', 'For multiple patterns, comma-separate them.'], 'required': False, 'default': '.*'}",
    "file_change_strategy": "{'description': ['Difference determination method to allow changes-only syncing. Unlike rsync, files are not patched- they are fully skipped or fully uploaded.', "date_size will upload if file sizes don't match or if local file modified date is newer than s3's version", "checksum will compare etag values based on s3's implementation of chunked md5s.", 'force will always upload all files.'], 'required': False, 'default': 'date_size', 'choices': ['force', 'checksum', 'date_size']}",
    "file_root": "{'description': ['File/directory path for synchronization. This is a local path.', 'This root path is scrubbed from the key name, so subdirectories will remain as keys.'], 'required': True}",
    "include": "{'description': ['Shell pattern-style file matching.', 'Used before exclude to determine eligible files (for instance, only "*.gif")', 'For multiple patterns, comma-separate them.'], 'required': False, 'default': '*'}",
    "key_prefix": "{'description': ['In addition to file path, prepend s3 path with this prefix. Module will add slash at end of prefix if necessary.'], 'required': False}",
    "mime_map": "{'description': ['Dict entry from extension to MIME type. This will override any default/sniffed MIME type. For example C({".txt": "application/text", ".yml": "application/text"})\n'], 'required': False}",
    "mode": "{'description': ['sync direction.'], 'required': True, 'default': 'push', 'choices': ['push']}",
    "permission": "{'description': ['Canned ACL to apply to synced files.', 'Changing this ACL only changes newly synced files, it does not trigger a full reupload.'], 'required': False, 'choices': ['', 'private', 'public-read', 'public-read-write', 'authenticated-read', 'aws-exec-read', 'bucket-owner-read', 'bucket-owner-full-control']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: basic upload
  s3_sync:
    bucket: tedder
    file_root: roles/s3/files/

- name: all the options
  s3_sync:
    bucket: tedder
    file_root: roles/s3/files
    mime_map:
      .yml: application/text
      .json: application/text
    key_prefix: config_files/web
    file_change_strategy: force
    permission: public-read
    cache_control: "public, max-age=31536000"
    include: "*"
    exclude: "*.txt,.*"

```

## License

TODO

## Author Information
  - ['Ted Timmons (@tedder)']
