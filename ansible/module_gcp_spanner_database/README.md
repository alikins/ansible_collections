# Ansible module: ansible.module_gcp_spanner_database


Creates a GCP Database

## Description

A Cloud Spanner Database which is hosted on a Spanner instance.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "extra_statements": "{'description': ['An optional list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.'], 'required': False}",
    "instance": "{'description': ['The instance to create the database on.'], 'required': True}",
    "name": "{'description': ['A unique identifier for the database, which cannot be changed after the instance is created. Values are of the form projects/<project>/instances/[a-z][-a-z0-9]*[a-z0-9]. The final segment of the name must be between 6 and 30 characters in length.'], 'required': False}",
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
      name: "instance-database"
      display_name: My Spanner Instance
      node_count: 2
      labels:
        cost_center: ti-1700004
      config: regional-us-central1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instance

- name: create a database
  gcp_spanner_database:
      name: webstore
      instance: "{{ instance }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
