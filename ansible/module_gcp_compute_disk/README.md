# Ansible module: ansible.module_gcp_compute_disk


Creates a GCP Disk

## Description

Persistent disks are durable storage devices that function similarly to the physical disks in a desktop or a server. Compute Engine manages the hardware behind these devices to ensure data redundancy and optimize performance for you. Persistent disks are available as either standard hard disk drives (HDD) or solid-state drives (SSD).
Persistent disks are located independently from your virtual machine instances, so you can detach or move persistent disks to keep your data even after you delete your instances. Persistent disk performance scales automatically with size, so you can resize your existing persistent disks or add more persistent disks to an instance to meet your performance and storage space requirements.
Add a persistent disk to your instance when you need reliable and affordable storage with consistent performance characteristics.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "disk_encryption_key": "{'description': ['Encrypts the disk using a customer-supplied encryption key.', 'After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk snapshot or an image, or to attach the disk to a virtual machine).', 'Customer-supplied encryption keys do not protect access to metadata of the disk.', 'If you do not provide an encryption key when creating the disk, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}",
    "labels": "{'description': ['Labels to apply to this disk.  A list of key->value pairs.'], 'required': False, 'version_added': 2.7}",
    "licenses": "{'description': ['Any applicable publicly visible licenses.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "size_gb": "{'description': ['Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.', 'If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot.'], 'required': False}",
    "source_image": "{'description': ['The source image used to create this disk. If the source image is deleted, this field will not be set.', 'To create a disk with one of the public operating system images, specify the image by its family name. For example, specify family/debian-8 to use the latest Debian 8 image:  projects/debian-cloud/global/images/family/debian-8  Alternatively, use a specific version of a public operating system image:  projects/debian-cloud/global/images/debian-8-jessie-vYYYYMMDD  To create a disk with a private image that you created, specify the image name in the following format:  global/images/my-private-image  You can also specify a private image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name:  global/images/family/my-private-family .'], 'required': False}",
    "source_image_encryption_key": "{'description': ['The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}",
    "source_snapshot": "{'description': ['The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: * `U(https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot`) * `projects/project/global/snapshots/snapshot` * `global/snapshots/snapshot` .'], 'required': False}",
    "source_snapshot_encryption_key": "{'description': ['The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk.'], 'required': False, 'version_added': 2.7}",
    "zone": "{'description': ['A reference to the zone where the disk resides.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a disk
  gcp_compute_disk:
      name: "test_object"
      size_gb: 50
      disk_encryption_key:
        raw_key: SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=
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
