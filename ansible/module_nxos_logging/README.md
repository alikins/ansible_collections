# Ansible module: ansible.module_nxos_logging


Manage logging on network devices

## Description

This module provides declarative management of logging on Cisco NX-OS devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of logging definitions.']}",
    "dest": "{'description': ['Destination of the logs.'], 'choices': ['console', 'logfile', 'module', 'monitor', 'server']}",
    "dest_level": "{'description': ['Set logging severity levels.'], 'aliases': ['level']}",
    "event": "{'description': ['Link/trunk enable/default interface configuration logging'], 'choices': ['link-enable', 'link-default', 'trunk-enable', 'trunk-default'], 'version_added': '2.8'}",
    "facility": "{'description': ['Facility name for logging.']}",
    "facility_level": "{'description': ['Set logging serverity levels for facility based log messages.']}",
    "facility_link_status": "{'description': ['Set logging facility ethpm link status. Not idempotent with version 6.0 images.'], 'choices': ['link-down-notif', 'link-down-error', 'link-up-notif', 'link-up-error'], 'version_added': '2.8'}",
    "file_size": "{'description': ['Set logfile size'], 'version_added': '2.8'}",
    "interface": "{'description': ["Interface to be used while configuring source-interface for logging (e.g., 'Ethernet1/2', 'mgmt0')"], 'version_added': '2.7'}",
    "message": "{'description': ['Add interface description to interface syslogs. Does not work with version 6.0 images using nxapi as a transport.'], 'choices': ['add-interface-description'], 'version_added': '2.8'}",
    "name": "{'description': ['If value of C(dest) is I(logfile) it indicates file-name.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "purge": "{'description': ['Remove any switch logging configuration that does not match what has been configured'], 'type': 'bool', 'default': False, 'version_added': '2.8'}",
    "remote_server": "{'description': ["Hostname or IP Address for remote logging (when dest is 'server')."], 'version_added': '2.7'}",
    "state": "{'description': ['State of the logging configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timestamp": "{'description': ['Set logging timestamp format'], 'choices': ['microseconds', 'milliseconds', 'seconds'], 'version_added': '2.8'}",
    "use_vrf": "{'description': ["VRF to be used while configuring remote logging (when dest is 'server')."], 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: configure console logging with level
  nxos_logging:
    dest: console
    level: 2
    state: present
- name: remove console logging configuration
  nxos_logging:
    dest: console
    level: 2
    state: absent
- name: configure file logging with level
  nxos_logging:
    dest: logfile
    name: testfile
    dest_level: 3
    state: present
- name: Configure logging logfile with size
  nxos_logging:
    dest: logfile
    name: testfile
    dest_level: 3
    file_size: 16384
- name: configure facility level logging
  nxos_logging:
    facility: daemon
    facility_level: 0
    state: present
- name: remove facility level logging
  nxos_logging:
    facility: daemon
    facility_level: 0
    state: absent
- name: Configure Remote Logging
  nxos_logging:
    dest: server
    remote_server: test-syslogserver.com
    facility: auth
    facility_level: 1
    use_vrf: management
    state: present
- name: Configure Source Interface for Logging
  nxos_logging:
    interface: mgmt0
    state: present
- name: Purge nxos_logging configuration not managed by this playbook
  nxos_logging:
    purge: true
- name: Configure logging timestamp
  nxos_logging:
    timestamp: milliseconds
    state: present
- name: Configure logging facility ethpm link status
  nxos_logging:
    facility: ethpm
    facility_link_status: link-up-notif
    state: present
- name: Configure logging message ethernet description
  nxos_logging:
    message: add-interface-description
    state: present
- name: Configure logging event link enable
  nxos_logging:
    event: link-enable
    state: present
- name: Configure logging using aggregate
  nxos_logging:
    aggregate:
      - { dest: console, dest_level: 2 }
      - { dest: logfile, dest_level: 2, name: testfile }
      - { facility: daemon, facility_level: 0 }
    state: present

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
