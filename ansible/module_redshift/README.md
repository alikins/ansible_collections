# Ansible module: ansible.module_redshift


create, delete, or modify an Amazon Redshift instance

## Description

Creates, deletes, or modifies amazon Redshift cluster instances.

## Requirements

TODO

## Arguments

``` json
{
    "allow_version_upgrade": "{'description': ['flag to determinate if upgrade of version is possible'], 'aliases': ['version_upgrade'], 'default': 'yes'}",
    "automated_snapshot_retention_period": "{'description': ['period when the snapshot take place'], 'aliases': ['retention_period']}",
    "availability_zone": "{'description': ['availability zone in which to launch cluster'], 'aliases': ['zone', 'aws_zone']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cluster_parameter_group_name": "{'description': ['name of the cluster parameter group'], 'aliases': ['param_group_name']}",
    "cluster_security_groups": "{'description': ['in which security group the cluster belongs'], 'aliases': ['security_groups']}",
    "cluster_subnet_group_name": "{'description': ['which subnet to place the cluster'], 'aliases': ['subnet']}",
    "cluster_type": "{'description': ['The type of cluster.'], 'choices': ['multi-node', 'single-node'], 'default': 'single-node'}",
    "cluster_version": "{'description': ['which version the cluster should have'], 'aliases': ['version'], 'choices': ['1.0']}",
    "command": "{'description': ['Specifies the action to take.'], 'required': True, 'choices': ['create', 'facts', 'delete', 'modify']}",
    "db_name": "{'description': ['Name of the database.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "elastic_ip": "{'description': ['if the cluster has an elastic IP or not']}",
    "encrypted": "{'description': ['if the cluster is encrypted or not'], 'default': 'no'}",
    "final_cluster_snapshot_identifier": "{'description': ['identifier of the final snapshot to be created before deleting the cluster. If this parameter is provided, final_cluster_snapshot_identifier must be false. Used only when command=delete.'], 'aliases': ['final_snapshot_id'], 'version_added': '2.4'}",
    "identifier": "{'description': ['Redshift cluster identifier.'], 'required': True}",
    "new_cluster_identifier": "{'description': ['Only used when command=modify.'], 'aliases': ['new_identifier']}",
    "node_type": "{'description': ['The node type of the cluster. Must be specified when command=create.'], 'choices': ['ds1.xlarge', 'ds1.8xlarge', 'ds2.xlarge', 'ds2.8xlarge', 'dc1.large', 'dc1.8xlarge', 'dc2.large', 'dc2.8xlarge', 'dw1.xlarge', 'dw1.8xlarge', 'dw2.large', 'dw2.8xlarge']}",
    "number_of_nodes": "{'description': ['Number of nodes. Only used when cluster_type=multi-node.']}",
    "password": "{'description': ['Master database password. Used only when command=create.']}",
    "port": "{'description': ['which port the cluster is listining']}",
    "preferred_maintenance_window": "{'description': ['maintenance window'], 'aliases': ['maintance_window', 'maint_window']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "publicly_accessible": "{'description': ['if the cluster is accessible publicly or not'], 'default': 'no'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "skip_final_cluster_snapshot": "{'description': ['skip a final snapshot before deleting the cluster. Used only when command=delete.'], 'aliases': ['skip_final_snapshot'], 'default': 'no', 'version_added': '2.4'}",
    "username": "{'description': ['Master database username. Used only when command=create.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_security_group_ids": "{'description': ['VPC security group'], 'aliases': ['vpc_security_groups']}",
    "wait": "{'description': ["When command=create, modify or restore then wait for the database to enter the 'available' state. When command=delete wait for the database to be terminated."], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

# Basic cluster provisioning example
- redshift: >
    command=create
    node_type=ds1.xlarge
    identifier=new_cluster
    username=cluster_admin
    password=1nsecure

# Cluster delete example
- redshift:
    command: delete
    identifier: new_cluster
    skip_final_cluster_snapshot: true
    wait: true

```

## License

TODO

## Author Information
  - ['Jens Carl (@j-carl), Hothead Games Inc.']
