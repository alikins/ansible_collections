# Ansible module: ansible.module_panos_query_rules


PANOS module that allows search for security rules in PANW NGFW devices

## Description

-
 
S
e
c
u
r
i
t
y
 
p
o
l
i
c
i
e
s
 
a
l
l
o
w
 
y
o
u
 
t
o
 
e
n
f
o
r
c
e
 
r
u
l
e
s
 
a
n
d
 
t
a
k
e
 
a
c
t
i
o
n
,
 
a
n
d
 
c
a
n
 
b
e
 
a
s
 
g
e
n
e
r
a
l
 
o
r
 
s
p
e
c
i
f
i
c
 
a
s
 
n
e
e
d
e
d
.
 
T
h
e
 
p
o
l
i
c
y
 
r
u
l
e
s
 
a
r
e
 
c
o
m
p
a
r
e
d
 
a
g
a
i
n
s
t
 
t
h
e
 
i
n
c
o
m
i
n
g
 
t
r
a
f
f
i
c
 
i
n
 
s
e
q
u
e
n
c
e
,
 
a
n
d
 
b
e
c
a
u
s
e
 
t
h
e
 
f
i
r
s
t
 
r
u
l
e
 
t
h
a
t
 
m
a
t
c
h
e
s
 
t
h
e
 
t
r
a
f
f
i
c
 
i
s
 
a
p
p
l
i
e
d
,
 
t
h
e
 
m
o
r
e
 
s
p
e
c
i
f
i
c
 
r
u
l
e
s
 
m
u
s
t
 
p
r
e
c
e
d
e
 
t
h
e
 
m
o
r
e
 
g
e
n
e
r
a
l
 
o
n
e
s
.



## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "application": "{'description': ['Name of the application or application group to be queried.']}",
    "destination_ip": "{'description': ['The destination IP address to be queried.']}",
    "destination_port": "{'description': ['The destination port to be queried.']}",
    "destination_zone": "{'description': ['Name of the destination security zone to be queried.']}",
    "devicegroup": "{'description': ['The Panorama device group in which to conduct the query.']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS firewall or Panorama management console being queried.'], 'required': True}",
    "password": "{'description': ['Password credentials to use for authentication.'], 'required': True}",
    "protocol": "{'description': ['The protocol used to be queried.  Must be either I(tcp) or I(udp).']}",
    "source_ip": "{'description': ['The source IP address to be queried.']}",
    "source_port": "{'description': ['The source port to be queried.']}",
    "source_zone": "{'description': ['Name of the source security zone to be queried.']}",
    "tag_name": "{'description': ['Name of the rule tag to be queried.']}",
    "username": "{'description': ['Username credentials to use for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: search for rules with tcp/3306
  panos_query_rules:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    source_zone: 'DevNet'
    destination_zone: 'DevVPC'
    destination_port: '3306'
    protocol: 'tcp'

- name: search devicegroup for inbound rules to dmz host
  panos_query_rules:
    ip_address: '{{ ip_address }}'
    api_key: '{{ api_key }}'
    destination_zone: 'DMZ'
    destination_ip: '10.100.42.18'
    address: 'DeviceGroupA'

- name: search for rules containing a specified rule tag
  panos_query_rules:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    tag_name: 'ProjectX'

```

## License

TODO

## Author Information
  - ['Bob Hagen (@rnh556)']
