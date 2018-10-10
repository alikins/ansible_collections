# Ansible module: ansible.module_zabbix_host


Zabbix host creates/updates/deletes

## Description

This module allows you to create, modify and delete Zabbix host entries and associated group and template data.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the host in Zabbix.'], 'version_added': '2.5'}",
    "force": "{'description': ['Overwrite the host configuration, even if already present.'], 'type': 'bool', 'default': True, 'version_added': '2.0'}",
    "host_groups": "{'description': ['List of host groups the host is part of.']}",
    "host_name": "{'description': ['Name of the host in Zabbix.', 'host_name is the unique identifier used and cannot be updated using this module.'], 'required': True}",
    "http_login_password": "{'description': ['Basic Auth password'], 'version_added': '2.1'}",
    "http_login_user": "{'description': ['Basic Auth login'], 'version_added': '2.1'}",
    "interfaces": "{'description': ['List of interfaces to be created for the host (see example below).', 'Available keys are: I(dns), I(ip), I(main), I(port), I(type), I(useip), and I(bulk).', 'Please review the interface documentation for more information on the supported properties', 'https://www.zabbix.com/documentation/2.0/manual/appendix/api/hostinterface/definitions#host_interface', 'If an interface definition is incomplete, this module will attempt to fill in sensible values.', 'I(type) can also be C(agent), C(snmp), C(ipmi), or C(jmx) instead of its numerical value.'], 'default': []}",
    "inventory_mode": "{'description': ['Configure the inventory mode.'], 'choices': ['automatic', 'manual', 'disabled'], 'version_added': '2.1'}",
    "inventory_zabbix": "{'description': ['Add Facts for a zabbix inventory (e.g. Tag) (see example below).', 'Please review the interface documentation for more information on the supported properties', 'https://www.zabbix.com/documentation/3.2/manual/api/reference/host/object#host_inventory'], 'version_added': '2.5'}",
    "ipmi_authtype": "{'description': ['IPMI authentication algorithm.', 'Please review the Host object documentation for more information on the supported properties', 'https://www.zabbix.com/documentation/3.4/manual/api/reference/host/object', 'Possible values are, C(0) (none), C(1) (MD2), C(2) (MD5), C(4) (straight), C(5) (OEM), C(6) (RMCP+), with -1 being the API default.', 'Please note that the Zabbix API will treat absent settings as default when updating any of the I(ipmi_)-options; this means that if you attempt to set any of the four options individually, the rest will be reset to default values.'], 'version_added': '2.5'}",
    "ipmi_password": "{'description': ['IPMI password.', 'also see the last note in the I(ipmi_authtype) documentation'], 'version_added': '2.5'}",
    "ipmi_privilege": "{'description': ['IPMI privilege level.', 'Please review the Host object documentation for more information on the supported properties', 'https://www.zabbix.com/documentation/3.4/manual/api/reference/host/object', 'Possible values are C(1) (callback), C(2) (user), C(3) (operator), C(4) (admin), C(5) (OEM), with C(2) being the API default.', 'also see the last note in the I(ipmi_authtype) documentation'], 'version_added': '2.5'}",
    "ipmi_username": "{'description': ['IPMI username.', 'also see the last note in the I(ipmi_authtype) documentation'], 'version_added': '2.5'}",
    "link_templates": "{'description': ['List of templates linked to the host.']}",
    "login_password": "{'description': ['Zabbix user password.'], 'required': True}",
    "login_user": "{'description': ['Zabbix user name.'], 'required': True}",
    "proxy": "{'description': ['The name of the Zabbix proxy to be used.']}",
    "server_url": "{'description': ['URL of Zabbix server, with protocol (http or https). C(url) is an alias for C(server_url).'], 'required': True, 'aliases': ['url']}",
    "state": "{'description': ['State of the host.', 'On C(present), it will create if host does not exist or update the host if the associated data is different.', 'On C(absent) will remove a host if it exists.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "status": "{'description': ['Monitoring status of the host.'], 'choices': ['enabled', 'disabled'], 'default': 'enabled'}",
    "timeout": "{'description': ['The timeout of API request (seconds).'], 'default': 10}",
    "tls_accept": "{'description': ['Specifies what types of connections are allowed for incoming connections.', 'The tls_accept parameter accepts values of 1 to 7', 'Possible values, 1 (no encryption), 2 (PSK), 4 (certificate).', 'Values can be combined.', 'Works only with >= Zabbix 3.0'], 'default': 1, 'version_added': '2.5'}",
    "tls_connect": "{'description': ['Specifies what encryption to use for outgoing connections.', 'Possible values, 1 (no encryption), 2 (PSK), 4 (certificate).', 'Works only with >= Zabbix 3.0'], 'default': 1, 'version_added': '2.5'}",
    "tls_issuer": "{'description': ['Required certificate issuer.', 'Works only with >= Zabbix 3.0'], 'version_added': '2.5'}",
    "tls_psk": "{'description': ['PSK value is a hard to guess string of hexadecimal digits.', 'The preshared key, at least 32 hex digits. Required if either tls_connect or tls_accept has PSK enabled.', 'Works only with >= Zabbix 3.0'], 'version_added': '2.5'}",
    "tls_psk_identity": "{'description': ['It is a unique name by which this specific PSK is referred to by Zabbix components', 'Do not put sensitive information in the PSK identity string, it is transmitted over the network unencrypted.', 'Works only with >= Zabbix 3.0'], 'version_added': '2.5'}",
    "tls_subject": "{'description': ['Required certificate subject.', 'Works only with >= Zabbix 3.0'], 'version_added': '2.5'}",
    "validate_certs": "{'description': ['If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
    "visible_name": "{'description': ['Visible name of the host in Zabbix.'], 'version_added': '2.3'}",
}
```

## Examples


``` yaml

