# Ansible module: ansible.module_ec2


create, terminate, start or stop an instance in ec2

## Description

Creates or terminates ec2 instances.

## Requirements

TODO

## Arguments

``` json
{
    "assign_public_ip": "{'version_added': '1.5', 'description': ['when provisioning within vpc, assign a public IP address. Boto library must be 2.13.0+'], 'type': 'bool'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "count": "{'description': ['number of instances to launch'], 'default': 1}",
    "count_tag": "{'version_added': '1.5', 'description': ['Used with \'exact_count\' to determine how many nodes based on a specific tag criteria should be running. This can be expressed in multiple ways and is shown in the EXAMPLES section.  For instance, one can request 25 servers that are tagged with "class=webserver". The specified tag must already exist or be passed in as the \'instance_tags\' option.']}",
    "ebs_optimized": "{'version_added': '1.6', 'description': ['whether instance is using optimized EBS volumes, see U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)'], 'default': 'no'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "exact_count": "{'version_added': '1.5', 'description': ["An integer value which indicates how many instances that match the 'count_tag' parameter should be running. Instances are either created or terminated based on this value."]}",
    "group": "{'description': ['security group (or list of groups) to use with the instance'], 'aliases': ['groups']}",
    "group_id": "{'description': ['security group id (or list of ids) to use with the instance']}",
    "id": "{'description': ['identifier for this instance or set of instances, so that the module will be idempotent with respect to EC2 instances. This identifier is valid for at least 24 hours after the termination of the instance, and should not be reused for another call later on. For details, see the description of client token at U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html).']}",
    "image": "{'description': ['I(ami) ID to use for the instance'], 'required': True}",
    "instance_ids": "{'version_added': '1.3', 'description': ['list of instance ids, currently used for states: absent, running, stopped'], 'aliases': ['instance_id']}",
    "instance_initiated_shutdown_behavior": "{'version_added': '2.2', 'description': ['Set whether AWS will Stop or Terminate an instance on shutdown. This parameter is ignored when using instance-store images (which require termination on shutdown).'], 'default': 'stop', 'choices': ['stop', 'terminate']}",
    "instance_profile_name": "{'version_added': '1.3', 'description': ['Name of the IAM instance profile (i.e. what the EC2 console refers to as an "IAM Role") to use. Boto library must be 2.5.0+']}",
    "instance_tags": "{'description': ['a hash/dictionary of tags to add to the new instance or for starting/stopping instance by tag; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\'']}",
    "instance_type": "{'description': ['instance type to use for the instance, see U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)'], 'required': True}",
    "kernel": "{'description': ['kernel I(eki) to use for the instance']}",
    "key_name": "{'description': ['key pair to use on the instance'], 'aliases': ['keypair']}",
    "monitoring": "{'description': ['enable detailed monitoring (CloudWatch) for instance'], 'type': 'bool', 'default': False}",
    "network_interfaces": "{'version_added': '2.0', 'description': ['A list of existing network interfaces to attach to the instance at launch. When specifying existing network interfaces, none of the assign_public_ip, private_ip, vpc_subnet_id, group, or group_id parameters may be used. (Those parameters are for creating a new network interface at launch.)'], 'aliases': ['network_interface']}",
    "placement_group": "{'version_added': '1.3', 'description': ['placement group for the instance when using EC2 Clustered Compute']}",
    "private_ip": "{'description': ['the private ip address to assign the instance (from the vpc subnet)']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "ramdisk": "{'description': ['ramdisk I(eri) to use for the instance']}",
    "region": "{'description': ['The AWS region to use.  Must be specified if ec2_url is not used. If not specified then the value of the EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_dest_check": "{'version_added': '1.6', 'description': ['Enable or Disable the Source/Destination checks (for NAT instances and Virtual Routers). When initially creating an instance the EC2 API defaults this to True.'], 'type': 'bool'}",
    "spot_launch_group": "{'version_added': '2.1', 'description': ['Launch group for spot request, see U(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html#spot-launch-group)']}",
    "spot_price": "{'version_added': '1.5', 'description': ['Maximum spot price to bid, If not set a regular on-demand instance is requested. A spot request is made with this maximum bid. When it is filled, the instance is started.']}",
    "spot_type": "{'version_added': '2.0', 'description': ['Type of spot request; one of "one-time" or "persistent". Defaults to "one-time" if not supplied.'], 'default': 'one-time', 'choices': ['one-time', 'persistent']}",
    "spot_wait_timeout": "{'version_added': '1.5', 'description': ['how long to wait for the spot instance request to be fulfilled'], 'default': 600}",
    "state": "{'version_added': '1.3', 'description': ["create, terminate, start, stop or restart instances. The state 'restarted' was added in 2.2"], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'running', 'restarted', 'stopped']}",
    "tenancy": "{'version_added': '1.9', 'description': ['An instance with a tenancy of "dedicated" runs on single-tenant hardware and can only be launched into a VPC. Note that to use dedicated tenancy you MUST specify a vpc_subnet_id as well. Dedicated tenancy is not available for EC2 "micro" instances.'], 'default': 'default', 'choices': ['default', 'dedicated']}",
    "termination_protection": "{'version_added': '2.0', 'description': ['Enable or Disable the Termination Protection'], 'type': 'bool', 'default': False}",
    "user_data": "{'description': ['opaque blob of data which is made available to the ec2 instance']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volumes": "{'version_added': '1.5', 'description': ['a list of hash/dictionaries of volumes to add to the new instance; \'[{"key":"value", "key":"value"}]\'; keys allowed are - device_name (str; required), delete_on_termination (bool; False), device_type (deprecated), ephemeral (str), encrypted (bool; False), snapshot (str), volume_type (str), volume_size (int, GB), iops (int) - device_type is deprecated use volume_type, iops must be set when volume_type=\'io1\', ephemeral and snapshot are mutually exclusive.']}",
    "vpc_subnet_id": "{'description': ['the subnet ID in which to launch the instance (VPC)']}",
    "wait": "{'description': ["wait for the instance to reach its desired state before returning.  Does not wait for SSH, see 'wait_for_connection' example for details."], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
    "zone": "{'description': ['AWS availability zone in which to launch the instance'], 'aliases': ['aws_zone', 'ec2_zone']}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic provisioning example
- ec2:
    key_name: mykey
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    group: webserver
    count: 3
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Advanced example with tagging and CloudWatch
- ec2:
    key_name: mykey
    group: databases
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
       db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Single instance with additional IOPS volume from snapshot and volume delete on termination
- ec2:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/sdb
        snapshot: snap-abcdef12
        volume_type: io1
        iops: 1000
        volume_size: 100
        delete_on_termination: true
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Single instance with ssd gp2 root volume
- ec2:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/xvda
        volume_type: gp2
        volume_size: 8
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    count_tag:
      Name: dbserver
    exact_count: 1

# Multiple groups example
- ec2:
    key_name: mykey
    group: ['databases', 'internal-services', 'sshable', 'and-so-forth']
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
        db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Multiple instances with additional volume from snapshot
- ec2:
    key_name: mykey
    group: webserver
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    volumes:
    - device_name: /dev/sdb
      snapshot: snap-abcdef12
      volume_size: 10
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Dedicated tenancy example
- local_action:
    module: ec2
    assign_public_ip: yes
    group_id: sg-1dc53f72
    key_name: mykey
    image: ami-6e649707
    instance_type: m1.small
    tenancy: dedicated
    vpc_subnet_id: subnet-29e63245
    wait: yes

# Spot instance example
- ec2:
    spot_price: 0.24
    spot_wait_timeout: 600
    keypair: mykey
    group_id: sg-1dc53f72
    instance_type: m1.small
    image: ami-6e649707
    wait: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    spot_launch_group: report_generators

# Examples using pre-existing network interfaces
- ec2:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interface: eni-deadbeef

- ec2:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interfaces: ['eni-deadbeef', 'eni-5ca1ab1e']

# Launch instances, runs some tasks
# and then terminate them

- name: Create a sandbox instance
  hosts: localhost
  gather_facts: False
  vars:
    keypair: my_keypair
    instance_type: m1.small
    security_group: my_securitygroup
    image: my_ami_id
    region: us-east-1
  tasks:
    - name: Launch instance
      ec2:
         key_name: "{{ keypair }}"
         group: "{{ security_group }}"
         instance_type: "{{ instance_type }}"
         image: "{{ image }}"
         wait: true
         region: "{{ region }}"
         vpc_subnet_id: subnet-29e63245
         assign_public_ip: yes
      register: ec2

    - name: Add new instance to host group
      add_host:
        hostname: "{{ item.public_ip }}"
        groupname: launched
      with_items: "{{ ec2.instances }}"

    - name: Wait for SSH to come up
      delegate_to: "{{ item.public_dns_name }}"
      wait_for_connection:
        delay: 60
        timeout: 320
      with_items: "{{ ec2.instances }}"

- name: Configure instance(s)
  hosts: launched
  become: True
  gather_facts: True
  roles:
    - my_awesome_role
    - my_awesome_test

- name: Terminate instances
  hosts: localhost
  connection: local
  tasks:
    - name: Terminate instances that were previously launched
      ec2:
        state: 'absent'
        instance_ids: '{{ ec2.instance_ids }}'

# Start a few existing instances, run some tasks
# and stop the instances

- name: Start sandbox instances
  hosts: localhost
  gather_facts: false
  connection: local
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Start the sandbox instances
      ec2:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: running
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes
  roles:
    - do_neat_stuff
    - do_more_neat_stuff

- name: Stop sandbox instances
  hosts: localhost
  gather_facts: false
  connection: local
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Stop the sandbox instances
      ec2:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: stopped
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes

#
# Start stopped instances specified by tag
#
- local_action:
    module: ec2
    instance_tags:
        Name: ExtraPower
    state: running

#
# Restart instances specified by tag
#
- local_action:
    module: ec2
    instance_tags:
        Name: ExtraPower
    state: restarted

#
# Enforce that 5 instances with a tag "foo" are running
# (Highly recommended!)
#

- ec2:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        foo: bar
    exact_count: 5
    count_tag: foo
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

#
# Enforce that 5 running instances named "database" with a "dbtype" of "postgres"
#

- ec2:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        Name: database
        dbtype: postgres
    exact_count: 5
    count_tag:
        Name: database
        dbtype: postgres
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

#
# count_tag complex argument examples
#

    # instances with tag foo
- ec2:
    count_tag:
        foo:

    # instances with tag foo=bar
- ec2:
    count_tag:
        foo: bar

    # instances with tags foo=bar & baz
- ec2:
    count_tag:
        foo: bar
        baz:

    # instances with tags foo & bar & baz=bang
- ec2:
    count_tag:
        - foo
        - bar
        - baz: bang


```

## License

TODO

## Author Information
  - ['Tim Gerla (@tgerla)', 'Lester Wade (@lwade)', 'Seth Vidal']
  - ['Tim Gerla (@tgerla)', 'Lester Wade (@lwade)', 'Seth Vidal']
  - ['Tim Gerla (@tgerla)', 'Lester Wade (@lwade)', 'Seth Vidal']
