# Ansible module: ansible.module_os_router


Create or delete routers from OpenStack

## Description

Create or Delete routers from OpenStack. Although Neutron allows routers to share the same name, this module enforces name uniqueness to be more user friendly.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state_up": "{'description': ['Desired admin state of the created or existing router.'], 'type': 'bool', 'default': True}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "enable_snat": "{'description': ['Enable Source NAT (SNAT) attribute.'], 'type': 'bool'}",
    "external_fixed_ips": "{'description': ['The IP address parameters for the external gateway network. Each is a dictionary with the subnet name or ID (subnet) and the IP address to assign on the subnet (ip). If no IP is specified, one is automatically assigned from that subnet.']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "interfaces": "{'description': ["List of subnets to attach to the router internal interface. Default gateway associated with the subnet will be automatically attached with the router's internal interface. In order to provide an ip address different from the default gateway,parameters are passed as dictionary with keys as network name or ID(net), subnet name or ID (subnet) and the IP of port (portip) from the network. User defined portip is often required when a multiple router need to be connected to a single subnet for which the default gateway has been already used."]}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['Name to be give to the router'], 'required': True}",
    "network": "{'description': ['Unique name or ID of the external gateway network.', 'required I(interfaces) or I(enable_snat) are provided.']}",
    "project": "{'description': ['Unique name or ID of the project.'], 'version_added': '2.2'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a simple router, not attached to a gateway or subnets.
- os_router:
    cloud: mycloud
    state: present
    name: simple_router

# Create a simple router, not attached to a gateway or subnets for a given project.
- os_router:
    cloud: mycloud
    state: present
    name: simple_router
    project: myproj

# Creates a router attached to ext_network1 on an IPv4 subnet and one
# internal subnet interface.
- os_router:
    cloud: mycloud
    state: present
    name: router1
    network: ext_network1
    external_fixed_ips:
      - subnet: public-subnet
        ip: 172.24.4.2
    interfaces:
      - private-subnet

# Create another router with two internal subnet interfaces.One with user defined port
# ip and another with default gateway.
- os_router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Create another router with two internal subnet interface.One with user defined port
# ip and and another with default gateway.
- os_router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Create another router with two internal subnet interface. one with  user defined port
# ip and and another  with default gateway.
- os_router:
    cloud: mycloud
    state: present
    name: router2
    network: ext_network1
    interfaces:
      - net: private-net
        subnet: private-subnet
        portip: 10.1.1.10
      - project-subnet

# Update existing router1 external gateway to include the IPv6 subnet.
# Note that since 'interfaces' is not provided, any existing internal
# interfaces on an existing router will be left intact.
- os_router:
    cloud: mycloud
    state: present
    name: router1
    network: ext_network1
    external_fixed_ips:
      - subnet: public-subnet
        ip: 172.24.4.2
      - subnet: ipv6-public-subnet
        ip: 2001:db8::3

# Delete router1
- os_router:
    cloud: mycloud
    state: absent
    name: router1

```

## License

TODO

## Author Information
  - ['David Shrewsbury (@Shrews)']
