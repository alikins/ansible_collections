# Ansible module: ansible.module_os_floating_ip


Add/Remove floating IP from an instance

## Description

Add or Remove a floating IP to an instance

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
    "fixed_address": "{'description': ['To which fixed IP of server the floating IP address should be attached to.']}",
    "floating_ip_address": "{'description': ['A floating IP address to attach or to detach. Required only if I(state) is absent. When I(state) is present can be used to specify a IP address to attach.']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "nat_destination": "{'description': ['The name or id of a neutron private network that the fixed IP to attach floating IP is on'], 'aliases': ['fixed_network', 'internal_network'], 'version_added': '2.3'}",
    "network": "{'description': ['The name or ID of a neutron external network or a nova pool name.']}",
    "purge": "{'description': ['When I(state) is absent, indicates whether or not to delete the floating IP completely, or only detach it from the server. Default is to detach only.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "reuse": "{'description': ['When I(state) is present, and I(floating_ip_address) is not present, this parameter can be used to specify whether we should try to reuse a floating IP address already allocated to the project.'], 'type': 'bool', 'default': False}",
    "server": "{'description': ['The name or ID of the instance to which the IP address should be assigned.'], 'required': True}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Time to wait for an IP address to appear as attached. See wait.'], 'required': False, 'default': 60}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['When attaching a floating IP address, specify whether we should wait for it to appear as attached.'], 'type': 'bool', 'required': False, 'default': False}",
}
```

## Examples


``` yaml

# Assign a floating IP to the fist interface of `cattle001` from an exiting
# external network or nova pool. A new floating IP from the first available
# external network is allocated to the project.
- os_floating_ip:
     cloud: dguerri
     server: cattle001

# Assign a new floating IP to the instance fixed ip `192.0.2.3` of
# `cattle001`. If a free floating IP is already allocated to the project, it is
# reused; if not, a new one is created.
- os_floating_ip:
     cloud: dguerri
     state: present
     reuse: yes
     server: cattle001
     network: ext_net
     fixed_address: 192.0.2.3
     wait: true
     timeout: 180

# Assign a new floating IP from the network `ext_net` to the instance fixed
# ip in network `private_net` of `cattle001`.
- os_floating_ip:
     cloud: dguerri
     state: present
     server: cattle001
     network: ext_net
     nat_destination: private_net
     wait: true
     timeout: 180

# Detach a floating IP address from a server
- os_floating_ip:
     cloud: dguerri
     state: absent
     floating_ip_address: 203.0.113.2
     server: cattle001

```

## License

TODO

## Author Information
  - ['Davide Guerri (@dguerri) <davide.guerri@hp.com>']
