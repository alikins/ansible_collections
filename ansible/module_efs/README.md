# Ansible module: ansible.module_efs


create and maintain EFS file systems

## Description

Module allows create, search and destroy Amazon EFS file systems

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "encrypt": "{'description': ['A boolean value that, if true, creates an encrypted file system. This can not be modfied after the file system is created.'], 'type': 'bool', 'default': False, 'version_added': 2.5}",
    "id": "{'description': ['ID of Amazon EFS. Either name or ID required for delete.']}",
    "kms_key_id": "{'description': ['The id of the AWS KMS CMK that will be used to protect the encrypted file system. This parameter is only required if you want to use a non-default CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. The key id can be Key ID, Key ID ARN, Key Alias or Key Alias ARN.'], 'version_added': 2.5}",
    "name": "{'description': ['Creation Token of Amazon EFS file system. Required for create and update. Either name or ID required for delete.']}",
    "performance_mode": "{'description': ["File system's performance mode to use. Only takes effect during creation."], 'default': 'general_purpose', 'choices': ['general_purpose', 'max_io']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "provisioned_throughput_in_mibps": "{'description': ['If the throughput_mode is provisioned, select the amount of throughput to provisioned in Mibps.', 'Requires botocore >= 1.10.57'], 'type': 'float', 'version_added': 2.8}",
    "purge_tags": "{'description': ['If yes, existing tags will be purged from the resource to match exactly what is defined by I(tags) parameter. If the I(tags) parameter is not set then tags will not be modified.'], 'type': 'bool', 'default': True, 'version_added': 2.5}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Allows to create, search and destroy Amazon EFS file system'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ["List of tags of Amazon EFS. Should be defined as dictionary In case of 'present' state with list of tags and existing EFS (matched by 'name'), tags of EFS will be replaced with provided data."]}",
    "targets": "{'description': ["List of mounted targets. It should be a list of dictionaries, every dictionary should include next attributes: - subnet_id - Mandatory. The ID of the subnet to add the mount target in. - ip_address - Optional. A valid IPv4 address within the address range of the specified subnet. - security_groups - Optional. List of security group IDs, of the form 'sg-xxxxxxxx'. These must be for the same VPC as subnet specified This data may be modified for existing EFS using state 'present' and new list of mount targets."]}",
    "throughput_mode": "{'description': ['The throughput_mode for the file system to be created.', 'Requires botocore >= 1.10.57'], 'choices': ['bursting', 'provisioned'], 'version_added': 2.8}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ["In case of 'present' state should wait for EFS 'available' life cycle state (of course, if current state not 'deleting' or 'deleted') In case of 'absent' state should wait for EFS 'deleted' life cycle state"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['How long the module should wait (in seconds) for desired state before returning. Zero means wait as long as necessary.'], 'default': 0}",
}
```

## Examples


``` yaml

# EFS provisioning
- efs:
    state: present
    name: myTestEFS
    tags:
        name: myTestNameTag
        purpose: file-storage
    targets:
        - subnet_id: subnet-748c5d03
          security_groups: [ "sg-1a2b3c4d" ]

# Modifying EFS data
- efs:
    state: present
    name: myTestEFS
    tags:
        name: myAnotherTestTag
    targets:
        - subnet_id: subnet-7654fdca
          security_groups: [ "sg-4c5d6f7a" ]

# Deleting EFS
- efs:
    state: absent
    name: myTestEFS

```

## License

TODO

## Author Information
  - ['Ryan Sydnor (@ryansydnor)', 'Artem Kazakov (@akazakov)']
  - ['Ryan Sydnor (@ryansydnor)', 'Artem Kazakov (@akazakov)']
