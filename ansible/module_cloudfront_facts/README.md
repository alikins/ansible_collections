# Ansible module: ansible.module_cloudfront_facts


Obtain facts about an AWS CloudFront distribution

## Description

Gets information about an AWS CloudFront distribution

## Requirements

TODO

## Arguments

``` json
{
    "all_lists": "{'description': ['Get all cloudfront lists that do not require parameters.'], 'required': False, 'default': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "distribution": "{'description': ['Get information about a distribution. Requires I(distribution_id) or I(domain_name_alias) to be specified.'], 'required': False, 'default': False}",
    "distribution_config": "{'description': ['Get the configuration information about a distribution. Requires I(distribution_id) or I(domain_name_alias) to be specified.'], 'required': False, 'default': False}",
    "distribution_id": "{'description': ['The id of the CloudFront distribution. Used with I(distribution), I(distribution_config), I(invalidation), I(streaming_distribution), I(streaming_distribution_config), I(list_invalidations).'], 'required': False}",
    "domain_name_alias": "{'description': ['Can be used instead of I(distribution_id) - uses the aliased CNAME for the cloudfront distribution to get the distribution id where required.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "invalidation": "{'description': ['Get information about an invalidation. Requires I(invalidation_id) to be specified.'], 'required': False, 'default': False}",
    "invalidation_id": "{'description': ['The id of the invalidation to get information about. Used with I(invalidation).'], 'required': False}",
    "list_distributions": "{'description': ['Get a list of cloudfront distributions.'], 'required': False, 'default': False}",
    "list_distributions_by_web_acl_id": "{'description': ['Get a list of distributions using web acl id as a filter. Requires I(web_acl_id) to be set.'], 'required': False, 'default': False}",
    "list_invalidations": "{'description': ['Get a list of invalidations. Requires I(distribution_id) or I(domain_name_alias) to be specified.'], 'required': False, 'default': False}",
    "list_origin_access_identities": "{'description': ['Get a list of cloudfront origin access identities. Requires I(origin_access_identity_id) to be set.'], 'required': False, 'default': False}",
    "list_streaming_distributions": "{'description': ['Get a list of streaming distributions.'], 'required': False, 'default': False}",
    "origin_access_identity": "{'description': ['Get information about an origin access identity. Requires I(origin_access_identity_id) to be specified.'], 'required': False, 'default': False}",
    "origin_access_identity_config": "{'description': ['Get the configuration information about an origin access identity. Requires I(origin_access_identity_id) to be specified.'], 'required': False, 'default': False}",
    "origin_access_identity_id": "{'description': ['The id of the cloudfront origin access identity to get information about.'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "streaming_distribution": "{'description': ['Get information about a specified RTMP distribution. Requires I(distribution_id) or I(domain_name_alias) to be specified.'], 'required': False, 'default': False}",
    "streaming_distribution_config": "{'description': ['Get the configuration information about a specified RTMP distribution. Requires I(distribution_id) or I(domain_name_alias) to be specified.'], 'required': False, 'default': False}",
    "summary": "{'description': ['Returns a summary of all distributions, streaming distributions and origin_access_identities. This is the default behaviour if no option is selected.'], 'required': False, 'default': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "web_acl_id": "{'description': ['Used with I(list_distributions_by_web_acl_id).'], 'required': False}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Get a summary of distributions
- cloudfront_facts:
    summary: true

# Get information about a distribution
- cloudfront_facts:
    distribution: true
    distribution_id: my-cloudfront-distribution-id

# Get information about a distribution using the CNAME of the cloudfront distribution.
- cloudfront_facts:
    distribution: true
    domain_name_alias: www.my-website.com

# Facts are published in ansible_facts['cloudfront'][<distribution_name>]
- debug:
    msg: "{{ ansible_facts['cloudfront']['my-cloudfront-distribution-id'] }}"

- debug:
    msg: "{{ ansible_facts['cloudfront']['www.my-website.com'] }}"

# Get all information about an invalidation for a distribution.
- cloudfront_facts:
    invalidation: true
    distribution_id: my-cloudfront-distribution-id
    invalidation_id: my-cloudfront-invalidation-id

# Get all information about a cloudfront origin access identity.
- cloudfront_facts:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

# Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
- cloudfront_facts:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

# Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
- cloudfront_facts:
    all_lists: true

```

## License

TODO

## Author Information
  - ['Willem van Ketwich (@wilvk)']
