# Ansible module: ansible.module_cs_storage_pool


Manages Primary Storage Pools on Apache CloudStack based clouds

## Description

Create, update, put into maintenance, disable, enable and remove storage pools.

## Requirements

TODO

## Arguments

``` json
{
    "allocation_state": "{'description': ['Allocation state of the storage pool.'], 'choices': ['enabled', 'disabled', 'maintenance']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "capacity_bytes": "{'description': ['Bytes CloudStack can provision from this storage pool.']}",
    "capacity_iops": "{'description': ['Bytes CloudStack can provision from this storage pool.']}",
    "cluster": "{'description': ['Name of the cluster.']}",
    "hypervisor": "{'description': ['Required when creating a zone scoped pool.'], 'choices': ['KVM', 'VMware', 'BareMetal', 'XenServer', 'LXC', 'HyperV', 'UCS', 'OVM', 'Simulator']}",
    "managed": "{'description': ['Whether the storage pool should be managed by CloudStack.', 'Only considere on creation.']}",
    "name": "{'description': ['Name of the storage pool.'], 'required': True}",
    "pod": "{'description': ['Name of the pod.']}",
    "provider": "{'description': ['Name of the storage provider e.g. SolidFire, SolidFireShared, DefaultPrimary, CloudByte.'], 'default': 'DefaultPrimary'}",
    "scope": "{'description': ['The scope of the storage pool.', 'Defaults to cluster when C(cluster) is provided, otherwise zone.'], 'choices': ['cluster', 'zone']}",
    "state": "{'description': ['State of the storage pool.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "storage_tags": "{'description': ['Tags associated with this storage pool.']}",
    "storage_url": "{'description': ['URL of the storage pool.', 'Required if C(state=present).']}",
    "zone": "{'description': ['Name of the zone in which the host should be deployed.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: ensure a zone scoped storage_pool is present
  local_action:
    module: cs_storage_pool
    zone: zone01
    storage_url: rbd://admin:SECRET@ceph-mons.domain/poolname
    provider: DefaultPrimary
    name: Ceph RBD
    scope: zone
    hypervisor: KVM

- name: ensure a cluster scoped storage_pool is disabled
  local_action:
    module: cs_storage_pool
    name: Ceph RBD
    zone: zone01
    cluster: cluster01
    pod: pod01
    storage_url: rbd://admin:SECRET@ceph-the-mons.domain/poolname
    provider: DefaultPrimary
    scope: cluster
    allocation_state: disabled

- name: ensure a cluster scoped storage_pool is in maintenance
  local_action:
    module: cs_storage_pool
    name: Ceph RBD
    zone: zone01
    cluster: cluster01
    pod: pod01
    storage_url: rbd://admin:SECRET@ceph-the-mons.domain/poolname
    provider: DefaultPrimary
    scope: cluster
    allocation_state: maintenance

- name: ensure a storage_pool is absent
  local_action:
    module: cs_storage_pool
    name: Ceph RBD
    state: absent

```

## License

TODO

## Author Information
  - ['Netservers Ltd. (@netservers)', 'René Moser (@resmo)']
  - ['Netservers Ltd. (@netservers)', 'René Moser (@resmo)']
