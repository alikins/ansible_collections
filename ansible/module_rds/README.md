# Ansible module: ansible.module_rds


create, delete, or modify an Amazon rds instance

## Description

Creates, deletes, or modifies rds instances.  When creating an instance it can be either a new instance or a read-only replica of an existing instance. This module has a dependency on python-boto >= 2.5. The 'promote' command requires boto >= 2.18.0. Certain features such as tags rely on boto.rds2 (boto >= 2.26.0)

## Requirements

TODO

## Arguments

``` json
{
    "apply_immediately": "{'description': ['Used only when command=modify.  If enabled, the modifications will be applied as soon as possible rather than waiting for the next preferred maintenance window.'], 'type': 'bool', 'default': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "backup_retention": "{'description': ['Number of days backups are retained.  Set to 0 to disable backups.  Default is 1 day.  Valid range: 0-35. Used only when command=create or command=modify.\n']}",
    "backup_window": "{'description': ['Backup window in format of hh24:mi-hh24:mi.  If not specified then a random backup window is assigned. Used only when command=create or command=modify.']}",
    "character_set_name": "{'description': ['Associate the DB instance with a specified character set. Used with command=create.'], 'version_added': '1.9'}",
    "command": "{'description': ["Specifies the action to take. The 'reboot' option is available starting at version 2.0"], 'required': True, 'choices': ['create', 'replicate', 'delete', 'facts', 'modify', 'promote', 'snapshot', 'reboot', 'restore']}",
    "db_engine": "{'description': ['The type of database.  Used only when command=create.', 'mariadb was added in version 2.2'], 'choices': ['mariadb', 'MySQL', 'oracle-se1', 'oracle-se2', 'oracle-se', 'oracle-ee', 'sqlserver-ee', 'sqlserver-se', 'sqlserver-ex', 'sqlserver-web', 'postgres', 'aurora']}",
    "db_name": "{'description': ['Name of a database to create within the instance.  If not specified then no database is created. Used only when command=create.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "engine_version": "{'description': ['Version number of the database engine to use. Used only when command=create. If not specified then the current Amazon RDS default engine version is used']}",
    "force_failover": "{'description': ['Used only when command=reboot.  If enabled, the reboot is done using a MultiAZ failover.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "instance_name": "{'description': ['Database instance identifier. Required except when using command=facts or command=delete on just a snapshot']}",
    "instance_type": "{'description': ['The instance type of the database.  Must be specified when command=create. Optional when command=replicate, command=modify or command=restore. If not specified then the replica inherits the same instance type as the source instance.']}",
    "iops": "{'description': ['Specifies the number of IOPS for the instance.  Used only when command=create or command=modify. Must be an integer greater than 1000.']}",
    "license_model": "{'description': ['The license model for this DB instance. Used only when command=create or command=restore.'], 'choices': ['license-included', 'bring-your-own-license', 'general-public-license', 'postgresql-license']}",
    "maint_window": "{'description': ['Maintenance window in format of ddd:hh24:mi-ddd:hh24:mi.  (Example: Mon:22:00-Mon:23:15) If not specified then a random maintenance window is assigned. Used only when command=create or command=modify.\n']}",
    "multi_zone": "{'description': ['Specifies if this is a Multi-availability-zone deployment. Can not be used in conjunction with zone parameter. Used only when command=create or command=modify.'], 'type': 'bool'}",
    "new_instance_name": "{'description': ['Name to rename an instance to. Used only when command=modify.'], 'version_added': '1.5'}",
    "option_group": "{'description': ['The name of the option group to use.  If not specified then the default option group is used. Used only when command=create.']}",
    "parameter_group": "{'description': ['Name of the DB parameter group to associate with this instance.  If omitted then the RDS default DBParameterGroup will be used. Used only when command=create or command=modify.']}",
    "password": "{'description': ['Password for the master database username. Used only when command=create or command=modify.']}",
    "port": "{'description': ['Port number that the DB instance uses for connections. Used only when command=create or command=replicate.', 'Prior to 2.0 it always defaults to null and the API would use 3306, it had to be set to other DB default values when not using MySql. Starting at 2.0 it automatically defaults to what is expected for each C(db_engine).'], 'default': '3306 for mysql, 1521 for Oracle, 1433 for SQL Server, 5432 for PostgreSQL.'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "publicly_accessible": "{'description': ['explicitly set whether the resource should be publicly accessible or not. Used with command=create, command=replicate. Requires boto >= 2.26.0'], 'version_added': '1.9'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the EC2_REGION environment variable, if any, is used.'], 'required': True, 'aliases': ['aws_region', 'ec2_region']}",
    "security_groups": "{'description': ['Comma separated list of one or more security groups.  Used only when command=create or command=modify.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "size": "{'description': ['Size in gigabytes of the initial storage for the DB instance. Used only when command=create or command=modify.']}",
    "snapshot": "{'description': ['Name of snapshot to take. When command=delete, if no snapshot name is provided then no snapshot is taken. If used with command=delete with no instance_name, the snapshot is deleted. Used with command=facts, command=delete or command=snapshot.']}",
    "source_instance": "{'description': ['Name of the database to replicate. Used only when command=replicate.']}",
    "subnet": "{'description': ['VPC subnet group.  If specified then a VPC instance is created. Used only when command=create.']}",
    "tags": "{'description': ['tags dict to apply to a resource. Used with command=create, command=replicate, command=restore. Requires boto >= 2.26.0'], 'version_added': '1.9'}",
    "upgrade": "{'description': ['Indicates that minor version upgrades should be applied automatically. Used only when command=create or command=replicate.'], 'type': 'bool', 'default': False}",
    "username": "{'description': ['Master database username. Used only when command=create.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_security_groups": "{'description': ['Comma separated list of one or more vpc security group ids. Also requires `subnet` to be specified. Used only when command=create or command=modify.']}",
    "wait": "{'description': ["When command=create, replicate, modify or restore then wait for the database to enter the 'available' state.  When command=delete wait for the database to be terminated."], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
    "zone": "{'description': ['availability zone in which to launch the instance. Used only when command=create, command=replicate or command=restore.'], 'aliases': ['aws_zone', 'ec2_zone']}",
}
```

