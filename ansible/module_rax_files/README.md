# Ansible module: ansible.module_rax_files


Manipulate Rackspace Cloud Files Containers

## Description

Manipulate Rackspace Cloud Files Containers

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "clear_meta": "{'description': ['Optionally clear existing metadata when applying metadata to existing containers. Selecting this option is only appropriate when setting type=meta'], 'type': 'bool', 'default': False}",
    "container": "{'description': ['The container to use for container or metadata operations.'], 'required': True}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "meta": "{'description': ['A hash of items to set as metadata values on a container']}",
    "private": "{'description': ['Used to set a container as private, removing it from the CDN.  B(Warning!) Private containers, if previously made public, can have live objects available until the TTL on cached objects expires']}",
    "public": "{'description': ['Used to set a container as public, available via the Cloud Files CDN']}",
    "region": "{'description': ['Region to create an instance in'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "ttl": "{'description': ['In seconds, set a container-wide TTL for all objects cached on CDN edge nodes. Setting a TTL is only appropriate for containers that are public']}",
    "type": "{'description': ['Type of object to do work on, i.e. metadata object or a container object'], 'choices': ['file', 'meta'], 'default': 'file'}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "web_error": "{'description': ['Sets an object to be presented as the HTTP error page when accessed by the CDN URL']}",
    "web_index": "{'description': ['Sets an object to be presented as the HTTP index page when accessed by the CDN URL']}",
}
```

## Examples


``` yaml

- name: "Test Cloud Files Containers"
  hosts: local
  gather_facts: no
  tasks:
    - name: "List all containers"
      rax_files:
        state: list

    - name: "Create container called 'mycontainer'"
      rax_files:
        container: mycontainer

    - name: "Create container 'mycontainer2' with metadata"
      rax_files:
        container: mycontainer2
        meta:
          key: value
          file_for: someuser@example.com

    - name: "Set a container's web index page"
      rax_files:
        container: mycontainer
        web_index: index.html

    - name: "Set a container's web error page"
      rax_files:
        container: mycontainer
        web_error: error.html

    - name: "Make container public"
      rax_files:
        container: mycontainer
        public: yes

    - name: "Make container public with a 24 hour TTL"
      rax_files:
        container: mycontainer
        public: yes
        ttl: 86400

    - name: "Make container private"
      rax_files:
        container: mycontainer
        private: yes

- name: "Test Cloud Files Containers Metadata Storage"
  hosts: local
  gather_facts: no
  tasks:
    - name: "Get mycontainer2 metadata"
      rax_files:
        container: mycontainer2
        type: meta

    - name: "Set mycontainer2 metadata"
      rax_files:
        container: mycontainer2
        type: meta
        meta:
          uploaded_by: someuser@example.com

    - name: "Remove mycontainer2 metadata"
      rax_files:
        container: "mycontainer2"
        type: meta
        state: absent
        meta:
          key: ""
          file_for: ""

```

## License

TODO

## Author Information
  - ['Paul Durivage (@angstwad)']
