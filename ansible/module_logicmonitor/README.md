# Ansible module: ansible.module_logicmonitor


Manage your LogicMonitor account through Ansible Playbooks

## Description

LogicMonitor is a hosted, full-stack, infrastructure monitoring platform.
This module manages hosts, host groups, and collectors within your LogicMonitor account.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The action you wish to perform on target.', 'Add: Add an object to your LogicMonitor account.', 'Remove: Remove an object from your LogicMonitor account.', 'Update: Update properties, description, or groups (target=host) for an object in your LogicMonitor account.', 'SDT: Schedule downtime for an object in your LogicMonitor account.'], 'required': True, 'choices': ['add', 'remove', 'update', 'sdt']}",
    "alertenable": "{'description': ['A boolean flag to turn alerting on or off for an object.', 'Optional for managing all hosts (action=add or action=update).'], 'type': 'bool', 'default': True}",
    "collector": "{'description': ['The fully qualified domain name of a collector in your LogicMonitor account.', 'This is required for the creation of a LogicMonitor host (target=host action=add).', "This is required for updating, removing or scheduling downtime for hosts if 'displayname' isn't specified (target=host action=update action=remove action=sdt)."]}",
    "company": "{'description': ['The LogicMonitor account company name. If you would log in to your account at "superheroes.logicmonitor.com" you would use "superheroes."'], 'required': True}",
    "description": "{'description': ['The long text description of the object in your LogicMonitor account.', 'Optional for managing hosts and host groups (target=host or target=hostgroup; action=add or action=update).'], 'default': ''}",
    "displayname": "{'description': ['The display name of a host in your LogicMonitor account or the desired display name of a device to manage.', 'Optional for managing hosts (target=host).'], 'default': 'hostname -f'}",
    "duration": "{'description': ['The duration (minutes) of the Scheduled Down Time (SDT).', 'Optional for putting an object into SDT (action=sdt).'], 'default': 30}",
    "fullpath": "{'description': ['The fullpath of the host group object you would like to manage.', 'Recommend running on a single Ansible host.', 'Required for management of LogicMonitor host groups (target=hostgroup).']}",
    "groups": "{'description': ['A list of groups that the host should be a member of.', 'Optional for managing hosts (target=host; action=add or action=update).'], 'default': []}",
    "hostname": "{'description': ['The hostname of a host in your LogicMonitor account, or the desired hostname of a device to manage.', 'Optional for managing hosts (target=host).'], 'default': 'hostname -f'}",
    "id": "{'description': ['ID of the datasource to target.', 'Required for management of LogicMonitor datasources (target=datasource).']}",
    "password": "{'description': ['The password of the specified LogicMonitor user'], 'required': True}",
    "properties": "{'description': ['A dictionary of properties to set on the LogicMonitor host or host group.', 'Optional for managing hosts and host groups (target=host or target=hostgroup; action=add or action=update).', 'This parameter will add or update existing properties in your LogicMonitor account.'], 'default': {}}",
    "starttime": "{'description': ['The time that the Scheduled Down Time (SDT) should begin.', 'Optional for managing SDT (action=sdt).', 'Y-m-d H:M'], 'default': 'Now'}",
    "target": "{'description': ['The type of LogicMonitor object you wish to manage.', 'Collector: Perform actions on a LogicMonitor collector.', "NOTE You should use Ansible service modules such as M(service) or M(supervisorctl) for managing the Collector 'logicmonitor-agent' and 'logicmonitor-watchdog' services. Specifically, you'll probably want to start these services after a Collector add and stop these services before a Collector remove.", 'Host: Perform actions on a host device.', 'Hostgroup: Perform actions on a LogicMonitor host group.', 'NOTE Host and Hostgroup tasks should always be performed via delegate_to: localhost. There are no benefits to running these tasks on the remote host and doing so will typically cause problems.\n'], 'required': True, 'choices': ['collector', 'host', 'datsource', 'hostgroup']}",
    "user": "{'description': ['A LogicMonitor user name. The module will authenticate and perform actions on behalf of this user.'], 'required': True}",
}
```

## Examples


``` yaml

# example of adding a new LogicMonitor collector to these devices
---
- hosts: collectors
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Deploy/verify LogicMonitor collectors
    become: yes
    logicmonitor:
      target: collector
      action: add
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'

