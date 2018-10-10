# Ansible module: ansible.module_ovirt_snapshot


Module to manage Virtual Machine Snapshots in oVirt/RHV

## Description

Module to manage Virtual Machine Snapshots in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "description": "{'description': ['Description of the snapshot.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "keep_days_old": "{'description': ['Number of days after which should snapshot be deleted.', 'It will check all snapshots of virtual machine and delete them, if they are older.'], 'version_added': '2.8'}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "snapshot_id": "{'description': ['ID of the snapshot to manage.']}",
    "state": "{'description': ['Should the Virtual Machine snapshot be restore/present/absent.'], 'choices': ['restore', 'present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "use_memory": "{'description': ["If I(true) and C(state) is I(present) save memory of the Virtual Machine if it's running.", 'If I(true) and C(state) is I(restore) restore memory of the Virtual Machine.', 'Note that Virtual Machine will be paused while saving the memory.'], 'aliases': ['restore_memory', 'save_memory'], 'type': 'bool'}",
    "vm_name": "{'description': ['Name of the Virtual Machine to manage.'], 'required': True}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create snapshot:
- ovirt_snapshot:
    vm_name: rhel7
    description: MySnapshot
  register: snapshot

# Create snapshot and save memory:
- ovirt_snapshot:
    vm_name: rhel7
    description: SnapWithMem
    use_memory: true
  register: snapshot

# Restore snapshot:
- ovirt_snapshot:
    state: restore
    vm_name: rhel7
    snapshot_id: "{{ snapshot.id }}"

# Remove snapshot:
- ovirt_snapshot:
    state: absent
    vm_name: rhel7
    snapshot_id: "{{ snapshot.id }}"

# Delete all snapshots older than 2 days
- ovirt_snapshot:
    vm_name: test
    keep_days_old: 2

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
