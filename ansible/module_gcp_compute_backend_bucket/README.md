# Ansible module: ansible.module_gcp_compute_backend_bucket


Creates a GCP BackendBucket

## Description

Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S) load balancing.
An HTTP(S) load balancer can direct traffic to specified URLs to a backend bucket rather than a backend service. It can send requests for static content to a Cloud Storage bucket and requests for dynamic content a virtual machine instance.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "bucket_name": "{'description': ['Cloud Storage bucket name.'], 'required': True}",
    "description": "{'description': ['An optional textual description of the resource; provided by the client when the resource is created.'], 'required': False}",
    "enable_cdn": "{'description': ['If true, enable Cloud CDN for this BackendBucket.'], 'required': False, 'type': 'bool'}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.  Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a bucket
  gcp_storage_bucket:
      name: "bucket-backendbucket"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: bucket

- name: create a backend bucket
  gcp_compute_backend_bucket:
      name: "test_object"
      bucket_name: "{{ bucket.name }}"
      description: A BackendBucket to connect LNB w/ Storage Bucket
      enable_cdn: true
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
