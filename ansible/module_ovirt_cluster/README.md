# Ansible module: ansible.module_ovirt_cluster


Module to manage clusters in oVirt/RHV

## Description

Module to manage clusters in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "ballooning": "{'description': ['If I(True) enable memory balloon optimization. Memory balloon is used to re-distribute / reclaim the host memory based on VM needs in a dynamic way.']}",
    "comment": "{'description': ['Comment of the cluster.']}",
    "compatibility_version": "{'description': ['The compatibility version of the cluster. All hosts in this cluster must support at least this compatibility version.']}",
    "cpu_arch": "{'description': ['CPU architecture of cluster.'], 'choices': ['x86_64', 'ppc64', 'undefined']}",
    "cpu_type": "{'description': ['CPU codename. For example I(Intel SandyBridge Family).']}",
    "data_center": "{'description': ['Datacenter name where cluster reside.']}",
    "description": "{'description': ['Description of the cluster.']}",
    "external_network_providers": "{'description': ['List of references to the external network providers available in the cluster. If the automatic deployment of the external network provider is supported, the networks of the referenced network provider are available on every host in the cluster.', 'External network provider is described by following dictionary:', 'C(name) - Name of the external network provider. Either C(name) or C(id) is required.', 'C(id) - ID of the external network provider. Either C(name) or C(id) is required.', 'This is supported since oVirt version 4.2.'], 'version_added': 2.5}",
    "fence_connectivity_threshold": "{'description': ['The threshold used by C(fence_skip_if_connectivity_broken).']}",
    "fence_enabled": "{'description': ['If I(True) enables fencing on the cluster.', 'Fencing is enabled by default.']}",
    "fence_skip_if_connectivity_broken": "{'description': ['If I(True) fencing will be temporarily disabled if the percentage of hosts in the cluster that are experiencing connectivity issues is greater than or equal to the defined threshold.', 'The threshold can be specified by C(fence_connectivity_threshold).']}",
    "fence_skip_if_sd_active": "{'description': ['If I(True) any hosts in the cluster that are Non Responsive and still connected to storage will not be fenced.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "gluster": "{'description': ['If I(True), hosts in this cluster will be used as Gluster Storage server nodes, and not for running virtual machines.', 'By default the cluster is created for virtual machine hosts.']}",
    "ha_reservation": "{'description': ['If I(True) enables the oVirt/RHV to monitor cluster capacity for highly available virtual machines.']}",
    "host_reason": "{'description': ['If I(True) enables an optional reason field when a host is placed into maintenance mode from the Manager, allowing the administrator to provide an explanation for the maintenance.']}",
    "id": "{'description': ['ID of the cluster to manage.'], 'version_added': '2.8'}",
    "ksm": "{'description': ['I I(True) MoM enables to run Kernel Same-page Merging I(KSM) when necessary and when it can yield a memory saving benefit that outweighs its CPU cost.']}",
    "ksm_numa": "{'description': ['If I(True) enables KSM C(ksm) for best performance inside NUMA nodes.']}",
    "mac_pool": "{'description': ['MAC pool to be used by this cluster.', 'C(Note:)', 'This is supported since oVirt version 4.1.'], 'version_added': 2.4}",
    "memory_policy": "{'description': ['I(disabled) - Disables memory page sharing.', 'I(server) - Sets the memory page sharing threshold to 150% of the system memory on each host.', 'I(desktop) - Sets the memory page sharing threshold to 200% of the system memory on each host.'], 'choices': ['disabled', 'server', 'desktop']}",
    "migration_auto_converge": "{'description': ['If I(True) auto-convergence is used during live migration of virtual machines.', 'Used only when C(migration_policy) is set to I(legacy).', 'Following options are supported:', 'C(true) - Override the global setting to I(true).', 'C(false) - Override the global setting to I(false).', 'C(inherit) - Use value which is set globally.'], 'choices': ['true', 'false', 'inherit']}",
    "migration_bandwidth": "{'description': ['The bandwidth settings define the maximum bandwidth of both outgoing and incoming migrations per host.', 'Following bandwidth options are supported:', 'C(auto) - Bandwidth is copied from the I(rate limit) [Mbps] setting in the data center host network QoS.', 'C(hypervisor_default) - Bandwidth is controlled by local VDSM setting on sending host.', 'C(custom) - Defined by user (in Mbps).'], 'choices': ['auto', 'hypervisor_default', 'custom']}",
    "migration_bandwidth_limit": "{'description': ['Set the I(custom) migration bandwidth limit.', 'This parameter is used only when C(migration_bandwidth) is I(custom).']}",
    "migration_compressed": "{'description': ['If I(True) compression is used during live migration of the virtual machine.', 'Used only when C(migration_policy) is set to I(legacy).', 'Following options are supported:', 'C(true) - Override the global setting to I(true).', 'C(false) - Override the global setting to I(false).', 'C(inherit) - Use value which is set globally.'], 'choices': ['true', 'false', 'inherit']}",
    "migration_policy": "{'description': ['A migration policy defines the conditions for live migrating virtual machines in the event of host failure.', 'Following policies are supported:', 'C(legacy) - Legacy behavior of 3.6 version.', 'C(minimal_downtime) - Virtual machines should not experience any significant downtime.', 'C(suspend_workload) - Virtual machines may experience a more significant downtime.', 'C(post_copy) - Virtual machines should not experience any significant downtime. If the VM migration is not converging for a long time, the migration will be switched to post-copy. Added in version I(2.4).'], 'choices': ['legacy', 'minimal_downtime', 'suspend_workload', 'post_copy']}",
    "name": "{'description': ['Name of the cluster to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "network": "{'description': ['Management network of cluster to access cluster hosts.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "resilience_policy": "{'description': ['The resilience policy defines how the virtual machines are prioritized in the migration.', 'Following values are supported:', 'C(do_not_migrate) -  Prevents virtual machines from being migrated. ', 'C(migrate) - Migrates all virtual machines in order of their defined priority.', 'C(migrate_highly_available) - Migrates only highly available virtual machines to prevent overloading other hosts.'], 'choices': ['do_not_migrate', 'migrate', 'migrate_highly_available']}",
    "rng_sources": "{'description': ['List that specify the random number generator devices that all hosts in the cluster will use.', 'Supported generators are: I(hwrng) and I(random).']}",
    "scheduling_policy": "{'description': ['Name of the scheduling policy to be used for cluster.']}",
    "scheduling_policy_properties": "{'description': ['Custom scheduling policy properties of the cluster.', 'These optional properties override the properties of the scheduling policy specified by the C(scheduling_policy) parameter.'], 'version_added': '2.6'}",
    "serial_policy": "{'description': ['Specify a serial number policy for the virtual machines in the cluster.', 'Following options are supported:', "C(vm) - Sets the virtual machine's UUID as its serial number.", "C(host) - Sets the host's UUID as the virtual machine's serial number.", 'C(custom) - Allows you to specify a custom serial number in C(serial_policy_value).']}",
    "serial_policy_value": "{'description': ['Allows you to specify a custom serial number.', 'This parameter is used only when C(serial_policy) is I(custom).']}",
    "spice_proxy": "{'description': ['The proxy by which the SPICE client will connect to virtual machines.', 'The address must be in the following format: I(protocol://[host]:[port])']}",
    "state": "{'description': ['Should the cluster be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "switch_type": "{'description': ['Type of switch to be used by all networks in given cluster. Either I(legacy) which is using linux bridge or I(ovs) using Open vSwitch.'], 'choices': ['legacy', 'ovs']}",
    "threads_as_cores": "{'description': ['If I(True) the exposed host threads would be treated as cores which can be utilized by virtual machines.']}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "trusted_service": "{'description': ['If I(True) enables integration with an OpenAttestation server.']}",
    "virt": "{'description': ['If I(True), hosts in this cluster will be used to run virtual machines.']}",
    "vm_reason": "{'description': ['If I(True) enables an optional reason field when a virtual machine is shut down from the Manager, allowing the administrator to provide an explanation for the maintenance.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create cluster
- ovirt_cluster:
    data_center: mydatacenter
    name: mycluster
    cpu_type: Intel SandyBridge Family
    description: mycluster
    compatibility_version: 4.0

# Create virt service cluster:
- ovirt_cluster:
    data_center: mydatacenter
    name: mycluster
    cpu_type: Intel Nehalem Family
    description: mycluster
    switch_type: legacy
    compatibility_version: 4.0
    ballooning: true
    gluster: false
    threads_as_cores: true
    ha_reservation: true
    trusted_service: false
    host_reason: false
    vm_reason: true
    ksm_numa: true
    memory_policy: server
    rng_sources:
      - hwrng
      - random

# Create cluster with default network provider
- ovirt_cluster:
    name: mycluster
    data_center: Default
    cpu_type: Intel SandyBridge Family
    external_network_providers:
      - name: ovirt-provider-ovn

# Remove cluster
- ovirt_cluster:
    state: absent
    name: mycluster

# Change cluster Name
- ovirt_cluster:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_cluster_name"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