- name: Create a new host or update an existing host's info
  local_action:
    module: zabbix_host
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    host_name: ExampleHost
    visible_name: ExampleName
    description: My ExampleHost Description
    host_groups:
      - Example group1
      - Example group2
    link_templates:
      - Example template1
      - Example template2
    status: enabled
    state: present
    inventory_mode: manual
    inventory_zabbix:
      tag: "{{ your_tag }}"
      alias: "{{ your_alias }}"
      notes: "Special Informations: {{ your_informations | default('None') }}"
      location: "{{ your_location }}"
      site_rack: "{{ your_site_rack }}"
      os: "{{ your_os }}"
      hardware: "{{ your_hardware }}"
    ipmi_authtype: 2
    ipmi_privilege: 4
    ipmi_username: username
    ipmi_password: password
    interfaces:
      - type: 1
        main: 1
        useip: 1
        ip: 10.xx.xx.xx
        dns: ""
        port: 10050
      - type: 4
        main: 1
        useip: 1
        ip: 10.xx.xx.xx
        dns: ""
        port: 12345
    proxy: a.zabbix.proxy
- name: Update an existing host's TLS settings
  local_action:
    module: zabbix_host
    server_url: http://monitor.example.com
    login_user: username
    login_password: password
    host_name: ExampleHost
    visible_name: ExampleName
    host_groups:
      - Example group1
    tls_psk_identity: test
    tls_connect: 2
    tls_psk: 123456789abcdef123456789abcdef12

```

## License

TODO

## Author Information
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)', 'Werner Dijkerman (@dj-wasabi)', 'Eike Frost (@eikef)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)', 'Werner Dijkerman (@dj-wasabi)', 'Eike Frost (@eikef)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)', 'Werner Dijkerman (@dj-wasabi)', 'Eike Frost (@eikef)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)', 'Werner Dijkerman (@dj-wasabi)', 'Eike Frost (@eikef)']
  - ['(@cove)', 'Tony Minfei Ding', 'Harrison Gu (@harrisongu)', 'Werner Dijkerman (@dj-wasabi)', 'Eike Frost (@eikef)']
