# Ansible lookup: ansible.lookup_nios


Query Infoblox NIOS objects

## Description

Uses the Infoblox WAPI API to fetch NIOS specified objects.  This lookup supports adding additional keywords to filter the return data and specify the desired set of returned fields.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The name of the object to return from NIOS'], 'required': True}",
    "extattrs": "{'description': ['a dict object that is used to filter on extattrs']}",
    "filter": "{'description': ['a dict object that is used to filter the return objects']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
    "return_fields": "{'description': ['The list of field names to return for the specified object.']}",
}
```

## Examples


``` yaml

- name: fetch all networkview objects
  set_fact:
    networkviews: "{{ lookup('nios', 'networkview', provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: fetch the default dns view
  set_fact:
    dns_views: "{{ lookup('nios', 'view', filter={'name': 'default'}, provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

# all of the examples below use credentials that are  set using env variables
# export INFOBLOX_HOST=nios01
# export INFOBLOX_USERNAME=admin
# export INFOBLOX_PASSWORD=admin

- name: fetch all host records and include extended attributes
  set_fact:
    host_records: "{{ lookup('nios', 'record:host', return_fields=['extattrs', 'name', 'view', 'comment']}) }}"


- name: use env variables to pass credentials
  set_fact:
    networkviews: "{{ lookup('nios', 'networkview') }}"

- name: get a host record
  set_fact:
    host: "{{ lookup('nios', 'record:host', filter={'name': 'hostname.ansible.com'}) }}"

- name: get the authoritative zone from a non default dns view
  set_fact:
    host: "{{ lookup('nios', 'zone_auth', filter={'fqdn': 'ansible.com', 'view': 'ansible-dns'}) }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
