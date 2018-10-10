# Ansible module: ansible.module_rax_files_objects


Upload, download, and delete objects in Rackspace Cloud Files

## Description

Upload, download, and delete objects in Rackspace Cloud Files

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "clear_meta": "{'description': ['Optionally clear existing metadata when applying metadata to existing objects. Selecting this option is only appropriate when setting type=meta'], 'type': 'bool', 'default': False}",
    "container": "{'description': ['The container to use for file object operations.'], 'required': True}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "dest": "{'description': ['The destination of a "get" operation; i.e. a local directory, "/home/user/myfolder". Used to specify the destination of an operation on a remote object; i.e. a file name, "file1", or a comma-separated list of remote objects, "file1,file2,file17"']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "expires": "{'description': ['Used to set an expiration on a file or folder uploaded to Cloud Files. Requires an integer, specifying expiration in seconds']}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "meta": "{'description': ['A hash of items to set as metadata values on an uploaded file or folder']}",
    "method": "{'description': ['The method of operation to be performed.  For example, put to upload files to Cloud Files, get to download files from Cloud Files or delete to delete remote objects in Cloud Files'], 'choices': ['get', 'put', 'delete'], 'default': 'get'}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "src": "{'description': ['Source from which to upload files.  Used to specify a remote object as a source for an operation, i.e. a file name, "file1", or a comma-separated list of remote objects, "file1,file2,file17".  src and dest are mutually exclusive on remote-only object operations']}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "structure": "{'description': ['Used to specify whether to maintain nested directory structure when downloading objects from Cloud Files.  Setting to false downloads the contents of a container to a single, flat directory'], 'type': 'bool', 'default': True}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "type": "{'description': ['Type of object to do work on', 'Metadata object or a file object'], 'choices': ['file', 'meta'], 'default': 'file'}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: "Test Cloud Files Objects"
  hosts: local
  gather_facts: False
  tasks:
    - name: "Get objects from test container"
      rax_files_objects:
        container: testcont
        dest: ~/Downloads/testcont

    - name: "Get single object from test container"
      rax_files_objects:
        container: testcont
        src: file1
        dest: ~/Downloads/testcont

    - name: "Get several objects from test container"
      rax_files_objects:
        container: testcont
        src: file1,file2,file3
        dest: ~/Downloads/testcont

    - name: "Delete one object in test container"
      rax_files_objects:
        container: testcont
        method: delete
        dest: file1

    - name: "Delete several objects in test container"
      rax_files_objects:
        container: testcont
        method: delete
        dest: file2,file3,file4

    - name: "Delete all objects in test container"
      rax_files_objects:
        container: testcont
        method: delete

    - name: "Upload all files to test container"
      rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/onehundred

    - name: "Upload one file to test container"
      rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/testcont/file1

    - name: "Upload one file to test container with metadata"
      rax_files_objects:
        container: testcont
        src: ~/Downloads/testcont/file2
        method: put
        meta:
          testkey: testdata
          who_uploaded_this: someuser@example.com

    - name: "Upload one file to test container with TTL of 60 seconds"
      rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/testcont/file3
        expires: 60

    - name: "Attempt to get remote object that does not exist"
      rax_files_objects:
        container: testcont
        method: get
        src: FileThatDoesNotExist.jpg
        dest: ~/Downloads/testcont
      ignore_errors: yes

    - name: "Attempt to delete remote object that does not exist"
      rax_files_objects:
        container: testcont
        method: delete
        dest: FileThatDoesNotExist.jpg
      ignore_errors: yes

- name: "Test Cloud Files Objects Metadata"
  hosts: local
  gather_facts: false
  tasks:
    - name: "Get metadata on one object"
      rax_files_objects:
        container: testcont
        type: meta
        dest: file2

    - name: "Get metadata on several objects"
      rax_files_objects:
        container: testcont
        type: meta
        src: file2,file1

    - name: "Set metadata on an object"
      rax_files_objects:
        container: testcont
        type: meta
        dest: file17
        method: put
        meta:
          key1: value1
          key2: value2
        clear_meta: true

    - name: "Verify metadata is set"
      rax_files_objects:
        container: testcont
        type: meta
        src: file17

    - name: "Delete metadata"
      rax_files_objects:
        container: testcont
        type: meta
        dest: file17
        method: delete
        meta:
          key1: ''
          key2: ''

    - name: "Get metadata on all objects"
      rax_files_objects:
        container: testcont
        type: meta

```

## License

TODO

## Author Information
  - ['Paul Durivage (@angstwad)']
