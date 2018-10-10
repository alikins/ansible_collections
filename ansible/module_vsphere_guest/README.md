# Ansible module: ansible.module_vsphere_guest


Create/delete/manage a guest VM through VMware vSphere

## Description

Create/delete/reconfigure a guest VM through VMware vSphere. This module has a dependency on pysphere >= 1.7

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['The name of the cluster to create the VM in. By default this is derived from the host you tell the module to build the guest on.']}",
    "esxi": "{'description': ['Dictionary which includes datacenter and hostname on which the VM should be created. For standalone ESXi hosts, ha-datacenter should be used as the datacenter name']}",
    "force": "{'description': ['Boolean. Allows you to run commands which may alter the running state of a guest. Also used to reconfigure and destroy.'], 'type': 'bool', 'default': False}",
    "from_template": "{'version_added': '1.9', 'description': ["Specifies if the VM should be deployed from a template (mutually exclusive with 'state' parameter). No guest customization changes to hardware such as CPU, RAM, NICs or Disks can be applied when launching from template."], 'type': 'bool', 'default': False}",
    "guest": "{'description': ['The virtual server name you wish to manage.'], 'required': True}",
    "password": "{'description': ['Password of the user to connect to vcenter as.'], 'required': True}",
    "power_on_after_clone": "{'description': ['Specifies if the VM should be powered on after the clone.'], 'type': 'bool', 'default': True}",
    "resource_pool": "{'description': ['The name of the resource_pool to create the VM in.']}",
    "snapshot_to_clone": "{'description': ['A string that when specified, will create a linked clone copy of the VM. Snapshot must already be taken in vCenter.'], 'version_added': '2.0'}",
    "state": "{'description': ["Indicate desired state of the vm. 'reconfigured' only applies changes to 'vm_cdrom', 'memory_mb', and 'num_cpus' in vm_hardware parameter. The 'memory_mb' and 'num_cpus' changes are applied to powered-on vms when hot-plugging is enabled for the guest."], 'default': 'present', 'choices': ['present', 'powered_off', 'absent', 'powered_on', 'restarted', 'reconfigured', 'reboot_guest', 'poweroff_guest']}",
    "template_src": "{'version_added': '1.9', 'description': ['Name of the source template to deploy from']}",
    "username": "{'description': ['Username to connect to vcenter as.'], 'required': True}",
    "validate_certs": "{'description': ['Validate SSL certs.  Note, if running on python without SSLContext support (typically, python < 2.7.9) you will have to set this to C(no) as pysphere does not support validating certificates on older python. Prior to 2.1, this module would always validate on python >= 2.7.9 and never validate on python <= 2.7.8.'], 'type': 'bool', 'default': True, 'version_added': 2.1}",
    "vcenter_hostname": "{'description': ['The hostname of the vcenter server the module will connect to, to create the guest.'], 'required': True}",
    "vm_disk": "{'description': ['A key, value list of disks and their sizes and which datastore to keep it in.']}",
    "vm_extra_config": "{'description': ['A key, value pair of any extra values you want set or changed in the vmx file of the VM. Useful to set advanced options on the VM.']}",
    "vm_hardware": "{'description': ["A key, value list of VM config settings. Must include ['memory_mb', 'num_cpus', 'osid', 'scsi']."]}",
    "vm_hw_version": "{'description': ['Desired hardware version identifier (for example, "vmx-08" for vms that needs to be managed with vSphere Client). Note that changing hardware version of existing vm is not supported.'], 'version_added': '1.7'}",
    "vm_nic": "{'description': ['A key, value list of nics, their types and what network to put them on.', 'Optionaly with their MAC address.']}",
    "vmware_guest_facts": "{'description': ['Gather facts from vCenter on a particular VM'], 'type': 'bool'}",
}
```

## Examples


``` yaml

