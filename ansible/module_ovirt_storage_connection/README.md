# Ansible module: ansible.module_ovirt_storage_connection


Module to manage storage connections in oVirt

## Description

Module to manage storage connections in oVirt

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Address of the storage server. E.g.: myserver.mydomain.com']}",
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "force": "{'description': ['This parameter is relevant only when updating a connection.', "If I(true) the storage domain don't have to be in I(MAINTENANCE) state, so the storage connection is updated."], 'type': 'bool'}",
    "id": "{'description': ['Id of the storage connection to manage.']}",
    "mount_options": "{'description': ['Option which will be passed when mounting storage.']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "nfs_retrans": "{'description': ['The number of times to retry a request before attempting further recovery actions. Range 0 to 65535.']}",
    "nfs_timeout": "{'description': ['The time in tenths of a second to wait for a response before retrying NFS requests. Range 0 to 65535.']}",
    "nfs_version": "{'description': ['NFS version. One of: I(auto), I(v3), I(v4) or I(v4_1).']}",
    "password": "{'description': ['A CHAP password for logging into a target.']}",
    "path": "{'description': ['Path of the mount point of the storage. E.g.: /path/to/my/data']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "port": "{'description': ['Port of the iSCSI storage server.']}",
    "state": "{'description': ['Should the storage connection be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage": "{'description': ['Name of the storage domain to be used with storage connection.']}",
    "target": "{'description': ['The target IQN for the storage device.']}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "type": "{'description': ['Storage type. For example: I(nfs), I(iscsi), etc.']}",
    "username": "{'description': ['A CHAP username for logging into a target.']}",
    "vfs_type": "{'description': ['Virtual File System type.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add new storage connection:
- ovirt_storage_connection:
    storage: myiscsi
    address: 10.34.63.199
    target: iqn.2016-08-09.domain-01:nickname
    port: 3260
    type: iscsi

# Update the existing storage connection address:
- ovirt_storage_connection:
    id: 26915c96-92ff-47e5-9e77-b581db2f2d36
    address: 10.34.63.204
    force: true

# Remove storage connection:
- ovirt_storage_connection:
    id: 26915c96-92ff-47e5-9e77-b581db2f2d36

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
