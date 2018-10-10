# Ansible module: ansible.module_cs_instance


Manages instances and virtual machines on Apache CloudStack based clouds

## Description

Deploy, start, update, scale, restart, restore, stop and destroy instances.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the instance is related to.']}",
    "affinity_groups": "{'description': ['Affinity groups names to be applied to the new instance.'], 'aliases': ['affinity_group']}",
    "allow_root_disk_shrink": "{'description': ['Enables a volume shrinkage when the new size is smaller than the old one.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cpu": "{'description': ['The number of CPUs to allocate to the instance, used with custom service offerings']}",
    "cpu_speed": "{'description': ['The clock speed/shares allocated to the instance, used with custom service offerings']}",
    "details": "{'description': ['Map to specify custom parameters.'], 'version_added': '2.6'}",
    "disk_offering": "{'description': ['Name of the disk offering to be used.']}",
    "disk_size": "{'description': ['Disk size in GByte required if deploying instance from ISO.']}",
    "display_name": "{'description': ['Custom display name of the instances.', 'Display name will be set to C(name) if not specified.', 'Either C(name) or C(display_name) is required.']}",
    "domain": "{'description': ['Domain the instance is related to.']}",
    "force": "{'description': ['Force stop/start the instance if required to apply changes, otherwise a running instance will not be changed.'], 'type': 'bool', 'default': False}",
    "group": "{'description': ['Group in where the new instance should be in.']}",
    "host": "{'description': ['Host on which an instance should be deployed or started on.', 'Only considered when I(state=started) or instance is running.', 'Requires root admin privileges.'], 'version_added': 2.6}",
    "hypervisor": "{'description': ['Name the hypervisor to be used for creating the new instance.', 'Relevant when using I(state=present), but only considered if not set on ISO/template.', 'If not set or found on ISO/template, first found hypervisor will be used.'], 'choices': ['KVM', 'kvm', 'VMware', 'vmware', 'BareMetal', 'baremetal', 'XenServer', 'xenserver', 'LXC', 'lxc', 'HyperV', 'hyperv', 'UCS', 'ucs', 'OVM', 'ovm', 'Simulator', 'simulator']}",
    "ip6_address": "{'description': ["IPv6 address for default instance's network."]}",
    "ip_address": "{'description': ["IPv4 address for default instance's network during creation."]}",
    "ip_to_networks": "{'description': ["List of mappings in the form I({'network': NetworkName, 'ip': 1.2.3.4})", 'Mutually exclusive with C(networks) option.'], 'aliases': ['ip_to_network']}",
    "iso": "{'description': ['Name or id of the ISO to be used for creating the new instance.', 'Required when using I(state=present).', 'Mutually exclusive with C(template) option.']}",
    "keyboard": "{'description': ['Keyboard device type for the instance.'], 'choices': ['de', 'de-ch', 'es', 'fi', 'fr', 'fr-be', 'fr-ch', 'is', 'it', 'jp', 'nl-be', 'no', 'pt', 'uk', 'us']}",
    "memory": "{'description': ['The memory allocated to the instance, used with custom service offerings']}",
    "name": "{'description': ['Host name of the instance. C(name) can only contain ASCII letters.', 'Name will be generated (UUID) by CloudStack if not specified and can not be changed afterwards.', 'Either C(name) or C(display_name) is required.']}",
    "networks": "{'description': ['List of networks to use for the new instance.'], 'aliases': ['network']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the instance to be deployed in.']}",
    "root_disk_size": "{'description': ['Root disk size in GByte required if deploying instance with KVM hypervisor and want resize the root disk size at startup (need CloudStack >= 4.4, cloud-initramfs-growroot installed and enabled in the template)']}",
    "security_groups": "{'description': ['List of security groups the instance to be applied to.'], 'aliases': ['security_group']}",
    "service_offering": "{'description': ['Name or id of the service offering of the new instance.', 'If not set, first found service offering is used.']}",
    "ssh_key": "{'description': ['Name of the SSH key to be deployed on the new instance.']}",
    "state": "{'description': ['State of the instance.'], 'default': 'present', 'choices': ['deployed', 'started', 'stopped', 'restarted', 'restored', 'destroyed', 'expunged', 'present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'If you want to delete all tags, set a empty list e.g. I(tags: []).'], 'aliases': ['tag']}",
    "template": "{'description': ['Name, display text or id of the template to be used for creating the new instance.', 'Required when using I(state=present).', 'Mutually exclusive with C(ISO) option.']}",
    "template_filter": "{'description': ['Name of the filter used to search for the template or iso.', 'Used for params C(iso) or C(template) on I(state=present).', 'The filter C(all) was added in 2.6.'], 'default': 'executable', 'choices': ['all', 'featured', 'self', 'selfexecutable', 'sharedexecutable', 'executable', 'community'], 'aliases': ['iso_filter'], 'version_added': '2.1'}",
    "user_data": "{'description': ['Optional data (ASCII) that can be sent to the instance upon a successful deployment.', 'The data will be automatically base64 encoded.', 'Consider switching to HTTP_POST by using I(CLOUDSTACK_METHOD=post) to increase the HTTP_GET size limit of 2KB to 32 KB.']}",
    "zone": "{'description': ['Name of the zone in which the instance should be deployed.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# NOTE: Names of offerings and ISOs depending on the CloudStack configuration.
- name: create a instance from an ISO
  cs_instance:
    name: web-vm-1
    iso: Linux Debian 7 64-bit
    hypervisor: VMware
    project: Integration
    zone: ch-zrh-ix-01
    service_offering: 1cpu_1gb
    disk_offering: PerfPlus Storage
    disk_size: 20
    networks:
      - Server Integration
      - Sync Integration
      - Storage Integration
  delegate_to: localhost

- name: for changing a running instance, use the 'force' parameter
  cs_instance:
    name: web-vm-1
    display_name: web-vm-01.example.com
    iso: Linux Debian 7 64-bit
    service_offering: 2cpu_2gb
    force: yes
  delegate_to: localhost

# NOTE: user_data can be used to kickstart the instance using cloud-init yaml config.
- name: create or update a instance on Exoscale's public cloud using display_name.
  cs_instance:
    display_name: web-vm-1
    template: Linux Debian 7 64-bit
    service_offering: Tiny
    ssh_key: john@example.com
    tags:
      - key: admin
        value: john
      - key: foo
        value: bar
    user_data: |
        #cloud-config
        packages:
          - nginx
  delegate_to: localhost

- name: create an instance with multiple interfaces specifying the IP addresses
  cs_instance:
    name: web-vm-1
    template: Linux Debian 7 64-bit
    service_offering: Tiny
    ip_to_networks:
      - network: NetworkA
        ip: 10.1.1.1
      - network: NetworkB
        ip: 192.0.2.1
  delegate_to: localhost

- name: ensure an instance is stopped
  cs_instance:
    name: web-vm-1
    state: stopped
  delegate_to: localhost

- name: ensure an instance is running
  cs_instance:
    name: web-vm-1
    state: started
  delegate_to: localhost

- name: remove an instance
  cs_instance:
    name: web-vm-1
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
