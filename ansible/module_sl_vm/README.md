# Ansible module: ansible.module_sl_vm


create or cancel a virtual instance in SoftLayer

## Description

Creates or cancels SoftLayer instances.
When created, optionally waits for it to be 'running'.

## Requirements

TODO

## Arguments

``` json
{
    "cpus": "{'description': ['Count of cpus to be assigned to new virtual instance.'], 'required': True}",
    "datacenter": "{'description': ['Datacenter for the virtual instance to be deployed.']}",
    "dedicated": "{'description': ['Flag to determine if the instance should be deployed in dedicated space.'], 'type': 'bool', 'default': False}",
    "disks": "{'description': ['List of disk sizes to be assigned to new virtual instance.'], 'required': True, 'default': [25]}",
    "domain": "{'description': ['Domain name to be provided to a virtual instance.']}",
    "hostname": "{'description': ['Hostname to be provided to a virtual instance.']}",
    "hourly": "{'description': ['Flag to determine if the instance should be hourly billed.'], 'type': 'bool', 'default': True}",
    "image_id": "{'description': ['Image Template to be used for new virtual instance.']}",
    "instance_id": "{'description': ['Instance Id of the virtual instance to perform action option.']}",
    "local_disk": "{'description': ['Flag to determine if local disk should be used for the new instance.'], 'type': 'bool', 'default': True}",
    "memory": "{'description': ['Amount of memory to be assigned to new virtual instance.'], 'required': True}",
    "nic_speed": "{'description': ['NIC Speed to be assigned to new virtual instance.'], 'default': 10}",
    "os_code": "{'description': ['OS Code to be used for new virtual instance.']}",
    "post_uri": "{'description': ['URL of a post provisioning script to be loaded and executed on virtual instance.']}",
    "private": "{'description': ['Flag to determine if the instance should be private only.'], 'type': 'bool', 'default': False}",
    "private_vlan": "{'description': ['VLAN by its Id to be assigned to the private NIC.']}",
    "public_vlan": "{'description': ['VLAN by its Id to be assigned to the public NIC.']}",
    "ssh_keys": "{'description': ['List of ssh keys by their Id to be assigned to a virtual instance.']}",
    "state": "{'description': ['Create, or cancel a virtual instance.', 'Specify C(present) for create, C(absent) to cancel.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "tags": "{'description': ['Tag or list of tags to be provided to a virtual instance.']}",
    "wait": "{'description': ['Flag used to wait for active status before returning.'], 'type': 'bool', 'default': True}",
    "wait_time": "{'description': ['Time in seconds before wait returns.'], 'default': 600}",
}
```

## Examples


``` yaml

- name: Build instance
  hosts: localhost
  gather_facts: no
  tasks:
  - name: Build instance request
    sl_vm:
      hostname: instance-1
      domain: anydomain.com
      datacenter: dal09
      tags: ansible-module-test
      hourly: yes
      private: no
      dedicated: no
      local_disk: yes
      cpus: 1
      memory: 1024
      disks: [25]
      os_code: UBUNTU_LATEST
      wait: no

- name: Build additional instances
  hosts: localhost
  gather_facts: no
  tasks:
  - name: Build instances request
    sl_vm:
      hostname: "{{ item.hostname }}"
      domain: "{{ item.domain }}"
      datacenter: "{{ item.datacenter }}"
      tags: "{{ item.tags }}"
      hourly: "{{ item.hourly }}"
      private: "{{ item.private }}"
      dedicated: "{{ item.dedicated }}"
      local_disk: "{{ item.local_disk }}"
      cpus: "{{ item.cpus }}"
      memory: "{{ item.memory }}"
      disks: "{{ item.disks }}"
      os_code: "{{ item.os_code }}"
      ssh_keys: "{{ item.ssh_keys }}"
      wait: "{{ item.wait }}"
    with_items:
      - hostname: instance-2
        domain: anydomain.com
        datacenter: dal09
        tags:
          - ansible-module-test
          - ansible-module-test-slaves
        hourly: yes
        private: no
        dedicated: no
        local_disk: yes
        cpus: 1
        memory: 1024
        disks:
          - 25
          - 100
        os_code: UBUNTU_LATEST
        ssh_keys: []
        wait: True
      - hostname: instance-3
        domain: anydomain.com
        datacenter: dal09
        tags:
          - ansible-module-test
          - ansible-module-test-slaves
        hourly: yes
        private: no
        dedicated: no
        local_disk: yes
        cpus: 1
        memory: 1024
        disks:
          - 25
          - 100
        os_code: UBUNTU_LATEST
        ssh_keys: []
        wait: yes

- name: Cancel instances
  hosts: localhost
  gather_facts: no
  tasks:
  - name: Cancel by tag
    sl_vm:
      state: absent
      tags: ansible-module-test

```

## License

TODO

## Author Information
  - ['Matt Colton (@mcltn)']
