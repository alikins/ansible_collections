# Ansible module: ansible.module_os_user


Manage OpenStack Identity Users

## Description

Manage OpenStack Identity users. Users can be created, updated or deleted using this module. A user will be updated if I(name) matches an existing user and I(state) is present. The value for I(name) cannot be updated without deleting and re-creating the user.

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
    "default_project": "{'description': ['Project name or ID that the user should be associated with by default']}",
    "description": "{'description': ['Description about the user'], 'version_added': '2.4'}",
    "domain": "{'description': ['Domain to create the user in if the cloud supports domains']}",
    "email": "{'description': ['Email address for the user']}",
    "enabled": "{'description': ['Is the user enabled'], 'type': 'bool', 'default': True}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Username for the user'], 'required': True}",
    "password": "{'description': ['Password for the user']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "update_password": "{'default': 'always', 'choices': ['always', 'on_create'], 'version_added': '2.3', 'description': ['C(always) will attempt to update password.  C(on_create) will only set the password for newly created users.']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a user
- os_user:
    cloud: mycloud
    state: present
    name: demouser
    password: secret
    email: demo@example.com
    domain: default
    default_project: demo

# Delete a user
- os_user:
    cloud: mycloud
    state: absent
    name: demouser

# Create a user but don't update password if user exists
- os_user:
    cloud: mycloud
    state: present
    name: demouser
    password: secret
    update_password: on_create
    email: demo@example.com
    domain: default
    default_project: demo

```

## License

TODO

## Author Information
  - ['David Shrewsbury']
