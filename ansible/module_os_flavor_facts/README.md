# Ansible module: ansible.module_os_flavor_facts


Retrieve facts about one or more flavors

## Description

Retrieve facts about available OpenStack instance flavors. By default, facts about ALL flavors are retrieved. Filters can be applied to get facts for only matching flavors. For example, you can filter on the amount of RAM available to the flavor, or the number of virtual CPUs available to the flavor, or both. When specifying multiple filters, *ALL* filters must match on a flavor before that flavor is returned as a fact.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "ephemeral": "{'description': ['A string used for filtering flavors based on the amount of ephemeral storage. Format is the same as the I(ram) parameter'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "limit": "{'description': ['Limits the number of flavors returned. All matching flavors are returned by default.']}",
    "name": "{'description': ['A flavor name. Cannot be used with I(ram) or I(vcpus) or I(ephemeral).']}",
    "ram": "{'description': ["A string used for filtering flavors based on the amount of RAM (in MB) desired. This string accepts the following special values: 'MIN' (return flavors with the minimum amount of RAM), and 'MAX' (return flavors with the maximum amount of RAM).", 'A specific amount of RAM may also be specified. Any flavors with this exact amount of RAM will be returned.', "A range of acceptable RAM may be given using a special syntax. Simply prefix the amount of RAM with one of these acceptable range values: '<', '>', '<=', '>='. These values represent less than, greater than, less than or equal to, and greater than or equal to, respectively."], 'type': 'bool', 'default': False}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "vcpus": "{'description': ['A string used for filtering flavors based on the number of virtual CPUs desired. Format is the same as the I(ram) parameter.'], 'type': 'bool', 'default': False}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Gather facts about all available flavors
- os_flavor_facts:
    cloud: mycloud

# Gather facts for the flavor named "xlarge-flavor"
- os_flavor_facts:
    cloud: mycloud
    name: "xlarge-flavor"

# Get all flavors that have exactly 512 MB of RAM.
- os_flavor_facts:
    cloud: mycloud
    ram: "512"

# Get all flavors that have 1024 MB or more of RAM.
- os_flavor_facts:
    cloud: mycloud
    ram: ">=1024"

# Get a single flavor that has the minimum amount of RAM. Using the 'limit'
# option will guarantee only a single flavor is returned.
- os_flavor_facts:
    cloud: mycloud
    ram: "MIN"
    limit: 1

# Get all flavors with 1024 MB of RAM or more, AND exactly 2 virtual CPUs.
- os_flavor_facts:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"

# Get all flavors with 1024 MB of RAM or more, exactly 2 virtual CPUs, and
# less than 30gb of ephemeral storage.
- os_flavor_facts:
    cloud: mycloud
    ram: ">=1024"
    vcpus: "2"
    ephemeral: "<30"

```

## License

TODO

## Author Information
  - ['David Shrewsbury (@Shrews)']
