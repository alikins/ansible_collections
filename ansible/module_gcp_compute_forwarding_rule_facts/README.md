# Ansible module: ansible.module_gcp_compute_forwarding_rule_facts


Gather facts for GCP ForwardingRule

## Description

Gather facts for GCP ForwardingRule

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "filters": "{'description': ['A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters). Each additional filter in the list will act be added as an AND condition (filter1 and filter2)']}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['A reference to the region where the regional forwarding rule resides.', 'This field is not applicable to global forwarding rules.'], 'required': True}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
}
```

## Examples


``` yaml

- name:  a forwarding rule facts
  gcp_compute_forwarding_rule_facts:
      region: us-west1
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
