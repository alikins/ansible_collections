# Ansible module: ansible.module_os_zone


Manage OpenStack DNS zones

## Description

Manage OpenStack DNS zones. Zones can be created, deleted or updated. Only the I(email), I(description), I(ttl) and I(masters) values can be updated.

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
    "description": "{'description': ['Zone description']}",
    "email": "{'description': ['Email of the zone owner (only applies if zone_type is primary)']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "masters": "{'description': ['Master nameservers (only applies if zone_type is secondary)']}",
    "name": "{'description': ['Zone name'], 'required': True}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "ttl": "{'description': ['TTL (Time To Live) value in seconds']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
    "zone_type": "{'description': ['Zone type'], 'choices': ['primary', 'secondary']}",
}
```

## Examples


``` yaml

# Create a zone named "example.net"
- os_zone:
    cloud: mycloud
    state: present
    name: example.net.
    zone_type: primary
    email: test@example.net
    description: Test zone
    ttl: 3600

# Update the TTL on existing "example.net." zone
- os_zone:
    cloud: mycloud
    state: present
    name: example.net.
    ttl: 7200

# Delete zone named "example.net."
- os_zone:
    cloud: mycloud
    state: absent
    name: example.net.

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
