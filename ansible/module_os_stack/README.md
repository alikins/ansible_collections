# Ansible module: ansible.module_os_stack


Add/Remove Heat Stack

## Description

Add or Remove a Stack to an OpenStack Heat

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
    "environment": "{'description': ['List of environment files that should be used for the stack creation']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Name of the stack that should be created, name could be char and digit, no space'], 'required': True}",
    "parameters": "{'description': ['Dictionary of parameters for the stack creation']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "rollback": "{'description': ['Rollback stack creation'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tag": "{'description': ['Tag for the stack that should be created, name could be char and digit, no space'], 'version_added': '2.5'}",
    "template": "{'description': ['Path of the template file to use for the stack creation']}",
    "timeout": "{'description': ['Maximum number of seconds to wait for the stack creation'], 'required': False, 'default': 3600}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

---
- name: create stack
  ignore_errors: True
  register: stack_create
  os_stack:
    name: "{{ stack_name }}"
    tag: "{{ tag_name }}"
    state: present
    template: "/path/to/my_stack.yaml"
    environment:
    - /path/to/resource-registry.yaml
    - /path/to/environment.yaml
    parameters:
        bmc_flavor: m1.medium
        bmc_image: CentOS
        key_name: default
        private_net: "{{ private_net_param }}"
        node_count: 2
        name: undercloud
        image: CentOS
        my_flavor: m1.large
        external_net: "{{ external_net_param }}"

```

## License

TODO

## Author Information
  - ['Mathieu Bultel (matbu), Steve Baker (steveb)']
