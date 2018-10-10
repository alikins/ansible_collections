# Ansible module: ansible.module_gce_labels


Create, Update or Destroy GCE Labels

## Description

Create, Update or Destroy GCE Labels on instances, disks, snapshots, etc. When specifying the GCE resource, users may specifiy the full URL for the resource (its 'self_link'), or the individual parameters of the resource (type, location, name). Examples for the two options can be seen in the documentaion. See U(https://cloud.google.com/compute/docs/label-or-tag-resources) for more information about GCE Labels. Labels are gradually being added to more GCE resources, so this module will need to be updated as new resources are added to the GCE (v1) API.

## Requirements

TODO

## Arguments

``` json
{
    "labels": "{'description': ['A list of labels (key/value pairs) to add or remove for the resource.'], 'required': False}",
    "resource_location": "{'description': ['The location of resource (global, us-central1-f, etc.)'], 'required': False}",
    "resource_name": "{'description': ['The name of resource.'], 'required': False}",
    "resource_type": "{'description': ['The type of resource (instances, disks, snapshots, images)'], 'required': False}",
    "resource_url": "{'description': ["The 'self_link' for the resource (instance, disk, snapshot, etc)"], 'required': False}",
}
```

## Examples


``` yaml

- name: Add labels on an existing instance (using resource_url)
  gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      webserver-frontend: homepage
      environment: test
      experiment-name: kennedy
    resource_url: https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-f/instances/example-instance
    state: present
- name: Add labels on an image (using resource params)
  gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      webserver-frontend: homepage
      environment: test
      experiment-name: kennedy
    resource_type: images
    resource_location: global
    resource_name: my-custom-image
    state: present
- name: Remove specified labels from the GCE instance
  gce_labels:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    labels:
      environment: prod
      experiment-name: kennedy
    resource_url: https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-f/instances/example-instance
    state: absent

```

## License

TODO

## Author Information
  - ['Eric Johnson (@erjohnso) <erjohnso@google.com>']
