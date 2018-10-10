# Ansible module: ansible.module_os_loadbalancer


Add/Delete load balancer from OpenStack Cloud

## Description

Add or Remove load balancer from the OpenStack load-balancer service(Octavia). Load balancer update is not supported for now.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "auto_public_ip": "{'description': ['Allocate a public IP address and associate with the VIP automatically.'], 'type': 'bool', 'default': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "delete_public_ip": "{'description': ['When C(state=absent) and this option is true, any public IP address associated with the VIP will be deleted along with the load balancer.'], 'type': 'bool', 'default': False}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "listeners": "{'description': ['A list of listeners that attached to the load balancer.'], 'suboptions': {'name': {'description': ['The listener name or ID.']}, 'protocol': {'description': ['The protocol for the listener.'], 'default': 'HTTP'}, 'protocol_port': {'description': ['The protocol port number for the listener.'], 'default': 80}, 'pool': {'description': ['The pool attached to the listener.'], 'suboptions': {'name': {'description': ['The pool name or ID.']}, 'protocol': {'description': ['The protocol for the pool.'], 'default': 'HTTP'}, 'lb_algorithm': {'description': ['The load balancing algorithm for the pool.'], 'default': 'ROUND_ROBIN'}, 'members': {'description': ['A list of members that added to the pool.'], 'suboptions': {'name': {'description': ['The member name or ID.']}, 'address': {'description': ['The IP address of the member.']}, 'protocol_port': {'description': ['The protocol port number for the member.'], 'default': 80}, 'subnet': {'description': ['The name or ID of the subnet the member service is accessible from.']}}}}}}}",
    "name": "{'description': ['Name that has to be given to the load balancer'], 'required': True}",
    "public_ip_address": "{'description': ['Public IP address associated with the VIP.']}",
    "public_network": "{'description': ['The name or ID of a Neutron external network.']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time the module should wait.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "vip_address": "{'description': ['IP address of the load balancer virtual IP.']}",
    "vip_network": "{'description': ['The name or id of the network for the virtual IP of the load balancer. One of I(vip_network), I(vip_subnet), or I(vip_port) must be specified for creation.']}",
    "vip_port": "{'description': ['The name or id of the load balancer virtual IP port. One of I(vip_network), I(vip_subnet), or I(vip_port) must be specified for creation.']}",
    "vip_subnet": "{'description': ['The name or id of the subnet for the virtual IP of the load balancer. One of I(vip_network), I(vip_subnet), or I(vip_port) must be specified for creation.']}",
    "wait": "{'description': ['If the module should wait for the load balancer to be created or deleted.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a load balancer by specifying the VIP subnet.
- os_loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: present
    name: my_lb
    vip_subnet: my_subnet
    timeout: 150

# Create a load balancer by specifying the VIP network and the IP address.
- os_loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: present
    name: my_lb
    vip_network: my_network
    vip_address: 192.168.0.11

# Create a load balancer together with its sub-resources in the 'all in one'
# way. A public IP address is also allocated to the load balancer VIP.
- os_loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    name: lingxian_test
    state: present
    vip_subnet: kong_subnet
    auto_public_ip: yes
    public_network: public
    listeners:
      - name: lingxian_80
        protocol: TCP
        protocol_port: 80
        pool:
          name: lingxian_80_pool
          protocol: TCP
          members:
            - name: mywebserver1
              address: 192.168.2.81
              protocol_port: 80
              subnet: webserver_subnet
      - name: lingxian_8080
        protocol: TCP
        protocol_port: 8080
        pool:
          name: lingxian_8080-pool
          protocol: TCP
          members:
            - name: mywebserver2
              address: 192.168.2.82
              protocol_port: 8080
    wait: yes
    timeout: 600

# Delete a load balancer(and all its related resources)
- os_loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: absent
    name: my_lb

# Delete a load balancer(and all its related resources) together with the
# public IP address(if any) attached to it.
- os_loadbalancer:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    state: absent
    name: my_lb
    delete_public_ip: yes

```

## License

TODO

## Author Information
  - ['Lingxian Kong (@lingxiankong)']
