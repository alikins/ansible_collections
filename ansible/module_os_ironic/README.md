# Ansible module: ansible.module_os_ironic


Create/Delete Bare Metal Resources from OpenStack

## Description

Create or Remove Ironic nodes from OpenStack.

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
    "chassis_uuid": "{'description': ['Associate the node with a pre-defined chassis.']}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "driver": "{'description': ['The name of the Ironic Driver to use with this node.'], 'required': True}",
    "driver_info": "{'description': ["Information for this server's driver. Will vary based on which driver is in use. Any sub-field which is populated will be validated during creation."], 'suboptions': {'power': {'description': ['Information necessary to turn this server on / off. This often includes such things as IPMI username, password, and IP address.'], 'required': True}, 'deploy': {'description': ['Information necessary to deploy this server directly, without using Nova. THIS IS NOT RECOMMENDED.']}, 'console': {'description': ["Information necessary to connect to this server's serial console.  Not all drivers support this."]}, 'management': {'description': ["Information necessary to interact with this server's management interface. May be shared by power_info in some cases."], 'required': True}}}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "ironic_url": "{'description': ['If noauth mode is utilized, this is required to be set to the endpoint URL for the Ironic API.  Use with "auth" and "auth_type" settings set to None.']}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['unique name identifier to be given to the resource.']}",
    "nics": "{'description': ['A list of network interface cards, eg, " - mac: aa:bb:cc:aa:bb:cc"'], 'required': True}",
    "properties": "{'description': ['Definition of the physical characteristics of this server, used for scheduling purposes'], 'suboptions': {'cpu_arch': {'description': ['CPU architecture (x86_64, i686, ...)'], 'default': 'x86_64'}, 'cpus': {'description': ['Number of CPU cores this machine has'], 'default': 1}, 'ram': {'description': ['amount of RAM this machine has, in MB'], 'default': 1}, 'disk_size': {'description': ['size of first storage device in this machine (typically /dev/sda), in GB'], 'default': 1}}}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "skip_update_of_driver_password": "{'description': ['Allows the code that would assert changes to nodes to skip the update if the change is a single line consisting of the password field.  As of Kilo, by default, passwords are always masked to API requests, which means the logic as a result always attempts to re-assert the password field.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Indicates desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "uuid": "{'description': ['globally unique identifier (UUID) to be given to the resource. Will be auto-generated if not specified, and name is specified.', 'Definition of a UUID will always take precedence to a name value.']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Enroll a node with some basic properties and driver info
- os_ironic:
    cloud: "devstack"
    driver: "pxe_ipmitool"
    uuid: "00000000-0000-0000-0000-000000000002"
    properties:
      cpus: 2
      cpu_arch: "x86_64"
      ram: 8192
      disk_size: 64
    nics:
      - mac: "aa:bb:cc:aa:bb:cc"
      - mac: "dd:ee:ff:dd:ee:ff"
    driver_info:
      power:
        ipmi_address: "1.2.3.4"
        ipmi_username: "admin"
        ipmi_password: "adminpass"
    chassis_uuid: "00000000-0000-0000-0000-000000000001"


```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
