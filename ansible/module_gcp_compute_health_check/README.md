# Ansible module: ansible.module_gcp_compute_health_check


Creates a GCP HealthCheck

## Description

An HealthCheck resource. This resource defines a template for how individual virtual machines should be checked for health, via one of the supported protocols.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "check_interval_sec": "{'description': ['How often (in seconds) to send a health check. The default value is 5 seconds.'], 'required': False, 'default': 5}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "healthy_threshold": "{'description': ['A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.'], 'required': False}",
    "http_health_check": "{'description': ['A nested object resource.'], 'required': False, 'suboptions': {'host': {'description': ['The value of the host header in the HTTP health check request.', 'If left empty (default value), the public IP on behalf of which this health check is performed will be used.'], 'required': False}, 'request_path': {'description': ['The request path of the HTTP health check request.', 'The default value is /.'], 'required': False}, 'port': {'description': ['The TCP port number for the HTTP health check request.', 'The default value is 80.'], 'required': False}, 'port_name': {'description': ['Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.'], 'required': False}, 'proxy_header': {'description': ['Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.'], 'required': False, 'choices': ['NONE', 'PROXY_V1']}}}",
    "https_health_check": "{'description': ['A nested object resource.'], 'required': False, 'suboptions': {'host': {'description': ['The value of the host header in the HTTPS health check request.', 'If left empty (default value), the public IP on behalf of which this health check is performed will be used.'], 'required': False}, 'request_path': {'description': ['The request path of the HTTPS health check request.', 'The default value is /.'], 'required': False}, 'port': {'description': ['The TCP port number for the HTTPS health check request.', 'The default value is 443.'], 'required': False}, 'port_name': {'description': ['Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.'], 'required': False}, 'proxy_header': {'description': ['Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.'], 'required': False, 'choices': ['NONE', 'PROXY_V1']}}}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.  Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "ssl_health_check": "{'description': ['A nested object resource.'], 'required': False, 'suboptions': {'request': {'description': ['The application data to send once the SSL connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII.'], 'required': False}, 'response': {'description': ['The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.'], 'required': False}, 'port': {'description': ['The TCP port number for the SSL health check request.', 'The default value is 443.'], 'required': False}, 'port_name': {'description': ['Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.'], 'required': False}, 'proxy_header': {'description': ['Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.'], 'required': False, 'choices': ['NONE', 'PROXY_V1']}}}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tcp_health_check": "{'description': ['A nested object resource.'], 'required': False, 'suboptions': {'request': {'description': ['The application data to send once the TCP connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII.'], 'required': False}, 'response': {'description': ['The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII.'], 'required': False}, 'port': {'description': ['The TCP port number for the TCP health check request.', 'The default value is 443.'], 'required': False}, 'port_name': {'description': ['Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.'], 'required': False}, 'proxy_header': {'description': ['Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.'], 'required': False, 'choices': ['NONE', 'PROXY_V1']}}}",
    "timeout_sec": "{'description': ['How long (in seconds) to wait before claiming failure.', 'The default value is 5 seconds.  It is invalid for timeoutSec to have greater value than checkIntervalSec.'], 'required': False, 'default': 5, 'aliases': ['timeout_seconds']}",
    "type": "{'description': ['Specifies the type of the healthCheck, either TCP, SSL, HTTP or HTTPS. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.'], 'required': False, 'choices': ['TCP', 'SSL', 'HTTP']}",
    "unhealthy_threshold": "{'description': ['A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.'], 'required': False, 'default': 2}",
}
```

## Examples


``` yaml

- name: create a health check
  gcp_compute_health_check:
      name: "test_object"
      type: TCP
      tcp_health_check:
        port_name: service-health
        request: ping
        response: pong
      healthy_threshold: 10
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
