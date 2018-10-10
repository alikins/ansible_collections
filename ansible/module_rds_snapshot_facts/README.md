# Ansible module: ansible.module_rds_snapshot_facts


obtain facts about one or more RDS snapshots

## Description

obtain facts about one or more RDS snapshots. These can be for unclustered snapshots or snapshots of clustered DBs (Aurora)
Aurora snapshot facts may be obtained if no identifier parameters are passed or if one of the cluster parameters are passed.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "db_cluster_identifier": "{'description': ['RDS cluster name for which to find snapshots. Mutually exclusive with I(db_snapshot_identifier), I(db_instance_identifier), I(db_cluster_snapshot_identifier)'], 'required': False}",
    "db_cluster_snapshot_identifier": "{'description': ['Name of an RDS cluster snapshot. Mutually exclusive with I(db_instance_identifier), I(db_snapshot_identifier), I(db_cluster_identifier)'], 'required': False}",
    "db_instance_identifier": "{'description': ['RDS instance name for which to find snapshots. Mutually exclusive with I(db_snapshot_identifier), I(db_cluster_identifier), I(db_cluster_snapshot_identifier)'], 'required': False}",
    "db_snapshot_identifier": "{'description': ['Name of an RDS (unclustered) snapshot. Mutually exclusive with I(db_instance_identifier), I(db_cluster_identifier), I(db_cluster_snapshot_identifier)'], 'required': False, 'aliases': ['snapshot_name']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "snapshot_type": "{'description': ['Type of snapshot to find. By default both automated and manual snapshots will be returned.'], 'required': False, 'choices': ['automated', 'manual', 'shared', 'public']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Get facts about an snapshot
- rds_snapshot_facts:
    db_snapshot_identifier: snapshot_name
  register: new_database_facts

# Get all RDS snapshots for an RDS instance
- rds_snapshot_facts:
    db_instance_identifier: helloworld-rds-master

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)']
