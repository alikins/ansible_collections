# Ansible module: ansible.module_win_iis_webbinding


Configures a IIS Web site binding

## Description

Creates, removes and configures a binding to an existing IIS Web site.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_hash": "{'description': ['Certificate hash (thumbprint) for the SSL binding. The certificate hash is the unique identifier for the certificate.']}",
    "certificate_store_name": "{'description': ['Name of the certificate store where the certificate for the binding is located.'], 'default': 'my'}",
    "host_header": "{'description': ['The host header to bind to / use for the new site.', "If you are creating/removing a catch-all binding, omit this parameter rather than defining it as '*'."]}",
    "ip": "{'description': ['The IP address to bind to / use for the new site.'], 'default': '*'}",
    "name": "{'description': ['Names of web site.'], 'required': True, 'aliases': ['website']}",
    "port": "{'description': ['The port to bind to / use for the new site.'], 'default': 80}",
    "protocol": "{'description': ['The protocol to be used for the Web binding (usually HTTP, HTTPS, or FTP).'], 'default': 'http'}",
    "ssl_flags": "{'description': ['This parameter is only valid on Server 2012 and newer.', 'Primarily used for enabling and disabling server name indication (SNI).', 'Set to c(0) to disable SNI.', 'Set to c(1) to enable SNI.'], 'version_added': '2.5'}",
    "state": "{'description': ['State of the binding.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add a HTTP binding on port 9090
  win_iis_webbinding:
    name: Default Web Site
    port: 9090
    state: present

- name: Remove the HTTP binding on port 9090
  win_iis_webbinding:
    name: Default Web Site
    port: 9090
    state: absent

- name: Remove the default http binding
  win_iis_webbinding:
    name: Default Web Site
    port: 80
    ip: '*'
    state: absent

- name: Add a HTTPS binding
  win_iis_webbinding:
    name: Default Web Site
    protocol: https
    port: 443
    ip: 127.0.0.1
    certificate_hash: B0D0FA8408FC67B230338FCA584D03792DA73F4C
    state: present

- name: Add a HTTPS binding with host header and SNI enabled
  win_iis_webbinding:
    name: Default Web Site
    protocol: https
    port: 443
    host_header: test.com
    ssl_flags: 1
    certificate_hash: D1A3AF8988FD32D1A3AF8988FD323792DA73F4C
    state: present

```

## License

TODO

## Author Information
  - ['Noah Sparks (@nwsparks)', 'Henrik Wallström']
  - ['Noah Sparks (@nwsparks)', 'Henrik Wallström']
