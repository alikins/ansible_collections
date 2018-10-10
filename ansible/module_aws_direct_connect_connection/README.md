# Ansible module: ansible.module_aws_direct_connect_connection


Creates, deletes, modifies a DirectConnect connection

## Description

Create, update, or delete a Direct Connect connection between a network and a specific AWS Direct Connect location. Upon creation the connection may be added to a link aggregation group or established as a standalone connection. The connection may later be associated or disassociated with a link aggregation group.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bandwidth": "{'description': ['The bandwidth of the Direct Connect connection. Required when I(state=present).'], 'choices': ['1Gbps', '10Gbps']}",
    "connection_id": "{'description': ['The ID of the Direct Connect connection. I(name) or I(connection_id) is required to recreate or delete a connection. Modifying attributes of a connection with I(forced_update) will result in a new Direct Connect connection ID.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "forced_update": "{'description': ['To modify bandwidth or location the connection will need to be deleted and recreated. By default this will not happen - this option must be set to True.'], 'type': 'bool'}",
    "link_aggregation_group": "{'description': ['The ID of the link aggregation group you want to associate with the connection. This is optional in case a stand-alone connection is desired.']}",
    "location": "{'description': ['Where the Direct Connect connection is located. Required when I(state=present).']}",
    "name": "{'description': ['The name of the Direct Connect connection. This is required to create a new connection. To recreate or delete a connection I(name) or I(connection_id) is required.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The state of the Direct Connect connection.'], 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml


# create a Direct Connect connection
- aws_direct_connect_connection:
    name: ansible-test-connection
    state: present
    location: EqDC2
    link_aggregation_group: dxlag-xxxxxxxx
    bandwidth: 1Gbps
  register: dc

# disassociate the LAG from the connection
- aws_direct_connect_connection:
    state: present
    connection_id: dc.connection.connection_id
    location: EqDC2
    bandwidth: 1Gbps

# replace the connection with one with more bandwidth
- aws_direct_connect_connection:
    state: present
    name: ansible-test-connection
    location: EqDC2
    bandwidth: 10Gbps
    forced_update: True

# delete the connection
- aws_direct_connect_connection:
    state: absent
    name: ansible-test-connection

```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
