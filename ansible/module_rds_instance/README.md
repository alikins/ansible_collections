# Ansible module: ansible.module_rds_instance


Manage RDS instances

## Description

Create, modify, and delete RDS instances.

## Requirements

TODO

## Arguments

``` json
{
    "allocated_storage": "{'description': ['The amount of storage (in gibibytes) to allocate for the DB instance.']}",
    "allow_major_version_upgrade": "{'description': ['Whether to allow major version upgrades.'], 'type': 'bool'}",
    "apply_immediately": "{'description': ['A value that specifies whether modifying a cluster with I(new_db_instance_identifier) and I(master_user_password) should be applied as soon as possible, regardless of the I(preferred_maintenance_window) setting. If false, changes are applied during the next maintenance window.'], 'type': 'bool', 'default': False}",
    "auto_minor_version_upgrade": "{'description': ['Whether minor version upgrades are applied automatically to the DB instance during the maintenance window.'], 'type': 'bool'}",
    "availability_zone": "{'description': ['A list of EC2 Availability Zones that instances in the DB cluster can be created in. May be used when creating a cluster or when restoring from S3 or a snapshot. Mutually exclusive with I(multi_az).'], 'aliases': ['az', 'zone']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "backup_retention_period": "{'description': ['The number of days for which automated backups are retained (must be greater or equal to 1). May be used when creating a new cluster, when restoring from S3, or when modifying a cluster.']}",
    "ca_certificate_identifier": "{'description': ['The identifier of the CA certificate for the DB instance.']}",
    "character_set_name": "{'description': ['The character set to associate with the DB cluster.']}",
    "copy_tags_to_snapshot": "{'description': ['Whether or not to copy all tags from the DB instance to snapshots of the instance. When initially creating a DB instance the RDS API defaults this to false if unspecified.'], 'type': 'bool'}",
    "creation_source": "{'description': ['Which source to use if restoring from a template (an existing instance, S3 bucket, or snapshot).'], 'choices': ['snapshot', 's3', 'instance']}",
    "db_cluster_identifier": "{'description': ['The DB cluster (lowercase) identifier to add the aurora DB instance to. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens.'], 'aliases': ['cluster_id']}",
    "db_instance_class": "{'description': ['The compute and memory capacity of the DB instance, for example db.t2.micro.'], 'aliases': ['class', 'instance_type']}",
    "db_instance_identifier": "{'description': ['The DB instance (lowercase) identifier. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens.'], 'aliases': ['instance_id', 'id'], 'required': True}",
    "db_name": "{'description': ['The name for your database. If a name is not provided Amazon RDS will not create a database.']}",
    "db_parameter_group_name": "{'description': ['The name of the DB parameter group to associate with this DB instance. When creating the DB instance if this argument is omitted the default DBParameterGroup for the specified engine is used.']}",
    "db_security_groups": "{'description': ['(EC2-Classic platform) A list of DB security groups to associate with this DB instance.'], 'type': 'list'}",
    "db_snapshot_identifier": "{'description': ['The identifier for the DB snapshot to restore from if using I(creation_source=snapshot).']}",
    "db_subnet_group_name": "{'description': ['The DB subnet group name to use for the DB instance.'], 'aliases': ['subnet_group']}",
    "domain": "{'description': ['The Active Directory Domain to restore the instance in.']}",
    "domain_iam_role_name": "{'description': ['The name of the IAM role to be used when making API calls to the Directory Service.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "enable_cloudwatch_logs_exports": "{'description': ['A list of log types that need to be enabled for exporting to CloudWatch Logs.'], 'aliases': ['cloudwatch_log_exports'], 'type': 'list'}",
    "enable_iam_database_authentication": "{'description': ['Enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. If this option is omitted when creating the cluster, Amazon RDS sets this to False.'], 'type': 'bool'}",
    "enable_performance_insights": "{'description': ['Whether to enable Performance Insights for the DB instance.'], 'type': 'bool'}",
    "engine": "{'description': ['The name of the database engine to be used for this DB instance. This is required to create an instance. Valid choices are aurora | aurora-mysql | aurora-postgresql | mariadb | mysql | oracle-ee | oracle-se | oracle-se1 | oracle-se2 | postgres | sqlserver-ee | sqlserver-ex | sqlserver-se | sqlserver-web']}",
    "engine_version": "{'description': ['The version number of the database engine to use. For Aurora MySQL that could be 5.6.10a , 5.7.12. Aurora PostgreSQL example, 9.6.3']}",
    "final_db_snapshot_identifier": "{'description': ['The DB instance snapshot identifier of the new DB instance snapshot created when I(skip_final_snapshot) is false.'], 'aliases': ['final_snapshot_identifier']}",
    "force_failover": "{'description': ['Set to true to conduct the reboot through a MultiAZ failover.'], 'type': 'bool'}",
    "force_update_password": "{'description': ['Set to True to update your cluster password with I(master_user_password). Since comparing passwords to determine if it needs to be updated is not possible this is set to False by default to allow idempotence.'], 'type': 'bool', 'default': False}",
    "iops": "{'description': ['The Provisioned IOPS (I/O operations per second) value.']}",
    "kms_key_id": "{'description': ['The ARN of the AWS KMS key identifier for an encrypted DB instance. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.', 'If I(storage_encrypted) is true and and this option is not provided, the default encryption key is used.']}",
    "license_model": "{'description': ['The license model for the DB instance.'], 'choices': ['license-included', 'bring-your-own-license', 'general-public-license']}",
    "master_user_password": "{'description': ['An 8-41 character password for the master database user. The password can contain any printable ASCII character except "/", """, or "@". To modify the password use I(force_password_update). Use I(apply immediately) to change the password immediately, otherwise it is updated during the next maintenance window.'], 'aliases': ['password']}",
    "master_username": "{'description': ['The name of the master user for the DB cluster. Must be 1-16 letters or numbers and begin with a letter.'], 'aliases': ['username']}",
    "monitoring_interval": "{'description': ['The interval, in seconds, when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting metrics, specify 0. Amazon RDS defaults this to 0 if omitted when initially creating a DB instance.']}",
    "monitoring_role_arn": "{'description': ['The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.']}",
    "multi_az": "{'description': ['Specifies if the DB instance is a Multi-AZ deployment. Mutually exclusive with I(availability_zone).'], 'type': 'bool'}",
    "new_db_instance_identifier": "{'description': ['The new DB cluster (lowercase) identifier for the DB cluster when renaming a DB instance. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. Use I(apply_immediately) to rename immediately, otherwise it is updated during the next maintenance window.'], 'aliases': ['new_instance_id', 'new_id']}",
    "option_group_name": "{'description': ['The option group to associate with the DB instance.']}",
    "performance_insights_kms_key_id": "{'description': ['The AWS KMS key identifier (ARN, name, or alias) for encryption of Performance Insights data.']}",
    "performance_insights_retention_period": "{'description': ['The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731.']}",
    "port": "{'description': ['The port number on which the instances accept connections.']}",
    "preferred_backup_window": "{'description': ['The daily time range (in UTC) of at least 30 minutes, during which automated backups are created if automated backups are enabled using I(backup_retention_period). The option must be in the format of "hh24:mi-hh24:mi" and not conflict with I(preferred_maintenance_window).'], 'aliases': ['backup_window']}",
    "preferred_maintenance_window": "{'description': ['The weekly time range (in UTC) of at least 30 minutes, during which system maintenance can occur. The option must be in the format "ddd:hh24:mi-ddd:hh24:mi" where ddd is one of Mon, Tue, Wed, Thu, Fri, Sat, Sun.'], 'aliases': ['maintenance_window']}",
    "processor_features": "{'description': ['A dictionary of Name, Value pairs to indicate the number of CPU cores and the number of threads per core for the DB instance class of the DB instance. Names are threadsPerCore and coreCount. Set this option to an empty dictionary to use the default processor features.'], 'suboptions': {'threadsPerCore': {'description': 'The number of threads per core'}, 'coreCount': {'description': 'The number of CPU cores'}}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "promotion_tier": "{'description': ['An integer that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.']}",
    "publicly_accessible": "{'description': ['Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.'], 'type': 'bool'}",
    "purge_cloudwatch_logs_exports": "{'description': ["Set to False to retain any enabled cloudwatch logs that aren't specified in the task and are associated with the instance."], 'type': 'bool', 'default': True}",
    "purge_tags": "{'description': ["Set to False to retain any tags that aren't specified in task and are associated with the instance."], 'type': 'bool', 'default': True}",
    "read_replica": "{'description': ["Set to False to promote a read replica cluster or true to create one. When creating a read replica C(creation_source) should be set to 'instance' or not provided. C(source_db_instance_identifier) must be provided with this option."], 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "restore_time": "{'description': ['If using I(creation_source=instance) this indicates the UTC date and time to restore from the source instance. For example, "2009-09-07T23:45:00Z". May alternatively set c(use_latest_restore_time) to True.']}",
    "s3_bucket_name": "{'description': ['The name of the Amazon S3 bucket that contains the data used to create the Amazon DB instance.']}",
    "s3_ingestion_role_arn": "{'description': ['The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf.']}",
    "s3_prefix": "{'description': ['The prefix for all of the file names that contain the data used to create the Amazon DB instance. If you do not specify a SourceS3Prefix value, then the Amazon DB instance is created by using all of the files in the Amazon S3 bucket.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "skip_final_snapshot": "{'description': ['Whether a final DB cluster snapshot is created before the DB cluster is deleted. If this is false I(final_db_snapshot_identifier) must be provided.'], 'type': 'bool', 'default': False}",
    "snapshot_identifier": "{'description': ['The ARN of the DB snapshot to restore from when using I(creation_source=snapshot).']}",
    "source_db_instance_identifier": "{'description': ['The identifier or ARN of the source DB instance from which to restore when creating a read replica or spinning up a point-in-time DB instance using I(creation_source=instance). If the source DB is not in the same region this should be an ARN.']}",
    "source_engine": "{'description': ['The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.'], 'choices': ['mysql']}",
    "source_engine_version": "{'description': ['The version of the database that the backup files were created from.']}",
    "source_region": "{'description': ['The region of the DB instance from which the replica is created.']}",
    "state": "{'description': ['Whether the snapshot should exist or not. I(rebooted) is not idempotent and will leave the DB instance in a running state and start it prior to rebooting if it was stopped. I(present) will leave the DB instance in the current running/stopped state, (running if creating the DB instance).', 'I(state=running) and I(state=started) are synonyms, as are I(state=rebooted) and I(state=restarted). Note - rebooting the instance is not idempotent.'], 'choices': ['present', 'absent', 'terminated', 'running', 'started', 'stopped', 'rebooted', 'restarted'], 'default': 'present'}",
    "storage_encrypted": "{'description': ['Whether the DB instance is encrypted.'], 'type': 'bool'}",
    "storage_type": "{'description': ['The storage type to be associated with the DB instance. I(storage_type) does not apply to Aurora DB instances.'], 'choices': ['standard', 'gp2', 'io1']}",
    "tags": "{'description': ['A dictionary of key value pairs to assign the DB cluster.']}",
    "tde_credential_arn": "{'description': ['The ARN from the key store with which to associate the instance for Transparent Data Encryption. This is supported by Oracle or SQL Server DB instances and may be used in conjunction with C(storage_encrypted) though it might slightly affect the performance of your database.'], 'aliases': ['transparent_data_encryption_arn']}",
    "tde_credential_password": "{'description': ['The password for the given ARN from the key store in order to access the device.'], 'aliases': ['transparent_data_encryption_password']}",
    "timezone": "{'description': ['The time zone of the DB instance.']}",
    "use_latest_restorable_time": "{'description': ['Whether to restore the DB instance to the latest restorable backup time. Only one of I(use_latest_restorable_time) and I(restore_to_time) may be provided.'], 'type': 'bool', 'aliases': ['restore_from_latest']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_security_group_ids": "{'description': ['A list of EC2 VPC security groups to associate with the DB cluster.'], 'type': 'list'}",
    "wait": "{'description': ['Whether to wait for the cluster to be available, stopped, or deleted. At a later time a wait_timeout option may be added. Following each API call to create/modify/delete the instance a waiter is used with a 60 second delay 30 times until the instance reaches the expected state (available/stopped/deleted). The total task time may also be influenced by AWSRetry which helps stabilize if the instance is in an invalid state to operate on to begin with (such as if you try to stop it when it is in the process of rebooting). If setting this to False task retries and delays may make your playbook execution better handle timeouts for major modifications.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.
- name: create minimal aurora instance in default VPC and default subnet group
  rds_instance:
    engine: aurora
    db_instance_identifier: ansible-test-aurora-db-instance
    instance_type: db.t2.small
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: ansible-test-cluster  # This cluster must exist - see rds_cluster to manage it

- name: Create a DB instance using the default AWS KMS encryption key
  rds_instance:
    id: test-encrypted-db
    state: present
    engine: mariadb
    storage_encrypted: True
    db_instance_class: db.t2.medium
    username: "{{ username }}"
    password: "{{ password }}"
    allocated_storage: "{{ allocated_storage }}"

- name: remove the DB instance without a final snapshot
  rds_instance:
    id: "{{ instance_id }}"
    state: absent
    skip_final_snapshot: True

- name: remove the DB instance with a final snapshot
  rds_instance:
    id: "{{ instance_id }}"
    state: absent
    final_snapshot_identifier: "{{ snapshot_id }}"

```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
