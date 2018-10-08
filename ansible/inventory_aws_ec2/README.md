# Ansible inventory: ansible.inventory_aws_ec2


ec2 inventory source

## Description

Get inventory hosts from Amazon Web Services EC2.
Uses a <name>.aws_ec2.yaml (or <name>.aws_ec2.yml) YAML configuration file.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key_id": "{'description': ["The AWS access key to use. If you have specified a profile, you don't need to provide an access key/secret key/session token."], 'env': [{'name': 'AWS_ACCESS_KEY_ID'}, {'name': 'AWS_ACCESS_KEY'}, {'name': 'EC2_ACCESS_KEY'}]}",
    "aws_secret_access_key": "{'description': ["The AWS secret key that corresponds to the access key. If you have specified a profile, you don't need to provide an access key/secret key/session token."], 'env': [{'name': 'AWS_SECRET_ACCESS_KEY'}, {'name': 'AWS_SECRET_KEY'}, {'name': 'EC2_SECRET_KEY'}]}",
    "aws_security_token": "{'description': ['The AWS security token if using temporary access and secret keys.'], 'env': [{'name': 'AWS_SECURITY_TOKEN'}, {'name': 'AWS_SESSION_TOKEN'}, {'name': 'EC2_SECURITY_TOKEN'}]}",
    "boto_profile": "{'description': ['The boto profile to use.'], 'env': [{'name': 'AWS_PROFILE'}, {'name': 'AWS_DEFAULT_PROFILE'}]}",
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "filters": "{'description': ['A dictionary of filter value pairs. Available filters are listed here U(http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options)']}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "hostnames": "{'description': ['A list in order of precedence for hostname variables. You can use the options specified in U(http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options). To use tags as hostnames use the syntax tag:Name=Value to use the hostname Name_Value, or tag:Name to use the value of the Name tag.']}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'aws_ec2' plugin."], 'required': True, 'choices': ['aws_ec2']}",
    "regions": "{'description': ['A list of regions in which to describe EC2 instances. By default this is all regions except us-gov-west-1 and cn-north-1.']}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
    "strict_permissions": "{'description': ['By default if a 403 (Forbidden) is encountered this plugin will fail. You can set strict_permissions to False in the inventory config file which will allow 403 errors to be gracefully skipped.']}",
}
```

## Examples


``` yaml


# Minimal example using environment vars or instance role credentials
# Fetch all hosts in us-east-1, the hostname is the public DNS if it exists, otherwise the private IP address
plugin: aws_ec2
regions:
  - us-east-1

# Example using filters, ignoring permission errors, and specifying the hostname precedence
plugin: aws_ec2
boto_profile: aws_profile
regions: # populate inventory with instances in these regions
  - us-east-1
  - us-east-2
filters:
  # all instances with their `Environment` tag set to `dev`
  tag:Environment: dev
  # all dev and QA hosts
  tag:Environment:
    - dev
    - qa
  instance.group-id: sg-xxxxxxxx
# ignores 403 errors rather than failing
strict_permissions: False
# note: I(hostnames) sets the inventory_hostname. To modify ansible_host without modifying
# inventory_hostname use compose (see example below).
hostnames:
  - tag:Name=Tag1,Name=Tag2  # return specific hosts only
  - tag:CustomDNSName
  - dns-name
  - private-ip-address

# Example using constructed features to create groups and set ansible_host
plugin: aws_ec2
regions:
  - us-east-1
  - us-west-1
# keyed_groups may be used to create custom groups
strict: False
keyed_groups:
  # add e.g. x86_64 hosts to an arch_x86_64 group
  - prefix: arch
    key: 'architecture'
  # add hosts to tag_Name_Value groups for each Name/Value tag pair
  - prefix: tag
    key: tags
  # add hosts to e.g. instance_type_z3_tiny
  - prefix: instance_type
    key: instance_type
  # create security_groups_sg_abcd1234 group for each SG
  - key: 'security_groups|json_query("[].group_id")'
    prefix: 'security_groups'
  # create a group for each value of the Application tag
  - key: tags.Application
    separator: ''
  # create a group per region e.g. aws_region_us_east_2
  - key: placement.region
    prefix: aws_region
# set individual variables with compose
compose:
  # use the private IP address to connect to the host
  # (note: this does not modify inventory_hostname, which is set via I(hostnames))
  ansible_host: private_ip_address

```

## License

TODO

## Author Information
  - ['UNKNOWN']
