# Ansible module: ansible.module_snow_record


Create/Delete/Update records in ServiceNow

## Description

Creates/Deletes/Updates a single record in ServiceNow

## Requirements

TODO

## Arguments

``` json
{
    "attachment": "{'description': ['Attach a file to the record'], 'required': False}",
    "data": "{'description': ['key, value pairs of data to load into the record. See Examples. Required for C(state:present)']}",
    "instance": "{'description': ['The service now instance name'], 'required': True}",
    "lookup_field": "{'description': ['Changes the field that C(number) uses to find records'], 'required': False, 'default': 'number'}",
    "number": "{'description': ['Record number to update. Required for C(state:absent)'], 'required': False}",
    "password": "{'description': ['Password for username'], 'required': True}",
    "state": "{'description': ['If C(present) is supplied with a C(number) argument, the module will attempt to update the record with the supplied data.  If no such record exists, a new one will be created.  C(absent) will delete a record.'], 'choices': ['present', 'absent'], 'required': True}",
    "table": "{'description': ['Table to query for records'], 'required': False, 'default': 'incident'}",
    "username": "{'description': ['User to connect to ServiceNow as'], 'required': True}",
}
```

## Examples


``` yaml

- name: Grab a user record
  snow_record:
    username: ansible_test
    password: my_password
    instance: dev99999
    state: present
    number: 62826bf03710200044e0bfc8bcbe5df1
    table: sys_user
    lookup_field: sys_id

- name: Create an incident
  snow_record:
    username: ansible_test
    password: my_password
    instance: dev99999
    state: present
    data:
      short_description: "This is a test incident opened by Ansible"
      severity: 3
      priority: 2
  register: new_incident

- name: Delete the record we just made
  snow_record:
    username: admin
    password: xxxxxxx
    instance: dev99999
    state: absent
    number: "{{new_incident['record']['number']}}"

- name: Delete a non-existant record
  snow_record:
    username: ansible_test
    password: my_password
    instance: dev99999
    state: absent
    number: 9872354
  failed_when: false

- name: Update an incident
  snow_record:
    username: ansible_test
    password: my_password
    instance: dev99999
    state: present
    number: INC0000055
    data:
      work_notes : "Been working all day on this thing."

- name: Attach a file to an incident
  snow_record:
    username: ansible_test
    password: my_password
    instance: dev99999
    state: present
    number: INC0000055
    attachment: README.md
  tags: attach

```

## License

TODO

## Author Information
  - ['Tim Rightnour (@garbled1)']
