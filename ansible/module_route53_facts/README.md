# Ansible module: ansible.module_route53_facts


Retrieves route53 details using AWS methods

## Description

Gets various details related to Route53 zone, record set or health check details

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "change_id": "{'description': ['The ID of the change batch request. The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.'], 'required': False}",
    "delegation_set_id": "{'description': ['The DNS Zone delegation set ID'], 'required': False}",
    "dns_name": "{'description': ['The first name in the lexicographic ordering of domain names that you want the list_command to start listing from'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "health_check_id": "{'description': ['The ID of the health check'], 'required': False}",
    "health_check_method": "{'description': ['This is used in conjunction with query: health_check. It allows for listing details, counts or tags of various health check details.'], 'required': False, 'choices': ['list', 'details', 'status', 'failure_reason', 'count', 'tags'], 'default': 'list'}",
    "hosted_zone_id": "{'description': ['The Hosted Zone ID of the DNS zone'], 'required': False}",
    "hosted_zone_method": "{'description': ['This is used in conjunction with query: hosted_zone. It allows for listing details, counts or tags of various hosted zone details.'], 'required': False, 'choices': ['details', 'list', 'list_by_name', 'count', 'tags'], 'default': 'list'}",
    "max_items": "{'description': ['Maximum number of items to return for various get/list requests'], 'required': False}",
    "next_marker": "{'description': ['Some requests such as list_command: hosted_zones will return a maximum number of entries - EG 100 or the number specified by max_items. If the number of entries exceeds this maximum another request can be sent using the NextMarker entry from the first response to get the next page of results'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "query": "{'description': ['specifies the query action to take'], 'required': True, 'choices': ['change', 'checker_ip_range', 'health_check', 'hosted_zone', 'record_sets', 'reusable_delegation_set']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "resource_id": "{'description': ['The ID/s of the specified resource/s'], 'required': False, 'aliases': ['resource_ids']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "start_record_name": "{'description': ['The first name in the lexicographic ordering of domain names that you want the list_command: record_sets to start listing from'], 'required': False}",
    "type": "{'description': ['The type of DNS record'], 'required': False, 'choices': ['A', 'CNAME', 'MX', 'AAAA', 'TXT', 'PTR', 'SRV', 'SPF', 'CAA', 'NS']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Simple example of listing all hosted zones
- name: List all hosted zones
  route53_facts:
    query: hosted_zone
  register: hosted_zones

# Getting a count of hosted zones
- name: Return a count of all hosted zones
  route53_facts:
    query: hosted_zone
    hosted_zone_method: count
  register: hosted_zone_count

- name: List the first 20 resource record sets in a given hosted zone
  route53_facts:
    profile: account_name
    query: record_sets
    hosted_zone_id: ZZZ1111112222
    max_items: 20
  register: record_sets

- name: List first 20 health checks
  route53_facts:
    query: health_check
    health_check_method: list
    max_items: 20
  register: health_checks

- name: Get health check last failure_reason
  route53_facts:
    query: health_check
    health_check_method: failure_reason
    health_check_id: 00000000-1111-2222-3333-12345678abcd
  register: health_check_failure_reason

- name: Retrieve reusable delegation set details
  route53_facts:
    query: reusable_delegation_set
    delegation_set_id: delegation id
  register: delegation_sets

- name: setup of example for using next_marker
  route53_facts:
    query: hosted_zone
    max_items: 1
  register: first_facts

- name: example for using next_marker
  route53_facts:
    query: hosted_zone
    next_marker: "{{ first_facts.NextMarker }}"
    max_items: 1
  when: "{{ 'NextMarker' in first_facts }}"

```

## License

TODO

## Author Information
  - ['Karen Cheng (@Etherdaemon)']
