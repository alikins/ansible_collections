# Ansible module: ansible.module_netapp_e_host


NetApp E-Series manage eseries hosts

## Description

C
r
e
a
t
e
,
 
u
p
d
a
t
e
,
 
r
e
m
o
v
e
 
h
o
s
t
s
 
o
n
 
N
e
t
A
p
p
 
E
-
s
e
r
i
e
s
 
s
t
o
r
a
g
e
 
a
r
r
a
y
s

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "force_port": "{'description': ['Allow ports that are already assigned to be re-assigned to your current host'], 'required': False, 'type': 'bool', 'version_added': 2.7}",
    "group": "{'description': ['The unique identifier of the host-group you want the host to be a member of; this is used for clustering.'], 'required': False, 'aliases': ['cluster']}",
    "host_type_index": "{'description': ['The index that maps to host type you wish to create. It is recommended to use the M(netapp_e_facts) module to gather this information. Alternatively you can use the WSP portal to retrieve the information.', 'Required when C(state=present)'], 'aliases': ['host_type']}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False, 'version_added': 2.7}",
    "name": "{'description': ["If the host doesn't yet exist, the label/name to assign at creation time.", 'If the hosts already exists, this will be used to uniquely identify the host to make any required changes'], 'required': True, 'aliases': ['label']}",
    "ports": "{'description': ['A list of host ports you wish to associate with the host.', 'Host ports are uniquely identified by their WWN or IQN. Their assignments to a particular host are uniquely identified by a label and these must be unique.'], 'required': False, 'suboptions': {'type': {'description': ['The interface type of the port to define.', 'Acceptable choices depend on the capabilities of the target hardware/software platform.'], 'required': True, 'choices': ['iscsi', 'sas', 'fc', 'ib', 'nvmeof', 'ethernet']}, 'label': {'description': ['A unique label to assign to this port assignment.'], 'required': True}, 'port': {'description': ['The WWN or IQN of the hostPort to assign to this port definition.'], 'required': True}}}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Set to absent to remove an existing host', 'Set to present to modify or create a new host definition'], 'choices': ['absent', 'present'], 'default': 'present', 'version_added': 2.7}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Define or update an existing host named 'Host1'
      netapp_e_host:
        ssid: "1"
        api_url: "10.113.1.101:8443"
        api_username: "admin"
        api_password: "myPassword"
        name: "Host1"
        state: present
        host_type_index: 28
        ports:
          - type: 'iscsi'
            label: 'PORT_1'
            port: 'iqn.1996-04.de.suse:01:56f86f9bd1fe'
          - type: 'fc'
            label: 'FC_1'
            port: '10:00:FF:7C:FF:FF:FF:01'
          - type: 'fc'
            label: 'FC_2'
            port: '10:00:FF:7C:FF:FF:FF:00'

    - name: Ensure a host named 'Host2' doesn't exist
      netapp_e_host:
        ssid: "1"
        api_url: "10.113.1.101:8443"
        api_username: "admin"
        api_password: "myPassword"
        name: "Host2"
        state: absent


```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
