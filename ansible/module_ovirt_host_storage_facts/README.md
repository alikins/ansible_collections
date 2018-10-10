# Ansible module: ansible.module_ovirt_host_storage_facts


Retrieve facts about one or more oVirt/RHV HostStorages (applicable only for block storage)

## Description

Retrieve facts about one or more oVirt/RHV HostStorages (applicable only for block storage).

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url)- A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "fcp": "{'description': ['Dictionary with values for fibre channel storage type:', 'C(address) - Address of the fibre channel storage server.', 'C(port) - Port of the fibre channel storage server.', 'C(lun_id) - LUN id.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "host": "{'description': ['Host to get device list from.'], 'required': True}",
    "iscsi": "{'description': ['Dictionary with values for iSCSI storage type:', 'C(address) - Address of the iSCSI storage server.', 'C(target) - The target IQN for the storage device.', 'C(username) - A CHAP user name for logging into a target.', 'C(password) - A CHAP password for logging into a target.']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Gather facts about HostStorages with specified target and address:
- ovirt_host_storage_facts:
    host: myhost
    iscsi:
      target: iqn.2016-08-09.domain-01:nickname
      address: 10.34.63.204
- debug:
    var: ovirt_host_storages

```

## License

TODO

## Author Information
  - ['Daniel Erez (@derez)']
