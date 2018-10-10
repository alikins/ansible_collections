# Ansible module: ansible.module_os_member


Add/Delete a member for a pool in load balancer from OpenStack Cloud

## Description

Add or Remove a member for a pool from the OpenStack load-balancer service.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The IP address of the member.']}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Name that has to be given to the member'], 'required': True}",
    "pool": "{'description': ['The name or id of the pool that this member belongs to.'], 'required': True}",
    "protocol_port": "{'description': ['The protocol port number for the member.'], 'default': 80}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnet_id": "{'description': ['The subnet ID the member service is accessible from.']}",
    "timeout": "{'description': ['The amount of time the module should wait for the load balancer to get into ACTIVE state.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['If the module should wait for the load balancer to be ACTIVE.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a member, wait for the member to be created.
- os_member:
    cloud: mycloud
    endpoint_type: admin
    state: present
    name: test-member
    pool: test-pool
    address: 192.168.10.3
    protocol_port: 8080

# Delete a listener
- os_member:
    cloud: mycloud
    endpoint_type: admin
    state: absent
    name: test-member
    pool: test-pool

```

## License

TODO

## Author Information
  - ['Lingxian Kong (@lingxiankong)']
