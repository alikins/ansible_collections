# Ansible module: ansible.module_ovirt_affinity_group


Module to manage affinity groups in oVirt/RHV

## Description

This module manage affinity groups in oVirt/RHV. It can also manage assignments of those groups to VMs.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "cluster": "{'description': ['Name of the cluster of the affinity group.']}",
    "description": "{'description': ['Description of the affinity group.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "host_enforcing": "{'description': ['If I(yes) VM cannot start on host if it does not satisfy the C(host_rule).', 'This parameter is support since oVirt/RHV 4.1 version.'], 'type': 'bool'}",
    "host_rule": "{'description': ['If I(positive) I(all) VMs in this group should run on the this host.', 'If I(negative) I(no) VMs in this group should run on the this host.', 'This parameter is support since oVirt/RHV 4.1 version.'], 'choices': ['negative', 'positive']}",
    "hosts": "{'description': ['List of the hosts names, which should have assigned this affinity group.', 'This parameter is support since oVirt/RHV 4.1 version.']}",
    "name": "{'description': ['Name of the affinity group to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "state": "{'description': ['Should the affinity group be present or absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "vm_enforcing": "{'description': ['If I(yes) VM cannot start if it does not satisfy the C(vm_rule).'], 'type': 'bool'}",
    "vm_rule": "{'description': ['If I(positive) I(all) VMs in this group should run on the host defined by C(host_rule).', 'If I(negative) I(no) VMs in this group should run on the host defined by C(host_rule).', "If I(disabled) this affinity group doesn't take effect."], 'choices': ['disabled', 'negative', 'positive']}",
    "vms": "{'description': ['List of the VMs names, which should have assigned this affinity group.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Create(if not exists) and assign affinity group to VMs vm1 and vm2 and host host1
  ovirt_affinity_group:
    name: mygroup
    cluster: mycluster
    vm_enforcing: true
    vm_rule: positive
    host_enforcing: true
    host_rule: positive
    vms:
      - vm1
      - vm2
    hosts:
      - host1

- name: Detach VMs from affinity group and disable VM rule
  ovirt_affinity_group:
    name: mygroup
    cluster: mycluster
    vm_enforcing: false
    vm_rule: disabled
    host_enforcing: true
    host_rule: positive
    vms: []
    hosts:
      - host1
      - host2

- name: Remove affinity group
  ovirt_affinity_group:
    state: absent
    cluster: mycluster
    name: mygroup

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
