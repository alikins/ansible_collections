# Ansible module: ansible.module_ovirt_disk


Module to manage Virtual Machine and floating disks in oVirt/RHV

## Description

Module to manage Virtual Machine and floating disks in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "bootable": "{'description': ["I(True) if the disk should be bootable. By default when disk is created it isn't bootable."]}",
    "description": "{'description': ['Description of the disk image to manage.'], 'version_added': '2.5'}",
    "download_image_path": "{'description': ['Path on a file system where disk should be downloaded.', 'Note that you must have an valid oVirt/RHV engine CA in your system trust store or you must provide it in C(ca_file) parameter.', 'Note that the disk is not downloaded when the file already exists, but you can forcibly download the disk when using C(force) I (true).'], 'version_added': '2.3'}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "force": "{'description': ['Please take a look at C(image_path) documentation to see the correct usage of this parameter.'], 'version_added': '2.3'}",
    "format": "{'description': ['Specify format of the disk.', "Note that this option isn't idempotent as it's not currently possible to change format of the disk via API."], 'choices': ['raw', 'cow']}",
    "host": "{'description': ['When the hypervisor name is specified the newly created disk or an existing disk will refresh its information about the underlying storage( Disk size, Serial, Product ID, Vendor ID ...) The specified host will be used for gathering the storage related information. This option is only valid for passthrough disks. This option requires at least the logical_unit.id to be specified'], 'version_added': '2.8'}",
    "id": "{'description': ['ID of the disk to manage. Either C(id) or C(name) is required.']}",
    "image_provider": "{'description': ['When C(state) is I(exported) disk is exported to given Glance image provider.', 'C(**IMPORTANT**)', 'There is no reliable way to achieve idempotency, so every time you specify this parameter the disk is exported, so please handle your playbook accordingly to not export the disk all the time. This option is valid only for template disks.'], 'version_added': '2.4'}",
    "interface": "{'description': ['Driver of the storage interface.', "It's required parameter when creating the new disk."], 'choices': ['virtio', 'ide', 'virtio_scsi'], 'default': 'virtio'}",
    "logical_unit": "{'description': ['Dictionary which describes LUN to be directly attached to VM:', 'C(address) - Address of the storage server. Used by iSCSI.', 'C(port) - Port of the storage server. Used by iSCSI.', 'C(target) - iSCSI target.', 'C(lun_id) - LUN id.', 'C(username) - CHAP Username to be used to access storage server. Used by iSCSI.', 'C(password) - CHAP Password of the user to be used to access storage server. Used by iSCSI.', 'C(storage_type) - Storage type either I(fcp) or I(iscsi).']}",
    "name": "{'description': ['Name of the disk to manage. Either C(id) or C(name)/C(alias) is required.'], 'aliases': ['alias']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "openstack_volume_type": "{'description': ['Name of the openstack volume type. This is valid when working with cinder.'], 'version_added': '2.4'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "profile": "{'description': ['Disk profile name to be attached to disk. By default profile is chosen by oVirt/RHV engine.']}",
    "quota_id": "{'description': ['Disk quota ID to be used for disk. By default quota is chosen by oVirt/RHV engine.'], 'version_added': '2.5'}",
    "shareable": "{'description': ["I(True) if the disk should be shareable. By default when disk is created it isn't shareable."]}",
    "size": "{'description': ['Size of the disk. Size should be specified using IEC standard units. For example 10GiB, 1024MiB, etc.', 'Size can be only increased, not decreased.']}",
    "sparse": "{'required': False, 'version_added': '2.5', 'description': ['I(True) if the disk should be sparse (also known as I(thin provision)). If the parameter is omitted, cow disks will be created as sparse and raw disks as I(preallocated)', "Note that this option isn't idempotent as it's not currently possible to change sparseness of the disk via API."]}",
    "sparsify": "{'description': ['I(True) if the disk should be sparsified.', 'Sparsification frees space in the disk image that is not used by its filesystem. As a result, the image will occupy less space on the storage.', "Note that this parameter isn't idempotent, as it's not possible to check if the disk should be or should not be sparsified."], 'version_added': '2.4'}",
    "state": "{'description': ['Should the Virtual Machine disk be present/absent/attached/detached.'], 'choices': ['present', 'absent', 'attached', 'detached'], 'default': 'present'}",
    "storage_domain": "{'description': ['Storage domain name where disk should be created. By default storage is chosen by oVirt/RHV engine.']}",
    "storage_domains": "{'description': ['Storage domain names where disk should be copied.', 'C(**IMPORTANT**)', 'There is no reliable way to achieve idempotency, so every time you specify this parameter the disks are copied, so please handle your playbook accordingly to not copy the disks all the time. This is valid only for VM and floating disks, template disks works as expected.'], 'version_added': '2.3'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "upload_image_path": "{'description': ['Path to disk image, which should be uploaded.', 'Note that currently we support only compatibility version 0.10 of the qcow disk.', 'Note that you must have an valid oVirt/RHV engine CA in your system trust store or you must provide it in C(ca_file) parameter.', "Note that there is no reliable way to achieve idempotency, so if you want to upload the disk even if the disk with C(id) or C(name) exists, then please use C(force) I(true). If you will use C(force) I(false), which is default, then the disk image won't be uploaded."], 'version_added': '2.3'}",
    "vm_id": "{'description': ['ID of the Virtual Machine to manage. Either C(vm_id) or C(vm_name) is required if C(state) is I(attached) or I(detached).']}",
    "vm_name": "{'description': ['Name of the Virtual Machine to manage. Either C(vm_id) or C(vm_name) is required if C(state) is I(attached) or I(detached).']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
    "wipe_after_delete": "{'description': ["If the disk's Wipe After Delete is enabled, then the disk is first wiped."], 'type': 'bool', 'version_added': '2.8'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create and attach new disk to VM
- ovirt_disk:
    name: myvm_disk
    vm_name: rhel7
    size: 10GiB
    format: cow
    interface: virtio
    storage_domain: data

# Attach logical unit to VM rhel7
- ovirt_disk:
    vm_name: rhel7
    logical_unit:
      target: iqn.2016-08-09.brq.str-01:omachace
      id: 1IET_000d0001
      address: 10.34.63.204
    interface: virtio

# Detach disk from VM
- ovirt_disk:
    state: detached
    name: myvm_disk
    vm_name: rhel7
    size: 10GiB
    format: cow
    interface: virtio

# Change Disk Name
- ovirt_disk:
    id: 00000000-0000-0000-0000-000000000000
    storage_domain: data
    name: "new_disk_name"
    vm_name: rhel7

# Upload local image to disk and attach it to vm:
# Since Ansible 2.3
- ovirt_disk:
    name: mydisk
    vm_name: myvm
    interface: virtio
    size: 10GiB
    format: cow
    image_path: /path/to/mydisk.qcow2
    storage_domain: data

# Download disk to local file system:
# Since Ansible 2.3
- ovirt_disk:
    id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
    download_image_path: /home/user/mydisk.qcow2

# Export disk as image to Glance domain
# Since Ansible 2.4
- ovirt_disks:
    id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
    image_provider: myglance
    state: exported

# Defining a specific quota while creating a disk image:
# Since Ansible 2.5
- ovirt_quotas_facts:
    data_center: Default
    name: myquota
- ovirt_disk:
    name: mydisk
    size: 10GiB
    storage_domain: data
    description: somedescriptionhere
    quota_id: "{{ ovirt_quotas[0]['id'] }}"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
