# Ansible module: ansible.module_route53_health_check


add or delete health-checks in Amazons Route53 DNS service

## Description

Creates and deletes DNS Health checks in Amazons Route53 service
Only the port, resource_path, string_match and request_interval are considered when updating existing health-checks.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "failure_threshold": "{'description': ['The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.'], 'required': True, 'default': 3, 'choices': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}",
    "fqdn": "{'description': ['Domain name of the endpoint to check. Either this or `ip_address` has to be provided. When both are given the `fqdn` is used in the `Host:` header of the HTTP request.']}",
    "ip_address": "{'description': ['IP address of the end-point to check. Either this or `fqdn` has to be provided.']}",
    "port": "{'description': ['The port on the endpoint on which you want Amazon Route 53 to perform health checks. Required for TCP checks.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "request_interval": "{'description': ['The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.'], 'required': True, 'default': 30, 'choices': [10, 30]}",
    "resource_path": "{'description': ['The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.', 'Required for all checks except TCP.', 'The path must begin with a /', 'Maximum 255 characters.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Specifies the action to take.'], 'required': True, 'choices': ['present', 'absent']}",
    "string_match": "{'description': ['If the check type is HTTP_STR_MATCH or HTTP_STR_MATCH, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the first 5120 bytes of the response body, Amazon Route 53 considers the resource healthy.']}",
    "type": "{'description': ['The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.'], 'required': True, 'choices': ['HTTP', 'HTTPS', 'HTTP_STR_MATCH', 'HTTPS_STR_MATCH', 'TCP']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create a health-check for host1.example.com and use it in record
- route53_health_check:
    state: present
    fqdn: host1.example.com
    type: HTTP_STR_MATCH
    resource_path: /
    string_match: "Hello"
    request_interval: 10
    failure_threshold: 2
  register: my_health_check

- route53:
    action: create
    zone: "example.com"
    type: CNAME
    record: "www.example.com"
    value: host1.example.com
    ttl: 30
    # Routing policy
    identifier: "host1@www"
    weight: 100
    health_check: "{{ my_health_check.health_check.id }}"

# Delete health-check
- route53_health_check:
    state: absent
    fqdn: host1.example.com


```

## License

TODO

## Author Information
  - ['zimbatm (@zimbatm)']
