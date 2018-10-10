# Ansible module: ansible.module_sf_snapshot_schedule_manager


Manage SolidFire snapshot schedules

## Description

Create, destroy, or update accounts on SolidFire

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['Name for the snapshot schedule.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "paused": "{'description': ['Pause / Resume a schedule.'], 'required': False}",
    "recurring": "{'description': ['Should the schedule recur?'], 'required': False}",
    "retention": "{'description': ['Retention period for the snapshot.', "Format is 'HH:mm:ss'."], 'required': False}",
    "schedule_id": "{'description': ['The schedule ID for the schedule that you want to update or delete.'], 'required': False}",
    "snapshot_name": "{'description': ['Name for the created snapshots.'], 'required': False}",
    "starting_date": "{'description': ['Starting date for the schedule.', 'Required when C(state=present).', "Please use two '-' in the above format, or you may see an error- TypeError, is not JSON serializable description.", 'Format: C(2016--12--01T00:00:00Z)'], 'required': False}",
    "state": "{'description': ['Whether the specified schedule should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "time_interval_days": "{'description': ['Time interval in days.'], 'required': False, 'default': 1}",
    "time_interval_hours": "{'description': ['Time interval in hours.'], 'required': False, 'default': 0}",
    "time_interval_minutes": "{'description': ['Time interval in minutes.'], 'required': False, 'default': 0}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "volumes": "{'description': ['Volume IDs that you want to set the snapshot schedule for.', 'At least 1 volume ID is required for creating a new schedule.', 'required when C(state=present)'], 'required': False}",
}
```

## Examples


``` yaml

   - name: Create Snapshot schedule
     sf_snapshot_schedule_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       name: Schedule_A
       time_interval_days: 1
       starting_date: 2016--12--01T00:00:00Z
       volumes: 7

   - name: Update Snapshot schedule
     sf_snapshot_schedule_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       schedule_id: 6
       recurring: True
       snapshot_name: AnsibleSnapshots

   - name: Delete Snapshot schedule
     sf_snapshot_schedule_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: absent
       schedule_id: 6

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
