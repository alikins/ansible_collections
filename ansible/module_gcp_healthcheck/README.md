# Ansible module: ansible.module_gcp_healthcheck


Create, Update or Destroy a Healthcheck

## Description

Create, Update or Destroy a Healthcheck. Currently only HTTP and HTTPS Healthchecks are supported. Healthchecks are used to monitor individual instances, managed instance groups and/or backend services. Healtchecks are reusable.
Visit U(https://cloud.google.com/compute/docs/load-balancing/health-checks) for an overview of Healthchecks on GCP.
See U(https://cloud.google.com/compute/docs/reference/latest/httpHealthChecks) for API details on HTTP Healthchecks.
See U(https://cloud.google.com/compute/docs/reference/latest/httpsHealthChecks) for more details on the HTTPS Healtcheck API.

## Requirements

TODO

## Arguments

``` json
{
    "check_interval": "{'description': ['How often (in seconds) to send a health check.'], 'default': 5}",
    "credentials_file": "{'description': ['Path to the JSON file associated with the service account email']}",
    "healthcheck_name": "{'description': ['Name of the Healthcheck.'], 'required': True}",
    "healthcheck_type": "{'description': ['Type of Healthcheck.'], 'required': True, 'choices': ['HTTP', 'HTTPS']}",
    "healthy_threshold": "{'description': ['A so-far unhealthy instance will be marked healthy after this many consecutive successes.'], 'default': 2}",
    "host_header": "{'description': ['The value of the host header in the health check request. If left empty, the public IP on behalf of which this health check is performed will be used.'], 'required': True, 'default': ''}",
    "port": "{'description': ['The TCP port number for the health check request. The default value is 443 for HTTPS and 80 for HTTP.']}",
    "project_id": "{'description': ['Your GCP project ID']}",
    "request_path": "{'description': ['The request path of the HTTPS health check request.'], 'required': False, 'default': '/'}",
    "service_account_email": "{'description': ['service account email']}",
    "service_account_permissions": "{'version_added': '2.0', 'description': ['service account permissions (see U(https://cloud.google.com/sdk/gcloud/reference/compute/instances/create), --scopes section for detailed information)'], 'choices': ['bigquery', 'cloud-platform', 'compute-ro', 'compute-rw', 'useraccounts-ro', 'useraccounts-rw', 'datastore', 'logging-write', 'monitoring', 'sql-admin', 'storage-full', 'storage-ro', 'storage-rw', 'taskqueue', 'userinfo-email']}",
    "state": "{'description': ['State of the Healthcheck.'], 'required': True, 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['How long (in seconds) to wait for a response before claiming failure. It is invalid for timeout to have a greater value than check_interval.'], 'default': 5}",
    "unhealthy_threshold": "{'description': ['A so-far healthy instance will be marked unhealthy after this many consecutive failures.'], 'default': 2}",
}
```

## Examples


``` yaml

- name: Create Minimum HealthCheck
  gcp_healthcheck:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    healthcheck_name: my-healthcheck
    healthcheck_type: HTTP
    state: present
- name: Create HTTP HealthCheck
  gcp_healthcheck:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    healthcheck_name: my-healthcheck
    healthcheck_type: HTTP
    host: my-host
    request_path: /hc
    check_interval: 10
    timeout: 30
    unhealthy_threshhold: 2
    healthy_threshhold: 1
    state: present
- name: Create HTTPS HealthCheck
  gcp_healthcheck:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    healthcheck_name: "{{ https_healthcheck }}"
    healthcheck_type: HTTPS
    host_header: my-host
    request_path: /hc
    check_interval: 5
    timeout: 5
    unhealthy_threshold: 2
    healthy_threshold: 1
    state: present

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
