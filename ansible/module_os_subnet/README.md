# Ansible module: ansible.module_os_subnet


Add/Remove subnet to an OpenStack network

## Description

Add or Remove a subnet to an OpenStack network

## Requirements

TODO

## Arguments

``` json
{
    "allocation_pool_end": "{'description': ['From the subnet pool the last IP that should be assigned to the virtual machines.']}",
    "allocation_pool_start": "{'description': ['From the subnet pool the starting address from which the IP should be allocated.']}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cidr": "{'description': ["The CIDR representation of the subnet that should be assigned to the subnet. Required when I(state) is 'present' and a subnetpool is not specified."]}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "dns_nameservers": "{'description': ['List of DNS nameservers for this subnet.']}",
    "enable_dhcp": "{'description': ['Whether DHCP should be enabled for this subnet.'], 'type': 'bool', 'default': True}",
    "extra_specs": "{'description': ['Dictionary with extra key/value pairs passed to the API'], 'required': False, 'default': {}, 'version_added': '2.7'}",
    "gateway_ip": "{'description': ['The ip that would be assigned to the gateway for this subnet']}",
    "host_routes": "{'description': ['A list of host route dictionaries for the subnet.']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "ip_version": "{'description': ['The IP version of the subnet 4 or 6'], 'default': 4}",
    "ipv6_address_mode": "{'description': ['IPv6 address mode'], 'choices': ['dhcpv6-stateful', 'dhcpv6-stateless', 'slaac']}",
    "ipv6_ra_mode": "{'description': ['IPv6 router advertisement mode'], 'choices': ['dhcpv6-stateful', 'dhcpv6-stateless', 'slaac']}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "name": "{'description': ['The name of the subnet that should be created. Although Neutron allows for non-unique subnet names, this module enforces subnet name uniqueness.'], 'required': True}",
    "network_name": "{'description': ['Name of the network to which the subnet should be attached', "Required when I(state) is 'present'"]}",
    "no_gateway_ip": "{'description': ['The gateway IP would not be assigned for this subnet'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "project": "{'description': ['Project name or ID containing the subnet (name admin-only)'], 'version_added': '2.1'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "use_default_subnetpool": "{'description': ['Use the default subnetpool for I(ip_version) to obtain a CIDR.'], 'type': 'bool', 'default': False}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a new (or update an existing) subnet on the specified network
- os_subnet:
    state: present
    network_name: network1
    name: net1subnet
    cidr: 192.168.0.0/24
    dns_nameservers:
       - 8.8.8.7
       - 8.8.8.8
    host_routes:
       - destination: 0.0.0.0/0
         nexthop: 12.34.56.78
       - destination: 192.168.0.0/24
         nexthop: 192.168.0.1

# Delete a subnet
- os_subnet:
    state: absent
    name: net1subnet

# Create an ipv6 stateless subnet
- os_subnet:
    state: present
    name: intv6
    network_name: internal
    ip_version: 6
    cidr: 2db8:1::/64
    dns_nameservers:
        - 2001:4860:4860::8888
        - 2001:4860:4860::8844
    ipv6_ra_mode: dhcpv6-stateless
    ipv6_address_mode: dhcpv6-stateless

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
