# Ansible module: ansible.module_cs_staticnat


Manages static NATs on Apache CloudStack based clouds

## Description

Create, update and remove static NATs.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the static NAT is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the static NAT is related to.']}",
    "ip_address": "{'description': ['Public IP address the static NAT is assigned to.'], 'required': True}",
    "network": "{'description': ['Network the IP address is related to.'], 'version_added': '2.2'}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the static NAT is related to.']}",
    "state": "{'description': ['State of the static NAT.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vm": "{'description': ['Name of virtual machine which we make the static NAT for.', 'Required if I(state=present).']}",
    "vm_guest_ip": "{'description': ['VM guest NIC secondary IP address for the static NAT.']}",
    "vpc": "{'description': ['VPC the network related to.'], 'version_added': '2.3'}",
    "zone": "{'description': ['Name of the zone in which the virtual machine is in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Create a static NAT for IP 1.2.3.4 to web01
  local_action:
    module: cs_staticnat
    ip_address: 1.2.3.4
    vm: web01

- name: Remove a static NAT
  local_action:
    module: cs_staticnat
    ip_address: 1.2.3.4
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
