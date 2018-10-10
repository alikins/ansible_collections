# Ansible module: ansible.module_ec2_lc


Create or delete AWS Autoscaling Launch Configurations

## Description

Can create or delete AWS Autoscaling Configurations
Works with the ec2_asg module to manage Autoscaling Groups

## Requirements

TODO

## Arguments

``` json
{
    "assign_public_ip": "{'description': ['Used for Auto Scaling groups that launch instances into an Amazon Virtual Private Cloud. Specifies whether to assign a public IP address to each instance launched in a Amazon VPC.'], 'version_added': '1.8'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "classic_link_vpc_id": "{'description': ['Id of ClassicLink enabled VPC'], 'version_added': '2.0'}",
    "classic_link_vpc_security_groups": "{'description': ['A list of security group IDs with which to associate the ClassicLink VPC instances.'], 'version_added': '2.0'}",
    "ebs_optimized": "{'description': ['Specifies whether the instance is optimized for EBS I/O (true) or not (false).'], 'default': False, 'version_added': '1.8'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "image_id": "{'description': ['The AMI unique identifier to be used for the group']}",
    "instance_id": "{'description': ['The Id of a running instance to use as a basis for a launch configuration. Can be used in place of image_id and instance_type.'], 'version_added': '2.4'}",
    "instance_monitoring": "{'description': ['Specifies whether instances are launched with detailed monitoring.'], 'type': 'bool', 'default': False}",
    "instance_profile_name": "{'description': ['The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instances.'], 'version_added': '1.8'}",
    "instance_type": "{'description': ['Instance type to use for the instance'], 'required': True}",
    "kernel_id": "{'description': ['Kernel id for the EC2 instance']}",
    "key_name": "{'description': ['The SSH key name to be used for access to managed instances']}",
    "name": "{'description': ['Unique name for configuration'], 'required': True}",
    "placement_tenancy": "{'description': ['Determines whether the instance runs on single-tenant harware or not.'], 'default': 'default', 'version_added': '2.4'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "ramdisk_id": "{'description': ['A RAM disk id for the instances.'], 'version_added': '1.8'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_groups": "{'description': ['A list of security groups to apply to the instances. Since version 2.4 you can specify either security group names or IDs or a mix.  Previous to 2.4, for VPC instances, specify security group IDs and for EC2-Classic, specify either security group names or IDs.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "spot_price": "{'description': ['The spot price you are bidding. Only applies for an autoscaling group with spot instances.']}",
    "state": "{'description': ['Register or deregister the instance'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user_data": "{'description': ['Opaque blob of data which is made available to the ec2 instance. Mutually exclusive with I(user_data_path).']}",
    "user_data_path": "{'description': ['Path to the file that contains userdata for the ec2 instances. Mutually exclusive with I(user_data).'], 'version_added': '2.3'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volumes": "{'description': ['A list of volume dicts, each containing device name and optionally ephemeral id or snapshot id. Size and type (and number of iops for io device type) must be specified for a new volume or a root volume, and may be passed for a snapshot volume. For any volume, a volume size less than 1 will be interpreted as a request not to create the volume.']}",
    "vpc_id": "{'description': ['VPC ID, used when resolving security group names to IDs.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml


# create a launch configuration using an AMI image and instance type as a basis

- name: note that encrypted volumes are only supported in >= Ansible 2.4
  ec2_lc:
    name: special
    image_id: ami-XXX
    key_name: default
    security_groups: ['group', 'group2' ]
    instance_type: t1.micro
    volumes:
    - device_name: /dev/sda1
      volume_size: 100
      volume_type: io1
      iops: 3000
      delete_on_termination: true
      encrypted: true
    - device_name: /dev/sdb
      ephemeral: ephemeral0

# create a launch configuration using a running instance id as a basis

- ec2_lc:
    name: special
    instance_id: i-00a48b207ec59e948
    key_name: default
    security_groups: ['launch-wizard-2' ]
    volumes:
    - device_name: /dev/sda1
      volume_size: 120
      volume_type: io1
      iops: 3000
      delete_on_termination: true

# create a launch configuration to omit the /dev/sdf EBS device that is included in the AMI image

- ec2_lc:
    name: special
    image_id: ami-XXX
    key_name: default
    security_groups: ['group', 'group2' ]
    instance_type: t1.micro
    volumes:
    - device_name: /dev/sdf
      no_device: true

```

## License

TODO

## Author Information
  - ['Gareth Rushgrove (@garethr)', 'Willem van Ketwich (@wilvk)']
  - ['Gareth Rushgrove (@garethr)', 'Willem van Ketwich (@wilvk)']
