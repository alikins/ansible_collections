# Ansible module: ansible.module_na_elementsw_snapshot_schedule


NetApp Element Software Snapshot Schedules

## Description

Create, destroy, or update accounts on ElementSW

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['Account ID for the owner of this volume.', 'It accepts either account_name or account_id', 'if account_id is digit, it will consider as account_id', 'If account_id is string, it will consider as account_name']}",
    "days_of_month_hours": "{'description': ['Time specified in hours'], 'default': 0}",
    "days_of_month_minutes": "{'description': ['Time specified in minutes.'], 'default': 0}",
    "days_of_month_monthdays": "{'description': ['List of days of the month (1-31)']}",
    "days_of_week_hours": "{'description': ['Time specified in hours'], 'default': 0}",
    "days_of_week_minutes": "{'description': ['Time specified in minutes.'], 'default': 0}",
    "days_of_week_weekdays": "{'description': ['List of days of the week (Sunday to Saturday)']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "name": "{'description': ['Name for the snapshot schedule.', 'It accepts either schedule_id or schedule_name', 'if name is digit, it will consider as schedule_id', 'If name is string, it will consider as schedule_name']}",
    "password": "{'required': True, 'description': ['Element SW access account password'], 'aliases': ['pass']}",
    "paused": "{'description': ['Pause / Resume a schedule.'], 'type': 'bool'}",
    "recurring": "{'description': ['Should the schedule recur?'], 'type': 'bool'}",
    "retention": "{'description': ['Retention period for the snapshot.', "Format is 'HH:mm:ss'."]}",
    "schedule_type": "{'description': ['Schedule type for creating schedule.'], 'choices': ['DaysOfWeekFrequency', 'DaysOfMonthFrequency', 'TimeIntervalFrequency']}",
    "snapshot_name": "{'description': ['Name for the created snapshots.']}",
    "starting_date": "{'description': ['Starting date for the schedule.', 'Required when C(state=present).', 'Format: C(2016-12-01T00:00:00Z)']}",
    "state": "{'description': ['Whether the specified schedule should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "time_interval_days": "{'description': ['Time interval in days.'], 'default': 1}",
    "time_interval_hours": "{'description': ['Time interval in hours.'], 'default': 0}",
    "time_interval_minutes": "{'description': ['Time interval in minutes.'], 'default': 0}",
    "username": "{'required': True, 'description': ['Element SW access account user-name'], 'aliases': ['user']}",
    "volumes": "{'description': ['Volume IDs that you want to set the snapshot schedule for.', 'It accepts both volume_name and volume_id']}",
}
```

## Examples


``` yaml

   - name: Create Snapshot schedule
     na_elementsw_snapshot_schedule:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       name: Schedule_A
       schedule_type: TimeIntervalFrequency
       time_interval_days: 1
       starting_date: '2016-12-01T00:00:00Z'
       volumes:
       - 7
       - test
       account_id: 1

   - name: Update Snapshot schedule
     na_elementsw_snapshot_schedule:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       name: Schedule_A
       schedule_type: TimeIntervalFrequency
       time_interval_days: 1
       starting_date: '2016-12-01T00:00:00Z'
       volumes:
       - 8
       - test1
       account_id: 1

   - name: Delete Snapshot schedule
     na_elementsw_snapshot_schedule:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       name: 6

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
