# Ansible module: ansible.module_gc_storage


This module manages objects/buckets in Google Cloud Storage

## Description

This module allows users to manage their objects/buckets in Google Cloud Storage.  It allows upload and download operations and can set some canned permissions. It also allows retrieval of URLs for objects for use in playbooks, and retrieval of string contents of objects.  This module requires setting the default project in GCS prior to playbook usage.  See U(https://developers.google.com/storage/docs/reference/v1/apiversion1) for information about setting the default project.

## Requirements

TODO

## Arguments

``` json
{
    "bucket": "{'description': ['Bucket name.'], 'required': True}",
    "dest": "{'description': ['The destination file path when downloading an object/key with a GET operation.']}",
    "expiration": "{'description': ['Time limit (in seconds) for the URL generated and returned by GCA when performing a mode=put or mode=get_url operation. This url is only available when public-read is the acl for the object.']}",
    "force": "{'description': ['Forces an overwrite either locally on the filesystem or remotely with the object/key. Used with PUT and GET operations.'], 'type': 'bool', 'default': True, 'aliases': ['overwrite']}",
    "gs_access_key": "{'description': ['GS access key. If not set then the value of the GS_ACCESS_KEY_ID environment variable is used.'], 'required': True}",
    "gs_secret_key": "{'description': ['GS secret key. If not set then the value of the GS_SECRET_ACCESS_KEY environment variable is used.'], 'required': True}",
    "headers": "{'version_added': '2.0', 'description': ['Headers to attach to object.'], 'default': {}}",
    "mode": "{'description': ['Switches the module behaviour between upload, download, get_url (return download url) , get_str (download object as string), create (bucket) and delete (bucket).'], 'required': True, 'choices': ['get', 'put', 'get_url', 'get_str', 'delete', 'create']}",
    "object": "{'description': ['Keyname of the object inside the bucket. Can be also be used to create "virtual directories" (see examples).']}",
    "permission": "{'description': ["This option let's the user set the canned permissions on the object/bucket that are created. The permissions that can be set are 'private', 'public-read', 'authenticated-read'."], 'default': 'private'}",
    "region": "{'version_added': '2.4', 'description': ["The gs region to use. If not defined then the value 'US' will be used. See U(https://cloud.google.com/storage/docs/bucket-locations)"], 'default': 'US'}",
    "src": "{'description': ['The source file path when performing a PUT operation.']}",
    "versioning": "{'version_added': '2.4', 'description': ['Whether versioning is enabled or disabled (note that once versioning is enabled, it can only be suspended)'], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Upload some content
  gc_storage:
    bucket: mybucket
    object: key.txt
    src: /usr/local/myfile.txt
    mode: put
    permission: public-read

- name: Upload some headers
  gc_storage:
    bucket: mybucket
    object: key.txt
    src: /usr/local/myfile.txt
    headers: '{"Content-Encoding": "gzip"}'

- name: Download some content
  gc_storage:
    bucket: mybucket
    object: key.txt
    dest: /usr/local/myfile.txt
    mode: get

- name: Download an object as a string to use else where in your playbook
  gc_storage:
    bucket: mybucket
    object: key.txt
    mode: get_str

- name: Create an empty bucket
  gc_storage:
    bucket: mybucket
    mode: create

- name: Create a bucket with key as directory
  gc_storage:
    bucket: mybucket
    object: /my/directory/path
    mode: create

- name: Delete a bucket and all contents
  gc_storage:
    bucket: mybucket
    mode: delete

- name: Create a bucket with versioning enabled
  gc_storage:
    bucket: "mybucket"
    versioning: yes
    mode: create

- name: Create a bucket located in the eu
  gc_storage:
    bucket: "mybucket"
    region: "europe-west3"
    mode: create


```

## License

TODO

## Author Information
  - ['Benno Joy (@bennojoy)', 'Lukas Beumer (@nitaco)']
  - ['Benno Joy (@bennojoy)', 'Lukas Beumer (@nitaco)']
