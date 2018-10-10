# Ansible module: ansible.module_ec2_instance


Create & manage EC2 instances

## Description

Create and manage AWS EC2 instance

## Requirements

TODO

## Arguments

``` json
{
    "availability_zone": "{'description': ['Specify an availability zone to use the default subnet it. Useful if not specifying the I(vpc_subnet_id) parameter.', 'If no subnet, ENI, or availability zone is provided, the default subnet in the default VPC will be used in the first AZ (alphabetically sorted).']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cpu_credit_specification": "{'description': ['For T2 series instances, choose whether to allow increased charges to buy CPU credits if the default pool is depleted.', 'Choose I(unlimited) to enable buying additional CPU credits.'], 'choices': ['unlimited', 'standard']}",
    "cpu_options": "{'description': ['Reduce the number of vCPU exposed to the instance.', 'Those parameters can only be set at instance launch. The two suboptions threads_per_core and core_count are mandatory.', 'See U(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for combinations available.', 'Requires botocore >= 1.10.16'], 'version_added': 2.7, 'suboptions': {'threads_per_core': {'description': ['Select the number of threads per core to enable. Disable or Enable Intel HT'], 'choices': [1, 2], 'required': True}, 'core_count': {'description': ['Set the number of core to enable.'], 'required': True}}}",
    "detailed_monitoring": "{'description': ['Whether to allow detailed cloudwatch metrics to be collected, enabling more detailed alerting.']}",
    "ebs_optimized": "{'description': ['Whether instance is should use optimized EBS volumes, see U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply when deciding whether existing instances match and should be altered. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) for possible filters. Filter names and values are case sensitive. By default, instances are filtered for counting by their "Name" tag, base AMI, state (running, by default), and subnet ID. Any queryable filter can be used. Good candidates are specific tags, SSH keys, or security groups.'], 'default': {'tag:Name': '<provided-Name-attribute>', 'subnet-id': '<provided-or-default subnet>'}}",
    "image": "{'description': ['An image to use for the instance. The ec2_ami_facts module may be used to retrieve images. One of I(image) or I(image_id) are required when instance is not already present.', 'Complex object containing I(image.id), I(image.ramdisk), and I(image.kernel).', 'I(image.id) is the AMI ID.', "I(image.ramdisk) overrides the AMI's default ramdisk ID.", 'I(image.kernel) is a string AKI to override the AMI kernel.']}",
    "image_id": "{'description': ['I(ami) ID to use for the instance. One of I(image) or I(image_id) are required when instance is not already present.', 'This is an alias for I(image.id).']}",
    "instance_ids": "{'description': ['If you specify one or more instance IDs, only instances that have the specified IDs are returned.']}",
    "instance_initiated_shutdown_behavior": "{'description': ['Whether to stop or terminate an instance upon shutdown.'], 'choices': ['stop', 'terminate']}",
    "instance_role": "{'description': ['The ARN or name of an EC2-enabled instance role to be used. If a name is not provided in arn format then the ListInstanceProfiles permission must also be granted. U(https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfiles.html) If no full ARN is provided, the role with a matching name will be used from the active AWS account.']}",
    "instance_type": "{'description': ['Instance type to use for the instance, see U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) Only required when instance is not already present'], 'default': 't2.micro'}",
    "key_name": "{'description': ['Name of the SSH access key to assign to the instance - must exist in the region the instance is created.']}",
    "launch_template": "{'description': ['The EC2 launch template to base instance configuration on.', 'I(launch_template.id) the ID or the launch template (optional if name is specified)', 'I(launch_template.name) the pretty name of the launch template (optional if id is specified)', 'I(launch_template.version) the specific version of the launch template to use. If unspecified, the template default is chosen.']}",
    "name": "{'description': ['The Name tag for the instance.']}",
    "network": "{'description': ["Either a dictionary containing the key 'interfaces' corresponding to a list of network interface IDs or containing specifications for a single network interface.", 'If specifications for a single network are given, accepted keys are assign_public_ip (bool), private_ip_address (str), ipv6_addresses (list), source_dest_check (bool), description (str), delete_on_termination (bool), device_index (int), groups (list of security group IDs), private_ip_addresses (list), subnet_id (str).', 'I(network.interfaces) should be a list of ENI IDs (strings) or a list of objects containing the key I(id).', 'Use the ec2_eni to create ENIs with special settings.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_tags": "{'description': ['Delete any tags not specified in the task that are on the instance. This means you have to specify all the desired tags on each task affecting an instance.'], 'default': False}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_group": "{'description': ['A security group ID or name. Mutually exclusive with I(security_groups).']}",
    "security_groups": "{'description': ['A list of security group IDs or names (strings). Mutually exclusive with I(security_group).']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Goal state for the instances'], 'choices': ['present', 'terminated', 'running', 'started', 'stopped', 'restarted', 'rebooted', 'absent'], 'default': 'present'}",
    "tags": "{'description': ['A hash/dictionary of tags to add to the new instance or to add/remove from an existing one.']}",
    "tenancy": "{'description': ['What type of tenancy to allow an instance to use. Default is shared tenancy. Dedicated tenancy will incur additional charges.'], 'choices': ['dedicated', 'default']}",
    "termination_protection": "{'description': ['Whether to enable termination protection. This module will not terminate an instance with termination protection active, it must be turned off first.']}",
    "tower_callback": "{'description': ['Preconfigured user-data to enable an instance to perform a Tower callback (Linux only).', 'Mutually exclusive with I(user_data).', 'For Windows instances, to enable remote access via Ansible set I(tower_callback.windows) to true, and optionally set an admin password.', "If using 'windows' and 'set_password', callback to Tower will not be performed but the instance will be ready to receive winrm connections from Ansible."], 'suboptions': {'tower_address': {'description': ['IP address or DNS name of Tower server. Must be accessible via this address from the VPC that this instance will be launched in.']}, 'job_template_id': {'description': ['Either the integer ID of the Tower Job Template, or the name (name supported only for Tower 3.2+)']}, 'host_config_key': {'description': ['Host configuration secret key generated by the Tower job template.']}}}",
    "user_data": "{'description': ['Opaque blob of data which is made available to the ec2 instance']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volumes": "{'description': ['A list of block device mappings, by default this will always use the AMI root device so the volumes option is primarily for adding more storage.', 'A mapping contains the (optional) keys device_name, virtual_name, ebs.volume_type, ebs.volume_size, ebs.kms_key_id, ebs.iops, and ebs.delete_on_termination.', 'For more information about each parameter, see U(https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html)']}",
    "vpc_subnet_id": "{'description': ['The subnet ID in which to launch the instance (VPC) If none is provided, ec2_instance will chose the default zone of the default VPC'], 'aliases': ['subnet_id']}",
    "wait": "{'description': ['Whether or not to wait for the desired state (use wait_timeout to customize this)'], 'default': True}",
    "wait_timeout": "{'description': ['How long to wait (in seconds) for the instance to finish booting/terminating'], 'default': 600}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Terminate every running instance in a region. Use with EXTREME caution.
- ec2_instance:
    state: absent
    filters:
      instance-state-name: running

# restart a particular instance by its ID
- ec2_instance:
    state: restarted
    instance_ids:
      - i-12345678

# start an instance with a public IP address
- ec2_instance:
    name: "public-compute-instance"
    key_name: "prod-ssh-key"
    vpc_subnet_id: subnet-5ca1ab1e
    instance_type: c5.large
    security_group: default
    network:
      assign_public_ip: true
    image_id: ami-123456
    tags:
      Environment: Testing

# start an instance and have it begin a Tower callback on boot
- ec2_instance:
    name: "tower-callback-test"
    key_name: "prod-ssh-key"
    vpc_subnet_id: subnet-5ca1ab1e
    security_group: default
    tower_callback:
      # IP or hostname of tower server
      tower_address: 1.2.3.4
      job_template_id: 876
      host_config_key: '[secret config key goes here]'
    network:
      assign_public_ip: true
    image_id: ami-123456
    cpu_credit_specification: unlimited
    tags:
      SomeThing: "A value"

```

## License

TODO

## Author Information
  - ['Ryan Scott Brown, @ryansb']
