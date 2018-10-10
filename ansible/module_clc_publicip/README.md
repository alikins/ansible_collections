# Ansible module: ansible.module_clc_publicip


Add and Delete public ips on servers in CenturyLink Cloud

## Description

An Ansible module to add or delete public ip addresses on an existing server or servers in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "ports": "{'description': ["A list of ports to expose. This is required when state is 'present'"]}",
    "protocol": "{'description': ['The protocol that the public IP will listen for.'], 'default': 'TCP', 'choices': ['TCP', 'UDP', 'ICMP']}",
    "server_ids": "{'description': ['A list of servers to create public ips on.'], 'required': True}",
    "state": "{'description': ['Determine whether to create or delete public IPs. If present module will not create a second public ip if one already exists.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "wait": "{'description': ['Whether to wait for the tasks to finish before returning.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Add Public IP to Server
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create Public IP For Servers
      clc_publicip:
        protocol: TCP
        ports:
          - 80
        server_ids:
          - UC1TEST-SVR01
          - UC1TEST-SVR02
        state: present
      register: clc

    - name: debug
      debug:
        var: clc

- name: Delete Public IP from Server
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create Public IP For Servers
      clc_publicip:
        server_ids:
          - UC1TEST-SVR01
          - UC1TEST-SVR02
        state: absent
      register: clc

    - name: debug
      debug:
        var: clc

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
