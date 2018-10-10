# Ansible module: ansible.module_ec2_vpc_dhcp_option


Manages DHCP Options, and can ensure the DHCP options for the given VPC match what's requested

## Description

This module removes, or creates DHCP option sets, and can associate them to a VPC. Optionally, a new DHCP Options set can be created that converges a VPC's existing DHCP option set with values provided. When dhcp_options_id is provided, the module will 1. remove (with state='absent') 2. ensure tags are applied (if state='present' and tags are provided 3. attach it to a VPC (if state='present' and a vpc_id is provided. If any of the optional values are missing, they will either be treated as a no-op (i.e., inherit what already exists for the VPC) To remove existing options while inheriting, supply an empty value (e.g. set ntp_servers to [] if you want to remove them from the VPC's options) Most of the options should be self-explanatory.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "delete_old": "{'description': ['Whether to delete the old VPC DHCP option set when associating a new one. This is primarily useful for debugging/development purposes when you want to quickly roll back to the old option set. Note that this setting will be ignored, and the old DHCP option set will be preserved, if it is in use by any other VPC. (Otherwise, AWS will return an error.)'], 'type': 'bool', 'default': True}",
    "dhcp_options_id": "{'description': ['The resource_id of an existing DHCP options set. If this is specified, then it will override other settings, except tags (which will be updated to match)'], 'version_added': '2.1'}",
    "dns_servers": "{'description': ['A list of hosts to set the DNS servers for the VPC to. (Should be a list of IP addresses rather than host names.)']}",
    "domain_name": "{'description': ['The domain name to set in the DHCP option sets']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "inherit_existing": "{'description': ['For any DHCP options not specified in these parameters, whether to inherit them from the options set already applied to vpc_id, or to reset them to be empty.'], 'type': 'bool', 'default': False}",
    "netbios_name_servers": "{'description': ['List of hosts to advertise as NetBIOS servers.']}",
    "netbios_node_type": "{'description': ['NetBIOS node type to advertise in the DHCP options. The AWS recommendation is to use 2 (when using netbios name services) http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html']}",
    "ntp_servers": "{'description': ['List of hosts to advertise as NTP servers for the VPC.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['create/assign or remove the DHCP options. If state is set to absent, then a DHCP options set matched either by id, or tags and options will be removed if possible.'], 'default': 'present', 'choices': ['absent', 'present'], 'version_added': '2.1'}",
    "tags": "{'description': ['Tags to be applied to a VPC options set if a new one is created, or if the resource_id is provided. (options must match)'], 'aliases': ['resource_tags'], 'version_added': '2.1'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['VPC ID to associate with the requested DHCP option set. If no vpc id is provided, and no matching option set is found then a new DHCP option set is created.']}",
}
```

## Examples


``` yaml

# Completely overrides the VPC DHCP options associated with VPC vpc-123456 and deletes any existing
# DHCP option set that may have been attached to that VPC.
- ec2_vpc_dhcp_option:
    domain_name: "foo.example.com"
    region: us-east-1
    dns_servers:
        - 10.0.0.1
        - 10.0.1.1
    ntp_servers:
        - 10.0.0.2
        - 10.0.1.2
    netbios_name_servers:
        - 10.0.0.1
        - 10.0.1.1
    netbios_node_type: 2
    vpc_id: vpc-123456
    delete_old: True
    inherit_existing: False


# Ensure the DHCP option set for the VPC has 10.0.0.4 and 10.0.1.4 as the specified DNS servers, but
# keep any other existing settings. Also, keep the old DHCP option set around.
- ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - "{{groups['dns-primary']}}"
      - "{{groups['dns-secondary']}}"
    vpc_id: vpc-123456
    inherit_existing: True
    delete_old: False


## Create a DHCP option set with 4.4.4.4 and 8.8.8.8 as the specified DNS servers, with tags
## but do not assign to a VPC
- ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - 4.4.4.4
      - 8.8.8.8
    tags:
      Name: google servers
      Environment: Test

## Delete a DHCP options set that matches the tags and options specified
- ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - 4.4.4.4
      - 8.8.8.8
    tags:
      Name: google servers
      Environment: Test
  state: absent

## Associate a DHCP options set with a VPC by ID
- ec2_vpc_dhcp_option:
    region: us-east-1
    dhcp_options_id: dopt-12345678
    vpc_id: vpc-123456


```

## License

TODO

## Author Information
  - ['Joel Thompson (@joelthompson)']
