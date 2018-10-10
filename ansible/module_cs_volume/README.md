# Ansible module: ansible.module_cs_volume


Manages volumes on Apache CloudStack based clouds

## Description

Create, destroy, attach, detach volumes.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the volume is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "custom_id": "{'description': ['Custom id to the resource.', 'Allowed to Root Admins only.']}",
    "disk_offering": "{'description': ['Name of the disk offering to be used.', 'Required one of C(disk_offering), C(snapshot) if volume is not already C(state=present).']}",
    "display_volume": "{'description': ['Whether to display the volume to the end user or not.', 'Allowed to Root Admins only.'], 'default': True}",
    "domain": "{'description': ['Name of the domain the volume to be deployed in.']}",
    "force": "{'description': ['Force removal of volume even it is attached to a VM.', 'Considered on C(state=absnet) only.'], 'default': False}",
    "max_iops": "{'description': ['Max iops']}",
    "min_iops": "{'description': ['Min iops']}",
    "name": "{'description': ['Name of the volume.', 'C(name) can only contain ASCII letters.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "project": "{'description': ['Name of the project the volume to be deployed in.']}",
    "shrink_ok": "{'description': ['Whether to allow to shrink the volume.'], 'default': False}",
    "size": "{'description': ['Size of disk in GB']}",
    "snapshot": "{'description': ['The snapshot name for the disk volume.', 'Required one of C(disk_offering), C(snapshot) if volume is not already C(state=present).']}",
    "state": "{'description': ['State of the volume.'], 'default': 'present', 'choices': ['present', 'absent', 'attached', 'detached']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "vm": "{'description': ['Name of the virtual machine to attach the volume to.']}",
    "zone": "{'description': ['Name of the zone in which the volume should be deployed.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: create volume within project and zone with specified storage options
  local_action:
    module: cs_volume
    name: web-vm-1-volume
    project: Integration
    zone: ch-zrh-ix-01
    disk_offering: PerfPlus Storage
    size: 20

- name: create/attach volume to instance
  local_action:
    module: cs_volume
    name: web-vm-1-volume
    disk_offering: PerfPlus Storage
    size: 20
    vm: web-vm-1
    state: attached

- name: detach volume
  local_action:
    module: cs_volume
    name: web-vm-1-volume
    state: detached

- name: remove volume
  local_action:
    module: cs_volume
    name: web-vm-1-volume
    state: absent

```

## License

TODO

## Author Information
  - ['Jefferson Girão (@jeffersongirao)', 'René Moser (@resmo)']
  - ['Jefferson Girão (@jeffersongirao)', 'René Moser (@resmo)']
