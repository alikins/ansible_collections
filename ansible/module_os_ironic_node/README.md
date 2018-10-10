# Ansible module: ansible.module_os_ironic_node


Activate/Deactivate Bare Metal Resources from OpenStack

## Description

Deploy to nodes controlled by Ironic.

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
    "config_drive": "{'description': ['A configdrive file or HTTP(S) URL that will be passed along to the node.']}",
    "deploy": "{'description': ['Indicates if the resource should be deployed. Allows for deployment logic to be disengaged and control of the node power or maintenance state to be changed.'], 'type': 'bool', 'default': True}",
    "instance_info": "{'description': ['Definition of the instance information which is used to deploy the node.  This information is only required when an instance is set to present.'], 'suboptions': {'image_source': {'description': ['An HTTP(S) URL where the image can be retrieved from.']}, 'image_checksum': {'description': ['The checksum of image_source.']}, 'image_disk_format': {'description': ['The type of image that has been requested to be deployed.']}}}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "ironic_url": "{'description': ['If noauth mode is utilized, this is required to be set to the endpoint URL for the Ironic API.  Use with "auth" and "auth_type" settings set to None.']}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "maintenance": "{'description': ['A setting to allow the direct control if a node is in maintenance mode.'], 'type': 'bool', 'default': False}",
    "maintenance_reason": "{'description': ['A string expression regarding the reason a node is in a maintenance mode.']}",
    "power": "{'description': ['A setting to allow power state to be asserted allowing nodes that are not yet deployed to be powered on, and nodes that are deployed to be powered off.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Indicates desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['An integer value representing the number of seconds to wait for the node activation or deactivation to complete.'], 'required': False, 'default': 180, 'version_added': '2.1'}",
    "uuid": "{'description': ['globally unique identifier (UUID) to be given to the resource.']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['A boolean value instructing the module to wait for node activation or deactivation to complete before returning.'], 'type': 'bool', 'required': False, 'default': False, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# Activate a node by booting an image with a configdrive attached
os_ironic_node:
  cloud: "openstack"
  uuid: "d44666e1-35b3-4f6b-acb0-88ab7052da69"
  state: present
  power: present
  deploy: True
  maintenance: False
  config_drive: "http://192.168.1.1/host-configdrive.iso"
  instance_info:
    image_source: "http://192.168.1.1/deploy_image.img"
    image_checksum: "356a6b55ecc511a20c33c946c4e678af"
    image_disk_format: "qcow"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
