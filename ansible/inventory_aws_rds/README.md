# Ansible inventory: ansible.inventory_aws_rds


rds instance source

## Description

Get instances and clusters from Amazon Web Services RDS.
Uses a <name>.aws_rds.yaml (or <name>.aws_rds.yml) YAML configuration file.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key_id": "{'description': ["The AWS access key to use. If you have specified a profile, you don't need to provide an access key/secret key/session token."], 'env': [{'name': 'AWS_ACCESS_KEY_ID'}, {'name': 'AWS_ACCESS_KEY'}, {'name': 'EC2_ACCESS_KEY'}]}",
    "aws_secret_access_key": "{'description': ["The AWS secret key that corresponds to the access key. If you have specified a profile, you don't need to provide an access key/secret key/session token."], 'env': [{'name': 'AWS_SECRET_ACCESS_KEY'}, {'name': 'AWS_SECRET_KEY'}, {'name': 'EC2_SECRET_KEY'}]}",
    "aws_security_token": "{'description': ['The AWS security token if using temporary access and secret keys.'], 'env': [{'name': 'AWS_SECURITY_TOKEN'}, {'name': 'AWS_SESSION_TOKEN'}, {'name': 'EC2_SECURITY_TOKEN'}]}",
    "boto_profile": "{'description': ['The boto profile to use. The plugin will look for an instance role if no credentials are provided.'], 'env': [{'name': 'AWS_PROFILE'}, {'name': 'AWS_DEFAULT_PROFILE'}]}",
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "filters": "{'description': ['A dictionary of filter value pairs. Available filters are listed here U(https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html#options). If you filter by db-cluster-id and I(include_clusters) is True it will apply to clusters as well.'], 'default': {}}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "include_clusters": "{'description': ['Whether or not to query for Aurora clusters as well as instances'], 'type': 'bool', 'default': False}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "regions": "{'description': ['A list of regions in which to describe RDS instances and clusters. Available regions are listed here U(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)'], 'default': []}",
    "statuses": "{'description': ["A list of desired states for instances/clusters to be added to inventory. Set to ['all'] as a shorthand to find everything."], 'type': 'list', 'default': ['creating', 'available']}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
    "strict_permissions": "{'description': ['By default if an AccessDenied exception is encountered this plugin will fail. You can set strict_permissions to False in the inventory config file which will allow the restrictions to be gracefully skipped.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

plugin: aws_rds
regions:
  - us-east-1
  - ca-central-1
keyed_groups:
  - key: 'db_parameter_groups|json_query("[].db_parameter_group_name")'
    prefix: rds_parameter_group
  - key: engine
    prefix: rds
  - key: tags
  - key: region

```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
