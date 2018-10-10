# Ansible module: ansible.module_cs_service_offering


Manages service offerings on Apache CloudStack based clouds

## Description

Create and delete service offerings for guest and system VMs.
Update display_text of existing service offering.

## Requirements

TODO

## Arguments

``` json
{
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "bytes_read_rate": "{'description': ['Bytes read rate of the disk offering.']}",
    "bytes_write_rate": "{'description': ['Bytes write rate of the disk offering.']}",
    "cpu_number": "{'description': ['The number of CPUs of the service offering.']}",
    "cpu_speed": "{'description': ['The CPU speed of the service offering in MHz.']}",
    "deployment_planner": "{'description': ['The deployment planner heuristics used to deploy a VM of this offering.', 'If not set, the value of global config C(vm.deployment.planner) is used.']}",
    "disk_iops_customized": "{'description': ['Whether compute offering iops is custom or not.'], 'default': False}",
    "disk_iops_max": "{'description': ['Max. iops of the compute offering.']}",
    "disk_iops_min": "{'description': ['Min. iops of the compute offering.']}",
    "disk_iops_read_rate": "{'description': ['IO requests read rate of the disk offering.']}",
    "disk_iops_write_rate": "{'description': ['IO requests write rate of the disk offering.']}",
    "display_text": "{'description': ['Display text of the service offering.', 'If not set, C(name) will be used as C(display_text) while creating.']}",
    "domain": "{'description': ['Domain the service offering is related to.', 'Public for all domains and subdomains if not set.']}",
    "host_tags": "{'description': ['The host tagsfor this service offering.'], 'aliases': ['host_tag']}",
    "hypervisor_snapshot_reserve": "{'description': ['Hypervisor snapshot reserve space as a percent of a volume.', 'Only for managed storage using Xen or VMware.']}",
    "is_system": "{'description': ['Whether it is a system VM offering or not.'], 'type': 'bool', 'default': False}",
    "is_volatile": "{'description': ['Whether the virtual machine needs to be volatile or not.', 'Every reboot of VM the root disk is detached then destroyed and a fresh root disk is created and attached to VM.'], 'type': 'bool', 'default': False}",
    "limit_cpu_usage": "{'description': ['Restrict the CPU usage to committed service offering.'], 'type': 'bool'}",
    "memory": "{'description': ['The total memory of the service offering in MB.']}",
    "name": "{'description': ['Name of the service offering.'], 'required': True}",
    "network_rate": "{'description': ['Data transfer rate in Mb/s allowed.', 'Supported only for non-system offering and system offerings having C(system_vm_type=domainrouter).']}",
    "offer_ha": "{'description': ['Whether HA is set for the service offering.'], 'type': 'bool', 'default': False}",
    "provisioning_type": "{'description': ['Provisioning type used to create volumes.'], 'choices': ['thin', 'sparse', 'fat']}",
    "service_offering_details": "{'description': ['Details for planner, used to store specific parameters.']}",
    "state": "{'description': ['State of the service offering.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage_tags": "{'description': ['The storage tags for this service offering.'], 'aliases': ['storage_tag']}",
    "storage_type": "{'description': ['The storage type of the service offering.'], 'choices': ['local', 'shared']}",
    "system_vm_type": "{'description': ['The system VM type.', 'Required if C(is_system=true).'], 'choices': ['domainrouter', 'consoleproxy', 'secondarystoragevm']}",
}
```

## Examples


``` yaml

- name: Create a non-volatile compute service offering with local storage
  local_action:
    module: cs_service_offering
    name: Micro
    display_text: Micro 512mb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 512
    host_tags: eco
    storage_type: local

- name: Create a volatile compute service offering with shared storage
  local_action:
    module: cs_service_offering
    name: Tiny
    display_text: Tiny 1gb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 1024
    storage_type: shared
    is_volatile: true
    host_tags: eco
    storage_tags: eco

- name: Create or update a volatile compute service offering with shared storage
  local_action:
    module: cs_service_offering
    name: Tiny
    display_text: Tiny 1gb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 1024
    storage_type: shared
    is_volatile: yes
    host_tags: eco
    storage_tags: eco

- name: Remove a compute service offering
  local_action:
    module: cs_service_offering
    name: Tiny
    state: absent

- name: Create or update a system offering for the console proxy
  local_action:
    module: cs_service_offering
    name: System Offering for Console Proxy 2GB
    display_text: System Offering for Console Proxy 2GB RAM
    is_system: yes
    system_vm_type: consoleproxy
    cpu_number: 1
    cpu_speed: 2198
    memory: 2048
    storage_type: shared
    storage_tags: perf

- name: Remove a system offering
  local_action:
    module: cs_service_offering
    name: System Offering for Console Proxy 2GB
    is_system: yes
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
