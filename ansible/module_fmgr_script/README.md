# Ansible module: ansible.module_fmgr_script


Add/Edit/Delete and execute scripts

## Description

C
r
e
a
t
e
/
e
d
i
t
/
d
e
l
e
t
e
 
s
c
r
i
p
t
s
 
a
n
d
 
e
x
e
c
u
t
e
 
t
h
e
 
s
c
r
i
p
t
s
 
o
n
 
t
h
e
 
F
o
r
t
i
M
a
n
a
g
e
r
 
u
s
i
n
g
 
j
s
o
n
r
p
c
 
A
P
I

## Requirements

TODO

## Arguments

``` json
{
    "adom": "{'description': ['The administrative domain (admon) the configuration belongs to'], 'required': True}",
    "host": "{'description': ["The FortiManager's Address."], 'required': True}",
    "password": "{'description': ['The password associated with the username account.'], 'required': False}",
    "script_content": "{'description': ['The script content that will be executed.'], 'required': False}",
    "script_description": "{'description': ['The description of the script.'], 'required': False}",
    "script_name": "{'description': ['The name of the script.'], 'required': True}",
    "script_package": "{'description': ['(datasource) Policy package object to run the script against'], 'required': False}",
    "script_scope": "{'description': ['(datasource) The devices that the script will run on, can have both device member and device group member.'], 'required': False}",
    "script_target": "{'description': ['The target of the script to be run.'], 'required': False}",
    "script_type": "{'description': ['The type of script (CLI or TCL).'], 'required': False}",
    "state": "{'description': ['The desired state of the specified object.', 'present - will create a script.', 'execute - execute the scipt.', 'delete - delete the script.'], 'required': False, 'default': 'present', 'choices': ['present', 'execute', 'delete']}",
    "username": "{'description': ['The username to log into the FortiManager'], 'required': True}",
    "vdom": "{'description': ['The virtual domain (vdom) the configuration belongs to']}",
}
```

## Examples


``` yaml

- name: CREATE SCRIPT
  fmgr_script:
    host: "{{inventory_hostname}}"
    username: "{{ username }}"
    password: "{{ password }}"
    adom: "root"
    script_name: "TestScript"
    script_type: "cli"
    script_target: "remote_device"
    script_description: "Create by Ansible"
    script_content: "get system status"

- name: EXECUTE SCRIPT
  fmgr_script:
    host: "{{inventory_hostname}}"
    username: "{{ username }}"
    password: "{{ password }}"
    adom: "root"
    script_name: "TestScript"
    state: "execute"
    script_scope: "FGT1,FGT2"

- name: DELETE SCRIPT
  fmgr_script:
    host: "{{inventory_hostname}}"
    username: "{{ username }}"
    password: "{{ password }}"
    adom: "root"
    script_name: "TestScript"
    state: "delete"

```

## License

TODO

## Author Information
  - ['Andrew Welsh']
