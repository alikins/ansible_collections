# Ansible module: ansible.module_aws_waf_condition


create and delete WAF Conditions

## Description

Read the AWS documentation for WAF U(https://aws.amazon.com/documentation/waf/)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A list of the filters against which to match', 'For I(type)=C(byte), valid keys are C(field_to_match), C(position), C(header), C(transformation)', 'For I(type)=C(geo), the only valid key is C(country)', 'For I(type)=C(ip), the only valid key is C(ip_address)', 'For I(type)=C(regex), valid keys are C(field_to_match), C(transformation) and C(regex_pattern)', 'For I(type)=C(size), valid keys are C(field_to_match), C(transformation), C(comparison) and C(size)', 'For I(type)=C(sql), valid keys are C(field_to_match) and C(transformation)', 'For I(type)=C(xss), valid keys are C(field_to_match) and C(transformation)', 'I(field_to_match) can be one of C(uri), C(query_string), C(header) C(method) and C(body)', 'If I(field_to_match) is C(header), then C(header) must also be specified', 'I(transformation) can be one of C(none), C(compress_white_space), C(html_entity_decode), C(lowercase), C(cmd_line), C(url_decode)', 'I(position), can be one of C(exactly), C(starts_with), C(ends_with), C(contains), C(contains_word),', 'I(comparison) can be one of C(EQ), C(NE), C(LE), C(LT), C(GE), C(GT),', 'I(target_string) is a maximum of 50 bytes', 'I(regex_pattern) is a dict with a C(name) key and C(regex_strings) list of strings to match']}",
    "name": "{'description': ['Name of the Web Application Firewall condition to manage'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_filters": "{'description': ['Whether to remove existing filters from a condition if not passed in I(filters). Defaults to false']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether the condition should be C(present) or C(absent)'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['the type of matching to perform'], 'choices': ['byte', 'geo', 'ip', 'regex', 'size', 'sql', 'xss']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

  - name: create WAF byte condition
    aws_waf_condition:
      name: my_byte_condition
      filters:
      - field_to_match: header
        position: STARTS_WITH
        target_string: Hello
        header: Content-type
      type: byte

  - name: create WAF geo condition
    aws_waf_condition:
      name: my_geo_condition
      filters:
        - country: US
        - country: AU
        - country: AT
      type: geo

  - name: create IP address condition
    aws_waf_condition:
      name: "{{ resource_prefix }}_ip_condition"
      filters:
        - ip_address: "10.0.0.0/8"
        - ip_address: "192.168.0.0/24"
      type: ip

  - name: create WAF regex condition
    aws_waf_condition:
      name: my_regex_condition
      filters:
        - field_to_match: query_string
          regex_pattern:
            name: greetings
            regex_strings:
              - '[hH]ello'
              - '^Hi there'
              - '.*Good Day to You'
      type: regex

  - name: create WAF size condition
    aws_waf_condition:
      name: my_size_condition
      filters:
        - field_to_match: query_string
          size: 300
          comparison: GT
      type: size

  - name: create WAF sql injection condition
    aws_waf_condition:
      name: my_sql_condition
      filters:
        - field_to_match: query_string
          transformation: url_decode
      type: sql

  - name: create WAF xss condition
    aws_waf_condition:
      name: my_xss_condition
      filters:
        - field_to_match: query_string
          transformation: url_decode
      type: xss


```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)', 'Mike Mochan (@mmochan)']
  - ['Will Thames (@willthames)', 'Mike Mochan (@mmochan)']
