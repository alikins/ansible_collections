# Ansible module: ansible.module_aws_direct_connect_virtual_interface


Manage Direct Connect virtual interfaces

## Description

Create, delete, or modify a Direct Connect public or private virtual interface.

## Requirements

TODO

## Arguments

``` json
{
    "address_type": "{'description': ['The type of IP address for the BGP peer.']}",
    "amazon_address": "{'description': ['The amazon address CIDR with which to create the virtual interface.']}",
    "authentication_key": "{'description': ['The authentication key for BGP configuration.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bgp_asn": "{'description': ['The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.'], 'default': 65000}",
    "cidr": "{'description': ['A list of route filter prefix CIDRs with which to create the public virtual interface.']}",
    "customer_address": "{'description': ['The customer address CIDR with which to create the virtual interface.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "id_to_associate": "{'description': ['The ID of the link aggrecation group or connection to associate with the virtual interface.'], 'aliases': ['link_aggregation_group_id', 'connection_id']}",
    "name": "{'description': ['The name of the virtual interface.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "public": "{'description': ['The type of virtual interface.'], 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The desired state of the Direct Connect virtual interface.'], 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "virtual_gateway_id": "{'description': ['The virtual gateway ID required for creating a private virtual interface.']}",
    "virtual_interface_id": "{'description': ['The virtual interface ID.']}",
    "vlan": "{'description': ['The VLAN ID.'], 'default': 100}",
}
```

## Examples


``` yaml

---
- name: create an association between a LAG and connection
  aws_direct_connect_virtual_interface:
    state: present
    name: "{{ name }}"
    link_aggregation_group_id: LAG-XXXXXXXX
    connection_id: dxcon-XXXXXXXX

- name: remove an association between a connection and virtual interface
  aws_direct_connect_virtual_interface:
    state: absent
    connection_id: dxcon-XXXXXXXX
    virtual_interface_id: dxv-XXXXXXXX


```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
