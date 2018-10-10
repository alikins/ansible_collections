# Ansible module: ansible.module_ovirt_vm


Module to manage Virtual Machines in oVirt/RHV

## Description

This module manages whole lifecycle of the Virtual Machine(VM) in oVirt/RHV.
Since VM can hold many states in oVirt/RHV, this see notes to see how the states of the VM are handled.

## Requirements

TODO

## Arguments

``` json
{
    "affinity_group_mappings": "{'description': ["Mapper which maps affinty name between VM's OVF and the destination affinity this VM should be registered to, relevant when C(state) is registered."], 'version_added': '2.5'}",
    "affinity_label_mappings": "{'description': ["Mappper which maps affinity label name between VM's OVF and the destination label this VM should be registered to, relevant when C(state) is registered."], 'version_added': '2.5'}",
    "allow_partial_import": "{'description': ['Boolean indication whether to allow partial registration of Virtual Machine when C(state) is registered.'], 'type': 'bool', 'version_added': '2.4'}",
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "ballooning_enabled": "{'description': ['If I(true), use memory ballooning.', "Memory balloon is a guest device, which may be used to re-distribute / reclaim the host memory based on VM needs in a dynamic way. In this way it's possible to create memory over commitment states."], 'type': 'bool', 'version_added': '2.5'}",
    "boot_devices": "{'description': ['List of boot devices which should be used to boot. For example C([ cdrom, hd ]).', 'Default value is set by oVirt/RHV engine.'], 'choices': ['cdrom', 'hd', 'network']}",
    "boot_menu": "{'description': ['I(True) enable menu to select boot device, I(False) to disable it. By default is chosen by oVirt/RHV engine.'], 'type': 'bool', 'version_added': '2.5'}",
    "cd_iso": "{'description': ['ISO file from ISO storage domain which should be attached to Virtual Machine.', 'If you pass empty string the CD will be ejected from VM.', 'If used with C(state) I(running) or I(present) and VM is running the CD will be attached to VM.', 'If used with C(state) I(running) or I(present) and VM is down the CD will be attached to VM persistently.']}",
    "clone": "{'description': ['If I(yes) then the disks of the created virtual machine will be cloned and independent of the template.', "This parameter is used only when C(state) is I(running) or I(present) and VM didn't exist before."], 'type': 'bool', 'default': False}",
    "clone_permissions": "{'description': ['If I(yes) then the permissions of the template (only the direct ones, not the inherited ones) will be copied to the created virtual machine.', "This parameter is used only when C(state) is I(running) or I(present) and VM didn't exist before."], 'type': 'bool', 'default': False}",
    "cloud_init": "{'description': ['Dictionary with values for Unix-like Virtual Machine initialization using cloud init.', 'C(host_name) - Hostname to be set to Virtual Machine when deployed.', 'C(timezone) - Timezone to be set to Virtual Machine when deployed.', 'C(user_name) - Username to be used to set password to Virtual Machine when deployed.', 'C(root_password) - Password to be set for user specified by C(user_name) parameter.', 'C(authorized_ssh_keys) - Use this SSH keys to login to Virtual Machine.', 'C(regenerate_ssh_keys) - If I(True) SSH keys will be regenerated on Virtual Machine.', 'C(custom_script) - Cloud-init script which will be executed on Virtual Machine when deployed.  This is appended to the end of the cloud-init script generated by any other options.', 'C(dns_servers) - DNS servers to be configured on Virtual Machine.', 'C(dns_search) - DNS search domains to be configured on Virtual Machine.', 'C(nic_boot_protocol) - Set boot protocol of the network interface of Virtual Machine. Can be one of C(none), C(dhcp) or C(static).', 'C(nic_ip_address) - If boot protocol is static, set this IP address to network interface of Virtual Machine.', 'C(nic_netmask) - If boot protocol is static, set this netmask to network interface of Virtual Machine.', 'C(nic_gateway) - If boot protocol is static, set this gateway to network interface of Virtual Machine.', 'C(nic_name) - Set name to network interface of Virtual Machine.', 'C(nic_on_boot) - If I(True) network interface will be set to start on boot.']}",
    "cloud_init_nics": "{'description': ['List of dictionaries representing network interfaces to be setup by cloud init.', 'This option is used, when user needs to setup more network interfaces via cloud init.', 'If one network interface is enough, user should use C(cloud_init) I(nic_*) parameters. C(cloud_init) I(nic_*) parameters are merged with C(cloud_init_nics) parameters.', 'Dictionary can contain following values.', 'C(nic_boot_protocol) - Set boot protocol of the network interface of Virtual Machine. Can be one of C(none), C(dhcp) or C(static).', 'C(nic_ip_address) - If boot protocol is static, set this IP address to network interface of Virtual Machine.', 'C(nic_netmask) - If boot protocol is static, set this netmask to network interface of Virtual Machine.', 'C(nic_gateway) - If boot protocol is static, set this gateway to network interface of Virtual Machine.', 'C(nic_name) - Set name to network interface of Virtual Machine.', 'C(nic_on_boot) - If I(True) network interface will be set to start on boot.'], 'version_added': '2.3'}",
    "cloud_init_persist": "{'description': ["If I(true) the C(cloud_init) or C(sysprep) parameters will be saved for the virtual machine and won't be virtual machine won't be started as run-once."], 'type': 'bool', 'version_added': '2.5', 'aliases': ['sysprep_persist']}",
    "cluster": "{'description': ['Name of the cluster, where Virtual Machine should be created.', 'Required if creating VM.']}",
    "cluster_mappings": "{'description': ["Mapper which maps cluster name between VM's OVF and the destination cluster this VM should be registered to, relevant when C(state) is registered. Cluster mapping is described by the following dictionary:", 'C(source_name): The name of the source cluster.', 'C(dest_name): The name of the destination cluster.'], 'version_added': '2.5'}",
    "comment": "{'description': ['Comment of the Virtual Machine.'], 'version_added': '2.3'}",
    "cpu_cores": "{'description': ['Number of virtual CPUs cores of the Virtual Machine.', 'Default value is set by oVirt/RHV engine.']}",
    "cpu_mode": "{'description': ['CPU mode of the virtual machine. It can be some of the following: I(host_passthrough), I(host_model) or I(custom).', 'For I(host_passthrough) CPU type you need to set C(placement_policy) to I(pinned).', 'If no value is passed, default value is set by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "cpu_pinning": "{'description': ['CPU Pinning topology to map virtual machine CPU to host CPU.', 'CPU Pinning topology is a list of dictionary which can have following values:', 'C(cpu) - Number of the host CPU.', 'C(vcpu) - Number of the virtual machine CPU.'], 'version_added': '2.5'}",
    "cpu_shares": "{'description': ['Set a CPU shares for this Virtual Machine.', 'Default value is set by oVirt/RHV engine.']}",
    "cpu_sockets": "{'description': ['Number of virtual CPUs sockets of the Virtual Machine.', 'Default value is set by oVirt/RHV engine.']}",
    "cpu_threads": "{'description': ['Number of virtual CPUs sockets of the Virtual Machine.', 'Default value is set by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "custom_compatibility_version": "{'description': ["Enables a virtual machine to be customized to its own compatibility version. If 'C(custom_compatibility_version)' is set, it overrides the cluster's compatibility version for this particular virtual machine."], 'version_added': '2.7'}",
    "custom_properties": "{'description': ['Properties sent to VDSM to configure various hooks.', 'Custom properties is a list of dictionary which can have following values:', 'C(name) - Name of the custom property. For example: I(hugepages), I(vhost), I(sap_agent), etc.', 'C(regexp) - Regular expression to set for custom property.', 'C(value) - Value to set for custom property.'], 'version_added': '2.5'}",
    "delete_protected": "{'description': ['If I(yes) Virtual Machine will be set as delete protected.', "If I(no) Virtual Machine won't be set as delete protected.", 'If no value is passed, default value is set by oVirt/RHV engine.'], 'type': 'bool'}",
    "description": "{'description': ['Description of the Virtual Machine.'], 'version_added': '2.3'}",
    "disk_format": "{'description': ['Specify format of the disk.', 'If C(cow) format is used, disk will by created as sparse, so space will be allocated for the volume as needed, also known as I(thin provision).', 'If C(raw) format is used, disk storage will be allocated right away, also known as I(preallocated).', "Note that this option isn't idempotent as it's not currently possible to change format of the disk via API.", 'This parameter is considered only when C(template) and C(storage domain) is provided.'], 'choices': ['cow', 'raw'], 'default': 'cow', 'version_added': '2.4'}",
    "disks": "{'description': ['List of disks, which should be attached to Virtual Machine. Disk is described by following dictionary.', 'C(name) - Name of the disk. Either C(name) or C(id) is required.', 'C(id) - ID of the disk. Either C(name) or C(id) is required.', 'C(interface) - Interface of the disk, either I(virtio) or I(IDE), default is I(virtio).', 'C(bootable) - I(True) if the disk should be bootable, default is non bootable.', 'C(activate) - I(True) if the disk should be activated, default is activated.', 'NOTE - This parameter is used only when C(state) is I(running) or I(present) and is able to only attach disks. To manage disks of the VM in more depth please use M(ovirt_disks) module instead.']}",
    "domain_mappings": "{'description': ["Mapper which maps aaa domain name between VM's OVF and the destination aaa domain this VM should be registered to, relevant when C(state) is registered. The aaa domain mapping is described by the following dictionary:", 'C(source_name): The name of the source aaa domain.', 'C(dest_name): The name of the destination aaa domain.'], 'version_added': '2.5'}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "force": "{'description': ['Please check to I(Synopsis) to more detailed description of force parameter, it can behave differently in different situations.'], 'type': 'bool', 'default': False}",
    "graphical_console": "{'description': ['Assign graphical console to the virtual machine.', 'Graphical console is a dictionary which can have following values:', 'C(headless_mode) - If I(true) disable the graphics console for this virtual machine.', 'C(protocol) - Graphical protocol, a list of I(spice), I(vnc), or both.'], 'version_added': '2.5'}",
    "high_availability": "{'description': ['If I(yes) Virtual Machine will be set as highly available.', "If I(no) Virtual Machine won't be set as highly available.", 'If no value is passed, default value is set by oVirt/RHV engine.'], 'type': 'bool'}",
    "high_availability_priority": "{'description': ['Indicates the priority of the virtual machine inside the run and migration queues. Virtual machines with higher priorities will be started and migrated before virtual machines with lower priorities. The value is an integer between 0 and 100. The higher the value, the higher the priority.', 'If no value is passed, default value is set by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "host": "{'description': ['Specify host where Virtual Machine should be running. By default the host is chosen by engine scheduler.', 'This parameter is used only when C(state) is I(running) or I(present).']}",
    "host_devices": "{'description': ['Single Root I/O Virtualization - technology that allows single device to expose multiple endpoints that can be passed to VMs', 'host_devices is an list which contain dictinary with name and state of device'], 'version_added': '2.7'}",
    "id": "{'description': ['ID of the Virtual Machine to manage.']}",
    "initrd_path": "{'description': ['Path to an initial ramdisk to be used with the kernel specified by C(kernel_path) option.', "Ramdisk image must be stored on either the ISO domain or on the host's storage."], 'version_added': '2.3'}",
    "instance_type": "{'description': ["Name of virtual machine's hardware configuration.", 'By default no instance type is used.'], 'version_added': '2.3'}",
    "io_threads": "{'description': ['Number of IO threads used by virtual machine. I(0) means IO threading disabled.'], 'version_added': '2.5'}",
    "kernel_params": "{'description': ['Kernel command line parameters (formatted as string) to be used with the kernel specified by C(kernel_path) option.'], 'version_added': '2.3'}",
    "kernel_params_persist": "{'description': ['If I(true) C(kernel_params), C(initrd_path) and C(kernel_path) will persist in virtual machine configuration, if I(False) it will be used for run once.'], 'type': 'bool', 'version_added': '2.8'}",
    "kernel_path": "{'description': ['Path to a kernel image used to boot the virtual machine.', "Kernel image must be stored on either the ISO domain or on the host's storage."], 'version_added': '2.3'}",
    "kvm": "{'description': ['Dictionary of values to be used to connect to kvm and import a virtual machine to oVirt.', 'Dictionary can contain following values.', 'C(name) - The name of the KVM virtual machine.', 'C(username) - The username to authenticate against the KVM.', 'C(password) - The password to authenticate against the KVM.', 'C(url) - The URL to be passed to the I(virt-v2v) tool for conversion. For example I(qemu:///system). This is required parameter.', 'C(drivers_iso) - The name of the ISO containing drivers that can be used during the I(virt-v2v) conversion process.', 'C(sparse) - Specifies the disk allocation policy of the resulting virtual machine. I(true) for sparse, I(false) for preallocated. Default value is I(true).', 'C(storage_domain) - Specifies the target storage domain for converted disks. This is required parameter.'], 'version_added': '2.3'}",
    "lease": "{'description': ['Name of the storage domain this virtual machine lease reside on.', 'NOTE - Supported since oVirt 4.1.'], 'version_added': '2.4'}",
    "lun_mappings": "{'description': ["Mapper which maps lun between VM's OVF and the destination lun this VM should contain, relevant when C(state) is registered. lun_mappings is described by the following dictionary: - C(logical_unit_id): The logical unit number to identify a logical unit, - C(logical_unit_port): The port being used to connect with the LUN disk. - C(logical_unit_portal): The portal being used to connect with the LUN disk. - C(logical_unit_address): The address of the block storage host. - C(logical_unit_target): The iSCSI specification located on an iSCSI server - C(logical_unit_username): Username to be used to connect to the block storage host. - C(logical_unit_password): Password to be used to connect to the block storage host. - C(storage_type): The storage type which the LUN reside on (iscsi or fcp)"], 'version_added': '2.5'}",
    "memory": "{'description': ['Amount of memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).', 'Default value is set by engine.']}",
    "memory_guaranteed": "{'description': ['Amount of minimal guaranteed memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).', "C(memory_guaranteed) parameter can't be lower than C(memory) parameter.", 'Default value is set by engine.']}",
    "memory_max": "{'description': ['Upper bound of virtual machine memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).', 'Default value is set by engine.'], 'version_added': '2.5'}",
    "name": "{'description': ['Name of the Virtual Machine to manage.', "If VM don't exists C(name) is required. Otherwise C(id) or C(name) can be used."]}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "nics": "{'description': ['List of NICs, which should be attached to Virtual Machine. NIC is described by following dictionary.', 'C(name) - Name of the NIC.', 'C(profile_name) - Profile name where NIC should be attached.', 'C(interface) -  Type of the network interface. One of following I(virtio), I(e1000), I(rtl8139), default is I(virtio).', "C(mac_address) - Custom MAC address of the network interface, by default it's obtained from MAC pool.", 'NOTE - This parameter is used only when C(state) is I(running) or I(present) and is able to only create NICs. To manage NICs of the VM in more depth please use M(ovirt_nics) module instead.']}",
    "numa_nodes": "{'description': ["List of vNUMA Nodes to set for this VM and pin them to assigned host's physical NUMA node.", 'Each vNUMA node is described by following dictionary:', 'C(index) -  The index of this NUMA node (mandatory).', 'C(memory) - Memory size of the NUMA node in MiB (mandatory).', 'C(cores) -  list of VM CPU cores indexes to be included in this NUMA node (mandatory).', 'C(numa_node_pins) - list of physical NUMA node indexes to pin this virtual NUMA node to.'], 'version_added': '2.6'}",
    "numa_tune_mode": "{'description': ['Set how the memory allocation for NUMA nodes of this VM is applied (relevant if NUMA nodes are set for this VM).', 'It can be one of the following: I(interleave), I(preferred) or I(strict).', 'If no value is passed, default value is set by oVirt/RHV engine.'], 'choices': ['interleave', 'preferred', 'strict'], 'version_added': '2.6'}",
    "operating_system": "{'description': ['Operating system of the Virtual Machine.', 'Default value is set by oVirt/RHV engine.', 'Possible values: debian_7, freebsd, freebsdx64, other, other_linux, other_linux_ppc64, other_ppc64, rhel_3, rhel_4, rhel_4x64, rhel_5, rhel_5x64, rhel_6, rhel_6x64, rhel_6_ppc64, rhel_7x64, rhel_7_ppc64, sles_11, sles_11_ppc64, ubuntu_12_04, ubuntu_12_10, ubuntu_13_04, ubuntu_13_10, ubuntu_14_04, ubuntu_14_04_ppc64, windows_10, windows_10x64, windows_2003, windows_2003x64, windows_2008, windows_2008x64, windows_2008r2x64, windows_2008R2x64, windows_2012x64, windows_2012R2x64, windows_7, windows_7x64, windows_8, windows_8x64, windows_xp']}",
    "placement_policy": "{'description': ["The configuration of the virtual machine's placement policy.", 'Placement policy can be one of the following values:', 'C(migratable) - Allow manual and automatic migration.', 'C(pinned) - Do not allow migration.', 'C(user_migratable) - Allow manual migration only.', 'If no value is passed, default value is set by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "quota_id": "{'description': ['Virtual Machine quota ID to be used for disk. By default quota is chosen by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "reassign_bad_macs": "{'description': ['Boolean indication whether to reassign bad macs when C(state) is registered.'], 'type': 'bool', 'version_added': '2.5'}",
    "rng_device": "{'description': ['Random number generator (RNG). You can choose of one the following devices I(urandom), I(random) or I(hwrng).', 'In order to select I(hwrng), you must have it enabled on cluster first.', '/dev/urandom is used for cluster version >= 4.1, and /dev/random for cluster version <= 4.0'], 'version_added': '2.5'}",
    "role_mappings": "{'description': ["Mapper which maps role name between VM's OVF and the destination role this VM should be registered to, relevant when C(state) is registered. Role mapping is described by the following dictionary:", 'C(source_name): The name of the source role.', 'C(dest_name): The name of the destination role.'], 'version_added': '2.5'}",
    "serial_console": "{'description': ['I(True) enable VirtIO serial console, I(False) to disable it. By default is chosen by oVirt/RHV engine.'], 'type': 'bool', 'version_added': '2.5'}",
    "serial_policy": "{'description': ['Specify a serial number policy for the Virtual Machine.', 'Following options are supported.', "C(vm) - Sets the Virtual Machine's UUID as its serial number.", "C(host) - Sets the host's UUID as the Virtual Machine's serial number.", 'C(custom) - Allows you to specify a custom serial number in C(serial_policy_value).'], 'choices': ['vm', 'host', 'custom'], 'version_added': '2.3'}",
    "serial_policy_value": "{'description': ['Allows you to specify a custom serial number.', 'This parameter is used only when C(serial_policy) is I(custom).'], 'version_added': '2.3'}",
    "smartcard_enabled": "{'description': ['If I(true), use smart card authentication.'], 'type': 'bool', 'version_added': '2.5'}",
    "soundcard_enabled": "{'description': ['If I(true), the sound card is added to the virtual machine.'], 'type': 'bool', 'version_added': '2.5'}",
    "sso": "{'description': ['I(True) enable Single Sign On by Guest Agent, I(False) to disable it. By default is chosen by oVirt/RHV engine.'], 'type': 'bool', 'version_added': '2.5'}",
    "state": "{'description': ["Should the Virtual Machine be running/stopped/present/absent/suspended/next_run/registered. When C(state) is I(registered) and the unregistered VM's name belongs to an already registered in engine VM in the same DC then we fail to register the unregistered template.", "I(present) state will create/update VM and don't change its state if it already exists.", 'I(running) state will create/update VM and start it.', 'I(next_run) state updates the VM and if the VM has next run configuration it will be rebooted.', 'Please check I(notes) to more detailed description of states.', 'I(registered) is supported since 2.4.'], 'choices': ['absent', 'next_run', 'present', 'registered', 'running', 'stopped', 'suspended'], 'default': 'present'}",
    "stateless": "{'description': ['If I(yes) Virtual Machine will be set as stateless.', 'If I(no) Virtual Machine will be unset as stateless.', 'If no value is passed, default value is set by oVirt/RHV engine.'], 'type': 'bool'}",
    "storage_domain": "{'description': ['Name of the storage domain where all template disks should be created.', 'This parameter is considered only when C(template) is provided.', "IMPORTANT - This parameter is not idempotent, if the VM exists and you specfiy different storage domain, disk won't move."], 'version_added': '2.4'}",
    "sysprep": "{'description': ['Dictionary with values for Windows Virtual Machine initialization using sysprep.', 'C(host_name) - Hostname to be set to Virtual Machine when deployed.', 'C(active_directory_ou) - Active Directory Organizational Unit, to be used for login of user.', 'C(org_name) - Organization name to be set to Windows Virtual Machine.', 'C(domain) - Domain to be set to Windows Virtual Machine.', 'C(timezone) - Timezone to be set to Windows Virtual Machine.', 'C(ui_language) - UI language of the Windows Virtual Machine.', 'C(system_locale) - System localization of the Windows Virtual Machine.', 'C(input_locale) - Input localization of the Windows Virtual Machine.', 'C(windows_license_key) - License key to be set to Windows Virtual Machine.', 'C(user_name) - Username to be used for set password to Windows Virtual Machine.', 'C(root_password) - Password to be set for username to Windows Virtual Machine.']}",
    "template": "{'description': ['Name of the template, which should be used to create Virtual Machine.', 'Required if creating VM.', "If template is not specified and VM doesn't exist, VM will be created from I(Blank) template."]}",
    "template_version": "{'description': ['Version number of the template to be used for VM.', 'By default the latest available version of the template is used.'], 'version_added': '2.3'}",
    "ticket": "{'description': ['If I(true), in addition return I(remote_vv_file) inside I(vm) dictionary, which contains compatible content for remote-viewer application. Works only C(state) is I(running).'], 'version_added': '2.7', 'type': 'bool'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "timezone": "{'description': ['Sets time zone offset of the guest hardware clock.', 'For example C(Etc/GMT)'], 'version_added': '2.3'}",
    "type": "{'description': ['Type of the Virtual Machine.', 'Default value is set by oVirt/RHV engine.', 'I(high_performance) is supported since Ansible 2.5 and oVirt/RHV 4.2.'], 'choices': ['desktop', 'server', 'high_performance']}",
    "usb_support": "{'description': ['I(True) enable USB support, I(False) to disable it. By default is chosen by oVirt/RHV engine.'], 'type': 'bool', 'version_added': '2.5'}",
    "use_latest_template_version": "{'description': ['Specify if latest template version should be used, when running a stateless VM.', 'If this parameter is set to I(yes) stateless VM is created.'], 'type': 'bool', 'version_added': '2.3'}",
    "vmware": "{'description': ['Dictionary of values to be used to connect to VMware and import a virtual machine to oVirt.', 'Dictionary can contain following values.', 'C(username) - The username to authenticate against the VMware.', 'C(password) - The password to authenticate against the VMware.', 'C(url) - The URL to be passed to the I(virt-v2v) tool for conversion. For example I(vpx://wmware_user@vcenter-host/DataCenter/Cluster/esxi-host?no_verify=1)', 'C(drivers_iso) - The name of the ISO containing drivers that can be used during the I(virt-v2v) conversion process.', 'C(sparse) - Specifies the disk allocation policy of the resulting virtual machine. I(true) for sparse, I(false) for preallocated. Default value is I(true).', 'C(storage_domain) - Specifies the target storage domain for converted disks. This is required parameter.'], 'version_added': '2.3'}",
    "vnic_profile_mappings": "{'description': ['Mapper which maps an external virtual NIC profile to one that exists in the engine when C(state) is registered. vnic_profile is described by the following dictionary:', 'C(source_network_name): The network name of the source network.', 'C(source_profile_name): The profile name related to the source network.', 'C(target_profile_id): The id of the target profile id to be mapped to in the engine.'], 'version_added': '2.5'}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
    "watchdog": "{'description': ['Assign watchdog device for the virtual machine.', 'Watchdogs is a dictionary which can have following values:', 'C(model) - Model of the watchdog device. For example: I(i6300esb), I(diag288) or I(null).', 'C(action) - Watchdog action to be performed when watchdog is triggered. For example: I(none), I(reset), I(poweroff), I(pause) or I(dump).'], 'version_added': '2.5'}",
    "xen": "{'description': ['Dictionary of values to be used to connect to XEN and import a virtual machine to oVirt.', 'Dictionary can contain following values.', 'C(url) - The URL to be passed to the I(virt-v2v) tool for conversion. For example I(xen+ssh://root@zen.server). This is required parameter.', 'C(drivers_iso) - The name of the ISO containing drivers that can be used during the I(virt-v2v) conversion process.', 'C(sparse) - Specifies the disk allocation policy of the resulting virtual machine. I(true) for sparse, I(false) for preallocated. Default value is I(true).', 'C(storage_domain) - Specifies the target storage domain for converted disks. This is required parameter.'], 'version_added': '2.3'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Creates a new Virtual Machine from template named 'rhel7_template'
  ovirt_vm:
    state: present
    name: myvm
    template: rhel7_template
    cluster: mycluster

- name: Register VM
  ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    name: myvm

- name: Register VM using id
  ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111

- name: Register VM, allowing partial import
  ovirt_vm:
    state: registered
    storage_domain: mystorage
    allow_partial_import: "True"
    cluster: mycluster
    id: 1111-1111-1111-1111

- name: Register VM with vnic profile mappings and reassign bad macs
  ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    vnic_profile_mappings:
    - source_network_name: mynetwork
      source_profile_name: mynetwork
      target_profile_id: 3333-3333-3333-3333
    - source_network_name: mynetwork2
      source_profile_name: mynetwork2
      target_profile_id: 4444-4444-4444-4444
    reassign_bad_macs: "True"

- name: Register VM with mappings
  ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    role_mappings:
      - source_name: Role_A
        dest_name: Role_B
    domain_mappings:
      - source_name: Domain_A
        dest_name: Domain_B
    lun_mappings:
      - source_storage_type: iscsi
        source_logical_unit_id: 1IET_000d0001
        source_logical_unit_port: 3260
        source_logical_unit_portal: 1
        source_logical_unit_address: 10.34.63.203
        source_logical_unit_target: iqn.2016-08-09.brq.str-01:omachace
        dest_storage_type: iscsi
        dest_logical_unit_id: 1IET_000d0002
        dest_logical_unit_port: 3260
        dest_logical_unit_portal: 1
        dest_logical_unit_address: 10.34.63.204
        dest_logical_unit_target: iqn.2016-08-09.brq.str-02:omachace
    affinity_group_mappings:
      - source_name: Affinity_A
        dest_name: Affinity_B
    affinity_label_mappings:
      - source_name: Label_A
        dest_name: Label_B
    cluster_mappings:
      - source_name: cluster_A
        dest_name: cluster_B

- name: Creates a stateless VM which will always use latest template version
  ovirt_vm:
    name: myvm
    template: rhel7
    cluster: mycluster
    use_latest_template_version: true

# Creates a new server rhel7 Virtual Machine from Blank template
# on brq01 cluster with 2GiB memory and 2 vcpu cores/sockets
# and attach bootable disk with name rhel7_disk and attach virtio NIC
- ovirt_vm:
    state: present
    cluster: brq01
    name: myvm
    memory: 2GiB
    cpu_cores: 2
    cpu_sockets: 2
    cpu_shares: 1024
    type: server
    operating_system: rhel_7x64
    disks:
      - name: rhel7_disk
        bootable: True
    nics:
      - name: nic1

# Change VM Name
- ovirt_vm:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_vm_name"

- name: Run VM with cloud init
  ovirt_vm:
    name: rhel7
    template: rhel7
    cluster: Default
    memory: 1GiB
    high_availability: true
    high_availability_priority: 50  # Available from Ansible 2.5
    cloud_init:
      nic_boot_protocol: static
      nic_ip_address: 10.34.60.86
      nic_netmask: 255.255.252.0
      nic_gateway: 10.34.63.254
      nic_name: eth1
      nic_on_boot: true
      host_name: example.com
      custom_script: |
        write_files:
         - content: |
             Hello, world!
           path: /tmp/greeting.txt
           permissions: '0644'
      user_name: root
      root_password: super_password

- name: Run VM with cloud init, with multiple network interfaces
  ovirt_vm:
    name: rhel7_4
    template: rhel7
    cluster: mycluster
    cloud_init_nics:
    - nic_name: eth0
      nic_boot_protocol: dhcp
      nic_on_boot: true
    - nic_name: eth1
      nic_boot_protocol: static
      nic_ip_address: 10.34.60.86
      nic_netmask: 255.255.252.0
      nic_gateway: 10.34.63.254
      nic_on_boot: true

- name: Run VM with sysprep
  ovirt_vm:
    name: windows2012R2_AD
    template: windows2012R2
    cluster: Default
    memory: 3GiB
    high_availability: true
    sysprep:
      host_name: windowsad.example.com
      user_name: Administrator
      root_password: SuperPassword123

- name: Migrate/Run VM to/on host named 'host1'
  ovirt_vm:
    state: running
    name: myvm
    host: host1

- name: Change VMs CD
  ovirt_vm:
    name: myvm
    cd_iso: drivers.iso

- name: Eject VMs CD
  ovirt_vm:
    name: myvm
    cd_iso: ''

- name: Boot VM from CD
  ovirt_vm:
    name: myvm
    cd_iso: centos7_x64.iso
    boot_devices:
        - cdrom

- name: Stop vm
  ovirt_vm:
    state: stopped
    name: myvm

- name: Upgrade memory to already created VM
  ovirt_vm:
    name: myvm
    memory: 4GiB

- name: Hot plug memory to already created and running VM (VM won't be restarted)
  ovirt_vm:
    name: myvm
    memory: 4GiB

# Create/update a VM to run with two vNUMA nodes and pin them to physical NUMA nodes as follows:
# vnuma index 0-> numa index 0, vnuma index 1-> numa index 1
- name: Create a VM to run with two vNUMA nodes
  ovirt_vm:
    name: myvm
    cluster: mycluster
    numa_tune_mode: "interleave"
    numa_nodes:
    - index: 0
      cores: [0]
      memory: 20
      numa_node_pins: [0]
    - index: 1
      cores: [1]
      memory: 30
      numa_node_pins: [1]

- name: Update an existing VM to run without previously created vNUMA nodes (i.e. remove all vNUMA nodes+NUMA pinning setting)
  ovirt_vm:
    name: myvm
    cluster: mycluster
    state: "present"
    numa_tune_mode: "interleave"
    numa_nodes:
    - index: -1

# When change on the VM needs restart of the VM, use next_run state,
# The VM will be updated and rebooted if there are any changes.
# If present state would be used, VM won't be restarted.
- ovirt_vm:
    state: next_run
    name: myvm
    boot_devices:
      - network

- name: Import virtual machine from VMware
  ovirt_vm:
    state: stopped
    cluster: mycluster
    name: vmware_win10
    timeout: 1800
    poll_interval: 30
    vmware:
      url: vpx://user@1.2.3.4/Folder1/Cluster1/2.3.4.5?no_verify=1
      name: windows10
      storage_domain: mynfs
      username: user
      password: password

- name: Create vm from template and create all disks on specific storage domain
  ovirt_vm:
    name: vm_test
    cluster: mycluster
    template: mytemplate
    storage_domain: mynfs
    nics:
    - name: nic1

- name: Remove VM, if VM is running it will be stopped
  ovirt_vm:
    state: absent
    name: myvm

# Defining a specific quota for a VM:
# Since Ansible 2.5
- ovirt_quotas_facts:
    data_center: Default
    name: myquota
- ovirt_vm:
    name: myvm
    sso: False
    boot_menu: True
    usb_support: True
    serial_console: True
    quota_id: "{{ ovirt_quotas[0]['id'] }}"

- name: Create a VM that has the console configured for both Spice and VNC
  ovirt_vm:
    name: myvm
    template: mytemplate
    cluster: mycluster
    graphical_console:
      protocol:
        - spice
        - vnc

# Execute remote viever to VM
- block:
  - name: Create a ticket for console for a running VM
    ovirt_vms:
      name: myvm
      ticket: true
      state: running
    register: myvm

  - name: Save ticket to file
    copy:
      content: "{{ myvm.vm.remote_vv_file }}"
      dest: ~/vvfile.vv

  - name: Run remote viewer with file
    command: remote-viewer ~/vvfile.vv

# Default value of host_device state is present
- name: Attach host devices to virtual machine
  ovirt_vm:
    name: myvm
    host: myhost
    placement_policy: pinned
    host_devices:
      - name: pci_0000_00_06_0
      - name: pci_0000_00_07_0
        state: absent
      - name: pci_0000_00_08_0
        state: present


```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
