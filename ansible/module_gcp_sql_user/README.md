# Ansible module: ansible.module_gcp_sql_user


Creates a GCP User

## Description

The Users resource represents a database user in a Cloud SQL instance.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "host": "{'description': ['The host name from which the user can connect. For insert operations, host defaults to an empty string. For update operations, host is specified as part of the request URL. The host name cannot be updated after insertion.'], 'required': True}",
    "instance": "{'description': ['The name of the Cloud SQL instance. This does not include the project ID.'], 'required': True}",
    "name": "{'description': ['The name of the user in the Cloud SQL instance.'], 'required': True}",
    "password": "{'description': ['The password for the user.'], 'required': False}",
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
      name: "instance-user"
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

- name: create a user
  gcp_sql_user:
      name: test-user
      host: 10.1.2.3
      password: secret-password
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
