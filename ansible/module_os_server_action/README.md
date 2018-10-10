# Ansible module: ansible.module_os_server_action


Perform actions on Compute Instances from OpenStack

## Description

Perform server actions on an existing compute instance from OpenStack. This module does not return any data other than changed true/false. When I(action) is 'rebuild', then I(image) parameter is required.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Perform the given action. The lock and unlock actions always return changed as the servers API does not provide lock status.'], 'choices': ['stop', 'start', 'pause', 'unpause', 'lock', 'unlock', 'suspend', 'resume', 'rebuild'], 'default': 'present'}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "image": "{'description': ['Image the server should be rebuilt with'], 'version_added': '2.3'}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "server": "{'description': ['Name or ID of the instance'], 'required': True}",
    "timeout": "{'description': ['The amount of time the module should wait for the instance to perform the requested action.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['If the module should wait for the instance action to be performed.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Pauses a compute instance
- os_server_action:
      action: pause
      auth:
        auth_url: https://identity.example.com
        username: admin
        password: admin
        project_name: admin
      server: vm1
      timeout: 200

```

## License

TODO

## Author Information
  - ['Jesse Keating (@omgjlk)']
