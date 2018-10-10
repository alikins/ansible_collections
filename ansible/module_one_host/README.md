# Ansible module: ansible.module_one_host


Manages OpenNebula Hosts

## Description

Manages OpenNebula Hosts

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['The password or token for XMLRPC authentication. If not specified then the value of the ONE_PASSWORD environment variable, if any, is used.'], 'aliases': ['api_token']}",
    "api_url": "{'description': ['The ENDPOINT URL of the XMLRPC server. If not specified then the value of the ONE_URL environment variable, if any, is used.'], 'aliases': ['api_endpoint']}",
    "api_username": "{'description': ['The name of the user for XMLRPC authentication. If not specified then the value of the ONE_USERNAME environment variable, if any, is used.']}",
    "cluster_id": "{'description': ['The cluster ID.'], 'default': 0}",
    "cluster_name": "{'description': ['The cluster specified by name.']}",
    "im_mad_name": "{'description': ['The name of the information manager, this values are taken from the oned.conf with the tag name IM_MAD (name)'], 'default': 'kvm'}",
    "labels": "{'description': ['The labels for this host.']}",
    "name": "{'description': ['Hostname of the machine to manage.'], 'required': True}",
    "state": "{'description': ['Takes the host to the desired lifecycle state.', 'If C(absent) the host will be deleted from the cluster.', 'If C(present) the host will be created in the cluster (includes C(enabled), C(disabled) and C(offline) states).', 'If C(enabled) the host is fully operational.', 'C(disabled), e.g. to perform maintenance operations.', 'C(offline), host is totally offline.'], 'choices': ['absent', 'present', 'enabled', 'disabled', 'offline'], 'default': 'present'}",
    "template": "{'description': ['The template or attribute changes to merge into the host template.'], 'aliases': ['attributes']}",
    "validate_certs": "{'description': ['Whether to validate the SSL certificates or not. This parameter is ignored if PYTHONHTTPSVERIFY environment variable is used.'], 'type': 'bool', 'default': True}",
    "vmm_mad_name": "{'description': ['The name of the virtual machine manager mad name, this values are taken from the oned.conf with the tag name VM_MAD (name)'], 'default': 'kvm'}",
    "wait_timeout": "{'description': ['time to wait for the desired state to be reached before timeout, in seconds.'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Create a new host in OpenNebula
  one_host:
    name: host1
    cluster_id: 1
    api_url: http://127.0.0.1:2633/RPC2

- name: Create a host and adjust its template
  one_host:
    name: host2
    cluster_name: default
    template:
        LABELS:
            - gold
            - ssd
        RESERVED_CPU: -100

```

## License

TODO

## Author Information
  - ['Rafael del Valle (@rvalle)']
