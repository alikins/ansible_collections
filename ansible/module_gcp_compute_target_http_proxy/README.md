# Ansible module: ansible.module_gcp_compute_target_http_proxy


Creates a GCP TargetHttpProxy

## Description

Represents a TargetHttpProxy resource, which is used by one or more global forwarding rule to route incoming HTTP requests to a URL map.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "url_map": "{'description': ['A reference to the UrlMap resource that defines the mapping from URL to the BackendService.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a instance group
  gcp_compute_instance_group:
      name: "instancegroup-targethttpproxy"
      zone: us-central1-a
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancegroup

- name: create a http health check
  gcp_compute_http_health_check:
      name: "httphealthcheck-targethttpproxy"
      healthy_threshold: 10
      port: 8080
      timeout_sec: 2
      unhealthy_threshold: 5
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: healthcheck

- name: create a backend service
  gcp_compute_backend_service:
      name: "backendservice-targethttpproxy"
      backends:
      - group: "{{ instancegroup }}"
      health_checks:
      - "{{ healthcheck.selfLink }}"
      enable_cdn: true
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: backendservice

- name: create a url map
  gcp_compute_url_map:
      name: "urlmap-targethttpproxy"
      default_service: "{{ backendservice }}"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: urlmap

- name: create a target http proxy
  gcp_compute_target_http_proxy:
      name: "test_object"
      url_map: "{{ urlmap }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
