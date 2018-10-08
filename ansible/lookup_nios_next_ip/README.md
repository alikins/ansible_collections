# Ansible lookup: ansible.lookup_nios_next_ip


Return the next available IP address for a network

## Description

Uses the Infoblox WAPI API to return the next available IP addresses for a given network CIDR

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The CIDR network to retrieve the next addresses from'], 'required': True}",
    "exclude": "{'version_added': '2.7', 'description': ["List of IP's that need to be excluded from returned IP addresses"], 'required': False}",
    "num": "{'description': ['The number of IP addresses to return'], 'required': False, 'default': 1}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
}
```

## Examples


``` yaml

- name: return next available IP address for network 192.168.10.0/24
  set_fact:
    ipaddr: "{{ lookup('nios_next_ip', '192.168.10.0/24', provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the next 3 available IP addresses for network 192.168.10.0/24
  set_fact:
    ipaddr: "{{ lookup('nios_next_ip', '192.168.10.0/24', num=3, provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the next 3 available IP addresses for network 192.168.10.0/24 excluding ip addresses - ['192.168.10.1', '192.168.10.2']
  set_fact:
    ipaddr: "{{ lookup('nios_next_ip', '192.168.10.0/24', num=3, exclude=['192.168.10.1', '192.168.10.2'],
                provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
