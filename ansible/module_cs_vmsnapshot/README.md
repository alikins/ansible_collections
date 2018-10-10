# Ansible module: ansible.module_cs_vmsnapshot


Manages VM snapshots on Apache CloudStack based clouds

## Description

Create, remove and revert VM from snapshots.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VM snapshot is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "description": "{'description': ['Description of the snapshot.']}",
    "domain": "{'description': ['Domain the VM snapshot is related to.']}",
    "name": "{'description': ['Unique Name of the snapshot. In CloudStack terms display name.'], 'required': True, 'aliases': ['display_name']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'required': False, 'default': True}",
    "project": "{'description': ['Name of the project the VM is assigned to.']}",
    "snapshot_memory": "{'description': ['Snapshot memory if set to true.'], 'default': False}",
    "state": "{'description': ['State of the snapshot.'], 'default': 'present', 'choices': ['present', 'absent', 'revert']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "vm": "{'description': ['Name of the virtual machine.'], 'required': True}",
    "zone": "{'description': ['Name of the zone in which the VM is in. If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Create a VM snapshot of disk and memory before an upgrade
  local_action:
    module: cs_vmsnapshot
    name: Snapshot before upgrade
    vm: web-01
    snapshot_memory: yes

- name: Revert a VM to a snapshot after a failed upgrade
  local_action:
    module: cs_vmsnapshot
    name: Snapshot before upgrade
    vm: web-01
    state: revert

- name: Remove a VM snapshot after successful upgrade
  local_action:
    module: cs_vmsnapshot
    name: Snapshot before upgrade
    vm: web-01
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
