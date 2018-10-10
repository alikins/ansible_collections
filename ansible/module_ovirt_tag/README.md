# Ansible module: ansible.module_ovirt_tag


Module to manage tags in oVirt/RHV

## Description

This module manage tags in oVirt/RHV. It can also manage assignments of those tags to entities.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "description": "{'description': ['Description of the tag to manage.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "hosts": "{'description': ['List of the hosts names, which should have assigned this tag.']}",
    "id": "{'description': ['ID of the tag to manage.'], 'version_added': '2.8'}",
    "name": "{'description': ['Name of the tag to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "parent": "{'description': ['Name of the parent tag.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "state": "{'description': ['Should the tag be present/absent/attached/detached.', 'C(Note): I(attached) and I(detached) states are supported since version 2.4.'], 'choices': ['present', 'absent', 'attached', 'detached'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "vms": "{'description': ['List of the VMs names, which should have assigned this tag.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create(if not exists) and assign tag to vms vm1 and vm2:
- ovirt_tag:
    name: mytag
    vms:
      - vm1
      - vm2

# Attach a tag to VM 'vm1', keeping the rest already attached tags on VM:
- ovirt_tag:
    name: mytag
    state: attached
    vms:
      - vm3

# Detach a tag from VM 'vm1', keeping the rest already attached tags on VM:
- ovirt_tag:
    name: mytag
    state: detached
    vms:
      - vm3

# To detach all VMs from tag:
- ovirt_tag:
    name: mytag
    vms: []

# Remove tag
- ovirt_tag:
    state: absent
    name: mytag

# Change cluster Name
- ovirt_tag:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_tag_name"

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
