# Ansible module: ansible.module_gcp_sql_database


Creates a GCP Database

## Description

Represents a SQL database inside the Cloud SQL instance, hosted in Google's cloud.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "charset": "{'description': ['The MySQL charset value.'], 'required': False}",
    "collation": "{'description': ['The MySQL collation value.'], 'required': False}",
    "instance": "{'description': ['The name of the Cloud SQL instance. This does not include the project ID.'], 'required': True}",
    "name": "{'description': ['The name of the database in the Cloud SQL instance.', 'This does not include the project ID or instance name.'], 'required': False}",
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
  gcp_sql_instance:
      name: "instance-database"
      settings:
        ip_configuration:
          authorized_networks:
          - name: google dns server
            value: 8.8.8.8/32
        tier: db-n1-standard-1
      region: us-central1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instance

- name: create a database
  gcp_sql_database:
      name: "test_object"
      charset: utf8
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
