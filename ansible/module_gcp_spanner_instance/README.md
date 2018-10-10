# Ansible module: ansible.module_gcp_spanner_instance


Creates a GCP Instance

## Description

An isolated set of Cloud Spanner resources on which databases can be hosted.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "config": "{'description': ['A reference to the instance configuration.'], 'required': False}",
    "display_name": "{'description': ['The descriptive name for this instance as it appears in UIs. Must be unique per project and between 4 and 30 characters in length.'], 'required': True}",
    "labels": "{'description': ["Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.).", 'Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.', 'Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.', 'No more than 64 labels can be associated with a given resource.', 'See U(https://goo.gl/xmQnxf) for more information on and examples of labels.', 'If you plan to use labels in your own code, please note that additional characters may be allowed in the future. And so you are advised to use an internal label representation, such as JSON, which doesn\'t rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release.', 'An object containing a list of "key": value pairs.', 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'], 'required': False}",
    "name": "{'description': ['A unique identifier for the instance, which cannot be changed after the instance is created. Values are of the form projects/<project>/instances/[a-z][-a-z0-9]*[a-z0-9]. The final segment of the name must be between 6 and 30 characters in length.'], 'required': False}",
    "node_count": "{'description': ['The number of nodes allocated to this instance.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a instance
  gcp_spanner_instance:
      name: "test_object"
      display_name: My Spanner Instance
      node_count: 2
      labels:
        cost_center: ti-1700004
      config: regional-us-central1
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
