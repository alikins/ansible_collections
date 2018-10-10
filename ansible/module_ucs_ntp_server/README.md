# Ansible module: ansible.module_ucs_ntp_server


Configures NTP server on Cisco UCS Manager

## Description

Configures NTP server on Cisco UCS Manager.
Examples can be used with the L(UCS Platform Emulator,https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A user-defined description of the NTP server.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr'], 'default': ''}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "ntp_server": "{'description': ['NTP server IP address or hostname.', 'Enter up to 63 characters that form a valid hostname.', 'Enter a valid IPV4 Address.'], 'aliases': ['name'], 'default': ''}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(absent), will remove an NTP server.', 'If C(present), will add or update an NTP server.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure NTP server
  ucs_ntp_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    ntp_server: 10.10.10.10
    description: Internal NTP Server by IP address
    state: present

- name: Configure NTP server
  ucs_ntp_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    ntp_server: pool.ntp.org
    description: External NTP Server by hostname
    state: present

- name: Remove NTP server
  ucs_ntp_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    ntp_server: 10.10.10.10
    state: absent

- name: Remove NTP server
  ucs_ntp_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    ntp_server: pool.ntp.org
    state: absent

```

## License

TODO

## Author Information
  - ['John McDonough (@movinalot)', 'CiscoUcs (@CiscoUcs)']
  - ['John McDonough (@movinalot)', 'CiscoUcs (@CiscoUcs)']
