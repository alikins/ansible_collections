# Ansible module: ansible.module_gcp_compute_route_facts


Gather facts for GCP Route

## Description

Gather facts for GCP Route

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "filters": "{'description': ['A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters). Each additional filter in the list will act be added as an AND condition (filter1 and filter2)']}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
}
```

## Examples


``` yaml

- name:  a route facts
  gcp_compute_route_facts:
      filters:
      - name = test_object
      project: test_project
      auth_kind: service_account
      service_account_file: "/tmp/auth.pem"

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
