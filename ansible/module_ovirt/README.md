# Ansible module: ansible.module_ovirt


oVirt/RHEV platform management

## Description

This module only supports oVirt/RHEV version 3. A newer module M(ovirt_vm) supports oVirt/RHV version 4.
Allows you to create new instances, either from scratch or an image, in addition to deleting or stopping instances on the oVirt/RHEV platform.

## Requirements

TODO

## Arguments

``` json
{
    "disk_alloc": "{'description': ['Define whether disk is thin or preallocated.'], 'choices': ['preallocated', 'thin'], 'default': 'thin'}",
    "disk_int": "{'description': ['Interface type of the disk.'], 'choices': ['ide', 'virtio'], 'default': 'virtio'}",
    "image": "{'description': ['The template to use for the instance.']}",
    "instance_cores": "{'description': ["Define the instance's number of cores."], 'default': 1, 'aliases': ['vmcores']}",
    "instance_cpus": "{'description': ["The instance's number of CPUs."], 'default': 1, 'aliases': ['vmcpus']}",
    "instance_disksize": "{'description': ["Size of the instance's disk in GB."], 'aliases': ['vm_disksize']}",
    "instance_dns": "{'description': ["Define the instance's Primary DNS server."], 'aliases': ['dns'], 'version_added': '2.1'}",
    "instance_domain": "{'description': ["Define the instance's Domain."], 'aliases': ['domain'], 'version_added': '2.1'}",
    "instance_hostname": "{'description': ["Define the instance's Hostname."], 'aliases': ['hostname'], 'version_added': '2.1'}",
    "instance_ip": "{'description': ["Define the instance's IP."], 'aliases': ['ip'], 'version_added': '2.1'}",
    "instance_key": "{'description': ["Define the instance's Authorized key."], 'aliases': ['key'], 'version_added': '2.1'}",
    "instance_mem": "{'description': ["The instance's amount of memory in MB."], 'aliases': ['vmmem']}",
    "instance_name": "{'description': ['The name of the instance to use.'], 'required': True, 'aliases': ['vmname']}",
    "instance_netmask": "{'description': ["Define the instance's Netmask."], 'aliases': ['netmask'], 'version_added': '2.1'}",
    "instance_network": "{'description': ['The logical network the machine should belong to.'], 'default': 'rhevm', 'aliases': ['vmnetwork']}",
    "instance_nic": "{'description': ['The name of the network interface in oVirt/RHEV.'], 'aliases': ['vmnic']}",
    "instance_os": "{'description': ['Type of Operating System.'], 'aliases': ['vmos']}",
    "instance_rootpw": "{'description': ["Define the instance's Root password."], 'aliases': ['rootpw'], 'version_added': '2.1'}",
    "instance_type": "{'description': ['Define whether the instance is a server, desktop or high_performance.', 'I(high_performance) is supported since Ansible 2.5 and oVirt/RHV 4.2.'], 'choices': ['desktop', 'server', 'high_performance'], 'default': 'server', 'aliases': ['vmtype']}",
    "password": "{'description': ['Password of the user to authenticate with.'], 'required': True}",
    "region": "{'description': ['The oVirt/RHEV datacenter where you want to deploy to.']}",
    "resource_type": "{'description': ['Whether you want to deploy an image or create an instance from scratch.'], 'choices': ['new', 'template']}",
    "sdomain": "{'description': ["The Storage Domain where you want to create the instance's disk on."]}",
    "state": "{'description': ['Create, terminate or remove instances.'], 'choices': ['absent', 'present', 'restarted', 'shutdown', 'started'], 'default': 'present'}",
    "url": "{'description': ['The url of the oVirt instance.'], 'required': True}",
    "user": "{'description': ['The user to authenticate with.'], 'required': True}",
    "zone": "{'description': ['Deploy the image to this oVirt cluster.']}",
}
```

## Examples


``` yaml

- name: Basic example to provision from image
  ovirt:
    user: admin@internal
    url: https://ovirt.example.com
    instance_name: ansiblevm04
    password: secret
    image: centos_64
    zone: cluster01
    resource_type: template

- name: Full example to create new instance from scratch
  ovirt:
    instance_name: testansible
    resource_type: new
    instance_type: server
    user: admin@internal
    password: secret
    url: https://ovirt.example.com
    instance_disksize: 10
    zone: cluster01
    region: datacenter1
    instance_cpus: 1
    instance_nic: nic1
    instance_network: rhevm
    instance_mem: 1000
    disk_alloc: thin
    sdomain: FIBER01
    instance_cores: 1
    instance_os: rhel_6x64
    disk_int: virtio

- name: Stopping an existing instance
  ovirt:
    instance_name: testansible
    state: stopped
    user: admin@internal
    password: secret
    url: https://ovirt.example.com

- name: Start an existing instance
  ovirt:
    instance_name: testansible
    state: started
    user: admin@internal
    password: secret
    url: https://ovirt.example.com

- name: Start an instance with cloud init information
  ovirt:
    instance_name: testansible
    state: started
    user: admin@internal
    password: secret
    url: https://ovirt.example.com
    hostname: testansible
    domain: ansible.local
    ip: 192.0.2.100
    netmask: 255.255.255.0
    gateway: 192.0.2.1
    rootpw: bigsecret

```

## License

TODO

## Author Information
  - ['Vincent Van der Kussen (@vincentvdk)']
