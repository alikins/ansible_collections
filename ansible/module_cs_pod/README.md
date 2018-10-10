# Ansible module: ansible.module_cs_pod


Manages pods on Apache CloudStack based clouds

## Description

Create, update, delete pods.

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
    "end_ip": "{'description': ['Ending IP address for the Pod.']}",
    "gateway": "{'description': ['Gateway for the Pod.', 'Required on C(state=present)']}",
    "id": "{'description': ['uuid of the existing pod.']}",
    "name": "{'description': ['Name of the pod.'], 'required': True}",
    "netmask": "{'description': ['Netmask for the Pod.', 'Required on C(state=present)']}",
    "start_ip": "{'description': ['Starting IP address for the Pod.', 'Required on C(state=present)']}",
    "state": "{'description': ['State of the pod.'], 'default': 'present', 'choices': ['present', 'enabled', 'disabled', 'absent']}",
    "zone": "{'description': ['Name of the zone in which the pod belongs to.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Ensure a pod is present
  local_action:
    module: cs_pod
    name: pod1
    zone: ch-zrh-ix-01
    start_ip: 10.100.10.101
    gateway: 10.100.10.1
    netmask: 255.255.255.0

- name: Ensure a pod is disabled
  local_action:
    module: cs_pod
    name: pod1
    zone: ch-zrh-ix-01
    state: disabled

- name: Ensure a pod is enabled
  local_action:
    module: cs_pod
    name: pod1
    zone: ch-zrh-ix-01
    state: enabled

- name: Ensure a pod is absent
  local_action:
    module: cs_pod
    name: pod1
    zone: ch-zrh-ix-01
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
