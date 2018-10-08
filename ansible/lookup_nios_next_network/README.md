# Ansible lookup: ansible.lookup_nios_next_network


Return the next available network range for a network-container

## Description

Uses the Infoblox WAPI API to return the next available network addresses for a given network CIDR

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The CIDR network to retrieve the next network from next available network within the specified container.'], 'required': True}",
    "cidr": "{'description': ['The CIDR of the network to retrieve the next network from next available network within the specified container. Also, Requested CIDR must be specified and greater than the parent CIDR.'], 'required': True, 'default': 24}",
    "exclude": "{'description': ["Network addresses returned from network-container excluding list of user's input network range"], 'required': False, 'default': ''}",
    "num": "{'description': ['The number of network addresses to return from network-container'], 'required': False, 'default': 1}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST', 'Value can also be specified using C(INFOBLOX_HOST) environment variable.'], 'required': True}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_USERNAME) environment variable.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote instance of NIOS.', 'Value can also be specified using C(INFOBLOX_PASSWORD) environment variable.']}, 'ssl_verify': {'description': ['Boolean value to enable or disable verifying SSL certificates', 'Value can also be specified using C(INFOBLOX_SSL_VERIFY) environment variable.'], 'type': 'bool', 'default': 'no'}, 'http_request_timeout': {'description': ['The amount of time before to wait before receiving a response', 'Value can also be specified using C(INFOBLOX_HTTP_REQUEST_TIMEOUT) environment variable.'], 'default': 10}, 'max_retries': {'description': ['Configures the number of attempted retries before the connection is declared usable', 'Value can also be specified using C(INFOBLOX_MAX_RETRIES) environment variable.'], 'default': 3}, 'wapi_version': {'description': ['Specifies the version of WAPI to use', 'Value can also be specified using C(INFOBLOX_WAP_VERSION) environment variable.'], 'default': 1.4}, 'max_results': {'description': ['Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.', 'Value can also be specified using C(INFOBLOX_MAX_RESULTS) environment variable.'], 'default': 1000}}}",
}
```

## Examples


``` yaml

- name: return next available network for network-container 192.168.10.0/24
  set_fact:
    networkaddr: "{{ lookup('nios_next_network', '192.168.10.0/24', cidr=25, provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the next 2 available network addresses for network-container 192.168.10.0/24
  set_fact:
    networkaddr: "{{ lookup('nios_next_network', '192.168.10.0/24', cidr=25, num=2,
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: return the available network addresses for network-container 192.168.10.0/24 excluding network range '192.168.10.0/25'
  set_fact:
    networkaddr: "{{ lookup('nios_next_network', '192.168.10.0/24', cidr=25, exclude=['192.168.10.0/25'],
                        provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
