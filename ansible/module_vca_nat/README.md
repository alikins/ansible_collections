# Ansible module: ansible.module_vca_nat


add remove nat rules in a gateway  in a vca

## Description

Adds or removes nat rules from a gateway in a vca environment

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The api version to be used with the vca.'], 'default': '5.7'}",
    "gateway_name": "{'description': ['The name of the gateway of the vdc where the rule should be added.'], 'default': 'gateway'}",
    "host": "{'description': ['The authentication host to be used when service type is vcd.']}",
    "instance_id": "{'description': ['The instance id in a vchs environment to be used for creating the vapp.']}",
    "nat_rules": "{'description': ['A list of rules to be added to the gateway, Please see examples on valid entries'], 'required': True, 'default': False}",
    "org": "{'description': ['The org to login to for creating vapp. This option is required when the C(service_type) is I(vdc).']}",
    "password": "{'description': ['The vca password, if not set the environment variable C(VCA_PASS) is checked for the password.'], 'aliases': ['pass', 'passwd']}",
    "purge_rules": "{'description': ['If set to true, it will delete all rules in the gateway that are not given as parameter to this module.'], 'type': 'bool', 'default': False}",
    "service_type": "{'description': ['The type of service we are authenticating against.'], 'default': 'vca', 'choices': ['vca', 'vchs', 'vcd']}",
    "state": "{'description': ['If the object should be added or removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The vca username or email address, if not set the environment variable C(VCA_USER) is checked for the username.'], 'aliases': ['user']}",
    "vdc_name": "{'description': ['The name of the vdc where the gateway is located.']}",
    "verify_certs": "{'description': ['If the certificates of the authentication is to be verified.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml


#An example for a source nat

- hosts: localhost
  connection: local
  tasks:
   - vca_nat:
       instance_id: 'b15ff1e5-1024-4f55-889f-ea0209726282'
       vdc_name: 'benz_ansible'
       state: 'present'
       nat_rules:
         - rule_type: SNAT
           original_ip: 192.0.2.42
           translated_ip: 203.0.113.23

#example for a DNAT
- hosts: localhost
  connection: local
  tasks:
   - vca_nat:
       instance_id: 'b15ff1e5-1024-4f55-889f-ea0209726282'
       vdc_name: 'benz_ansible'
       state: 'present'
       nat_rules:
         - rule_type: DNAT
           original_ip: 203.0.113.23
           original_port: 22
           translated_ip: 192.0.2.42
           translated_port: 22


```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
