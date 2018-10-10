# Ansible module: ansible.module_ovirt_host


Module to manage hosts in oVirt/RHV

## Description

Module to manage hosts in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "activate": "{'description': ['If C(state) is I(present) activate the host.', "This parameter is good to disable, when you don't want to change the state of host when using I(present) C(state)."], 'default': True, 'type': 'bool', 'version_added': 2.4}",
    "address": "{'description': ['Host address. It can be either FQDN (preferred) or IP address.']}",
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "check_upgrade": "{'description': ['If I(true) and C(state) is I(upgraded) run check for upgrade action before executing upgrade action.'], 'default': True, 'type': 'bool', 'version_added': 2.4}",
    "cluster": "{'description': ['Name of the cluster, where host should be created.']}",
    "comment": "{'description': ['Description of the host.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "force": "{'description': ['If True host will be forcibly moved to desired state.'], 'default': False, 'type': 'bool'}",
    "hosted_engine": "{'description': ['If I(deploy) it means this host should deploy also hosted engine components.', 'If I(undeploy) it means this host should un-deploy hosted engine components and this host will not function as part of the High Availability cluster.'], 'choices': ['deploy', 'undeploy']}",
    "id": "{'description': ['ID of the host to manage.'], 'version_added': '2.8'}",
    "iscsi": "{'description': ['If C(state) is I(iscsidiscover) it means that the iscsi attribute is being used to discover targets', 'If C(state) is I(iscsilogin) it means that the iscsi attribute is being used to login to the specified targets passed as part of the iscsi attribute'], 'version_added': '2.4'}",
    "kdump_integration": "{'description': ['Specify if host will have enabled Kdump integration.'], 'choices': ['enabled', 'disabled']}",
    "kernel_params": "{'description': ['List of kernel boot parameters.', 'Following are most common kernel parameters used for host:', 'Hostdev Passthrough & SR-IOV: intel_iommu=on', 'Nested Virtualization: kvm-intel.nested=1', 'Unsafe Interrupts: vfio_iommu_type1.allow_unsafe_interrupts=1', 'PCI Reallocation: pci=realloc', 'C(Note:)', 'Modifying kernel boot parameters settings can lead to a host boot failure. Please consult the product documentation before doing any changes.', 'Kernel boot parameters changes require host deploy and restart. The host needs to be I(reinstalled) successfully and then to be I(rebooted) for kernel boot parameters to be applied.']}",
    "name": "{'description': ['Name of the host to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "override_display": "{'description': ['Override the display address of all VMs on this host with specified address.'], 'type': 'bool'}",
    "override_iptables": "{'description': ['If True host iptables will be overridden by host deploy script.', 'Note that C(override_iptables) is I(false) by default in oVirt/RHV.'], 'type': 'bool'}",
    "password": "{'description': ["Password of the root. It's required in case C(public_key) is set to I(False)."]}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "power_management_enabled": "{'description': ['Enable or disable power management of the host.', 'For more comprehensive setup of PM use C(ovirt_host_pm) module.'], 'version_added': 2.4, 'type': 'bool'}",
    "public_key": "{'description': ['I(True) if the public key should be used to authenticate to host.', "It's required in case C(password) is not set."], 'default': False, 'type': 'bool', 'aliases': ['ssh_public_key']}",
    "reboot_after_upgrade": "{'description': ['If I(true) and C(state) is I(upgraded) reboot host after successful upgrade.'], 'default': True, 'type': 'bool', 'version_added': 2.6}",
    "spm_priority": "{'description': ['SPM priority of the host. Integer value from 1 to 10, where higher number means higher priority.']}",
    "state": "{'description': ['State which should a host to be in after successful completion.', 'I(iscsilogin) and I(iscsidiscover) are supported since version 2.4.'], 'choices': ['present', 'absent', 'maintenance', 'upgraded', 'started', 'restarted', 'stopped', 'reinstalled', 'iscsidiscover', 'iscsilogin'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the host to get into desired state.'], 'default': 600}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add host with username/password supporting SR-IOV.
# Note that override_iptables is false by default in oVirt/RHV:
- ovirt_host:
    cluster: Default
    name: myhost
    address: 10.34.61.145
    password: secret
    override_iptables: true
    kernel_params:
      - intel_iommu=on

# Add host using public key
- ovirt_host:
    public_key: true
    cluster: Default
    name: myhost2
    address: 10.34.61.145
    override_iptables: true

# Deploy hosted engine host
- ovirt_host:
    cluster: Default
    name: myhost2
    password: secret
    address: 10.34.61.145
    override_iptables: true
    hosted_engine: deploy

# Maintenance
- ovirt_host:
    state: maintenance
    name: myhost

# Restart host using power management:
- ovirt_host:
    state: restarted
    name: myhost

# Upgrade host
- ovirt_host:
    state: upgraded
    name: myhost

# discover iscsi targets
- ovirt_host:
    state: iscsidiscover
    name: myhost
    iscsi:
      username: iscsi_user
      password: secret
      address: 10.34.61.145
      port: 3260


# login to iscsi targets
- ovirt_host:
    state: iscsilogin
    name: myhost
    iscsi:
      username: iscsi_user
      password: secret
      address: 10.34.61.145
      target: "iqn.2015-07.com.mlipchuk2.redhat:444"
      port: 3260


# Reinstall host using public key
- ovirt_host:
    state: reinstalled
    name: myhost
    public_key: true

# Remove host
- ovirt_host:
    state: absent
    name: myhost
    force: True

# Change host Name
- ovirt_host:
    id: 00000000-0000-0000-0000-000000000000
    name: "new host name"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
