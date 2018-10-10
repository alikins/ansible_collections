# Ansible module: ansible.module_ec2_vpc_vpn


Create, modify, and delete EC2 VPN connections

## Description

This module creates, modifies, and deletes VPN connections. Idempotence is achieved by using the filters option or specifying the VPN connection identifier.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "connection_type": "{'description': ['The type of VPN connection.'], 'choices': ['ipsec.1'], 'default': 'ipsec.1'}",
    "customer_gateway_id": "{'description': ['The ID of the customer gateway.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ["An alternative to using vpn_connection_id. If multiple matches are found, vpn_connection_id is required. If one of the following suboptions is a list of items to filter by, only one item needs to match to find the VPN that correlates. e.g. if the filter 'cidr' is ['194.168.2.0/24', '192.168.2.0/24'] and the VPN route only has the destination cidr block of '192.168.2.0/24' it will be found with this filter (assuming there are not multiple VPNs that are matched). Another example, if the filter 'vpn' is equal to ['vpn-ccf7e7ad', 'vpn-cb0ae2a2'] and one of of the VPNs has the state deleted (exists but is unmodifiable) and the other exists and is not deleted, it will be found via this filter. See examples."], 'suboptions': {'cgw-config': {'description': ['The customer gateway configuration of the VPN as a string (in the format of the return value) or a list of those strings.']}, 'static-routes-only': {'description': ['The type of routing; true or false.']}, 'cidr': {'description': ["The destination cidr of the VPN's route as a string or a list of those strings."]}, 'bgp': {'description': ['The BGP ASN number associated with a BGP device. Only works if the connection is attached. This filtering option is currently not working.']}, 'vpn': {'description': ['The VPN connection id as a string or a list of those strings.']}, 'vgw': {'description': ['The virtual private gateway as a string or a list of those strings.']}, 'tag-keys': {'description': ['The key of a tag as a string or a list of those strings.']}, 'tag-values': {'description': ['The value of a tag as a string or a list of those strings.']}, 'tags': {'description': ['A dict of key value pairs.']}, 'cgw': {'description': ['The customer gateway id as a string or a list of those strings.']}}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_routes": "{'description': ['Whether or not to delete VPN connections routes that are not specified in the task.']}",
    "purge_tags": "{'description': ['Whether or not to delete VPN connections tags that are associated with the connection but not specified in the task.'], 'type': 'bool', 'default': False}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "routes": "{'description': ['Routes to add to the connection.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The desired state of the VPN connection.'], 'choices': ['present', 'absent'], 'default': 'present', 'required': False}",
    "static_only": "{'description': ["Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP."], 'default': False, 'required': False}",
    "tags": "{'description': ['Tags to attach to the VPN connection.']}",
    "tunnel_options": "{'description': ["An optional list object containing no more than two dict members, each of which may contain 'TunnelInsideCidr' and/or 'PreSharedKey' keys with appropriate string values.  AWS defaults will apply in absence of either of the aforementioned keys."], 'required': False, 'version_added': '2.5'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpn_connection_id": "{'description': ['The ID of the VPN connection. Required to modify or delete a connection if the filters option does not provide a unique match.']}",
    "vpn_gateway_id": "{'description': ['The ID of the virtual private gateway.']}",
}
```

## Examples


``` yaml

# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

- name: create a VPN connection
  ec2_vpc_vpn:
    state: present
    vpn_gateway_id: vgw-XXXXXXXX
    customer_gateway_id: cgw-XXXXXXXX

- name: modify VPN connection tags
  ec2_vpc_vpn:
    state: present
    vpn_connection_id: vpn-XXXXXXXX
    tags:
      Name: ansible-tag-1
      Other: ansible-tag-2

- name: delete a connection
  ec2_vpc_vpn:
    vpn_connection_id: vpn-XXXXXXXX
    state: absent

- name: modify VPN tags (identifying VPN by filters)
  ec2_vpc_vpn:
    state: present
    filters:
      cidr: 194.168.1.0/24
      tag-keys:
        - Ansible
        - Other
    tags:
      New: Tag
    purge_tags: true
    static_only: true

- name: set up VPN with tunnel options utilizing 'TunnelInsideCidr' only
  ec2_vpc_vpn:
    state: present
    filters:
      vpn: vpn-XXXXXXXX
    static_only: true
    tunnel_options:
      -
        TunnelInsideCidr: '169.254.100.1/30'
      -
        TunnelInsideCidr: '169.254.100.5/30'

- name: add routes and remove any preexisting ones
  ec2_vpc_vpn:
    state: present
    filters:
      vpn: vpn-XXXXXXXX
    routes:
      - 195.168.2.0/24
      - 196.168.2.0/24
    purge_routes: true

- name: remove all routes
  ec2_vpc_vpn:
    state: present
    vpn_connection_id: vpn-XXXXXXXX
    routes: []
    purge_routes: true

- name: delete a VPN identified by filters
  ec2_vpc_vpn:
    state: absent
    filters:
      tags:
        Ansible: Tag

```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
