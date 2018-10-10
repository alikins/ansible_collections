# Ansible module: ansible.module_gcdns_record


Creates or removes resource records in Google Cloud DNS

## Description

Creates or removes resource records in Google Cloud DNS.

## Requirements

TODO

## Arguments

``` json
{
    "credentials_file": "{'description': ['The path to the JSON file associated with the service account email.']}",
    "overwrite": "{'description': ['Whether an attempt to overwrite an existing record should succeed or fail. The behavior of this option depends on I(state).', 'If I(state) is C(present) and I(overwrite) is C(True), this module will replace an existing resource record of the same name with the provided I(record_data). If I(state) is C(present) and I(overwrite) is C(False), this module will fail if there is an existing resource record with the same name and type, but different resource data.', "If I(state) is C(absent) and I(overwrite) is C(True), this module will remove the given resource record unconditionally. If I(state) is C(absent) and I(overwrite) is C(False), this module will fail if the provided record_data do not match exactly with the existing resource record's record_data."], 'type': 'bool', 'default': False}",
    "pem_file": "{'description': ['The path to the PEM file associated with the service account email.', 'This option is deprecated and may be removed in a future release. Use I(credentials_file) instead.']}",
    "project_id": "{'description': ['The Google Cloud Platform project ID to use.']}",
    "record": "{'description': ['The fully-qualified domain name of the resource record.'], 'required': True, 'aliases': ['name']}",
    "record_data": "{'description': ['The record_data to use for the resource record.', 'I(record_data) must be specified if I(state) is C(present) or I(overwrite) is C(True), or the module will fail.', "Valid record_data vary based on the record's I(type). In addition, resource records that contain a DNS domain name in the value field (e.g., CNAME, PTR, SRV, .etc) MUST include a trailing dot in the value.", 'Individual string record_data for TXT records must be enclosed in double quotes.', 'For resource records that have the same name but different record_data (e.g., multiple A records), they must be defined as multiple list entries in a single record.'], 'required': False, 'aliases': ['value']}",
    "service_account_email": "{'description': ['The e-mail address for a service account with access to Google Cloud DNS.']}",
    "state": "{'description': ['Whether the given resource record should or should not be present.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "ttl": "{'description': ['The amount of time in seconds that a resource record will remain cached by a caching resolver.'], 'default': 300}",
    "type": "{'description': ['The type of resource record to add.'], 'required': True, 'choices': ['A', 'AAAA', 'CNAME', 'SRV', 'TXT', 'SOA', 'NS', 'MX', 'SPF', 'PTR']}",
    "zone": "{'description': ['The DNS domain name of the zone (e.g., example.com).', 'One of either I(zone) or I(zone_id) must be specified as an option, or the module will fail.', 'If both I(zone) and I(zone_id) are specified, I(zone_id) will be used.']}",
    "zone_id": "{'description': ['The Google Cloud ID of the zone (e.g., example-com).', 'One of either I(zone) or I(zone_id) must be specified as an option, or the module will fail.', 'These usually take the form of domain names with the dots replaced with dashes. A zone ID will never have any dots in it.', 'I(zone_id) can be faster than I(zone) in projects with a large number of zones.', 'If both I(zone) and I(zone_id) are specified, I(zone_id) will be used.']}",
}
```

## Examples


``` yaml

# Create an A record.
- gcdns_record:
    record: 'www1.example.com'
    zone: 'example.com'
    type: A
    value: '1.2.3.4'

# Update an existing record.
- gcdns_record:
    record: 'www1.example.com'
    zone: 'example.com'
    type: A
    overwrite: true
    value: '5.6.7.8'

# Remove an A record.
- gcdns_record:
    record: 'www1.example.com'
    zone_id: 'example-com'
    state: absent
    type: A
    value: '5.6.7.8'

# Create a CNAME record.
- gcdns_record:
    record: 'www.example.com'
    zone_id: 'example-com'
    type: CNAME
    value: 'www.example.com.'    # Note the trailing dot

# Create an MX record with a custom TTL.
- gcdns_record:
    record: 'example.com'
    zone: 'example.com'
    type: MX
    ttl: 3600
    value: '10 mail.example.com.'    # Note the trailing dot

# Create multiple A records with the same name.
- gcdns_record:
    record: 'api.example.com'
    zone_id: 'example-com'
    type: A
    record_data:
      - '192.0.2.23'
      - '10.4.5.6'
      - '198.51.100.5'
      - '203.0.113.10'

# Change the value of an existing record with multiple record_data.
- gcdns_record:
    record: 'api.example.com'
    zone: 'example.com'
    type: A
    overwrite: true
    record_data:           # WARNING: All values in a record will be replaced
      - '192.0.2.23'
      - '192.0.2.42'    # The changed record
      - '198.51.100.5'
      - '203.0.113.10'

# Safely remove a multi-line record.
- gcdns_record:
    record: 'api.example.com'
    zone_id: 'example-com'
    state: absent
    type: A
    record_data:           # NOTE: All of the values must match exactly
      - '192.0.2.23'
      - '192.0.2.42'
      - '198.51.100.5'
      - '203.0.113.10'

# Unconditionally remove a record.
- gcdns_record:
    record: 'api.example.com'
    zone_id: 'example-com'
    state: absent
    overwrite: true   # overwrite is true, so no values are needed
    type: A

# Create an AAAA record
- gcdns_record:
    record: 'www1.example.com'
    zone: 'example.com'
    type: AAAA
    value: 'fd00:db8::1'

# Create a PTR record
- gcdns_record:
    record: '10.5.168.192.in-addr.arpa'
    zone: '5.168.192.in-addr.arpa'
    type: PTR
    value: 'api.example.com.'    # Note the trailing dot.

# Create an NS record
- gcdns_record:
    record: 'subdomain.example.com'
    zone: 'example.com'
    type: NS
    ttl: 21600
    record_data:
      - 'ns-cloud-d1.googledomains.com.'    # Note the trailing dots on values
      - 'ns-cloud-d2.googledomains.com.'
      - 'ns-cloud-d3.googledomains.com.'
      - 'ns-cloud-d4.googledomains.com.'

# Create a TXT record
- gcdns_record:
    record: 'example.com'
    zone_id: 'example-com'
    type: TXT
    record_data:
      - '"v=spf1 include:_spf.google.com -all"'   # A single-string TXT value
      - '"hello " "world"'    # A multi-string TXT value

```

## License

TODO

## Author Information
  - ['William Albert (@walbert947)']
