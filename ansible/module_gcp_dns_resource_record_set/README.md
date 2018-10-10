# Ansible module: ansible.module_gcp_dns_resource_record_set


Creates a GCP ResourceRecordSet

## Description

A single DNS record that exists on a domain name (i.e. in a managed zone).
This record defines the information about the domain and where the domain / subdomains direct to.
The record will include the domain/subdomain name, a type (i.e. A, AAA, CAA, MX, CNAME, NS, etc) .

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "managed_zone": "{'description': ['Identifies the managed zone addressed by this request.', 'Can be the managed zone name or id.'], 'required': True}",
    "name": "{'description': ['For example, U(www.example.com.)'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "target": "{'description': ['As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) .'], 'required': False}",
    "ttl": "{'description': ['Number of seconds that this ResourceRecordSet can be cached by resolvers.'], 'required': False}",
    "type": "{'description': ['One of valid DNS resource types.'], 'required': True, 'choices': ['A', 'AAAA', 'CAA', 'CNAME', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']}",
}
```

## Examples


``` yaml

- name: create a managed zone
  gcp_dns_managed_zone:
      name: "managedzone-rrs"
      dns_name: testzone-4.com.
      description: test zone
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: managed_zone

- name: create a resource record set
  gcp_dns_resource_record_set:
      name: www.testzone-4.com.
      managed_zone: "{{ managed_zone }}"
      type: A
      ttl: 600
      target:
      - 10.1.2.3
      - 40.5.6.7
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
