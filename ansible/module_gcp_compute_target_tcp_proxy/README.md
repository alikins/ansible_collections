# Ansible module: ansible.module_gcp_compute_target_tcp_proxy


Creates a GCP TargetTcpProxy

## Description

Represents a TargetTcpProxy resource, which is used by one or more global forwarding rule to route incoming TCP requests to a Backend service.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "proxy_header": "{'description': ['Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.'], 'required': False, 'choices': ['NONE', 'PROXY_V1']}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service": "{'description': ['A reference to the BackendService resource.'], 'required': True}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a instance group
  gcp_compute_instance_group:
      name: "instancegroup-targettcpproxy"
      zone: us-central1-a
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancegroup

- name: create a health check
  gcp_compute_health_check:
      name: "healthcheck-targettcpproxy"
      type: TCP
      tcp_health_check:
        port_name: service-health
        request: ping
        response: pong
      healthy_threshold: 10
      timeout_sec: 2
      unhealthy_threshold: 5
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: healthcheck

- name: create a backend service
  gcp_compute_backend_service:
      name: "backendservice-targettcpproxy"
      backends:
      - group: "{{ instancegroup }}"
      health_checks:
      - "{{ healthcheck.selfLink }}"
      protocol: TCP
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: backendservice

- name: create a target tcp proxy
  gcp_compute_target_tcp_proxy:
      name: "test_object"
      proxy_header: PROXY_V1
      service: "{{ backendservice }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
