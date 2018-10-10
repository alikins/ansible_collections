# Ansible module: ansible.module_gcp_compute_https_health_check


Creates a GCP HttpsHealthCheck

## Description

An HttpsHealthCheck resource. This resource defines a template for how individual VMs should be checked for health, via HTTPS.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "check_interval_sec": "{'description': ['How often (in seconds) to send a health check. The default value is 5 seconds.'], 'required': False}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "healthy_threshold": "{'description': ['A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.'], 'required': False}",
    "host": "{'description': ['The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.  Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "port": "{'description': ['The TCP port number for the HTTPS health check request.', 'The default value is 80.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "request_path": "{'description': ['The request path of the HTTPS health check request.', 'The default value is /.'], 'required': False}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout_sec": "{'description': ['How long (in seconds) to wait before claiming failure.', 'The default value is 5 seconds.  It is invalid for timeoutSec to have greater value than checkIntervalSec.'], 'required': False, 'aliases': ['timeout_seconds']}",
    "unhealthy_threshold": "{'description': ['A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.'], 'required': False}",
}
```

## Examples


``` yaml

- name: create a https health check
  gcp_compute_https_health_check:
      name: "test_object"
      healthy_threshold: 10
      port: 8080
      timeout_sec: 2
      unhealthy_threshold: 5
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
