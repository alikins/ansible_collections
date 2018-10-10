# Ansible module: ansible.module_bigip_data_group


Manage data groups on a BIG-IP

## Description

Allows for managing data groups on a BIG-IP. Data groups provide a way to store collections of values on a BIG-IP for later use in things such as LTM rules, iRules, and ASM policies.

## Requirements

TODO

## Arguments

``` json
{
    "delete_data_group_file": "{'description': ['When C(yes), will ensure that the remote data group file is deleted.', 'This parameter is only relevant when C(state) is C(absent) and C(internal) is C(no).'], 'default': False, 'type': 'bool'}",
    "external_file_name": "{'description': ['When creating a new data group, this specifies the file name that you want to give an external data group file on the BIG-IP.', 'This parameter is ignored when C(internal) is C(yes).', 'This parameter can be used to select an existing data group file to use with an existing external data group.', 'If this value is not provided, it will be given the value specified in C(name) and, therefore, match the name of the data group.', 'This value may only contain letters, numbers, underscores, dashes, or a period.']}",
    "internal": "{'description': ['The type of this data group.', "You should only consider setting this value in cases where you know exactly what you're doing, B(or), you are working with a pre-existing internal data group.", 'Be aware that if you deliberately force this parameter to C(yes), and you have a either a large number of records or a large total records size, this large amount of data will be reflected in your BIG-IP configuration. This can lead to B(long) system configuration load times due to needing to parse and verify the large configuration.', 'There is a limit of either 4 megabytes or 65,000 records (whichever is more restrictive) for uploads when this parameter is C(yes).', 'This value cannot be changed once the data group is created.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Specifies the name of the data group.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "records": "{'description': ['Specifies the records that you want to add to a data group.', 'If you have a large number of records, it is recommended that you use C(records_content) instead of typing all those records here.', 'The technical limit of either 1. the number of records, or 2. the total size of all records, varies with the size of the total resources on your system; in particular, RAM.', 'When C(internal) is C(no), at least one record must be specified in either C(records) or C(records_content).'], 'suboptions': {'key': {'description': ['The key describing the record in the data group.', 'Your key will be used for validation of the C(type) parameter to this module.'], 'required': True}, 'value': {'description': ['The value of the key describing the record in the data group.']}}}",
    "records_src": "{'description': ['Path to a file with records in it.', 'The file should be well-formed. This means that it includes records, one per line, that resemble the following format "key separator value". For example, C(foo := bar).', 'BIG-IP is strict about this format, but this module is a bit more lax. It will allow you to include arbitrary amounts (including none) of empty space on either side of the separator. For an illustration of this, see the Examples section.', 'Record keys are limited in length to no more than 65520 characters.', 'Values of record keys are limited in length to no more than 65520 characters.', 'The total number of records you can have in your BIG-IP is limited by the memory of the BIG-IP.', 'The format of this content is slightly different depending on whether you specify a C(type) of C(address), C(integer), or C(string). See the examples section for examples of the different types of payload formats that are expected in your data group file.', 'When C(internal) is C(no), at least one record must be specified in either C(records) or C(records_content).']}",
    "separator": "{'description': ['When specifying C(records_content), this is the string of characters that will be used to break apart entries in the C(records_content) into key/value pairs.', "By default, this parameter's value is C(:=).", 'This value cannot be changed once it is set.', 'This parameter is only relevant when C(internal) is C(no). It will be ignored otherwise.'], 'default': ':='}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(state) is C(present), ensures the data group exists.', 'When C(state) is C(absent), ensures that the data group is removed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['The type of records in this data group.', 'This parameter is especially important because it causes BIG-IP to store your data in different ways so-as to optimize access to it. For example, it would be wrong to specify a list of records containing IP addresses, but label them as a C(string) type.', 'This value cannot be changed once the data group is created.'], 'choices': ['address', 'addr', 'ip', 'string', 'str', 'integer', 'int'], 'default': 'string'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a data group of addresses
  bigip_data_group:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    records:
      - key: 0.0.0.0/32
        value: External_NAT
      - key: 10.10.10.10
        value: No_NAT
    type: address
  delegate_to: localhost

- name: Create a data group of strings
  bigip_data_group:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    records:
      - key: caddy
        value: ""
      - key: cafeteria
        value: ""
      - key: cactus
        value: ""
    type: string
  delegate_to: localhost

- name: Create a data group of IP addresses from a file
  bigip_data_group:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    records_src: /path/to/dg-file
    type: address
  delegate_to: localhost

- name: Update an existing internal data group of strings
  bigip_data_group:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    internal: yes
    user: admin
    records:
      - key: caddy
        value: ""
      - key: cafeteria
        value: ""
      - key: cactus
        value: ""
  delegate_to: localhost

- name: Show the data format expected for records_content - address 1
  copy:
    dest: /path/to/addresses.txt
    content: |
      network 10.0.0.0 prefixlen 8 := "Network1",
      network 172.16.0.0 prefixlen 12 := "Network2",
      network 192.168.0.0 prefixlen 16 := "Network3",
      network 2402:9400:1000:0:: prefixlen 64 := "Network4",
      host 192.168.20.1 := "Host1",
      host 172.16.1.1 := "Host2",
      host 172.16.1.1/32 := "Host3",
      host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 := "Host4",
      host 2001:0db8:85a3:0000:0000:8a2e:0370:7334/128 := "Host5"

- name: Show the data format expected for records_content - address 2
  copy:
    dest: /path/to/addresses.txt
    content: |
      10.0.0.0/8 := "Network1",
      172.16.0.0/12 := "Network2",
      192.168.0.0/16 := "Network3",
      2402:9400:1000:0::/64 := "Network4",
      192.168.20.1 := "Host1",
      172.16.1.1 := "Host2",
      172.16.1.1/32 := "Host3",
      2001:0db8:85a3:0000:0000:8a2e:0370:7334 := "Host4",
      2001:0db8:85a3:0000:0000:8a2e:0370:7334/128 := "Host5"

- name: Show the data format expected for records_content - string
  copy:
    dest: /path/to/strings.txt
    content: |
      a := alpha,
      b := bravo,
      c := charlie,
      x := x-ray,
      y := yankee,
      z := zulu,

- name: Show the data format expected for records_content - integer
  copy:
    dest: /path/to/integers.txt
    content: |
      1 := bar,
      2 := baz,
      3,
      4,

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