## Examples


``` yaml

# Basic mysql provisioning example
- rds:
    command: create
    instance_name: new-database
    db_engine: MySQL
    size: 10
    instance_type: db.m1.small
    username: mysql_admin
    password: 1nsecure
    tags:
      Environment: testing
      Application: cms

# Create a read-only replica and wait for it to become available
- rds:
    command: replicate
    instance_name: new-database-replica
    source_instance: new_database
    wait: yes
    wait_timeout: 600

# Delete an instance, but create a snapshot before doing so
- rds:
    command: delete
    instance_name: new-database
    snapshot: new_database_snapshot

# Get facts about an instance
- rds:
    command: facts
    instance_name: new-database
  register: new_database_facts

# Rename an instance and wait for the change to take effect
- rds:
    command: modify
    instance_name: new-database
    new_instance_name: renamed-database
    wait: yes

# Reboot an instance and wait for it to become available again
- rds:
    command: reboot
    instance_name: database
    wait: yes

# Restore a Postgres db instance from a snapshot, wait for it to become available again, and
#  then modify it to add your security group. Also, display the new endpoint.
#  Note that the "publicly_accessible" option is allowed here just as it is in the AWS CLI
- local_action:
     module: rds
     command: restore
     snapshot: mypostgres-snapshot
     instance_name: MyNewInstanceName
     region: us-west-2
     zone: us-west-2b
     subnet: default-vpc-xx441xxx
     publicly_accessible: yes
     wait: yes
     wait_timeout: 600
     tags:
         Name: pg1_test_name_tag
  register: rds

- local_action:
     module: rds
     command: modify
     instance_name: MyNewInstanceName
     region: us-west-2
     vpc_security_groups: sg-xxx945xx

- debug:
    msg: "The new db endpoint is {{ rds.instance.endpoint }}"

```

## License

TODO

## Author Information
  - ['Bruce Pennypacker (@bpennypacker)', 'Will Thames (@willthames)']
  - ['Bruce Pennypacker (@bpennypacker)', 'Will Thames (@willthames)']
