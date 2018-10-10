# Ansible module: ansible.module_cs_template


Manages templates on Apache CloudStack based clouds

## Description

Register templates from an URL.
Create templates from a ROOT volume of a stopped VM or its snapshot.
Update (since version 2.7), extract and delete templates.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the template, snapshot or VM is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "bits": "{'description': ['32 or 64 bits support.'], 'default': 64, 'choices': [32, 64]}",
    "checksum": "{'description': ['The MD5 checksum value of this template.', 'If set, we search by checksum instead of name.']}",
    "cross_zones": "{'description': ['Whether the template should be synced or removed across zones.', 'Only used if C(state) is present or absent.'], 'default': False, 'type': 'bool'}",
    "details": "{'description': ['Template details in key/value pairs.']}",
    "display_text": "{'description': ['Display text of the template.']}",
    "domain": "{'description': ['Domain the template, snapshot or VM is related to.']}",
    "format": "{'description': ['The format for the template.', 'Only considered if I(state=present).'], 'choices': ['QCOW2', 'RAW', 'VHD', 'OVA']}",
    "hypervisor": "{'description': ['Name the hypervisor to be used for creating the new template.', 'Relevant when using I(state=present).'], 'choices': ['KVM', 'kvm', 'VMware', 'vmware', 'BareMetal', 'baremetal', 'XenServer', 'xenserver', 'LXC', 'lxc', 'HyperV', 'hyperv', 'UCS', 'ucs', 'OVM', 'ovm', 'Simulator', 'simulator']}",
    "is_dynamically_scalable": "{'description': ['Register the template having XS/VMWare tools installed in order to support dynamic scaling of VM CPU/memory.', 'Only used if C(state) is present.'], 'type': 'bool'}",
    "is_extractable": "{'description': ['Allows the template or its derivatives to be extractable.'], 'type': 'bool'}",
    "is_featured": "{'description': ['Register the template to be featured.', 'Only used if C(state) is present.'], 'type': 'bool'}",
    "is_public": "{'description': ['Register the template to be publicly available to all users.', 'Only used if C(state) is present.'], 'type': 'bool'}",
    "is_ready": "{'description': ['Note: this flag was not implemented and therefore marked as deprecated.', 'Deprecated, will be removed in version 2.11.'], 'type': 'bool'}",
    "is_routing": "{'description': ['Sets the template type to routing, i.e. if template is used to deploy routers.', 'Only considered if C(url) is used.'], 'type': 'bool'}",
    "mode": "{'description': ['Mode for the template extraction.', 'Only used if I(state=extracted).'], 'default': 'http_download', 'choices': ['http_download', 'ftp_upload']}",
    "name": "{'description': ['Name of the template.'], 'required': True}",
    "os_type": "{'description': ['OS type that best represents the OS of this template.']}",
    "password_enabled": "{'description': ['Enable template password reset support.'], 'type': 'bool'}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the template to be registered in.']}",
    "requires_hvm": "{'description': ['Whether the template requires HVM or not.', 'Only considered while creating the template.'], 'type': 'bool'}",
    "snapshot": "{'description': ['Name of the snapshot, created from the VM ROOT volume, the template will be created from.', 'C(vm) is required together with this argument.']}",
    "sshkey_enabled": "{'description': ['True if the template supports the sshkey upload feature.', 'Only considered if C(url) is used (API limitation).'], 'type': 'bool'}",
    "state": "{'description': ['State of the template.'], 'default': 'present', 'choices': ['present', 'absent', 'extracted']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "template_filter": "{'description': ['Name of the filter used to search for the template.', 'The filter C(all) was added in 2.7.'], 'default': 'self', 'choices': ['all', 'featured', 'self', 'selfexecutable', 'sharedexecutable', 'executable', 'community']}",
    "template_find_options": "{'description': ['Options to find a template uniquely.', 'More than one allowed.'], 'choices': ['display_text', 'checksum', 'cross_zones'], 'version_added': 2.7, 'aliases': ['template_find_option'], 'default': []}",
    "template_tag": "{'description': ['The tag for this template.']}",
    "url": "{'description': ['URL of where the template is hosted on I(state=present).', 'URL to which the template would be extracted on I(state=extracted).', 'Mutually exclusive with C(vm).']}",
    "vm": "{'description': ['VM name the template will be created from its volume or alternatively from a snapshot.', 'VM must be in stopped state if created from its volume.', 'Mutually exclusive with C(url).']}",
    "zone": "{'description': ['Name of the zone you wish the template to be registered or deleted from.', 'If not specified, first found zone will be used.']}",
}
```

## Examples


``` yaml

- name: register a systemvm template
  local_action:
    module: cs_template
    name: systemvm-vmware-4.5
    url: "http://packages.shapeblue.com/systemvmtemplate/4.5/systemvm64template-4.5-vmware.ova"
    hypervisor: VMware
    format: OVA
    cross_zones: yes
    os_type: Debian GNU/Linux 7(64-bit)

- name: Create a template from a stopped virtual machine's volume
  local_action:
    module: cs_template
    name: Debian 9 (64-bit) 20GB ({{ ansible_date_time.date }})
    vm: debian-9-base-vm
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

# Note: Use template_find_option(s) when a template name is not unique
- name: Create a template from a stopped virtual machine's volume
  local_action:
    module: cs_template
    name: Debian 9 (64-bit)
    display_text: Debian 9 (64-bit) 20GB ({{ ansible_date_time.date }})
    template_find_option: display_text
    vm: debian-9-base-vm
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

- name: create a template from a virtual machine's root volume snapshot
  local_action:
    module: cs_template
    name: Debian 9 (64-bit) Snapshot ROOT-233_2015061509114
    snapshot: ROOT-233_2015061509114
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

- name: Remove a template
  local_action:
    module: cs_template
    name: systemvm-4.2
    cross_zones: yes
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
