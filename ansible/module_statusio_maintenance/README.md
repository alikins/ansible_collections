# Ansible module: ansible.module_statusio_maintenance


Create maintenance windows for your status.io dashboard

## Description

Creates a maintenance window for status.io
Deletes a maintenance window for status.io

## Requirements

TODO

## Arguments

``` json
{
    "all_infrastructure_affected": "{'description': ['If it affects all components and containers'], 'type': 'bool', 'default': False}",
    "api_id": "{'description': ['Your unique API ID from status.io'], 'required': True}",
    "api_key": "{'description': ['Your unique API Key from status.io'], 'required': True}",
    "automation": "{'description': ['Automatically start and end the maintenance window'], 'type': 'bool', 'default': False}",
    "components": "{'description': ['The given name of your component (server name)'], 'aliases': ['component']}",
    "containers": "{'description': ['The given name of your container (data center)'], 'aliases': ['container']}",
    "desc": "{'description': ['Message describing the maintenance window'], 'default': 'Created by Ansible'}",
    "maintenance_id": "{'description': ['The maintenance id number when deleting a maintenance window']}",
    "maintenance_notify_1_hr": "{'description': ['Notify subscribers 1 hour before maintenance start time'], 'type': 'bool', 'default': False}",
    "maintenance_notify_24_hr": "{'description': ['Notify subscribers 24 hours before maintenance start time'], 'type': 'bool', 'default': False}",
    "maintenance_notify_72_hr": "{'description': ['Notify subscribers 72 hours before maintenance start time'], 'type': 'bool', 'default': False}",
    "maintenance_notify_now": "{'description': ['Notify subscribers now'], 'type': 'bool', 'default': False}",
    "minutes": "{'description': ['The length of time in UTC that the maintenance will run             (starting from playbook runtime)'], 'default': 10}",
    "start_date": "{'description': ['Date maintenance is expected to start (Month/Day/Year) (UTC)', 'End Date is worked out from start_date + minutes']}",
    "start_time": "{'description': ['Time maintenance is expected to start (Hour:Minutes) (UTC)', 'End Time is worked out from start_time + minutes']}",
    "state": "{'description': ['Desired state of the package.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "statuspage": "{'description': ['Your unique StatusPage ID from status.io'], 'required': True}",
    "title": "{'description': ['A descriptive title for the maintenance window'], 'default': 'A new maintenance window'}",
    "url": "{'description': ['Status.io API URL. A private apiary can be used instead.'], 'default': 'https://api.status.io'}",
}
```

## Examples


``` yaml

- name: Create a maintenance window for 10 minutes on server1, with automation to stop the maintenance
  statusio_maintenance:
    title: Router Upgrade from ansible
    desc: Performing a Router Upgrade
    components: server1.example.com
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    maintenance_notify_1_hr: True
    automation: True

- name: Create a maintenance window for 60 minutes on server1 and server2
  statusio_maintenance:
    title: Routine maintenance
    desc: Some security updates
    components:
      - server1.example.com
      - server2.example.com
    minutes: 60
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    maintenance_notify_1_hr: True
    automation: True
  delegate_to: localhost

- name: Create a future maintenance window for 24 hours to all hosts inside the Primary Data Center
  statusio_maintenance:
    title: Data center downtime
    desc: Performing a Upgrade to our data center
    components: Primary Data Center
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    start_date: 01/01/2016
    start_time: 12:00
    minutes: 1440

- name: Delete a maintenance window
  statusio_maintenance:
    title: Remove a maintenance window
    maintenance_id: 561f90faf74bc94a4700087b
    statuspage: statuspage_id
    api_id: api_id
    api_key: api_key
    state: absent


```

## License

TODO

## Author Information
  - ['Benjamin Copeland (@bhcopeland) <ben@copeland.me.uk>']
