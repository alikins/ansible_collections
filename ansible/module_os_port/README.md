# Ansible module: ansible.module_os_port


Add/Update/Delete ports from an OpenStack cloud

## Description

Add, Update or Remove ports from an OpenStack cloud. A I(state) of 'present' will ensure the port is created or updated if required.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state_up": "{'description': ['Sets admin state.']}",
    "allowed_address_pairs": "{'description': ['Allowed address pairs list.  Allowed address pairs are supported with dictionary structure. e.g.  allowed_address_pairs: - ip_address: 10.1.0.12 mac_address: ab:cd:ef:12:34:56 - ip_address: ...']}",
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "device_id": "{'description': ['Device ID of device using this port.']}",
    "device_owner": "{'description': ['The ID of the entity that uses this port.']}",
    "extra_dhcp_opts": "{'description': ['Extra dhcp options to be assigned to this port.  Extra options are supported with dictionary structure. e.g.  extra_dhcp_opts: - opt_name: opt name1 opt_value: value1 - opt_name: ...']}",
    "fixed_ips": "{'description': ['Desired IP and/or subnet for this port.  Subnet is referenced by subnet_id and IP is referenced by ip_address.']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "mac_address": "{'description': ['MAC address of this port.']}",
    "name": "{'description': ['Name that has to be given to the port.']}",
    "network": "{'description': ['Network ID or name this port belongs to.'], 'required': True}",
    "no_security_groups": "{'description': ['Do not associate a security group with this port.'], 'default': 'no'}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "security_groups": "{'description': ['Security group(s) ID(s) or name(s) associated with the port (comma separated string or YAML list)']}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a port
- os_port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo

# Create a port with a static IP
- os_port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    fixed_ips:
      - ip_address: 10.1.0.21

# Create a port with No security groups
- os_port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    network: foo
    no_security_groups: True

# Update the existing 'port1' port with multiple security groups (version 1)
- os_port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    security_groups: 1496e8c7-4918-482a-9172-f4f00fc4a3a5,057d4bdf-6d4d-472...

# Update the existing 'port1' port with multiple security groups (version 2)
- os_port:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: port1
    security_groups:
      - 1496e8c7-4918-482a-9172-f4f00fc4a3a5
      - 057d4bdf-6d4d-472...

```

## License

TODO

## Author Information
  - ['Davide Agnello (@dagnello)']
