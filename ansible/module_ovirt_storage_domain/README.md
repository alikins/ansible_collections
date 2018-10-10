# Ansible module: ansible.module_ovirt_storage_domain


Module to manage storage domains in oVirt/RHV

## Description

Module to manage storage domains in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "backup": "{'description': ['Boolean flag which indicates whether the storage domain is configured as backup or not.'], 'type': 'bool', 'version_added': '2.5'}",
    "comment": "{'description': ['Comment of the storage domain.']}",
    "critical_space_action_blocker": "{'description': ['Indicates the minimal free space the storage domain should contain in percentages.'], 'version_added': '2.5'}",
    "data_center": "{'description': ['Data center name where storage domain should be attached.', "This parameter isn't idempotent, it's not possible to change data center of storage domain."]}",
    "description": "{'description': ['Description of the storage domain.']}",
    "destroy": "{'description': ["Logical remove of the storage domain. If I(true) retains the storage domain's data for import.", 'This parameter is relevant only when C(state) is I(absent).'], 'type': 'bool'}",
    "discard_after_delete": "{'description': ['If I(True) storage domain blocks will be discarded upon deletion. Enabled by default.', 'This parameter is relevant only for block based storage domains.'], 'type': 'bool', 'version_added': 2.5}",
    "domain_function": "{'description': ['Function of the storage domain.', "This parameter isn't idempotent, it's not possible to change domain function of storage domain."], 'choices': ['data', 'iso', 'export'], 'default': 'data', 'aliases': ['type']}",
    "fcp": "{'description': ['Dictionary with values for fibre channel storage type:', 'C(lun_id) - LUN id.', 'C(override_luns) - If I(True) FCP storage domain LUNs will be overridden before adding.', 'Note that these parameters are not idempotent.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "format": "{'description': ['If I(True) storage domain will be formatted after removing it from oVirt/RHV.', 'This parameter is relevant only when C(state) is I(absent).'], 'type': 'bool'}",
    "glusterfs": "{'description': ['Dictionary with values for GlusterFS storage type:', 'C(address) - Address of the Gluster server. E.g.: myserver.mydomain.com', 'C(path) - Path of the mount point. E.g.: /path/to/my/data', 'C(mount_options) - Option which will be passed when mounting storage.', 'Note that these parameters are not idempotent.']}",
    "host": "{'description': ['Host to be used to mount storage.']}",
    "id": "{'description': ['Id of the storage domain to be imported.'], 'version_added': '2.4'}",
    "iscsi": "{'description': ['Dictionary with values for iSCSI storage type:', 'C(address) - Address of the iSCSI storage server.', 'C(port) - Port of the iSCSI storage server.', 'C(target) - The target IQN for the storage device.', 'C(lun_id) - LUN id(s).', 'C(username) - A CHAP user name for logging into a target.', 'C(password) - A CHAP password for logging into a target.', 'C(override_luns) - If I(True) ISCSI storage domain luns will be overridden before adding.', 'C(target_lun_map) - List of dictionary containing targets and LUNs."', 'Note that these parameters are not idempotent.', 'Parameter C(target_lun_map) is supported since Ansible 2.5.']}",
    "localfs": "{'description': ['Dictionary with values for localfs storage type:', 'C(path) - Path of the mount point. E.g.: /path/to/my/data', 'Note that these parameters are not idempotent.'], 'version_added': '2.4'}",
    "name": "{'description': ['Name of the storage domain to manage. (Not required when state is I(imported))']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "nfs": "{'description': ['Dictionary with values for NFS storage type:', 'C(address) - Address of the NFS server. E.g.: myserver.mydomain.com', 'C(path) - Path of the mount point. E.g.: /path/to/my/data', 'C(version) - NFS version. One of: I(auto), I(v3), I(v4) or I(v4_1).', 'C(timeout) - The time in tenths of a second to wait for a response before retrying NFS requests. Range 0 to 65535.', 'C(retrans) - The number of times to retry a request before attempting further recovery actions. Range 0 to 65535.', 'C(mount_options) - Option which will be passed when mounting storage.', 'Note that these parameters are not idempotent.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "posixfs": "{'description': ['Dictionary with values for PosixFS storage type:', 'C(path) - Path of the mount point. E.g.: /path/to/my/data', 'C(vfs_type) - Virtual File System type.', 'C(mount_options) - Option which will be passed when mounting storage.', 'Note that these parameters are not idempotent.']}",
    "state": "{'description': ['Should the storage domain be present/absent/maintenance/unattached/imported/update_ovf_store', 'I(imported) is supported since version 2.4.', "I(update_ovf_store) is supported since version 2.5, currently if C(wait) is (true), we don't wait for update."], 'choices': ['present', 'absent', 'maintenance', 'unattached', 'imported', 'update_ovf_store'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
    "warning_low_space": "{'description': ['Indicates the minimum percentage of a free space in a storage domain to present a warning.'], 'version_added': '2.5'}",
    "wipe_after_delete": "{'description': ['Boolean flag which indicates whether the storage domain should wipe the data after delete.'], 'type': 'bool', 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add data NFS storage domain
- ovirt_storage_domain:
    name: data_nfs
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/data

# Add data NFS storage domain with id for data center
- ovirt_storage_domain:
    name: data_nfs
    host: myhost
    data_center: 11111
    nfs:
      address: 10.34.63.199
      path: /path/data
      mount_options: noexec,nosuid

# Add data localfs storage domain
- ovirt_storage_domain:
    name: data_localfs
    host: myhost
    data_center: mydatacenter
    localfs:
      path: /path/to/data

# Add data iSCSI storage domain:
- ovirt_storage_domain:
    name: data_iscsi
    host: myhost
    data_center: mydatacenter
    iscsi:
      target: iqn.2016-08-09.domain-01:nickname
      lun_id:
       - 1IET_000d0001
       - 1IET_000d0002
      address: 10.34.63.204
    discard_after_delete: True
    backup: False
    critical_space_action_blocker: 5
    warning_low_space: 10

# Since Ansible 2.5 you can specify multiple targets for storage domain,
# Add data iSCSI storage domain with multiple targets:
- ovirt_storage_domain:
    name: data_iscsi
    host: myhost
    data_center: mydatacenter
    iscsi:
      target_lun_map:
        - target: iqn.2016-08-09.domain-01:nickname
          lun_id: 1IET_000d0001
        - target: iqn.2016-08-09.domain-02:nickname
          lun_id: 1IET_000d0002
      address: 10.34.63.204
    discard_after_delete: True

# Add data glusterfs storage domain
-  ovirt_storage_domain:
    name: glusterfs_1
    host: myhost
    data_center: mydatacenter
    glusterfs:
      address: 10.10.10.10
      path: /path/data

# Create export NFS storage domain:
- ovirt_storage_domain:
    name: myexportdomain
    domain_function: export
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/export
    wipe_after_delete: False
    backup: True
    critical_space_action_blocker: 2
    warning_low_space: 5

# Import export NFS storage domain:
- ovirt_storage_domain:
    state: imported
    domain_function: export
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/export

# Import FCP storage domain:
- ovirt_storage_domain:
    state: imported
    name: data_fcp
    host: myhost
    data_center: mydatacenter
    fcp: {}

# Update OVF_STORE:
- ovirt_storage_domain:
    state: update_ovf_store
    name: domain

# Create ISO NFS storage domain
- ovirt_storage_domain:
    name: myiso
    domain_function: iso
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/iso

# Remove storage domain
- ovirt_storage_domain:
    state: absent
    name: mystorage_domain
    format: true

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
