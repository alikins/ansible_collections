# Ansible module: ansible.module_gcp_backend_service


Create or Destroy a Backend Service

## Description

Create or Destroy a Backend Service.  See U(https://cloud.google.com/compute/docs/load-balancing/http/backend-service) for an overview. Full install/configuration instructions for the Google Cloud modules can be found in the comments of ansible/test/gce_tests.py.

## Requirements

TODO

## Arguments

``` json
{
    "backend_service_name": "{'description': ['Name of the Backend Service.'], 'required': True}",
    "backends": "{'description': ['List of backends that make up the backend service. A backend is made up of an instance group and optionally several other parameters.  See U(https://cloud.google.com/compute/docs/reference/latest/backendServices) for details.'], 'required': True}",
    "credentials_file": "{'description': ['Path to the JSON file associated with the service account email.']}",
    "enable_cdn": "{'description': ['If true, enable Cloud CDN for this Backend Service.']}",
    "healthchecks": "{'description': ['List of healthchecks. Only one healthcheck is supported.'], 'required': True}",
    "port_name": "{'description': ['Name of the port on the managed instance group (MIG) that backend services can forward data to. Required for external load balancing.']}",
    "project_id": "{'description': ['GCE project ID.']}",
    "protocol": "{'description': ['The protocol this Backend Service uses to communicate with backends. Possible values are HTTP, HTTPS, TCP, and SSL. The default is HTTP.'], 'required': False}",
    "service_account_email": "{'description': ['Service account email']}",
    "state": "{'description': ['Desired state of the resource'], 'default': 'present', 'choices': ['absent', 'present']}",
    "timeout": "{'description': ['How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is 1-86400.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create Minimum Backend Service
  gcp_backend_service:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    backend_service_name: "{{ bes }}"
    backends:
    - instance_group: managed_instance_group_1
    healthchecks:
    - healthcheck_name_for_backend_service
    port_name: myhttpport
    state: present

- name: Create BES with extended backend parameters
  gcp_backend_service:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    backend_service_name: "{{ bes }}"
    backends:
    - instance_group: managed_instance_group_1
      max_utilization: 0.6
      max_rate: 10
    - instance_group: managed_instance_group_2
      max_utilization: 0.5
      max_rate: 4
    healthchecks:
    - healthcheck_name_for_backend_service
    port_name: myhttpport
    state: present
    timeout: 60

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
