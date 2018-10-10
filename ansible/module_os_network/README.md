# Ansible module: ansible.module_os_network


Creates/removes networks from OpenStack

## Description

Add or remove network from OpenStack.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state_up": "{'description': ['Whether the state should be marked as up or down.'], 'type': 'bool', 'default': True}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "external": "{'description': ['Whether this network is externally accessible.'], 'type': 'bool', 'default': False}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Name to be assigned to the network.'], 'required': True}",
    "project": "{'description': ['Project name or ID containing the network (name admin-only)'], 'version_added': '2.1'}",
    "provider_network_type": "{'description': ['The type of physical network that maps to this network resource.'], 'version_added': '2.1'}",
    "provider_physical_network": "{'description': ['The physical network where this network object is implemented.'], 'version_added': '2.1'}",
    "provider_segmentation_id": "{'description': ['An isolated segment on the physical network. The I(network_type) attribute defines the segmentation model. For example, if the I(network_type) value is vlan, this ID is a vlan identifier. If the I(network_type) value is gre, this ID is a gre key.'], 'version_added': '2.1'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "shared": "{'description': ['Whether this network is shared or not.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Indicate desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create an externally accessible network named 'ext_network'.
- os_network:
    cloud: mycloud
    state: present
    name: ext_network
    external: true

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