#example of adding a list of hosts into monitoring
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Deploy LogicMonitor Host
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: host
      action: add
      collector: mycompany-Collector
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      groups: /servers/production,/datacenter1
      properties:
        snmp.community: secret
        dc: 1
        type: prod
    delegate_to: localhost

#example of putting a datasource in SDT
---
- hosts: localhost
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: SDT a datasource
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: datasource
      action: sdt
      id: 123
      duration: 3000
      starttime: '2017-03-04 05:06'
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'

#example of creating a hostgroup
---
- hosts: localhost
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Create a host group
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: add
      fullpath: /servers/development
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      properties:
        snmp.community: commstring
        type: dev

#example of putting a list of hosts into SDT
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: SDT hosts
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: host
      action: sdt
      duration: 3000
      starttime: '2016-11-10 09:08'
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      collector: mycompany-Collector
    delegate_to: localhost

#example of putting a host group in SDT
---
- hosts: localhost
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: SDT a host group
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: sdt
      fullpath: /servers/development
      duration: 3000
      starttime: '2017-03-04 05:06'
      company=: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'

#example of updating a list of hosts
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Update a list of hosts
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: host
      action: update
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      collector: mycompany-Collector
      groups: /servers/production,/datacenter5
      properties:
        snmp.community: commstring
        dc: 5
    delegate_to: localhost

#example of updating a hostgroup
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Update a host group
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: update
      fullpath: /servers/development
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      properties:
        snmp.community: hg
        type: dev
        status: test
    delegate_to: localhost

#example of removing a list of hosts from monitoring
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Remove LogicMonitor hosts
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: host
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      collector: mycompany-Collector
    delegate_to: localhost

#example of removing a host group
---
- hosts: hosts
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Remove LogicMonitor development servers hostgroup
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      fullpath: /servers/development
    delegate_to: localhost
  - name: Remove LogicMonitor servers hostgroup
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      fullpath: /servers
    delegate_to: localhost
  - name: Remove LogicMonitor datacenter1 hostgroup
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      fullpath: /datacenter1
    delegate_to: localhost
  - name: Remove LogicMonitor datacenter5 hostgroup
    # All tasks except for target=collector should use delegate_to: localhost
    logicmonitor:
      target: hostgroup
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      fullpath: /datacenter5
    delegate_to: localhost

### example of removing a new LogicMonitor collector to these devices
---
- hosts: collectors
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Remove LogicMonitor collectors
    become: yes
    logicmonitor:
      target: collector
      action: remove
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'

#complete example
---
- hosts: localhost
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Create a host group
    logicmonitor:
      target: hostgroup
      action: add
      fullpath: /servers/production/database
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      properties:
        snmp.community: commstring
  - name: SDT a host group
    logicmonitor:
      target: hostgroup
      action: sdt
      fullpath: /servers/production/web
      duration: 3000
      starttime: '2012-03-04 05:06'
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'

- hosts: collectors
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: Deploy/verify LogicMonitor collectors
    logicmonitor:
      target: collector
      action: add
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
  - name: Place LogicMonitor collectors into 30 minute Scheduled downtime
    logicmonitor:
      target: collector
      action: sdt
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
  - name: Deploy LogicMonitor Host
    logicmonitor:
      target: host
      action: add
      collector: agent1.ethandev.com
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      properties:
        snmp.community: commstring
        dc: 1
      groups: /servers/production/collectors, /datacenter1
    delegate_to: localhost

- hosts: database-servers
  remote_user: '{{ username }}'
  vars:
    company: mycompany
    user: myusername
    password: mypassword
  tasks:
  - name: deploy logicmonitor hosts
    logicmonitor:
      target: host
      action: add
      collector: monitoring.dev.com
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
      properties:
        snmp.community: commstring
        type: db
        dc: 1
      groups: /servers/production/database, /datacenter1
    delegate_to: localhost
  - name: schedule 5 hour downtime for 2012-11-10 09:08
    logicmonitor:
      target: host
      action: sdt
      duration: 3000
      starttime: '2012-11-10 09:08'
      company: '{{ company }}'
      user: '{{ user }}'
      password: '{{ password }}'
    delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ethan Culler-Mayeno (@ethanculler)', 'Jeff Wozniak (@woz5999)']
  - ['Ethan Culler-Mayeno (@ethanculler)', 'Jeff Wozniak (@woz5999)']
