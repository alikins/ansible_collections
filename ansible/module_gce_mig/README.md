# Ansible module: ansible.module_gce_mig


Create, Update or Destroy a Managed Instance Group (MIG)

## Description

Create, Update or Destroy a Managed Instance Group (MIG).  See U(https://cloud.google.com/compute/docs/instance-groups) for an overview. Full install/configuration instructions for the gce* modules can be found in the comments of ansible/test/gce_tests.py.

## Requirements

TODO

## Arguments

``` json
{
    "autoscaling": "{'description': ["A dictionary of configuration for the autoscaler. 'enabled (bool)', 'name (str)' and policy.max_instances (int) are required fields if autoscaling is used. See U(https://cloud.google.com/compute/docs/reference/beta/autoscalers) for more information on Autoscaling."]}",
    "credentials_file": "{'description': ['Path to the JSON file associated with the service account email']}",
    "name": "{'description': ['Name of the Managed Instance Group.'], 'required': True}",
    "named_ports": "{'version_added': '2.3', 'description': ['Define named ports that backend services can forward data to.  Format is a a list of name:port dictionaries.']}",
    "project_id": "{'description': ['GCE project ID']}",
    "service_account_email": "{'description': ['service account email']}",
    "size": "{'description': ['Size of Managed Instance Group.  If MIG already exists, it will be resized to the number provided here.  Required for creating MIGs.']}",
    "state": "{'description': ['desired state of the resource'], 'default': 'present', 'choices': ['absent', 'present']}",
    "template": "{'description': ['Instance Template to be used in creating the VMs.  See U(https://cloud.google.com/compute/docs/instance-templates) to learn more about Instance Templates.  Required for creating MIGs.']}",
    "zone": "{'description': ['The GCE zone to use for this Managed Instance Group.'], 'required': True}",
}
```

## Examples


``` yaml

# Following playbook creates, rebuilds instances, resizes and then deletes a MIG.
# Notes:
# - Two valid Instance Templates must exist in your GCE project in order to run
#   this playbook.  Change the fields to match the templates used in your
#   project.
# - The use of the 'pause' module is not required, it is just for convenience.
- name: Managed Instance Group Example
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create MIG
      gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 1
        template: my-instance-template-1
        named_ports:
        - name: http
          port: 80
        - name: foobar
          port: 82

    - name: Pause for 30 seconds
      pause:
        seconds: 30

    - name: Recreate MIG Instances with Instance Template change.
      gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        template: my-instance-template-2-small
        recreate_instances: yes

    - name: Pause for 30 seconds
      pause:
        seconds: 30

    - name: Resize MIG
      gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 3

    - name: Update MIG with Autoscaler
      gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 3
        template: my-instance-template-2-small
        recreate_instances: yes
        autoscaling:
          enabled: yes
          name: my-autoscaler
          policy:
            min_instances: 2
            max_instances: 5
            cool_down_period: 37
            cpu_utilization:
              target: .39
            load_balancing_utilization:
              target: 0.4

    - name: Pause for 30 seconds
      pause:
        seconds: 30

    - name: Delete MIG
      gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: absent
        autoscaling:
          enabled: no
          name: my-autoscaler

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
