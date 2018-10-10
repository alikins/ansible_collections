# Ansible module: ansible.module_netscaler_cs_action


Manage content switching actions

## Description

Manage content switching actions
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Comments associated with this cs action.']}",
    "name": "{'description': ['Name for the content switching action. Must begin with an ASCII alphanumeric or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at sign C(@), equal sign C(=), and hyphen C(-) characters. Can be changed after the content switching action is created.']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "targetlbvserver": "{'description': ['Name of the load balancing virtual server to which the content is switched.']}",
    "targetvserver": "{'description': ['Name of the VPN virtual server to which the content is switched.']}",
    "targetvserverexpr": "{'description': ['Information about this content switching action.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

# lb_vserver_1 must have been already created with the netscaler_lb_vserver module

- name: Configure netscaler content switching action
  delegate_to: localhost
  netscaler_cs_action:
      nsip: 172.18.0.2
      nitro_user: nsroot
      nitro_pass: nsroot
      validate_certs: no

      state: present

      name: action-1
      targetlbvserver: lb_vserver_1

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
