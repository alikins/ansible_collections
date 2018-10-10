# Ansible module: ansible.module_gcdns_zone


Creates or removes zones in Google Cloud DNS

## Description

Creates or removes managed zones in Google Cloud DNS.

## Requirements

TODO

## Arguments

``` json
{
    "credentials_file": "{'description': ['The path to the JSON file associated with the service account email.']}",
    "description": "{'description': ['An arbitrary text string to use for the zone description.'], 'default': ''}",
    "pem_file": "{'description': ['The path to the PEM file associated with the service account email.', 'This option is deprecated and may be removed in a future release. Use I(credentials_file) instead.']}",
    "project_id": "{'description': ['The Google Cloud Platform project ID to use.']}",
    "service_account_email": "{'description': ['The e-mail address for a service account with access to Google Cloud DNS.']}",
    "state": "{'description': ['Whether the given zone should or should not be present.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "zone": "{'description': ['The DNS domain name of the zone.', 'This is NOT the Google Cloud DNS zone ID (e.g., example-com). If you attempt to specify a zone ID, this module will attempt to create a TLD and will fail.'], 'required': True, 'aliases': ['name']}",
}
```

## Examples


``` yaml

# Basic zone creation example.
- name: Create a basic zone with the minimum number of parameters.
  gcdns_zone: zone=example.com

# Zone removal example.
- name: Remove a zone.
  gcdns_zone: zone=example.com state=absent

# Zone creation with description
- name: Creating a zone with a description
  gcdns_zone: zone=example.com description="This is an awesome zone"

```

## License

TODO

## Author Information
  - ['William Albert (@walbert947)']
