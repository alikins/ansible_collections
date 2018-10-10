# Ansible module: ansible.module_bigip_firewall_address_list


Manage address lists on BIG-IP AFM

## Description

Manages the AFM address lists on a BIG-IP. This module can be used to add and remove address list entries.

## Requirements

TODO

## Arguments

``` json
{
    "address_lists": "{'description': ['Simple list of existing address lists to add to this list. Address lists can be specified in either their fully qualified name (/Common/foo) or their short name (foo). If a short name is used, the C(partition) argument will automatically be prepended to the short name.']}",
    "address_ranges": "{'description': ['A list of address ranges where the range starts with a port number, is followed by a dash (-) and then a second number.', 'If the first address is greater than the second number, the numbers will be reversed so-as to be properly formatted. ie, C(2.2.2.2-1.1.1). would become C(1.1.1.1-2.2.2.2).']}",
    "addresses": "{'description': ['Individual addresses that you want to add to the list. These addresses differ from ranges, and lists of lists such as what can be used in C(address_ranges) and C(address_lists) respectively.', 'This list can also include networks that have CIDR notation.']}",
    "description": "{'description': ['Description of the address list']}",
    "fqdns": "{'description': ['A list of fully qualified domain names (FQDNs).', 'An FQDN has at least one decimal point in it, separating the host from the domain.', 'To add FQDNs to a list requires that a global FQDN resolver be configured. At the moment, this must either be done via C(bigip_command), or, in the GUI of BIG-IP. If using C(bigip_command), this can be done with C(tmsh modify security firewall global-fqdn-policy FOO) where C(FOO) is a DNS resolver configured at C(tmsh create net dns-resolver FOO).']}",
    "geo_locations": "{'description': ['List of geolocations specified by their C(country) and C(region).'], 'suboptions': {'country': {'description': ['The country name, or code, of the geolocation to use.', 'In addition to the country full names, you may also specify their abbreviated form, such as C(US) instead of C(United States).', 'Valid country codes can be found here https://countrycode.org/.'], 'required': True, 'choices': ['Any valid 2 character ISO country code.', 'Any valid country name.']}, 'region': {'description': ['Region name of the country to use.']}}}",
    "name": "{'description': ['Specifies the name of the address list.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the address list and entries exists.', 'When C(absent), ensures the address list is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create an address list
  bigip_firewall_address_list:
    name: foo
    addresses:
      - 3.3.3.3
      - 4.4.4.4
      - 5.5.5.5
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
