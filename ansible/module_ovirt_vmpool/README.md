# Ansible module: ansible.module_ovirt_vmpool


Module to manage VM pools in oVirt/RHV

## Description

Module to manage VM pools in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "cluster": "{'description': ['Name of the cluster, where VM pool should be created.']}",
    "comment": "{'description': ['Comment of the Virtual Machine pool.']}",
    "description": "{'description': ['Description of the VM pool.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "id": "{'description': ['ID of the vmpool to manage.'], 'version_added': '2.8'}",
    "name": "{'description': ['Name of the VM pool to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "prestarted": "{'description': ['Number of pre-started VMs defines the number of VMs in run state, that are waiting to be attached to Users.', 'Default value is set by engine.']}",
    "state": "{'description': ['Should the VM pool be present/absent.', 'Note that when C(state) is I(absent) all VMs in VM pool are stopped and removed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "template": "{'description': ['Name of the template, which will be used to create VM pool.']}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "type": "{'description': ['Type of the VM pool. Either manual or automatic.', 'C(manual) - The administrator is responsible for explicitly returning the virtual machine to the pool. The virtual machine reverts to the original base image after the administrator returns it to the pool.', 'C(Automatic) - When the virtual machine is shut down, it automatically reverts to its base image and is returned to the virtual machine pool.', 'Default value is set by engine.'], 'choices': ['manual', 'automatic']}",
    "vm_count": "{'description': ['Number of VMs in the pool.', 'Default value is set by engine.']}",
    "vm_per_user": "{'description': ['Maximum number of VMs a single user can attach to from this pool.', 'Default value is set by engine.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create VM pool from template
- ovirt_vmpool:
    cluster: mycluster
    name: myvmpool
    template: rhel7
    vm_count: 2
    prestarted: 2
    vm_per_user: 1

# Remove vmpool, note that all VMs in pool will be stopped and removed:
- ovirt_vmpool:
    state: absent
    name: myvmpool

# Change Pool Name
- ovirt_vmpool:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_pool_name"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
