# Ansible module: ansible.module_cloudfront_distribution


create, update and delete aws cloudfront distributions

## Description

Allows for easy creation, updating and deletion of CloudFront distributions.

## Requirements

TODO

## Arguments

``` json
{
    "alias": "{'description': ['The name of an alias (CNAME) that is used in a distribution. This is used to effectively reference a distribution by its alias as an alias can only be used by one distribution per AWS account. This variable avoids having to provide the I(distribution_id) as well as the I(e_tag), or I(caller_reference) of an existing distribution.']}",
    "aliases": "{'description': ['A I(list[]) of domain name aliases (CNAMEs) as strings to be used for the distribution. Each alias must be unique across all distribution for the AWS account.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cache_behaviors": "{'description': ['A config element that is a I(list[]) of complex cache behavior objects to be specified for the distribution. The order of the list is preserved across runs unless C(purge_cache_behavior) is enabled. Each cache behavior comprises the attributes I(path_pattern) I(target_origin_id) I(forwarded_values) I(query_string) I(cookies) I(forward) I(whitelisted_names) I(headers[]) I(query_string_cache_keys[]) I(trusted_signers) I(enabled) I(items[]) I(viewer_protocol_policy) I(min_ttl) I(allowed_methods) I(items[]) I(cached_methods[]) I(smooth_streaming) I(default_ttl) I(max_ttl) I(compress) I(lambda_function_associations[]) I(field_level_encryption_id)']}",
    "caller_reference": "{'description': ["A unique identifier for creating and updating cloudfront distributions. Each caller reference must be unique across all distributions. e.g. a caller reference used in a web distribution cannot be reused in a streaming distribution. This parameter can be used instead of I(distribution_id) to reference an existing distribution. If not specified, this defaults to a datetime stamp of the format 'YYYY-MM-DDTHH:MM:SS.ffffff'."]}",
    "comment": "{'description': ['A comment that describes the cloudfront distribution. If not specified, it defaults to a generic message that it has been created with Ansible, and a datetime stamp.']}",
    "custom_error_responses": "{'description': ['A config element that is a I(list[]) of complex custom error responses to be specified for the distribution. This attribute configures custom http error messages returned to the user. Each custom error response object comprises the attributes I(error_code) I(reponse_page_path) I(response_code) I(error_caching_min_ttl)']}",
    "default_cache_behavior": "{'description': ['A config element that is a complex object specifying the default cache behavior of the distribution. If not specified, the I(target_origin_id) is defined as the I(target_origin_id) of the first valid I(cache_behavior) in I(cache_behaviors) with defaults. The default cache behavior comprises the attributes I(target_origin_id) I(forwarded_values) I(query_string) I(cookies) I(forward) I(whitelisted_names) I(headers[]) I(query_string_cache_keys[]) I(trusted_signers) I(enabled) I(items[]) I(viewer_protocol_policy) I(min_ttl) I(allowed_methods) I(items[]) I(cached_methods[]) I(smooth_streaming) I(default_ttl) I(max_ttl) I(compress) I(lambda_function_associations[]) I(lambda_function_arn) I(event_type) I(field_level_encryption_id)']}",
    "default_origin_domain_name": "{'description': ['The domain name to use for an origin if no I(origins) have been specified. Should only be used on a first run of generating a distribution and not on subsequent runs. Should not be used in conjunction with I(distribution_id), I(caller_reference) or I(alias).']}",
    "default_origin_path": "{'description': ['The default origin path to specify for an origin if no I(origins) have been specified. Defaults to empty if not specified.']}",
    "default_root_object": "{'description': ["A config element that specifies the path to request when the user requests the origin. e.g. if specified as 'index.html', this maps to www.example.com/index.html when www.example.com is called by the user. This prevents the entire distribution origin from being exposed at the root."]}",
    "distribution_id": "{'description': ['The id of the cloudfront distribution. This parameter can be exchanged with I(alias) or I(caller_reference) and is used in conjunction with I(e_tag).']}",
    "e_tag": "{'description': ['A unique identifier of a modified or existing distribution. Used in conjunction with I(distribution_id). Is determined automatically if not specified.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "enabled": "{'description': ['A boolean value that specifies whether the distribution is enabled or disabled.'], 'default': True, 'type': 'bool'}",
    "http_version": "{'description': ['The version of the http protocol to use for the distribution.'], 'choices': ['http1.1', 'http2'], 'default': "aws defaults this to 'http2'"}",
    "ipv6_enabled": "{'description': ['Determines whether IPv6 support is enabled or not.'], 'type': 'bool', 'default': False}",
    "logging": "{'description': ['A config element that is a complex object that defines logging for the distribution. The logging object comprises the attributes I(enabled) I(include_cookies) I(bucket) I(prefix)']}",
    "origins": "{'description': ['A config element that is a I(list[]) of complex origin objects to be specified for the distribution. Used for creating and updating distributions. Each origin item comprises the attributes I(id) I(domain_name) (defaults to default_origin_domain_name if not specified) I(origin_path) (defaults to default_origin_path if not specified) I(custom_headers[]) I(header_name) I(header_value) I(s3_origin_access_identity_enabled) I(custom_origin_config) I(http_port) I(https_port) I(origin_protocol_policy) I(origin_ssl_protocols[]) I(origin_read_timeout) I(origin_keepalive_timeout)']}",
    "price_class": "{'description': ['A string that specifies the pricing class of the distribution. As per U(https://aws.amazon.com/cloudfront/pricing/) I(price_class=PriceClass_100) consists of the areas United States Canada Europe I(price_class=PriceClass_200) consists of the areas United States Canada Europe Hong Kong, Philippines, S. Korea, Singapore & Taiwan Japan India I(price_class=PriceClass_All) consists of the areas United States Canada Europe Hong Kong, Philippines, S. Korea, Singapore & Taiwan Japan India South America Australia'], 'choices': ['PriceClass_100', 'PriceClass_200', 'PriceClass_All'], 'default': "aws defaults this to 'PriceClass_All'"}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_aliases": "{'description': ['Specifies whether existing aliases will be removed before adding new aliases. When I(purge_aliases=yes), existing aliases are removed and I(aliases) are added.'], 'default': False, 'type': 'bool'}",
    "purge_cache_behaviors": "{'description': ["Whether to remove any cache behaviors that aren't listed in I(cache_behaviors). This switch also allows the reordering of cache_behaviors."], 'default': False}",
    "purge_custom_error_responses": "{'description': ["Whether to remove any custom error responses that aren't listed in I(custom_error_responses)"], 'default': False}",
    "purge_origins": "{'description': ["Whether to remove any origins that aren't listed in I(origins)"], 'default': False}",
    "purge_tags": "{'description': ['Specifies whether existing tags will be removed before adding new tags. When I(purge_tags=yes), existing tags are removed and I(tags) are added, if specified. If no tags are specified, it removes all existing tags for the distribution. When I(purge_tags=no), existing tags are kept and I(tags) are added, if specified.'], 'default': False, 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "restrictions": "{'description': ["A config element that is a complex object that describes how a distribution should restrict it's content. The restriction object comprises the following attributes I(geo_restriction) I(restriction_type) I(items[])"]}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The desired state of the distribution present - creates a new distribution or updates an existing distribution. absent - deletes an existing distribution.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tags": "{'description': ['Should be input as a dict() of key-value pairs. Note that numeric keys or values must be wrapped in quotes. e.g. "Priority:" \'1\'']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "viewer_certificate": "{'description': ['A config element that is a complex object that specifies the encryption details of the distribution. Comprises the following attributes I(cloudfront_default_certificate) I(iam_certificate_id) I(acm_certificate_arn) I(ssl_support_method) I(minimum_protocol_version) I(certificate) I(certificate_source)']}",
    "wait": "{'description': ['Specifies whether the module waits until the distribution has completed processing the creation or update.'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['Specifies the duration in seconds to wait for a timeout of a cloudfront create or update. Defaults to 1800 seconds (30 minutes).'], 'default': 1800}",
    "web_acl_id": "{'description': ['The id of a Web Application Firewall (WAF) Access Control List (ACL).']}",
}
```

