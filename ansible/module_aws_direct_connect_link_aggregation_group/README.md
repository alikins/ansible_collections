# Ansible module: ansible.module_aws_direct_connect_link_aggregation_group


Manage Direct Connect LAG bundles

## Description

Create, delete, or modify a Direct Connect link aggregation group.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bandwidth": "{'description': ['The bandwidth of the link aggregation group.']}",
    "connection_id": "{'description': ['A connection ID to link with the link aggregation group upon creation.']}",
    "delete_with_disassociation": "{'description': ['To be used with I(state=absent) to delete connections after disassociating them with the LAG.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "force_delete": "{'description': ['This allows the minimum number of links to be set to 0, any hosted connections disassociated, and any virtual interfaces associated to the LAG deleted.']}",
    "link_aggregation_group_id": "{'description': ['The ID of the Direct Connect link aggregation group.']}",
    "location": "{'description': ['The location of the link aggregation group.']}",
    "min_links": "{'description': ['The minimum number of physical connections that must be operational for the LAG itself to be operational.']}",
    "name": "{'description': ['The name of the Direct Connect link aggregation group.']}",
    "num_connections": "{'description': ['The number of connections with which to intialize the link aggregation group.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The state of the Direct Connect link aggregation group.'], 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Whether or not to wait for the operation to complete. May be useful when waiting for virtual interfaces to be deleted. May modify the time of waiting with C(wait_timeout).'], 'type': 'bool'}",
    "wait_timeout": "{'description': ['The duration in seconds to wait if I(wait) is True.'], 'default': 120}",
}
```

## Examples


``` yaml


# create a Direct Connect connection
- aws_direct_connect_link_aggregation_group:
  state: present
  location: EqDC2
  lag_id: dxlag-xxxxxxxx
  bandwidth: 1Gbps


```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
