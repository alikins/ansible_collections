# Ansible module: ansible.module_netscaler_server


Manage server configuration

## Description

Manage server entities configuration.
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Any information about the server.']}",
    "delay": "{'description': ['Time, in seconds, after which all the services configured on the server are disabled.', 'This option is meaningful only when setting the I(disabled) option to C(true)'], 'version_added': '2.5'}",
    "disabled": "{'description': ['When set to C(true) the server state will be set to C(disabled).', 'When set to C(false) the server state will be set to C(enabled).', 'Note that due to limitations of the underlying NITRO API a C(disabled) state change alone does not cause the module result to report a changed status.'], 'type': 'bool', 'default': False}",
    "domain": "{'description': ['Domain name of the server. For a domain based configuration, you must create the server first.', 'Minimum length = 1']}",
    "domainresolveretry": "{'description': ['Time, in seconds, for which the NetScaler appliance must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.', 'Minimum value = C(5)', 'Maximum value = C(20939)'], 'default': 5}",
    "graceful": "{'description': ['Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.', 'This option is meaningful only when setting the I(disabled) option to C(true)'], 'type': 'bool', 'version_added': '2.5'}",
    "ipaddress": "{'description': ['IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.']}",
    "ipv6address": "{'description': ['Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.'], 'default': False, 'type': 'bool'}",
    "name": "{'description': ['Name for the server.', 'Must begin with an ASCII alphabetic or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at C(@), equals C(=), and hyphen C(-) characters.', 'Can be changed after the name is created.', 'Minimum length = 1']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "td": "{'description': ['Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.', 'Minimum value = C(0)', 'Maximum value = C(4094)']}",
    "translationip": "{'description': ["IP address used to transform the server's DNS-resolved IP address."]}",
    "translationmask": "{'description': ['The netmask of the translation ip.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

- name: Setup server
  delegate_to: localhost
  netscaler_server:
      nsip: 172.18.0.2
      nitro_user: nsroot
      nitro_pass: nsroot

      state: present

      name: server-1
      ipaddress: 192.168.1.1

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
