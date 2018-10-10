# Ansible module: ansible.module_gcp_compute_image


Creates a GCP Image

## Description

Represents an Image resource.
Google Compute Engine uses operating system images to create the root persistent disks for your instances. You specify an image when you create an instance. Images contain a boot loader, an operating system, and a root file system. Linux operating system images are also capable of running containers on Compute Engine.
Images can be either public or custom.
Public images are provided and maintained by Google, open-source communities, and third-party vendors. By default, all projects have access to these images and can use them to create instances.  Custom images are available only to your project. You can create a custom image from root persistent disks and other images. Then, use the custom image to create an instance.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "disk_size_gb": "{'description': ['Size of the image when restored onto a persistent disk (in GB).'], 'required': False}",
    "family": "{'description': ['The name of the image family to which this image belongs. You can create disks by specifying an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with RFC1035.'], 'required': False}",
    "guest_os_features": "{'description': ['A list of features to enable on the guest OS. Applicable for bootable images only. Currently, only one feature can be enabled, VIRTIO_SCSI_MULTIQUEUE, which allows each virtual CPU to have its own queue. For Windows images, you can only enable VIRTIO_SCSI_MULTIQUEUE on images with driver version 1.2.0.1621 or higher. Linux images with kernel versions 3.17 and higher will support VIRTIO_SCSI_MULTIQUEUE.', 'For new Windows images, the server might also populate this field with the value WINDOWS, to indicate that this is a Windows image.', 'This value is purely informational and does not enable or disable any features.'], 'required': False, 'suboptions': {'type': {'description': ['The type of supported feature. Currenty only VIRTIO_SCSI_MULTIQUEUE is supported. For newer Windows images, the server might also populate this property with the value WINDOWS to indicate that this is a Windows image. This value is purely informational and does not enable or disable any features.'], 'required': False, 'choices': ['VIRTIO_SCSI_MULTIQUEUE']}}}",
    "image_encryption_key": "{'description': ['Encrypts the image using a customer-supplied encryption key.', 'After you encrypt an image with a customer-supplied key, you must provide the same key if you use the image later (e.g. to create a disk from the image) .'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}",
    "licenses": "{'description': ['Any applicable license URI.'], 'required': False}",
    "name": "{'description': ['Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "raw_disk": "{'description': ['The parameters of the raw disk image.'], 'required': False, 'suboptions': {'container_type': {'description': ['The format used to encode and transmit the block device, which should be TAR. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created.'], 'required': False, 'choices': ['TAR']}, 'sha1_checksum': {'description': ['An optional SHA1 checksum of the disk image before unpackaging.', 'This is provided by the client when the disk image is created.'], 'required': False}, 'source': {'description': ['The full Google Cloud Storage URL where disk storage is stored You must provide either this property or the sourceDisk property but not both.'], 'required': False}}}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "source_disk": "{'description': ['Refers to a gcompute_disk object You must provide either this property or the rawDisk.source property but not both to create an image.'], 'required': False}",
    "source_disk_encryption_key": "{'description': ['The customer-supplied encryption key of the source disk. Required if the source disk is protected by a customer-supplied encryption key.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}",
    "source_disk_id": "{'description': ['The ID value of the disk used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given disk name.'], 'required': False}",
    "source_type": "{'description': ['The type of the image used to create this disk. The default and only value is RAW .'], 'required': False, 'choices': ['RAW']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a disk
  gcp_compute_disk:
      name: "disk-image"
      zone: us-central1-a
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: disk

- name: create a image
  gcp_compute_image:
      name: "test_object"
      source_disk: "{{ disk }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
