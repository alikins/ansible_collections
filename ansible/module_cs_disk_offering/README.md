# Ansible module: ansible.module_cs_disk_offering


Manages disk offerings on Apache CloudStack based clouds

## Description

Create and delete disk offerings for guest VMs.
Update display_text or display_offering of existing disk offering.

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
    "customized": "{'description': ['Whether disk offering iops is custom or not.'], 'type': 'bool', 'default': False}",
    "disk_size": "{'description': ['Size of the disk offering in GB (1GB = 1,073,741,824 bytes).']}",
    "display_offering": "{'description': ['An optional field, whether to display the offering to the end user or not.'], 'type': 'bool'}",
    "display_text": "{'description': ['Display text of the disk offering.', 'If not set, C(name) will be used as C(display_text) while creating.']}",
    "domain": "{'description': ['Domain the disk offering is related to.', 'Public for all domains and subdomains if not set.']}",
    "hypervisor_snapshot_reserve": "{'description': ['Hypervisor snapshot reserve space as a percent of a volume.', 'Only for managed storage using Xen or VMware.']}",
    "iops_max": "{'description': ['Max. iops of the disk offering.']}",
    "iops_min": "{'description': ['Min. iops of the disk offering.']}",
    "iops_read_rate": "{'description': ['IO requests read rate of the disk offering.']}",
    "iops_write_rate": "{'description': ['IO requests write rate of the disk offering.']}",
    "name": "{'description': ['Name of the disk offering.'], 'required': True}",
    "provisioning_type": "{'description': ['Provisioning type used to create volumes.'], 'choices': ['thin', 'sparse', 'fat']}",
    "state": "{'description': ['State of the disk offering.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage_tags": "{'description': ['The storage tags for this disk offering.'], 'aliases': ['storage_tag']}",
    "storage_type": "{'description': ['The storage type of the disk offering.'], 'choices': ['local', 'shared']}",
}
```

## Examples


``` yaml

- name: Create a disk offering with local storage
  local_action:
    module: cs_disk_offering
    name: small
    display_text: Small 10GB
    disk_size: 10
    storage_type: local

- name: Create or update a disk offering with shared storage
  local_action:
    module: cs_disk_offering
    name: small
    display_text: Small 10GB
    disk_size: 10
    storage_type: shared
    storage_tags: SAN01

- name: Remove a disk offering
  local_action:
    module: cs_disk_offering
    name: small
    state: absent

```

## License

TODO

## Author Information
  - ['David Passante (@dpassante)', 'René Moser(@resmo)']
  - ['David Passante (@dpassante)', 'René Moser(@resmo)']
