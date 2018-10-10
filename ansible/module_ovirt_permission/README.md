# Ansible module: ansible.module_ovirt_permission


Module to manage permissions of users/groups in oVirt/RHV

## Description

Module to manage permissions of users/groups in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "authz_name": "{'description': ['Authorization provider of the user/group.'], 'required': True, 'aliases': ['domain']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "group_name": "{'description': ['Name of the group to manage.', 'Note that if group does not exist in the system this module will fail, you should ensure the group exists by using M(ovirt_groups) module.']}",
    "namespace": "{'description': ['Namespace of the authorization provider, where user/group resides.']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "object_id": "{'description': ['ID of the object where the permissions should be managed.']}",
    "object_name": "{'description': ['Name of the object where the permissions should be managed.']}",
    "object_type": "{'description': ['The object where the permissions should be managed.'], 'choices': ['cluster', 'cpu_profile', 'data_center', 'disk', 'disk_profile', 'host', 'network', 'storage_domain', 'system', 'template', 'vm', 'vm_pool', 'vnic_profile'], 'default': 'vm'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "quota_name": "{'description': ['Name of the quota to assign permission. Works only with C(object_type) I(data_center).'], 'version_added': '2.7'}",
    "role": "{'description': ['Name of the role to be assigned to user/group on specific object.'], 'default': 'UserRole'}",
    "state": "{'description': ['Should the permission be present/absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "user_name": "{'description': ["Username of the user to manage. In most LDAPs it's I(uid) of the user, but in Active Directory you must specify I(UPN) of the user.", 'Note that if user does not exist in the system this module will fail, you should ensure the user exists by using M(ovirt_users) module.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Add user user1 from authorization provider example.com-authz
  ovirt_permission:
    user_name: user1
    authz_name: example.com-authz
    object_type: vm
    object_name: myvm
    role: UserVmManager

- name: Remove permission from user
  ovirt_permission:
    state: absent
    user_name: user1
    authz_name: example.com-authz
    object_type: cluster
    object_name: mycluster
    role: ClusterAdmin

- name: Assign QuotaConsumer role to user
  ovirt_permissions:
    state: present
    user_name: user1
    authz_name: example.com-authz
    object_type: data_center
    object_name: mydatacenter
    quota_name: myquota
    role: QuotaConsumer

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
