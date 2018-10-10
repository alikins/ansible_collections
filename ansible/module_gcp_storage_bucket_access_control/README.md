# Ansible module: ansible.module_gcp_storage_bucket_access_control


Creates a GCP BucketAccessControl

## Description

The BucketAccessControls resource represents the Access Control Lists (ACLs) for buckets within Google Cloud Storage. ACLs let you specify who has access to your data and to what extent.
There are three roles that can be assigned to an entity:  READERs can get the bucket, though no acl property will be returned, and list the bucket's objects.  WRITERs are READERs, and they can insert objects into the bucket and delete the bucket's objects.  OWNERs are WRITERs, and they can get the acl property of a bucket, update a bucket, and call all BucketAccessControls methods on the bucket.  For more information, see Access Control, with the caveat that this API uses READER, WRITER, and OWNER instead of READ, WRITE, and FULL_CONTROL.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "bucket": "{'description': ['The name of the bucket.'], 'required': True}",
    "entity": "{'description': ['The entity holding the permission, in one of the following forms: user-userId user-email group-groupId group-email domain-domain project-team-projectId allUsers allAuthenticatedUsers Examples: The user liz@example.com would be user-liz@example.com.', 'The group example@googlegroups.com would be   group-example@googlegroups.com.', 'To refer to all members of the Google Apps for Business domain   example.com, the entity would be domain-example.com.'], 'required': True}",
    "entity_id": "{'description': ['The ID for the entity.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "project_team": "{'description': ['The project team associated with the entity.'], 'required': False, 'suboptions': {'project_number': {'description': ['The project team associated with the entity.'], 'required': False}, 'team': {'description': ['The team.'], 'required': False, 'choices': ['editors', 'owners', 'viewers']}}}",
    "role": "{'description': ['The access permission for the entity.'], 'required': False, 'choices': ['OWNER', 'READER', 'WRITER']}",
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
      name: "bucket-bac"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: bucket

- name: create a bucket access control
  gcp_storage_bucket_access_control:
      bucket: "{{ bucket }}"
      entity: user-alexstephen@google.com
      role: WRITER
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
