# Ansible module: ansible.module_ovirt_template


Module to manage virtual machine templates in oVirt/RHV

## Description

Module to manage virtual machine templates in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "allow_partial_import": "{'description': ['Boolean indication whether to allow partial registration of a template when C(state) is registered.'], 'type': 'bool', 'version_added': '2.4'}",
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "clone_permissions": "{'description': ['If I(True) then the permissions of the VM (only the direct ones, not the inherited ones) will be copied to the created template.', 'This parameter is used only when C(state) I(present).'], 'type': 'bool', 'default': False}",
    "cluster": "{'description': ['Name of the cluster, where template should be created/imported.']}",
    "cluster_mappings": "{'description': ["Mapper which maps cluster name between Template's OVF and the destination cluster this Template should be registered to, relevant when C(state) is registered. Cluster mapping is described by the following dictionary:", 'C(source_name): The name of the source cluster.', 'C(dest_name): The name of the destination cluster.'], 'version_added': '2.5'}",
    "cpu_profile": "{'description': ['CPU profile to be set to template.']}",
    "description": "{'description': ['Description of the template.']}",
    "domain_mappings": "{'description': ["Mapper which maps aaa domain name between Template's OVF and the destination aaa domain this Template should be registered to, relevant when C(state) is registered. The aaa domain mapping is described by the following dictionary:", 'C(source_name): The name of the source aaa domain.', 'C(dest_name): The name of the destination aaa domain.'], 'version_added': '2.5'}",
    "exclusive": "{'description': ['When C(state) is I(exported) this parameter indicates if the existing templates with the same name should be overwritten.'], 'type': 'bool'}",
    "export_domain": "{'description': ['When C(state) is I(exported) or I(imported) this parameter specifies the name of the export storage domain.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "id": "{'description': ['ID of the template to be registered.'], 'version_added': '2.4'}",
    "image_disk": "{'description': ['When C(state) is I(imported) and C(image_provider) is used this parameter specifies the name of disk to be imported as template.'], 'aliases': ['glance_image_disk_name']}",
    "image_provider": "{'description': ['When C(state) is I(imported) this parameter specifies the name of the image provider to be used.']}",
    "io_threads": "{'description': ['Number of IO threads used by virtual machine. I(0) means IO threading disabled.'], 'version_added': '2.7'}",
    "memory": "{'description': ['Amount of memory of the template. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).'], 'version_added': '2.6'}",
    "memory_guaranteed": "{'description': ['Amount of minimal guaranteed memory of the template. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).', "C(memory_guaranteed) parameter can't be lower than C(memory) parameter."], 'version_added': '2.6'}",
    "memory_max": "{'description': ['Upper bound of template memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).'], 'version_added': '2.6'}",
    "name": "{'description': ['Name of the template to manage.']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "operating_system": "{'description': ['Operating system of the template.', 'Default value is set by oVirt/RHV engine.', 'Possible values are: debian_7, freebsd, freebsdx64, other, other_linux, other_linux_ppc64, other_ppc64, rhel_3, rhel_4, rhel_4x64, rhel_5, rhel_5x64, rhel_6, rhel_6x64, rhel_6_ppc64, rhel_7x64, rhel_7_ppc64, sles_11, sles_11_ppc64, ubuntu_12_04, ubuntu_12_10, ubuntu_13_04, ubuntu_13_10, ubuntu_14_04, ubuntu_14_04_ppc64, windows_10, windows_10x64, windows_2003, windows_2003x64, windows_2008, windows_2008x64, windows_2008r2x64, windows_2008R2x64, windows_2012x64, windows_2012R2x64, windows_7, windows_7x64, windows_8, windows_8x64, windows_xp'], 'version_added': '2.6'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "role_mappings": "{'description': ["Mapper which maps role name between Template's OVF and the destination role this Template should be registered to, relevant when C(state) is registered. Role mapping is described by the following dictionary:", 'C(source_name): The name of the source role.', 'C(dest_name): The name of the destination role.'], 'version_added': '2.5'}",
    "seal": "{'description': ["'Sealing' is an operation that erases all machine-specific configurations from a filesystem: This includes SSH keys, UDEV rules, MAC addresses, system ID, hostname, etc. If I(true) subsequent virtual machines made from this template will avoid configuration inheritance.", 'This parameter is used only when C(state) I(present).'], 'default': False, 'type': 'bool', 'version_added': '2.5'}",
    "state": "{'description': ["Should the template be present/absent/exported/imported/registered. When C(state) is I(registered) and the unregistered template's name belongs to an already registered in engine template in the same DC then we fail to register the unregistered template."], 'choices': ['present', 'absent', 'exported', 'imported', 'registered'], 'default': 'present'}",
    "storage_domain": "{'description': ['When C(state) is I(imported) this parameter specifies the name of the destination data storage domain. When C(state) is I(registered) this parameter specifies the name of the data storage domain of the unregistered template.']}",
    "template_image_disk_name": "{'description': ['When C(state) is I(imported) and C(image_provider) is used this parameter specifies the new name for imported disk, if omitted then I(image_disk) name is used by default. This parameter is used only in case of importing disk image from Glance domain.'], 'version_added': '2.4'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "vm": "{'description': ['Name of the VM, which will be used to create template.']}",
    "vnic_profile_mappings": "{'description': ['Mapper which maps an external virtual NIC profile to one that exists in the engine when C(state) is registered. vnic_profile is described by the following dictionary:', 'C(source_network_name): The network name of the source network.', 'C(source_profile_name): The profile name related to the source network.', 'C(target_profile_id): The id of the target profile id to be mapped to in the engine.'], 'version_added': '2.5'}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create template from vm
- ovirt_template:
    cluster: Default
    name: mytemplate
    vm: rhel7
    cpu_profile: Default
    description: Test

# Import template
- ovirt_template:
  state: imported
  name: mytemplate
  export_domain: myexport
  storage_domain: mystorage
  cluster: mycluster

# Remove template
- ovirt_template:
    state: absent
    name: mytemplate

# Change Template Name
- ovirt_template:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_template_name"

# Register template
- ovirt_template:
  state: registered
  storage_domain: mystorage
  cluster: mycluster
  name: mytemplate

# Register template using id
- ovirt_template:
  state: registered
  storage_domain: mystorage
  cluster: mycluster
  id: 1111-1111-1111-1111

# Register template, allowing partial import
- ovirt_template:
  state: registered
  storage_domain: mystorage
  allow_partial_import: "True"
  cluster: mycluster
  id: 1111-1111-1111-1111

# Register template with vnic profile mappings
- ovirt_template:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    vnic_profile_mappings:
      - source_network_name: mynetwork
        source_profile_name: mynetwork
        target_profile_id: 3333-3333-3333-3333
      - source_network_name: mynetwork2
        source_profile_name: mynetwork2
        target_profile_id: 4444-4444-4444-4444

# Register template with mapping
- ovirt_template:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    role_mappings:
      - source_name: Role_A
        dest_name: Role_B
    domain_mappings:
      - source_name: Domain_A
        dest_name: Domain_B
    cluster_mappings:
      - source_name: cluster_A
        dest_name: cluster_B

# Import image from Glance s a template
- ovirt_template:
    state: imported
    name: mytemplate
    image_disk: "centos7"
    template_image_disk_name: centos7_from_glance
    image_provider: "glance_domain"
    storage_domain: mystorage
    cluster: mycluster

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
