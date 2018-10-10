# Ansible module: ansible.module_cs_network_offering


Manages network offerings on Apache CloudStack based clouds

## Description

Create, update, enable, disable and remove network offerings.

## Requirements

TODO

## Arguments

``` json
{
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "availability": "{'description': ['The availability of network offering. Default value is Optional']}",
    "conserve_mode": "{'description': ['Whether the network offering has IP conserve mode enabled.'], 'type': 'bool'}",
    "details": "{'description': ['Network offering details in key/value pairs.', 'with service provider as a value'], 'choices': ['internallbprovider', 'publiclbprovider']}",
    "display_text": "{'description': ['Display text of the network offerings.']}",
    "egress_default_policy": "{'description': ['Whether the default egress policy is allow or to deny.'], 'choices': ['allow', 'deny']}",
    "guest_ip_type": "{'description': ['Guest type of the network offering.'], 'choices': ['Shared', 'Isolated']}",
    "keepalive_enabled": "{'description': ['If true keepalive will be turned on in the loadbalancer.', 'At the time of writing this has only an effect on haproxy.', 'the mode http and httpclose options are unset in the haproxy conf file.'], 'type': 'bool'}",
    "max_connections": "{'description': ['Maximum number of concurrent connections supported by the network offering.']}",
    "name": "{'description': ['The name of the network offering.'], 'required': True}",
    "network_rate": "{'description': ['Data transfer rate in megabits per second allowed.']}",
    "persistent": "{'description': ['True if network offering supports persistent networks', 'defaulted to false if not specified']}",
    "service_capabilities": "{'description': ['Desired service capabilities as part of network offering.'], 'aliases': ['service_capability']}",
    "service_offering": "{'description': ['The service offering name or ID used by virtual router provider.']}",
    "service_provider": "{'description': ['Provider to service mapping.', 'If not specified, the provider for the service will be mapped to the default provider on the physical network.'], 'aliases': ['service_provider']}",
    "specify_ip_ranges": "{'description': ['Wheter the network offering supports specifying IP ranges.', 'Defaulted to C(no) by the API if not specified.'], 'type': 'bool'}",
    "specify_vlan": "{'description': ['Whether the network offering supports vlans or not.'], 'type': 'bool'}",
    "state": "{'description': ['State of the network offering.'], 'choices': ['enabled', 'present', 'disabled', 'absent'], 'default': 'present'}",
    "supported_services": "{'description': ['Services supported by the network offering.', 'One or more of the choices.'], 'choices': ['Dns', 'PortForwarding', 'Dhcp', 'SourceNat', 'UserData', 'Firewall', 'StaticNat', 'Vpn', 'Lb'], 'aliases': ['supported_service']}",
    "traffic_type": "{'description': ['The traffic type for the network offering.'], 'default': 'Guest'}",
}
```

## Examples


``` yaml

- name: Create a network offering and enable it
  local_action:
    module: cs_network_offering
    name: my_network_offering
    display_text: network offering description
    state: enabled
    guest_ip_type: Isolated
    supported_services: [ Dns, PortForwarding, Dhcp, SourceNat, UserData, Firewall, StaticNat, Vpn, Lb ]
    service_providers:
      - { service: 'dns', provider: 'virtualrouter' }
      - { service: 'dhcp', provider: 'virtualrouter' }


- name: Remove a network offering
  local_action:
    module: cs_network_offering
    name: my_network_offering
    state: absent

```

## License

TODO

## Author Information
  - ['David Passante (@dpassante)']
