# Ansible module: ansible.module_gce_tag


add or remove tag(s) to/from GCE instances

## Description

This module can add or remove tags U(https://cloud.google.com/compute/docs/label-or-tag-resources#tags) to/from GCE instances.  Use 'instance_pattern' to update multiple instances in a specify zone.

## Requirements

TODO

## Arguments

``` json
{
    "instance_name": "{'description': ['The name of the GCE instance to add/remove tags.', 'Required if C(instance_pattern) is not specified.']}",
    "instance_pattern": "{'description': ['The pattern of GCE instance names to match for adding/removing tags.  Full-Python regex is supported. See U(https://docs.python.org/2/library/re.html) for details.', 'If C(instance_name) is not specified, this field is required.'], 'version_added': '2.3'}",
    "pem_file": "{'description': ['Path to the PEM file associated with the service account email.']}",
    "project_id": "{'description': ['Your GCE project ID.']}",
    "service_account_email": "{'description': ['Service account email.']}",
    "state": "{'description': ['Desired state of the tags.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "tags": "{'description': ['Comma-separated list of tags to add or remove.'], 'required': True}",
    "zone": "{'description': ['The zone of the disk specified by source.'], 'default': 'us-central1-a'}",
}
```

## Examples


``` yaml

- name: Add tags to instance
  gce_tag:
    instance_name: staging-server
    tags: http-server,https-server,staging
    zone: us-central1-a
    state: present

- name: Remove tags from instance in default zone (us-central1-a)
  gce_tag:
    instance_name: test-server
    tags: foo,bar
    state: absent

- name: Add tags to instances in zone that match pattern
  gce_tag:
    instance_pattern: test-server-*
    tags: foo,bar
    zone: us-central1-a
    state: present

```

## License

TODO

## Author Information
  - ['Do Hoang Khiem (dohoangkhiem@gmail.com)', 'Tom Melendez (@supertom)']
  - ['Do Hoang Khiem (dohoangkhiem@gmail.com)', 'Tom Melendez (@supertom)']
