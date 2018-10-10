# Ansible module: ansible.module_gce_snapshot


Create or destroy snapshots for GCE storage volumes

## Description

Manages snapshots for GCE instances. This module manages snapshots for the storage volumes of a GCE compute instance. If there are multiple volumes, each snapshot will be prepended with the disk name

## Requirements

TODO

## Arguments

``` json
{
    "credentials_file": "{'description': ['The path to the credentials file associated with the service account'], 'required': True}",
    "disks": "{'description': ['A list of disks to create snapshots for. If none is provided, all of the volumes will be snapshotted'], 'default': 'all', 'required': False}",
    "instance_name": "{'description': ['The GCE instance to snapshot'], 'required': True}",
    "project_id": "{'description': ['The GCP project ID to use'], 'required': True}",
    "service_account_email": "{'description': ['GCP service account email for the project where the instance resides'], 'required': True}",
    "snapshot_name": "{'description': ['The name of the snapshot to manage']}",
    "state": "{'description': ['Whether a snapshot should be C(present) or C(absent)'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Create gce snapshot
  gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: present
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost

- name: Delete gce snapshot
  gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: absent
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost

# This example creates snapshots for only two of the available disks as
# disk0-example-snapshot and disk1-example-snapshot
- name: Create snapshots of specific disks
  gce_snapshot:
    instance_name: example-instance
    snapshot_name: example-snapshot
    state: present
    disks:
      - disk0
      - disk1
    service_account_email: project_name@appspot.gserviceaccount.com
    credentials_file: /path/to/credentials
    project_id: project_name
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Rob Wagner (@robwagner33)']
