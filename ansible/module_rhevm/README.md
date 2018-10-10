# Ansible module: ansible.module_rhevm


RHEV/oVirt automation

## Description

This module only supports oVirt/RHEV version 3. A newer module M(ovirt_vm) supports oVirt/RHV version 4.
Allows you to create/remove/update or powermanage virtual machines on a RHEV/oVirt platform.

## Requirements

TODO

## Arguments

``` json
{
    "boot_order": "{'description': ['This option uses complex arguments and is a list of items that specify the bootorder.'], 'default': ['network', 'hd']}",
    "cd_drive": "{'description': ["The CD you wish to have mounted on the VM when I(state = 'CD')."]}",
    "cluster": "{'description': ['The rhev/ovirt cluster in which you want you VM to start.']}",
    "cpu_share": "{'description': ['This parameter is used to configure the cpu share.'], 'default': '0'}",
    "datacenter": "{'description': ['The rhev/ovirt datacenter in which you want you VM to start.'], 'default': 'Default'}",
    "del_prot": "{'description': ['This option sets the delete protection checkbox.'], 'type': 'bool', 'default': True}",
    "disks": "{'description': ['This option uses complex arguments and is a list of disks with the options name, size and domain.']}",
    "ifaces": "{'description': ['This option uses complex arguments and is a list of interfaces with the options name and vlan.'], 'aliases': ['nics', 'interfaces']}",
    "image": "{'description': ['The template to use for the VM.']}",
    "insecure_api": "{'description': ['A boolean switch to make a secure or insecure connection to the server.'], 'type': 'bool', 'default': False}",
    "mempol": "{'description': ['The minimum amount of memory you wish to reserve for this system.'], 'default': '1'}",
    "name": "{'description': ['The name of the VM.']}",
    "osver": "{'description': ['The operationsystem option in RHEV/oVirt.'], 'default': 'rhel_6x64'}",
    "port": "{'description': ['The port on which the API is reacheable.'], 'default': '443'}",
    "server": "{'description': ['The name/ip of your RHEV-m/oVirt instance.'], 'default': '127.0.0.1'}",
    "state": "{'description': ['This serves to create/remove/update or powermanage your VM.'], 'default': 'present', 'choices': ['ping', 'present', 'absent', 'up', 'down', 'restarted', 'cd', 'info']}",
    "timeout": "{'description': ['The timeout you wish to define for power actions.', "When I(state = 'up')", "When I(state = 'down')", "When I(state = 'restarted')"]}",
    "type": "{'description': ['To define if the VM is a server or desktop.'], 'default': 'server', 'choices': ['server', 'desktop', 'host']}",
    "user": "{'description': ['The user to authenticate with.'], 'default': 'admin@internal'}",
    "vm_ha": "{'description': ['To make your VM High Available.'], 'type': 'bool', 'default': True}",
    "vmcpu": "{'description': ['The number of CPUs you want in your VM.'], 'default': '2'}",
    "vmhost": "{'description': ['The host you wish your VM to run on.']}",
    "vmmem": "{'description': ['The amount of memory you want your VM to use (in GB).'], 'default': '1'}",
}
```

## Examples


``` yaml

# basic get info from VM
  - rhevm:
      name: "demo"
      user: "{{ rhev.admin.name }}"
      password: "{{ rhev.admin.pass }}"
      server: "rhevm01"
      state: "info"

# basic create example from image
  - rhevm:
      name: "demo"
      user: "{{ rhev.admin.name }}"
      password: "{{ rhev.admin.pass }}"
      server: "rhevm01"
      state: "present"
      image: "centos7_x64"
      cluster: "centos"

# power management
  - rhevm:
      name: "uptime_server"
      user: "{{ rhev.admin.name }}"
      password: "{{ rhev.admin.pass }}"
      server: "rhevm01"
      cluster: "RH"
      state: "down"
      image: "centos7_x64"

# multi disk, multi nic create example
  - rhevm:
      name: "server007"
      user: "{{ rhev.admin.name }}"
      password: "{{ rhev.admin.pass }}"
      server: "rhevm01"
      cluster: "RH"
      state: "present"
      type: "server"
      vmcpu: 4
      vmmem: 2
      ifaces:
        - name: "eth0"
          vlan: "vlan2202"
        - name: "eth1"
          vlan: "vlan36"
        - name: "eth2"
          vlan: "vlan38"
        - name: "eth3"
          vlan: "vlan2202"
      disks:
        - name: "root"
          size: 10
          domain: "ssd-san"
        - name: "swap"
          size: 10
          domain: "15kiscsi-san"
        - name: "opt"
          size: 10
          domain: "15kiscsi-san"
        - name: "var"
          size: 10
          domain: "10kiscsi-san"
        - name: "home"
          size: 10
          domain: "sata-san"
      boot_order:
        - "network"
        - "hd"

# add a CD to the disk cd_drive
  - rhevm:
      name: 'server007'
      user: "{{ rhev.admin.name }}"
      password: "{{ rhev.admin.pass }}"
      state: 'cd'
      cd_drive: 'rhev-tools-setup.iso'

# new host deployment + host network configuration
  - rhevm:
      name: "ovirt_node007"
      password: "{{ rhevm.admin.pass }}"
      type: "host"
      state: present
      cluster: "rhevm01"
      ifaces:
        - name: em1
        - name: em2
        - name: p3p1
          ip: '172.31.224.200'
          netmask: '255.255.254.0'
        - name: p3p2
          ip: '172.31.225.200'
          netmask: '255.255.254.0'
        - name: bond0
          bond:
            - em1
            - em2
          network: 'rhevm'
          ip: '172.31.222.200'
          netmask: '255.255.255.0'
          management: True
        - name: bond0.36
          network: 'vlan36'
          ip: '10.2.36.200'
          netmask: '255.255.254.0'
          gateway: '10.2.36.254'
        - name: bond0.2202
          network: 'vlan2202'
        - name: bond0.38
          network: 'vlan38'

```

## License

TODO

## Author Information
  - ['Timothy Vandenbrande (@TimothyVandenbrande)']
