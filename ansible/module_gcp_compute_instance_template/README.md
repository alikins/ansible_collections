# Ansible module: ansible.module_gcp_compute_instance_template


Creates a GCP InstanceTemplate

## Description

Defines an Instance Template resource that provides configuration settings for your virtual machine instances. Instance templates are not tied to the lifetime of an instance and can be used and reused as to deploy virtual machines. You can also use different templates to create different virtual machine configurations. Instance templates are required when you create a managed instance group.
Tip: Disks should be set to autoDelete=true so that leftover disks are not left behind on machine deletion.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. The name is 1-63 characters long and complies with RFC1035.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "properties": "{'description': ['The instance properties for this instance template.'], 'required': False, 'suboptions': {'can_ip_forward': {'description': ['Enables instances created based on this template to send packets with source IP addresses other than their own and receive packets with destination IP addresses other than their own. If these instances will be used as an IP gateway or it will be set as the next-hop in a Route resource, specify true. If unsure, leave this set to false.'], 'required': False, 'type': 'bool'}, 'description': {'description': ['An optional text description for the instances that are created from this instance template.'], 'required': False}, 'disks': {'description': ['An array of disks that are associated with the instances that are created from this template.'], 'required': False, 'suboptions': {'auto_delete': {'description': ['Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).', 'Tip: Disks should be set to autoDelete=true so that leftover disks are not left behind on machine deletion.'], 'required': False, 'type': 'bool'}, 'boot': {'description': ['Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.'], 'required': False, 'type': 'bool'}, 'device_name': {'description': ['Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-* tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.'], 'required': False}, 'disk_encryption_key': {'description': ['Encrypts or decrypts a disk using a customer-supplied encryption key.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'rsa_encrypted_key': {'description': ['Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied encryption key to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}, 'index': {'description': ['Assigns a zero-based index to this disk, where 0 is reserved for the boot disk. For example, if you have many disks attached to an instance, each disk would have a unique index number. If not specified, the server will choose an appropriate value.'], 'required': False}, 'initialize_params': {'description': ['Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.'], 'required': False, 'suboptions': {'disk_name': {'description': ['Specifies the disk name. If not specified, the default is to use the name of the instance.'], 'required': False}, 'disk_size_gb': {'description': ['Specifies the size of the disk in base-2 GB.'], 'required': False}, 'disk_type': {'description': ['Reference to a gcompute_disk_type resource.', 'Specifies the disk type to use to create the instance.', 'If not specified, the default is pd-standard.'], 'required': False}, 'source_image': {'description': ['The source image to create this disk. When creating a new instance, one of initializeParams.sourceImage or disks.source is required.  To create a disk with one of the public operating system images, specify the image by its family name.'], 'required': False}, 'source_image_encryption_key': {'description': ['The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.', 'Instance templates do not store customer-supplied encryption keys, so you cannot create disks for instances in a managed instance group if the source images are encrypted with your own keys.'], 'required': False, 'suboptions': {'raw_key': {'description': ['Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.'], 'required': False}, 'sha256': {'description': ['The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key that protects this resource.'], 'required': False}}}}}, 'interface': {'description': ['Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI.', 'Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI.'], 'required': False, 'choices': ['SCSI', 'NVME']}, 'mode': {'description': ['The mode in which to attach this disk, either READ_WRITE or READ_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode.'], 'required': False, 'choices': ['READ_WRITE', 'READ_ONLY']}, 'source': {'description': ['Reference to a gcompute_disk resource. When creating a new instance, one of initializeParams.sourceImage or disks.source is required.', 'If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.', 'Note that for InstanceTemplate, specify the disk name, not the URL for the disk.'], 'required': False}, 'type': {'description': ['Specifies the type of the disk, either SCRATCH or PERSISTENT. If not specified, the default is PERSISTENT.'], 'required': False, 'choices': ['SCRATCH', 'PERSISTENT']}}}, 'machine_type': {'description': ['Reference to a gcompute_machine_type resource.'], 'required': True}, 'metadata': {'description': ['The metadata key/value pairs to assign to instances that are created from this template. These pairs can consist of custom metadata or predefined keys.'], 'required': False}, 'guest_accelerators': {'description': ['List of the type and count of accelerator cards attached to the instance .'], 'required': False, 'suboptions': {'accelerator_count': {'description': ['The number of the guest accelerator cards exposed to this instance.'], 'required': False}, 'accelerator_type': {'description': ['Full or partial URL of the accelerator type resource to expose to this instance.'], 'required': False}}}, 'network_interfaces': {'description': ['An array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Only one network interface is supported per instance.'], 'required': False, 'suboptions': {'access_configs': {'description': ['An array of configurations for this interface. Currently, only one access config, ONE_TO_ONE_NAT, is supported. If there are no accessConfigs specified, then this instance will have no external internet access.'], 'required': False, 'suboptions': {'name': {'description': ['The name of this access configuration. The default and recommended name is External NAT but you can use any arbitrary string you would like. For example, My external IP or Network Access.'], 'required': True}, 'nat_ip': {'description': ['Specifies the title of a gcompute_address.', 'An external IP address associated with this instance.', 'Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance.'], 'required': False}, 'type': {'description': ['The type of configuration. The default and only option is ONE_TO_ONE_NAT.'], 'required': True, 'choices': ['ONE_TO_ONE_NAT']}}}, 'alias_ip_ranges': {'description': ['An array of alias IP ranges for this network interface. Can only be specified for network interfaces on subnet-mode networks.'], 'required': False, 'suboptions': {'ip_cidr_range': {'description': ['The IP CIDR range represented by this alias IP range.', 'This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (e.g. 10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g. 10.1.2.0/24).'], 'required': False}, 'subnetwork_range_name': {'description': ['Optional subnetwork secondary range name specifying the secondary range from which to allocate the IP CIDR range for this alias IP range. If left unspecified, the primary range of the subnetwork will be used.'], 'required': False}}}, 'name': {'description': ['The name of the network interface, generated by the server. For network devices, these are eth0, eth1, etc .'], 'required': False}, 'network': {'description': ['Specifies the title of an existing gcompute_network.  When creating an instance, if neither the network nor the subnetwork is specified, the default network global/networks/default is used; if the network is not specified but the subnetwork is specified, the network is inferred.'], 'required': False}, 'network_ip': {'description': ['An IPv4 internal network address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system.'], 'required': False}, 'subnetwork': {'description': ['Reference to a gcompute_subnetwork resource.', 'If the network resource is in legacy mode, do not provide this property.  If the network is in auto subnet mode, providing the subnetwork is optional. If the network is in custom subnet mode, then this field should be specified.'], 'required': False}}}, 'scheduling': {'description': ['Sets the scheduling options for this instance.'], 'required': False, 'suboptions': {'automatic_restart': {'description': ['Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).', 'You can only set the automatic restart option for standard instances. Preemptible instances cannot be automatically restarted.'], 'required': False, 'type': 'bool'}, 'on_host_maintenance': {'description': ['Defines the maintenance behavior for this instance. For standard instances, the default behavior is MIGRATE. For preemptible instances, the default and only possible behavior is TERMINATE.', 'For more information, see Setting Instance Scheduling Options.'], 'required': False}, 'preemptible': {'description': ['Defines whether the instance is preemptible. This can only be set during instance creation, it cannot be set or changed after the instance has been created.'], 'required': False, 'type': 'bool'}}}, 'service_accounts': {'description': ['A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.'], 'required': False, 'suboptions': {'email': {'description': ['Email address of the service account.'], 'required': False}, 'scopes': {'description': ['The list of scopes to be made available for this service account.'], 'required': False}}}, 'tags': {'description': ['A list of tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply with RFC1035.'], 'required': False, 'suboptions': {'fingerprint': {'description': ["Specifies a fingerprint for this request, which is essentially a hash of the metadata's contents and used for optimistic locking.", 'The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata.'], 'required': False}, 'items': {'description': ['An array of tags. Each tag must be 1-63 characters long, and comply with RFC1035.'], 'required': False}}}}}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
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
      name: "test_object"
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
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
