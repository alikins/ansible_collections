# Ansible module: ansible.module_gcp_compute_url_map


Creates a GCP UrlMap

## Description

UrlMaps are used to route requests to a backend service based on rules that you define for the host and path of an incoming URL.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "default_service": "{'description': ['A reference to BackendService resource if none of the hostRules match.'], 'required': True}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "host_rules": "{'description': ['The list of HostRules to use against the URL.'], 'required': False, 'suboptions': {'description': {'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}, 'hosts': {'description': ['The list of host patterns to match. They must be valid hostnames, except * will match any string of ([a-z0-9-.]*). In that case, * must be the first character and must be followed in the pattern by either - or .'], 'required': False}, 'path_matcher': {'description': ["The name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion."], 'required': False}}}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': False}",
    "path_matchers": "{'description': ['The list of named PathMatchers to use against the URL.'], 'required': False, 'suboptions': {'default_service': {'description': ["A reference to a BackendService resource. This will be used if none of the pathRules defined by this PathMatcher is matched by the URL's path portion."], 'required': False}, 'description': {'description': ['An optional description of this resource.'], 'required': False}, 'name': {'description': ['The name to which this PathMatcher is referred by the HostRule.'], 'required': False}, 'path_rules': {'description': ['The list of path rules.'], 'required': False, 'suboptions': {'paths': {'description': ['The list of path patterns to match. Each must start with / and the only place a * is allowed is at the end following a /. The string fed to the path matcher does not include any text after the first ? or #, and those chars are not allowed here.'], 'required': False}, 'service': {'description': ['A reference to the BackendService resource if this rule is matched.'], 'required': False}}}}}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tests": "{'description': ['The list of expected URL mappings. Request to update this UrlMap will succeed only if all of the test cases pass.'], 'required': False, 'suboptions': {'description': {'description': ['Description of this test case.'], 'required': False}, 'host': {'description': ['Host portion of the URL.'], 'required': False}, 'path': {'description': ['Path portion of the URL.'], 'required': False}, 'service': {'description': ['A reference to expected BackendService resource the given URL should be mapped to.'], 'required': False}}}",
}
```

## Examples


``` yaml

- name: create a instance group
  gcp_compute_instance_group:
      name: "instancegroup-urlmap"
      zone: us-central1-a
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancegroup

- name: create a http health check
  gcp_compute_http_health_check:
      name: "httphealthcheck-urlmap"
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
      name: "backendservice-urlmap"
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
      name: "test_object"
      default_service: "{{ backendservice }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
