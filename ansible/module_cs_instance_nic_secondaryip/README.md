# Ansible module: ansible.module_cs_instance_nic_secondaryip


Manages secondary IPs of an instance on Apache CloudStack based clouds

## Description

Add and remove secondary IPs to and from a NIC of an instance.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the instance is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the instance is related to.']}",
    "network": "{'description': ['Name of the network.', 'Required to find the NIC if instance has multiple networks assigned.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "project": "{'description': ['Name of the project the instance is deployed in.']}",
    "state": "{'description': ['State of the ipaddress.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vm": "{'description': ['Name of instance.'], 'required': True, 'aliases': ['name']}",
    "vm_guest_ip": "{'description': ['Secondary IP address to be added to the instance nic.', 'If not set, the API always returns a new IP address and idempotency is not given.'], 'aliases': ['secondary_ip']}",
    "vpc": "{'description': ['Name of the VPC the C(vm) is related to.']}",
    "zone": "{'description': ['Name of the zone in which the instance is deployed in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Assign a specific IP to the default NIC of the VM
  local_action:
    module: cs_instance_nic_secondaryip
    vm: customer_xy
    vm_guest_ip: 10.10.10.10

# Note: If vm_guest_ip is not set, you will get a new IP address on every run.
- name: Assign an IP to the default NIC of the VM
  local_action:
    module: cs_instance_nic_secondaryip
    vm: customer_xy

- name: Remove a specific IP from the default NIC
  local_action:
    module: cs_instance_nic_secondaryip
    vm: customer_xy
    vm_guest_ip: 10.10.10.10
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
