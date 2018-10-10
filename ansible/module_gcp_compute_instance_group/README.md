# Ansible module: ansible.module_gcp_compute_instance_group


Creates a GCP InstanceGroup

## Description

Represents an Instance Group resource. Instance groups are self-managed and can contain identical or different instances. Instance groups do not use an instance template. Unlike managed instance groups, you must create and add instances to an instance group manually.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "name": "{'description': ['The name of the instance group.', 'The name must be 1-63 characters long, and comply with RFC1035.'], 'required': False}",
    "named_ports": "{'description': ['Assigns a name to a port number.', 'For example: {name: "http", port: 80}.', 'This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports.', 'For example: [{name: "http", port: 80},{name: "http", port: 8080}]  Named ports apply to all instances in this instance group.'], 'required': False, 'suboptions': {'name': {'description': ['The name for this named port.', 'The name must be 1-63 characters long, and comply with RFC1035.'], 'required': False}, 'port': {'description': ['The port number, which can be a value between 1 and 65535.'], 'required': False}}}",
    "network": "{'description': ['The network to which all instances in the instance group belong.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['The region where the instance group is located (for regional resources).'], 'required': False}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnetwork": "{'description': ['The subnetwork to which all instances in the instance group belong.'], 'required': False}",
    "zone": "{'description': ['A reference to the zone where the instance group resides.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a network
  gcp_compute_network:
      name: "network-instancegroup"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a instance group
  gcp_compute_instance_group:
      name: "test_object"
      named_ports:
      - name: ansible
        port: 1234
      network: "{{ network }}"
      zone: us-central1-a
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
