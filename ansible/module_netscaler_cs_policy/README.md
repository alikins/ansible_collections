# Ansible module: ansible.module_netscaler_cs_policy


Manage content switching policy

## Description

Manage content switching policy.
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Content switching action that names the target load balancing virtual server to which the traffic is switched.']}",
    "domain": "{'description': ['The domain name. The string value can range to 63 characters.', 'Minimum length = 1']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "policyname": "{'description': ['Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore C(_) character, and must contain only ASCII alphanumeric, underscore, hash C(#), period C(.), space C( ), colon C(:), at sign C(@), equal sign C(=), and hyphen C(-) characters. Cannot be changed after a policy is created.', 'The following requirement applies only to the NetScaler CLI:', 'If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my policy or my policy).', 'Minimum length = 1']}",
    "rule": "{'description': ['Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.', 'Note:', 'Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: \'"<string of 255 characters>" + "<string of 245 characters>"\'']}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "url": "{'description': ['URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: C([[prefix] [*]] [.suffix]).', 'Minimum length = 1', 'Maximum length = 208']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

- name: Create url cs policy
  delegate_to: localhost
  netscaler_cs_policy:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    validate_certs: no

    state: present

    policyname: policy_1
    url: /example/

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
