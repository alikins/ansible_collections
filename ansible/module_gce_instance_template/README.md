# Ansible module: ansible.module_gce_instance_template


create or destroy instance templates of Compute Engine of GCP

## Description

Creates or destroy Google instance templates of Compute Engine of Google Cloud Platform.

## Requirements

TODO

## Arguments

``` json
{
    "automatic_restart": "{'description': ['Defines whether the instance should be automatically restarted when it is terminated by Compute Engine.']}",
    "can_ip_forward": "{'description': ['Set to C(yes) to allow instance to send/receive non-matching src/dst packets.'], 'type': 'bool', 'default': False}",
    "credentials_file": "{'description': ['path to the JSON file associated with the service account email']}",
    "description": "{'description': ['description of instance template']}",
    "disk_auto_delete": "{'description': ['Indicate that the boot disk should be deleted when the Node is deleted.'], 'default': True}",
    "disk_type": "{'description': ['Specify a C(pd-standard) disk or C(pd-ssd) for an SSD disk.'], 'default': 'pd-standard'}",
    "disks": "{'description': ["a list of persistent disks to attach to the instance; a string value gives the name of the disk; alternatively, a dictionary value can define 'name' and 'mode' ('READ_ONLY' or 'READ_WRITE'). The first entry will be the boot disk (which must be READ_WRITE)."]}",
    "disks_gce_struct": "{'description': ['Support passing in the GCE-specific formatted formatted disks[] structure. Case sensitive. see U(https://cloud.google.com/compute/docs/reference/latest/instanceTemplates#resource) for detailed information'], 'version_added': '2.4'}",
    "external_ip": "{'description': ['The external IP address to use. If C(ephemeral), a new non-static address will be used.  If C(None), then no external address will be used.  To use an existing static IP address specify address name.'], 'default': 'ephemeral'}",
    "image": "{'description': ['The image to use to create the instance. Cannot specify both both I(image) and I(source).']}",
    "image_family": "{'description': ['The image family to use to create the instance. If I(image) has been used I(image_family) is ignored. Cannot specify both I(image) and I(source).']}",
    "metadata": "{'description': ['a hash/dictionary of custom data for the instance; \'{"key":"value", ...}\'']}",
    "name": "{'description': ['The name of the GCE instance template.']}",
    "network": "{'description': ['The network to associate with the instance.'], 'default': 'default'}",
    "nic_gce_struct": "{'description': ['Support passing in the GCE-specific formatted networkInterfaces[] structure.']}",
    "pem_file": "{'description': ["path to the pem file associated with the service account email This option is deprecated. Use 'credentials_file'."]}",
    "preemptible": "{'description': ['Defines whether the instance is preemptible.']}",
    "project_id": "{'description': ['your GCE project ID']}",
    "service_account_email": "{'description': ['service account email']}",
    "service_account_permissions": "{'description': ['service account permissions (see U(https://cloud.google.com/sdk/gcloud/reference/compute/instances/create), --scopes section for detailed information)'], 'choices': ['bigquery', 'cloud-platform', 'compute-ro', 'compute-rw', 'useraccounts-ro', 'useraccounts-rw', 'datastore', 'logging-write', 'monitoring', 'sql-admin', 'storage-full', 'storage-ro', 'storage-rw', 'taskqueue', 'userinfo-email']}",
    "size": "{'description': ['The desired machine type for the instance template.'], 'default': 'f1-micro'}",
    "source": "{'description': ['A source disk to attach to the instance. Cannot specify both I(image) and I(source).']}",
    "state": "{'description': ['The desired state for the instance template.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnetwork": "{'description': ['The Subnetwork resource name for this instance.']}",
    "subnetwork_region": "{'version_added': '2.4', 'description': ['Region that subnetwork resides in. (Required for subnetwork to successfully complete)']}",
    "tags": "{'description': ['a comma-separated list of tags to associate with the instance']}",
}
```

## Examples


``` yaml

# Usage
- name: create instance template named foo
  gce_instance_template:
    name: foo
    size: n1-standard-1
    image_family: ubuntu-1604-lts
    state: present
    project_id: "your-project-name"
    credentials_file: "/path/to/your-key.json"
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"

# Example Playbook
- name: Compute Engine Instance Template Examples
  hosts: localhost
  vars:
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
    credentials_file: "/path/to/your-key.json"
    project_id: "your-project-name"
  tasks:
    - name: create instance template
      gce_instance_template:
        name: my-test-instance-template
        size: n1-standard-1
        image_family: ubuntu-1604-lts
        state: present
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"
    - name: delete instance template
      gce_instance_template:
        name: my-test-instance-template
        size: n1-standard-1
        image_family: ubuntu-1604-lts
        state: absent
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"

# Example playbook using disks_gce_struct
- name: Compute Engine Instance Template Examples
  hosts: localhost
  vars:
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
    credentials_file: "/path/to/your-key.json"
    project_id: "your-project-name"
  tasks:
    - name: create instance template
      gce_instance_template:
        name: foo
        size: n1-standard-1
        state: present
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"
        disks_gce_struct:
          - device_name: /dev/sda
            boot: true
            autoDelete: true
            initializeParams:
              diskSizeGb: 30
              diskType: pd-ssd
              sourceImage: projects/debian-cloud/global/images/family/debian-8


```

## License

TODO

## Author Information
  - ['Gwenael Pellen (@GwenaelPellenArkeup) <gwenael.pellen@arkeup.com>']
