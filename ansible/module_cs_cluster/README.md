# Ansible module: ansible.module_cs_cluster


Manages host clusters on Apache CloudStack based clouds

## Description

Create, update and remove clusters.

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
    "cluster_type": "{'description': ['Type of the cluster.', 'Required if C(state=present)'], 'choices': ['CloudManaged', 'ExternalManaged']}",
    "guest_vswitch_name": "{'description': ['Name of virtual switch used for guest traffic in the cluster.', 'This would override zone wide traffic label setting.']}",
    "guest_vswitch_type": "{'description': ['Type of virtual switch used for guest traffic in the cluster.', 'Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)'], 'choices': ['vmwaresvs', 'vmwaredvs']}",
    "hypervisor": "{'description': ['Name the hypervisor to be used.', 'Required if C(state=present).'], 'choices': ['KVM', 'VMware', 'BareMetal', 'XenServer', 'LXC', 'HyperV', 'UCS', 'OVM']}",
    "name": "{'description': ['name of the cluster.'], 'required': True}",
    "ovm3_cluster": "{'description': ['Ovm3 native OCFS2 clustering enabled for cluster.']}",
    "ovm3_pool": "{'description': ['Ovm3 native pooling enabled for cluster.']}",
    "ovm3_vip": "{'description': ['Ovm3 vip to use for pool (and cluster).']}",
    "password": "{'description': ['Password for the cluster.']}",
    "pod": "{'description': ['Name of the pod in which the cluster belongs to.']}",
    "public_vswitch_name": "{'description': ['Name of virtual switch used for public traffic in the cluster.', 'This would override zone wide traffic label setting.']}",
    "public_vswitch_type": "{'description': ['Type of virtual switch used for public traffic in the cluster.', 'Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)'], 'choices': ['vmwaresvs', 'vmwaredvs']}",
    "state": "{'description': ['State of the cluster.'], 'default': 'present', 'choices': ['present', 'absent', 'disabled', 'enabled']}",
    "url": "{'description': ['URL for the cluster']}",
    "username": "{'description': ['Username for the cluster.']}",
    "vms_ip_address": "{'description': ['IP address of the VSM associated with this cluster.']}",
    "vms_password": "{'description': ['Password for the VSM associated with this cluster.']}",
    "vms_username": "{'description': ['Username for the VSM associated with this cluster.']}",
    "zone": "{'description': ['Name of the zone in which the cluster belongs to.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# Ensure a cluster is present
- local_action:
    module: cs_cluster
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    hypervisor: KVM
    cluster_type: CloudManaged

# Ensure a cluster is disabled
- local_action:
    module: cs_cluster
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: disabled

# Ensure a cluster is enabled
- local_action:
    module: cs_cluster
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: enabled

# Ensure a cluster is absent
- local_action:
    module: cs_cluster
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
