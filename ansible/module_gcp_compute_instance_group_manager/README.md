# Ansible module: ansible.module_gcp_compute_instance_group_manager


Creates a GCP InstanceGroupManager

## Description

Creates a managed instance group using the information that you specify in the request. After the group is created, it schedules an action to create instances in the group using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances.
A managed instance group can have up to 1000 VM instances per group.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "base_instance_name": "{'description': ['The base instance name to use for instances in this group. The value must be 1-58 characters long. Instances are named by appending a hyphen and a random four-character string to the base instance name.', 'The base instance name must comply with RFC1035.'], 'required': True}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "instance_template": "{'description': ['The instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group.'], 'required': True}",
    "name": "{'description': ['The name of the managed instance group. The name must be 1-63 characters long, and comply with RFC1035.'], 'required': True}",
    "named_ports": "{'description': ['Named ports configured for the Instance Groups complementary to this Instance Group Manager.'], 'required': False, 'suboptions': {'name': {'description': ['The name for this named port. The name must be 1-63 characters long, and comply with RFC1035.'], 'required': False}, 'port': {'description': ['The port number, which can be a value between 1 and 65535.'], 'required': False}}}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "target_pools": "{'description': ['TargetPool resources to which instances in the instanceGroup field are added. The target pools automatically apply to all of the instances in the managed instance group.'], 'required': False}",
    "target_size": "{'description': ['The target number of running instances for this managed instance group. Deleting or abandoning instances reduces this number. Resizing the group changes this number.'], 'required': False}",
    "zone": "{'description': ['The zone the managed instance group resides.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a network
  gcp_compute_network:
      name: "network-instancetemplate"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a address
  gcp_compute_address:
      name: "address-instancetemplate"
      region: us-west1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: address

- name: create a instance template
  gcp_compute_instance_template:
      name: "{{ resource_name }}"
      properties:
        disks:
        - auto_delete: true
          boot: true
          initialize_params:
            source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts
        machine_type: n1-standard-1
        network_interfaces:
        - network: "{{ network }}"
          access_configs:
          - name: test-config
            type: ONE_TO_ONE_NAT
            nat_ip: "{{ address }}"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancetemplate

- name: create a instance group manager
  gcp_compute_instance_group_manager:
      name: "test_object"
      base_instance_name: test1-child
      instance_template: "{{ instancetemplate }}"
      target_size: 3
      zone: us-west1-a
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
