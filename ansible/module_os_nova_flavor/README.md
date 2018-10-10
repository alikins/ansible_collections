# Ansible module: ansible.module_os_nova_flavor


Manage OpenStack compute flavors

## Description

Add or remove flavors from OpenStack.

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
    "disk": "{'description': ['Size of local disk, in GB.']}",
    "ephemeral": "{'description': ['Ephemeral space size, in GB.'], 'default': 0}",
    "extra_specs": "{'description': ['Metadata dictionary'], 'version_added': '2.3'}",
    "flavorid": "{'description': ['ID for the flavor. This is optional as a unique UUID will be assigned if a value is not specified.'], 'default': 'auto'}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "is_public": "{'description': ['Make flavor accessible to the public.'], 'type': 'bool', 'default': True}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Flavor name.'], 'required': True}",
    "ram": "{'description': ['Amount of memory, in MB.']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "rxtx_factor": "{'description': ['RX/TX factor.'], 'default': 1.0}",
    "state": "{'description': ["Indicate desired state of the resource. When I(state) is 'present', then I(ram), I(vcpus), and I(disk) are all required. There are no default values for those parameters."], 'choices': ['present', 'absent'], 'default': 'present'}",
    "swap": "{'description': ['Swap space size, in MB.'], 'default': 0}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "vcpus": "{'description': ['Number of virtual CPUs.']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

- name: "Create 'tiny' flavor with 1024MB of RAM, 1 virtual CPU, and 10GB of local disk, and 10GB of ephemeral."
  os_nova_flavor:
    cloud: mycloud
    state: present
    name: tiny
    ram: 1024
    vcpus: 1
    disk: 10
    ephemeral: 10

- name: "Delete 'tiny' flavor"
  os_nova_flavor:
    cloud: mycloud
    state: absent
    name: tiny

- name: Create flavor with metadata
  os_nova_flavor:
    cloud: mycloud
    state: present
    name: tiny
    ram: 1024
    vcpus: 1
    disk: 10
    extra_specs:
      "quota:disk_read_iops_sec": 5000
      "aggregate_instance_extra_specs:pinned": false

```

## License

TODO

## Author Information
  - ['David Shrewsbury (@Shrews)']
