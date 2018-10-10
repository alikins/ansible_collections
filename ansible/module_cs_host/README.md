# Ansible module: ansible.module_cs_host


Manages hosts on Apache CloudStack based clouds

## Description

Create, update and remove hosts.

## Requirements

TODO

## Arguments

``` json
{
    "allocation_state": "{'description': ['Allocation state of the host.'], 'choices': ['enabled', 'disabled']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cluster": "{'description': ['Name of the cluster.']}",
    "host_tags": "{'description': ['Tags of the host.'], 'aliases': ['host_tag']}",
    "hypervisor": "{'description': ['Name of the cluster.', 'Required if C(state=present) and host does not yet exist.'], 'choices': ['KVM', 'VMware', 'BareMetal', 'XenServer', 'LXC', 'HyperV', 'UCS', 'OVM', 'Simulator']}",
    "name": "{'description': ['Name of the host.'], 'required': True, 'aliases': ['ip_address']}",
    "password": "{'description': ['Password for the host.', 'Required if C(state=present) and host does not yet exist.']}",
    "pod": "{'description': ['Name of the pod.', 'Required if C(state=present) and host does not yet exist.']}",
    "state": "{'description': ['State of the host.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "url": "{'description': ['Url of the host used to create a host.', 'If not provided, C(http://) and param C(name) is used as url.', 'Only considered if C(state=present) and host does not yet exist.']}",
    "username": "{'description': ['Username for the host.', 'Required if C(state=present) and host does not yet exist.']}",
    "zone": "{'description': ['Name of the zone in which the host should be deployed.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Ensure a host is present but disabled
  local_action:
    module: cs_host
    name: ix-pod01-esx01.example.com
    cluster: vcenter.example.com/ch-zrh-ix/pod01-cluster01
    pod: pod01
    zone: ch-zrh-ix-01
    hypervisor: VMware
    allocation_state: disabled
    host_tags:
    - perf
    - gpu

- name: Ensure an existing host is disabled
  local_action:
    module: cs_host
    name: ix-pod01-esx01.example.com
    zone: ch-zrh-ix-01
    allocation_state: disabled

- name: Ensure an existing host is enabled
  local_action:
    module: cs_host
    name: ix-pod01-esx01.example.com
    zone: ch-zrh-ix-01
    allocation_state: enabled

- name: Ensure a host is absent
  local_action:
    module: cs_host
    name: ix-pod01-esx01.example.com
    zone: ch-zrh-ix-01
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
