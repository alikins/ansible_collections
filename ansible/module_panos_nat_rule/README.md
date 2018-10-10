# Ansible module: ansible.module_panos_nat_rule


create a policy NAT rule

## Description

-
 
C
r
e
a
t
e
 
a
 
p
o
l
i
c
y
 
n
a
t
 
r
u
l
e
.
 
K
e
e
p
 
i
n
 
m
i
n
d
 
t
h
a
t
 
w
e
 
c
a
n
 
e
i
t
h
e
r
 
e
n
d
 
u
p
 
c
o
n
f
i
g
u
r
i
n
g
 
s
o
u
r
c
e
 
N
A
T
,
 
d
e
s
t
i
n
a
t
i
o
n
 
N
A
T
,
 
o
r
 
b
o
t
h
.
 
I
n
s
t
e
a
d
 
o
f
 
s
p
l
i
t
t
i
n
g
 
i
t
 
i
n
t
o
 
t
w
o
 
w
e
 
w
i
l
l
 
m
a
k
e
 
a
 
f
a
i
r
 
a
t
t
e
m
p
t
 
t
o
 
d
e
t
e
r
m
i
n
e
 
w
h
i
c
h
 
o
n
e
 
t
h
e
 
u
s
e
r
 
w
a
n
t
s
.



## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "commit": "{'description': ['Commit configuration if changed.'], 'type': 'bool', 'default': True}",
    "destination_ip": "{'description': ['list of destination addresses'], 'default': ['any']}",
    "destination_zone": "{'description': ['destination zone'], 'required': True}",
    "dnat_address": "{'description': ['dnat translated address']}",
    "dnat_port": "{'description': ['dnat translated port']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device being configured.'], 'required': True}",
    "operation": "{'description': ['The action to be taken.  Supported values are I(add)/I(update)/I(find)/I(delete).']}",
    "password": "{'description': ['Password credentials to use for auth unless I(api_key) is set.'], 'required': True}",
    "rule_name": "{'description': ['name of the SNAT rule'], 'required': True}",
    "service": "{'description': ['service'], 'default': 'any'}",
    "snat_address_type": "{'description': ['type of source translation. Supported values are I(translated-address)/I(translated-address).'], 'default': 'translated-address'}",
    "snat_bidirectional": "{'description': ['bidirectional flag'], 'type': 'bool', 'default': False}",
    "snat_dynamic_address": "{'description': ['Source NAT translated address. Used with Dynamic-IP and Dynamic-IP-and-Port.']}",
    "snat_interface": "{'description': ['snat interface']}",
    "snat_interface_address": "{'description': ['snat interface address']}",
    "snat_static_address": "{'description': ['Source NAT translated address. Used with Static-IP translation.']}",
    "snat_type": "{'description': ['type of source translation']}",
    "source_ip": "{'description': ['list of source addresses'], 'default': ['any']}",
    "source_zone": "{'description': ['list of source zones'], 'required': True}",
    "username": "{'description': ['Username credentials to use for auth unless I(api_key) is set.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# Create a source and destination nat rule
  - name: Create NAT SSH rule for 10.0.1.101
    panos_nat_rule:
      ip_address: '{{ ip_address }}'
      username: '{{ username }}'
      password: '{{ password }}'
      rule_name: "Web SSH"
      source_zone: ["external"]
      destination_zone: "external"
      source: ["any"]
      destination: ["10.0.0.100"]
      service: "service-tcp-221"
      snat_type: "dynamic-ip-and-port"
      snat_interface: "ethernet1/2"
      dnat_address: "10.0.1.101"
      dnat_port: "22"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer), Robert Hagen (@rnh556)']
