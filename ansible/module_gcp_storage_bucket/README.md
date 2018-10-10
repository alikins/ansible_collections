# Ansible module: ansible.module_gcp_storage_bucket


Creates a GCP Bucket

## Description

The Buckets resource represents a bucket in Google Cloud Storage. There is a single global namespace shared by all buckets. For more information, see Bucket Name Requirements.
Buckets contain objects which can be accessed by their own methods. In addition to the acl property, buckets contain bucketAccessControls, for use in fine-grained manipulation of an existing bucket's access controls.
A bucket is always owned by the project team owners group.

## Requirements

TODO

## Arguments

``` json
{
    "acl": "{'description': ['Access controls on the bucket.'], 'required': False, 'suboptions': {'bucket': {'description': ['The name of the bucket.'], 'required': True}, 'domain': {'description': ['The domain associated with the entity.'], 'required': False}, 'email': {'description': ['The email address associated with the entity.'], 'required': False}, 'entity': {'description': ['The entity holding the permission, in one of the following forms: user-userId user-email group-groupId group-email domain-domain project-team-projectId allUsers allAuthenticatedUsers Examples: The user liz@example.com would be user-liz@example.com.', 'The group example@googlegroups.com would be   group-example@googlegroups.com.', 'To refer to all members of the Google Apps for Business domain   example.com, the entity would be domain-example.com.'], 'required': True}, 'entity_id': {'description': ['The ID for the entity.'], 'required': False}, 'id': {'description': ['The ID of the access-control entry.'], 'required': False}, 'project_team': {'description': ['The project team associated with the entity.'], 'required': False, 'suboptions': {'project_number': {'description': ['The project team associated with the entity.'], 'required': False}, 'team': {'description': ['The team.'], 'required': False, 'choices': ['editors', 'owners', 'viewers']}}}, 'role': {'description': ['The access permission for the entity.'], 'required': False, 'choices': ['OWNER', 'READER', 'WRITER']}}}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "cors": "{'description': ["The bucket's Cross-Origin Resource Sharing (CORS) configuration."], 'required': False, 'suboptions': {'max_age_seconds': {'description': ['The value, in seconds, to return in the Access-Control-Max-Age header used in preflight responses.'], 'required': False}, 'method': {'description': ['The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".'], 'required': False}, 'origin': {'description': ['The list of Origins eligible to receive CORS response headers.', 'Note: "*" is permitted in the list of origins, and means "any Origin".'], 'required': False}, 'response_header': {'description': ['The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains.'], 'required': False}}}",
    "default_object_acl": "{'description': ['Default access controls to apply to new objects when no ACL is provided.'], 'required': False, 'version_added': 2.7, 'suboptions': {'bucket': {'description': ['The name of the bucket.'], 'required': True}, 'domain': {'description': ['The domain associated with the entity.'], 'required': False}, 'email': {'description': ['The email address associated with the entity.'], 'required': False}, 'entity': {'description': ['The entity holding the permission, in one of the following forms: user-userId user-email group-groupId group-email domain-domain project-team-projectId allUsers allAuthenticatedUsers Examples: The user liz@example.com would be user-liz@example.com.', 'The group example@googlegroups.com would be   group-example@googlegroups.com.', 'To refer to all members of the Google Apps for Business domain   example.com, the entity would be domain-example.com.'], 'required': True}, 'entity_id': {'description': ['The ID for the entity.'], 'required': False}, 'generation': {'description': ['The content generation of the object, if applied to an object.'], 'required': False}, 'id': {'description': ['The ID of the access-control entry.'], 'required': False}, 'object': {'description': ['The name of the object, if applied to an object.'], 'required': False}, 'project_team': {'description': ['The project team associated with the entity.'], 'required': False, 'suboptions': {'project_number': {'description': ['The project team associated with the entity.'], 'required': False}, 'team': {'description': ['The team.'], 'required': False, 'choices': ['editors', 'owners', 'viewers']}}}, 'role': {'description': ['The access permission for the entity.'], 'required': False, 'choices': ['OWNER', 'READER']}}}",
    "lifecycle": "{'description': ["The bucket's lifecycle configuration.", 'See U(https://developers.google.com/storage/docs/lifecycle) for more information.'], 'required': False, 'suboptions': {'rule': {'description': ['A lifecycle management rule, which is made of an action to take and the condition(s) under which the action will be taken.'], 'required': False, 'suboptions': {'action': {'description': ['The action to take.'], 'required': False, 'suboptions': {'storage_class': {'description': ['Target storage class. Required iff the type of the action is SetStorageClass.'], 'required': False}, 'type': {'description': ['Type of the action. Currently, only Delete and SetStorageClass are supported.'], 'required': False, 'choices': ['Delete', 'SetStorageClass']}}}, 'condition': {'description': ['The condition(s) under which the action will be taken.'], 'required': False, 'suboptions': {'age_days': {'description': ['Age of an object (in days). This condition is satisfied when an object reaches the specified age.'], 'required': False}, 'created_before': {'description': ['A date in RFC 3339 format with only the date part (for instance, "2013-01-15"). This condition is satisfied when an object is created before midnight of the specified date in UTC.'], 'required': False}, 'is_live': {'description': ['Relevant only for versioned objects.  If the value is true, this condition matches live objects; if the value is false, it matches archived objects.'], 'required': False, 'type': 'bool'}, 'matches_storage_class': {'description': ['Objects having any of the storage classes specified by this condition will be matched. Values include MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, STANDARD, and DURABLE_REDUCED_AVAILABILITY.'], 'required': False}, 'num_newer_versions': {'description': ['Relevant only for versioned objects. If the value is N, this condition is satisfied when there are at least N versions (including the live version) newer than this version of the object.'], 'required': False}}}}}}}",
    "location": "{'description': ["The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the developer's guide for the authoritative list."], 'required': False}",
    "logging": "{'description': ["The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's logs."], 'required': False, 'suboptions': {'log_bucket': {'description': ["The destination bucket where the current bucket's logs should be placed."], 'required': False}, 'log_object_prefix': {'description': ['A prefix for log object names.'], 'required': False}}}",
    "metageneration": "{'description': ['The metadata generation of this bucket.'], 'required': False}",
    "name": "{'description': ['The name of the bucket.'], 'required': False}",
    "owner": "{'description': ["The owner of the bucket. This is always the project team's owner group."], 'required': False, 'suboptions': {'entity': {'description': ['The entity, in the form project-owner-projectId.'], 'required': False}, 'entity_id': {'description': ['The ID for the entity.'], 'required': False}}}",
    "predefined_default_object_acl": "{'description': ['Apply a predefined set of default object access controls to this bucket.', 'Acceptable values are:   - "authenticatedRead": Object owner gets OWNER access, and     allAuthenticatedUsers get READER access.', '- "bucketOwnerFullControl": Object owner gets OWNER access, and     project team owners get OWNER access.', '- "bucketOwnerRead": Object owner gets OWNER access, and project     team owners get READER access.', '- "private": Object owner gets OWNER access.', '- "projectPrivate": Object owner gets OWNER access, and project team     members get access according to their roles.', '- "publicRead": Object owner gets OWNER access, and allUsers get     READER access.'], 'required': False, 'choices': ['authenticatedRead', 'bucketOwnerFullControl', 'bucketOwnerRead', 'private', 'projectPrivate', 'publicRead']}",
    "project": "{'description': ['A valid API project identifier.'], 'default': None, 'required': False}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage_class": "{'description': ["The bucket's default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage.", 'Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see storage classes.'], 'required': False, 'choices': ['MULTI_REGIONAL', 'REGIONAL', 'STANDARD', 'NEARLINE', 'COLDLINE', 'DURABLE_REDUCED_AVAILABILITY']}",
    "versioning": "{'description': ["The bucket's versioning configuration."], 'required': False, 'suboptions': {'enabled': {'description': ['While set to true, versioning is fully enabled for this bucket.'], 'required': False, 'type': 'bool'}}}",
    "website": "{'description': ["The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the Static Website Examples for more information."], 'required': False, 'suboptions': {'main_page_suffix': {'description': ["If the requested object path is missing, the service will ensure the path has a trailing '/', append this suffix, and attempt to retrieve the resulting object. This allows the creation of index.html objects to represent directory pages."], 'required': False}, 'not_found_page': {'description': ['If the requested object path is missing, and any mainPageSuffix object is missing, if applicable, the service will return the named object from this bucket as the content for a 404 Not Found result.'], 'required': False}}}",
}
```

## Examples


``` yaml

- name: create a bucket
  gcp_storage_bucket:
      name: ansible-storage-module
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
