# Ansible module: ansible.module_gce_img


utilize GCE image resources

## Description

This module can create and delete GCE private images from gzipped compressed tarball containing raw disk data or from existing detached disks in any zone. U(https://cloud.google.com/compute/docs/images)

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['an optional description']}",
    "family": "{'description': ['an optional family name'], 'version_added': '2.2'}",
    "name": "{'description': ['the name of the image to create or delete'], 'required': True}",
    "pem_file": "{'description': ['path to the pem file associated with the service account email']}",
    "project_id": "{'description': ['your GCE project ID']}",
    "service_account_email": "{'description': ['service account email']}",
    "source": "{'description': ['the source disk or the Google Cloud Storage URI to create the image from']}",
    "state": "{'description': ['desired state of the image'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['timeout for the operation'], 'default': 180, 'version_added': '2.0'}",
    "zone": "{'description': ['the zone of the disk specified by source'], 'default': 'us-central1-a'}",
}
```

## Examples


``` yaml

# Create an image named test-image from the disk 'test-disk' in zone us-central1-a.
- gce_img:
    name: test-image
    source: test-disk
    zone: us-central1-a
    state: present

# Create an image named test-image from a tarball in Google Cloud Storage.
- gce_img:
    name: test-image
    source: https://storage.googleapis.com/bucket/path/to/image.tgz

# Alternatively use the gs scheme
- gce_img:
    name: test-image
    source: gs://bucket/path/to/image.tgz

# Delete an image named test-image.
- gce_img:
    name: test-image
    state: absent

```

## License

TODO

## Author Information
  - ['Tom Melendez (supertom)']
