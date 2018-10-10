# Ansible module: ansible.module_ovirt_datacenter


Module to manage data centers in oVirt/RHV

## Description

Module to manage data centers in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "comment": "{'description': ['Comment of the data center.']}",
    "compatibility_version": "{'description': ['Compatibility version of the data center.']}",
    "description": "{'description': ['Description of the data center.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "force": "{'description': ['This parameter can be used only when removing a data center. If I(True) data center will be forcibly removed, even though it contains some clusters. Default value is I(False), which means that only empty data center can be removed.'], 'version_added': '2.5', 'default': False}",
    "id": "{'description': ['ID of the datacenter to manage.'], 'version_added': '2.8'}",
    "local": "{'description': ['I(True) if the data center should be local, I(False) if should be shared.', 'Default value is set by engine.']}",
    "mac_pool": "{'description': ['MAC pool to be used by this datacenter.', 'IMPORTANT: This option is deprecated in oVirt/RHV 4.1. You should use C(mac_pool) in C(ovirt_clusters) module, as MAC pools are set per cluster since 4.1.']}",
    "name": "{'description': ['Name of the data center to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "quota_mode": "{'description': ['Quota mode of the data center. One of I(disabled), I(audit) or I(enabled)'], 'choices': ['disabled', 'audit', 'enabled']}",
    "state": "{'description': ['Should the data center be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create datacenter
- ovirt_datacenter:
    name: mydatacenter
    local: True
    compatibility_version: 4.0
    quota_mode: enabled

# Remove datacenter
- ovirt_datacenter:
    state: absent
    name: mydatacenter

# Change Datacenter Name
- ovirt_datacenter:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_datacenter_name"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