## Examples


``` yaml


# create a basic distribution with defaults and tags

- cloudfront_distribution:
    state: present
    default_origin_domain_name: www.my-cloudfront-origin.com
    tags:
      Name: example distribution
      Project: example project
      Priority: '1'

# update a distribution comment by distribution_id

- cloudfront_distribution:
    state: present
    distribution_id: E1RP5A2MJ8073O
    comment: modified by ansible cloudfront.py

# update a distribution comment by caller_reference

- cloudfront_distribution:
    state: present
    caller_reference: my cloudfront distribution 001
    comment: modified by ansible cloudfront.py

# update a distribution's aliases and comment using the distribution_id as a reference

- cloudfront_distribution:
    state: present
    distribution_id: E1RP5A2MJ8073O
    comment: modified by cloudfront.py again
    aliases: [ 'www.my-distribution-source.com', 'zzz.aaa.io' ]

# update a distribution's aliases and comment using an alias as a reference

- cloudfront_distribution:
    state: present
    caller_reference: my test distribution
    comment: modified by cloudfront.py again
    aliases:
      - www.my-distribution-source.com
      - zzz.aaa.io

# update a distribution's comment and aliases and tags and remove existing tags

- cloudfront_distribution:
    state: present
    distribution_id: E15BU8SDCGSG57
    comment: modified by cloudfront.py again
    aliases:
      - tested.com
    tags:
      Project: distribution 1.2
    purge_tags: yes

# create a distribution with an origin, logging and default cache behavior

- cloudfront_distribution:
    state: present
    caller_reference: unique test distribution id
    origins:
        - id: 'my test origin-000111'
          domain_name: www.example.com
          origin_path: /production
          custom_headers:
            - header_name: MyCustomHeaderName
              header_value: MyCustomHeaderValue
    default_cache_behavior:
      target_origin_id: 'my test origin-000111'
      forwarded_values:
        query_string: true
        cookies:
          forward: all
        headers:
         - '*'
      viewer_protocol_policy: allow-all
      smooth_streaming: true
      compress: true
      allowed_methods:
        items:
          - GET
          - HEAD
        cached_methods:
          - GET
          - HEAD
    logging:
      enabled: true
      include_cookies: false
      bucket: mylogbucket.s3.amazonaws.com
      prefix: myprefix/
    enabled: false
    comment: this is a cloudfront distribution with logging

# delete a distribution

- cloudfront_distribution:
    state: absent
    caller_reference: replaceable distribution

```

## License

TODO

## Author Information
  - ['Willem van Ketwich (@wilvk)', 'Will Thames (@willthames)']
  - ['Willem van Ketwich (@wilvk)', 'Will Thames (@willthames)']