---
# Create a new VM on an ESX server
# Returns changed = False when the VM already exists
# Returns changed = True and a adds ansible_facts from the new VM
# State will set the power status of a guest upon creation. Use powered_on to create and boot.
# Options ['state', 'vm_extra_config', 'vm_disk', 'vm_nic', 'vm_hardware', 'esxi'] are required together
# Note: vm_floppy support added in 2.0

- vsphere_guest:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    state: powered_on
    vm_extra_config:
      vcpu.hotadd: yes
      mem.hotadd:  yes
      notes: This is a test VM
      folder: MyFolder
    vm_disk:
      disk1:
        size_gb: 10
        type: thin
        datastore: storage001
        # VMs can be put into folders. The value given here is either the full path
        # to the folder (e.g. production/customerA/lamp) or just the last component
        # of the path (e.g. lamp):
        folder: production/customerA/lamp
    vm_nic:
      nic1:
        type: vmxnet3
        network: VM Network
        network_type: standard
      nic2:
        type: vmxnet3
        network: dvSwitch Network
        network_type: dvs
    vm_hardware:
      memory_mb: 2048
      num_cpus: 2
      osid: centos64Guest
      scsi: paravirtual
      vm_cdrom:
        type: "iso"
        iso_path: "DatastoreName/cd-image.iso"
      vm_floppy:
        type: "image"
        image_path: "DatastoreName/floppy-image.flp"
    esxi:
      datacenter: MyDatacenter
      hostname: esx001.mydomain.local
  delegate_to: localhost

# Reconfigure the CPU and Memory on the newly created VM
# Will return the changes made

- vsphere_guest:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    state: reconfigured
    vm_extra_config:
      vcpu.hotadd: yes
      mem.hotadd:  yes
      notes: This is a test VM
    vm_disk:
      disk1:
        size_gb: 10
        type: thin
        datastore: storage001
    vm_nic:
      nic1:
        type: vmxnet3
        network: VM Network
        network_type: standard
    vm_hardware:
      memory_mb: 4096
      num_cpus: 4
      osid: centos64Guest
      scsi: paravirtual
    esxi:
      datacenter: MyDatacenter
      hostname: esx001.mydomain.local
  delegate_to: localhost

# Deploy a guest from a template
- vsphere_guest:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    from_template: yes
    template_src: centosTemplate
    cluster: MainCluster
    resource_pool: "/Resources"
    vm_extra_config:
      folder: MyFolder
  delegate_to: localhost

# Task to gather facts from a vSphere cluster only if the system is a VMware guest
- vsphere_guest:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    vmware_guest_facts: yes
  delegate_to: localhost

---
# Typical output of a vsphere_facts run on a guest
# If vmware tools is not installed, ipadresses with return None

- hw_eth0:
  - addresstype: "assigned"
    label: "Network adapter 1"
    macaddress: "00:22:33:33:44:55"
    macaddress_dash: "00-22-33-33-44-55"
    ipaddresses: ['192.0.2.100', '2001:DB8:56ff:feac:4d8a']
    summary: "VM Network"
  hw_guest_full_name: "newvm001"
  hw_guest_id: "rhel6_64Guest"
  hw_memtotal_mb: 2048
  hw_name: "centos64Guest"
  hw_power_status: "POWERED ON"
  hw_processor_count: 2
  hw_product_uuid: "ef50bac8-2845-40ff-81d9-675315501dac"

# hw_power_status will be one of the following values:
#   - POWERED ON
#   - POWERED OFF
#   - SUSPENDED
#   - POWERING ON
#   - POWERING OFF
#   - SUSPENDING
#   - RESETTING
#   - BLOCKED ON MSG
#   - REVERTING TO SNAPSHOT
#   - UNKNOWN
# as seen in the VMPowerState-Class of PySphere: http://git.io/vlwOq

---
# Remove a vm from vSphere
# The VM must be powered_off or you need to use force to force a shutdown
- vsphere_guest:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    state: absent
    force: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Richard Hoop (@rhoop) <wrhoop@gmail.com>']
