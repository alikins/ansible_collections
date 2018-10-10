# Ansible module: ansible.module_ovirt_quota


Module to manage datacenter quotas in oVirt/RHV

## Description

Module to manage datacenter quotas in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "cluster_grace": "{'description': ['Cluster grace(hard limit) defined in percentage (1-100).'], 'aliases': ['cluster_hard_limit']}",
    "cluster_threshold": "{'description': ['Cluster threshold(soft limit) defined in percentage (0-100).'], 'aliases': ['cluster_soft_limit']}",
    "clusters": "{'description': ['List of dictionary of cluster limits, which is valid to specific cluster.', "If cluster isn't specified it's valid to all clusters in system:", 'C(cluster) - Name of the cluster.', 'C(memory) - Memory limit (in GiB).', 'C(cpu) - CPU limit.']}",
    "data_center": "{'description': ['Name of the datacenter where quota should be managed.'], 'required': True}",
    "description": "{'description': ['Description of the quota to manage.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "id": "{'description': ['ID of the quota to manage.'], 'version_added': '2.8'}",
    "name": "{'description': ['Name of the quota to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "state": "{'description': ['Should the quota be present/absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage_grace": "{'description': ['Storage grace(hard limit) defined in percentage (1-100).'], 'aliases': ['storage_hard_limit']}",
    "storage_threshold": "{'description': ['Storage threshold(soft limit) defined in percentage (0-100).'], 'aliases': ['storage_soft_limit']}",
    "storages": "{'description': ['List of dictionary of storage limits, which is valid to specific storage.', "If storage isn't specified it's valid to all storages in system:", 'C(storage) - Name of the storage.', 'C(size) - Size limit (in GiB).']}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add cluster quota to cluster cluster1 with memory limit 20GiB and CPU limit to 10:
- ovirt_quota:
    name: quota1
    data_center: dcX
    clusters:
        - name: cluster1
          memory: 20
          cpu: 10

# Add cluster quota to all clusters with memory limit 30GiB and CPU limit to 15:
- ovirt_quota:
    name: quota2
    data_center: dcX
    clusters:
        - memory: 30
          cpu: 15

# Add storage quota to storage data1 with size limit to 100GiB
- ovirt_quota:
    name: quota3
    data_center: dcX
    storage_grace: 40
    storage_threshold: 60
    storages:
        - name: data1
          size: 100

# Remove quota quota1 (Note the quota must not be assigned to any VM/disk):
- ovirt_quota:
    state: absent
    data_center: dcX
    name: quota1

# Change Quota Name
- ovirt_quota:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_quota_name"
    data_center: dcX

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
