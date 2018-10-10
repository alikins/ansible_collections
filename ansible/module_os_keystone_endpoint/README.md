# Ansible module: ansible.module_os_keystone_endpoint


Manage OpenStack Identity service endpoints

## Description

Create, update, or delete OpenStack Identity service endpoints. If a service with the same combination of I(service), I(interface) and I(region) exist, the I(url) and I(state) (C(present) or C(absent)) will be updated.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "enabled": "{'description': ['Is the service enabled.'], 'default': True}",
    "interface": "{'description': ['Interface of the service.'], 'choices': ['admin', 'public', 'internal'], 'required': True, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "region": "{'description': ['Region that the service belongs to. Note that I(region_name) is used for authentication.']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "service": "{'description': ['Name or id of the service.'], 'required': True}",
    "state": "{'description': ['Should the resource be C(present) or C(absent).'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "url": "{'description': ['URL of the service.'], 'required': True}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

- name: Create a service for glance
  os_keystone_endpoint:
     cloud: mycloud
     service: glance
     endpoint_interface: public
     url: http://controller:9292
     region: RegionOne
     state: present

- name: Delete a service for nova
  os_keystone_endpoint:
     cloud: mycloud
     service: nova
     endpoint_interface: public
     region: RegionOne
     state: absent

```

## License

TODO

## Author Information
  - ['Mohammed Naser (@mnaser)', 'Alberto Murillo (@albertomurillo)']
  - ['Mohammed Naser (@mnaser)', 'Alberto Murillo (@albertomurillo)']
