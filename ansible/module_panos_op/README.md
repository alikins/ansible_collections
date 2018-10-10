# Ansible module: ansible.module_panos_op


execute arbitrary OP commands on PANW devices (e.g. show interface all)

## Description

T
h
i
s
 
m
o
d
u
l
e
 
w
i
l
l
 
a
l
l
o
w
 
u
s
e
r
 
t
o
 
p
a
s
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
 
a
n
y
 
s
u
p
p
o
r
t
e
d
 
O
P
 
c
o
m
m
a
n
d
 
o
n
 
t
h
e
 
P
A
N
W
 
d
e
v
i
c
e
.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "cmd": "{'description': ['The OP command to be performed.'], 'required': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device or Panorama management console being configured.'], 'required': True}",
    "password": "{'description': ['Password credentials to use for authentication.'], 'required': True}",
    "username": "{'description': ['Username credentials to use for authentication.'], 'required': False, 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: show list of all interfaces
  panos_op:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    cmd: 'show interfaces all'

- name: show system info
  panos_op:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    cmd: 'show system info'

```

## License

TODO

## Author Information
  - ['Ivan Bojer (@ivanbojer)']
