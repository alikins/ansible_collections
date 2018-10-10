# Ansible module: ansible.module_cs_vpc_offering


Manages vpc offerings on Apache CloudStack based clouds

## Description

Create, update, enable, disable and remove CloudStack VPC offerings.

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
    "display_text": "{'description': ['Display text of the vpc offerings'], 'required': False}",
    "name": "{'description': ['The name of the vpc offering'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "service_capabilities": "{'description': ['Desired service capabilities as part of vpc offering.'], 'aliases': ['service_capability']}",
    "service_offering": "{'description': ['The name or ID of the service offering for the VPC router appliance.'], 'required': False}",
    "service_providers": "{'description': ['provider to service mapping. If not specified, the provider for the service will be mapped to the default provider on the physical network'], 'aliases': ['service_provider'], 'required': False}",
    "state": "{'description': ['State of the vpc offering.'], 'choices': ['enabled', 'present', 'disabled', 'absent'], 'required': False, 'default': 'present'}",
    "supported_services": "{'description': ['Services supported by the vpc offering'], 'aliases': ['supported_service'], 'required': False}",
}
```

## Examples


``` yaml

# Create a vpc offering and enable it
- local_action:
    module: cs_vpc_offering
    name: "my_vpc_offering"
    display_text: "vpc offering description"
    state: enabled
    supported_services: [ Dns, Dhcp ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}

# Create a vpc offering with redundant router
- local_action:
    module: cs_vpc_offering
    name: "my_vpc_offering"
    display_text: "vpc offering description"
    supported_services: [ Dns, Dhcp, SourceNat ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}
      - {service: 'SourceNat', provider: 'VpcVirtualRouter'}
    service_capabilities:
      - {service: 'SourceNat', capabilitytype: 'RedundantRouter', capabilityvalue: true}

# Create a region level vpc offering with distributed router
- local_action:
    module: cs_vpc_offering
    name: "my_vpc_offering"
    display_text: "vpc offering description"
    state: present
    supported_services: [ Dns, Dhcp, SourceNat ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}
      - {service: 'SourceNat', provider: 'VpcVirtualRouter'}
    service_capabilities:
      - {service: 'Connectivity', capabilitytype: 'DistributedRouter', capabilityvalue: true}
      - {service: 'Connectivity', capabilitytype: 'RegionLevelVPC', capabilityvalue: true}

# Remove a vpc offering
- local_action:
    module: cs_vpc_offering
    name: "my_vpc_offering"
    state: absent

```

## License

TODO

## Author Information
  - ['David Passante (@dpassante)']
