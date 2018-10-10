# Ansible module: ansible.module_gce


create or terminate GCE instances

## Description

Creates or terminates Google Compute Engine (GCE) instances.  See U(https://cloud.google.com/compute) for an overview. Full install/configuration instructions for the gce* modules can be found in the comments of ansible/test/gce_tests.py.

## Requirements

TODO

## Arguments

``` json
{
    "credentials_file": "{'version_added': '2.1.0', 'description': ['path to the JSON file associated with the service account email']}",
    "disk_auto_delete": "{'version_added': '1.9', 'description': ['if set boot disk will be removed after instance destruction'], 'type': 'bool', 'default': True}",
    "disk_size": "{'description': ['The size of the boot disk created for this instance (in GB)'], 'default': 10, 'version_added': '2.3'}",
    "disks": "{'description': ["a list of persistent disks to attach to the instance; a string value gives the name of the disk; alternatively, a dictionary value can define 'name' and 'mode' ('READ_ONLY' or 'READ_WRITE'). The first entry will be the boot disk (which must be READ_WRITE)."], 'version_added': '1.7'}",
    "external_ip": "{'version_added': '1.9', 'description': ["type of external ip, ephemeral by default; alternatively, a fixed gce ip or ip name can be given. Specify 'none' if no external ip is desired."], 'default': 'ephemeral'}",
    "external_projects": "{'description': ['A list of other projects (accessible with the provisioning credentials) to be searched for the image.'], 'version_added': '2.4'}",
    "image": "{'description': ['image string to use for the instance (default will follow latest stable debian image)'], 'default': 'debian-8'}",
    "image_family": "{'description': ['image family from which to select the image.  The most recent non-deprecated image in the family will be used.'], 'version_added': '2.4'}",
    "instance_names": "{'description': ['a comma-separated list of instance names to create or destroy']}",
    "ip_forward": "{'version_added': '1.9', 'description': ['set to C(yes) if the instance can forward ip packets (useful for gateways)'], 'type': 'bool', 'default': False}",
    "machine_type": "{'description': ["machine type to use for the instance, use 'n1-standard-1' by default"], 'default': 'n1-standard-1'}",
    "metadata": "{'description': ['a hash/dictionary of custom data for the instance; \'{"key":"value", ...}\'']}",
    "name": "{'description': ["either a name of a single instance or when used with 'num_instances', the base name of a cluster of nodes"], 'aliases': ['base_name']}",
    "network": "{'description': ["name of the network, 'default' will be used if not specified"], 'default': 'default'}",
    "num_instances": "{'description': ["can be used with 'name', specifies the number of nodes to provision using 'name' as a base name"], 'version_added': '2.3'}",
    "pem_file": "{'version_added': '1.5.1', 'description': ["path to the pem file associated with the service account email This option is deprecated. Use 'credentials_file'."]}",
    "persistent_boot_disk": "{'description': ['if set, create the instance with a persistent boot disk'], 'type': 'bool', 'default': False}",
    "preemptible": "{'version_added': '2.1', 'description': ['if set to C(yes), instances will be preemptible and time-limited. (requires libcloud >= 0.20.0)'], 'type': 'bool', 'default': False}",
    "project_id": "{'version_added': '1.5.1', 'description': ['your GCE project ID']}",
    "service_account_email": "{'version_added': '1.5.1', 'description': ['service account email']}",
    "service_account_permissions": "{'version_added': '2.0', 'description': ['service account permissions (see U(https://cloud.google.com/sdk/gcloud/reference/compute/instances/create), --scopes section for detailed information)'], 'choices': ['bigquery', 'cloud-platform', 'compute-ro', 'compute-rw', 'useraccounts-ro', 'useraccounts-rw', 'datastore', 'logging-write', 'monitoring', 'sql-admin', 'storage-full', 'storage-ro', 'storage-rw', 'taskqueue', 'userinfo-email']}",
    "state": "{'description': ['desired state of the resource'], 'default': 'present', 'choices': ['active', 'present', 'absent', 'deleted', 'started', 'stopped', 'terminated']}",
    "subnetwork": "{'description': ['name of the subnetwork in which the instance should be created'], 'version_added': '2.2'}",
    "tags": "{'description': ['a comma-separated list of tags to associate with the instance']}",
    "zone": "{'description': ['the GCE zone to use. The list of available zones is at U(https://cloud.google.com/compute/docs/regions-zones/regions-zones#available).'], 'required': True, 'default': 'us-central1-a'}",
}
```

## Examples


``` yaml

# Basic provisioning example.  Create a single Debian 8 instance in the
# us-central1-a Zone of the n1-standard-1 machine type.
# Create multiple instances by specifying multiple names, separated by
# commas in the instance_names field
# (e.g. my-test-instance1,my-test-instance2)
  - gce:
      instance_names: my-test-instance1
      zone: us-central1-a
      machine_type: n1-standard-1
      image: debian-8
      state: present
      service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
      credentials_file: "/path/to/your-key.json"
      project_id: "your-project-name"
      disk_size: 32

# Create a single instance of an image from the "my-base-image" image family
# in the us-central1-a Zone of the n1-standard-1 machine type.
# This image family is in the "my-other-project" GCP project.
  - gce:
      instance_names: my-test-instance1
      zone: us-central1-a
      machine_type: n1-standard-1
      image_family: my-base-image
      external_projects:
        - my-other-project
      state: present
      service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
      credentials_file: "/path/to/your-key.json"
      project_id: "your-project-name"
      disk_size: 32

# Create a single Debian 8 instance in the us-central1-a Zone
# Use existing disks, custom network/subnetwork, set service account permissions
# add tags and metadata.
  - gce:
      instance_names: my-test-instance
      zone: us-central1-a
      machine_type: n1-standard-1
      state: present
      metadata: '{"db":"postgres", "group":"qa", "id":500}'
      tags:
        - http-server
        - my-other-tag
      disks:
        - name: disk-2
          mode: READ_WRITE
        - name: disk-3
          mode: READ_ONLY
      disk_auto_delete: false
      network: foobar-network
      subnetwork: foobar-subnetwork-1
      preemptible: true
      ip_forward: true
      service_account_permissions:
        - storage-full
        - taskqueue
        - bigquery
        - https://www.googleapis.com/auth/ndev.clouddns.readwrite
      service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
      credentials_file: "/path/to/your-key.json"
      project_id: "your-project-name"

---
# Example Playbook
- name: Compute Engine Instance Examples
  hosts: localhost
  vars:
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
    credentials_file: "/path/to/your-key.json"
    project_id: "your-project-name"
  tasks:
    - name: create multiple instances
      # Basic provisioning example.  Create multiple Debian 8 instances in the
      # us-central1-a Zone of n1-standard-1 machine type.
      gce:
        instance_names: test1,test2,test3
        zone: us-central1-a
        machine_type: n1-standard-1
        image: debian-8
        state: present
        service_account_email: "{{ service_account_email }}"
        credentials_file: "{{ credentials_file }}"
        project_id: "{{ project_id }}"
        metadata : '{ "startup-script" : "apt-get update" }'
      register: gce

    - name: Save host data
      add_host:
        hostname: "{{ item.public_ip }}"
        groupname: gce_instances_ips
      with_items: "{{ gce.instance_data }}"

    - name: Wait for SSH for instances
      wait_for:
        delay: 1
        host: "{{ item.public_ip }}"
        port: 22
        state: started
        timeout: 30
      with_items: "{{ gce.instance_data }}"

    - name: Configure Hosts
      hosts: gce_instances_ips
      become: yes
      become_method: sudo
      roles:
        - my-role-one
        - my-role-two
      tags:
        - config

    - name: delete test-instances
      # Basic termination of instance.
      gce:
        service_account_email: "{{ service_account_email }}"
        credentials_file: "{{ credentials_file }}"
        project_id: "{{ project_id }}"
        instance_names: "{{ gce.instance_names }}"
        zone: us-central1-a
        state: absent
      tags:
        - delete

```

## License

TODO

## Author Information
  - ['Eric Johnson (@erjohnso) <erjohnso@google.com>, Tom Melendez (@supertom) <supertom@google.com>']
