# Ansible module: ansible.module_cs_snapshot_policy


Manages volume snapshot policies on Apache CloudStack based clouds

## Description

Create, update and delete volume snapshot policies.

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
    "device_id": "{'description': ['ID of the device on a VM the volume is attached to.', 'This will only be considered if VM has multiple DATADISK volumes.'], 'version_added': '2.3'}",
    "domain": "{'description': ['Domain the volume is related to.']}",
    "interval_type": "{'description': ['Interval of the snapshot.'], 'default': 'daily', 'choices': ['hourly', 'daily', 'weekly', 'monthly'], 'aliases': ['interval']}",
    "max_snaps": "{'description': ['Max number of snapshots.'], 'default': 8, 'aliases': ['max']}",
    "project": "{'description': ['Name of the project the volume is related to.']}",
    "schedule": "{'description': ['Time the snapshot is scheduled. Required if C(state=present).', 'Format for C(interval_type=HOURLY): C(MM)', 'Format for C(interval_type=DAILY): C(MM:HH)', 'Format for C(interval_type=WEEKLY): C(MM:HH:DD (1-7))', 'Format for C(interval_type=MONTHLY): C(MM:HH:DD (1-28))']}",
    "state": "{'description': ['State of the snapshot policy.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "time_zone": "{'description': ['Specifies a timezone for this command.'], 'default': 'UTC', 'aliases': ['timezone']}",
    "vm": "{'description': ['Name of the instance to select the volume from.', 'Use C(volume_type) if VM has a DATADISK and ROOT volume.', 'In case of C(volume_type=DATADISK), additionally use C(device_id) if VM has more than one DATADISK volume.', 'Either C(volume) or C(vm) is required.'], 'version_added': '2.3'}",
    "volume": "{'description': ['Name of the volume.', 'Either C(volume) or C(vm) is required.']}",
    "volume_type": "{'description': ['Type of the volume.'], 'choices': ['DATADISK', 'ROOT'], 'version_added': '2.3'}",
    "vpc": "{'description': ['Name of the vpc the instance is deployed in.'], 'version_added': '2.3'}",
}
```

## Examples


``` yaml

- name: ensure a snapshot policy daily at 1h00 UTC
  local_action:
    module: cs_snapshot_policy
    volume: ROOT-478
    schedule: '00:1'
    max_snaps: 3

- name: ensure a snapshot policy daily at 1h00 UTC on the second DATADISK of VM web-01
  local_action:
    module: cs_snapshot_policy
    vm: web-01
    volume_type: DATADISK
    device_id: 2
    schedule: '00:1'
    max_snaps: 3

- name: ensure a snapshot policy hourly at minute 5 UTC
  local_action:
    module: cs_snapshot_policy
    volume: ROOT-478
    schedule: '5'
    interval_type: hourly
    max_snaps: 1

- name: ensure a snapshot policy weekly on Sunday at 05h00, TZ Europe/Zurich
  local_action:
    module: cs_snapshot_policy
    volume: ROOT-478
    schedule: '00:5:1'
    interval_type: weekly
    max_snaps: 1
    time_zone: 'Europe/Zurich'

- name: ensure a snapshot policy is absent
  local_action:
    module: cs_snapshot_policy
    volume: ROOT-478
    interval_type: hourly
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
