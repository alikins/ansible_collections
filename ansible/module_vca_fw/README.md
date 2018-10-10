# Ansible module: ansible.module_vca_fw


add remove firewall rules in a gateway  in a vca

## Description

Adds or removes firewall rules from a gateway in a vca environment

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The api version to be used with the vca.'], 'default': '5.7'}",
    "fw_rules": "{'description': ['A list of firewall rules to be added to the gateway, Please see examples on valid entries'], 'required': True, 'default': False}",
    "gateway_name": "{'description': ['The name of the gateway of the vdc where the rule should be added.'], 'default': 'gateway'}",
    "host": "{'description': ['The authentication host to be used when service type is vcd.']}",
    "instance_id": "{'description': ['The instance id in a vchs environment to be used for creating the vapp.']}",
    "org": "{'description': ['The org to login to for creating vapp. This option is required when the C(service_type) is I(vdc).']}",
    "password": "{'description': ['The vca password, if not set the environment variable C(VCA_PASS) is checked for the password.'], 'aliases': ['pass', 'passwd']}",
    "service_type": "{'description': ['The type of service we are authenticating against.'], 'default': 'vca', 'choices': ['vca', 'vchs', 'vcd']}",
    "state": "{'description': ['If the object should be added or removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The vca username or email address, if not set the environment variable C(VCA_USER) is checked for the username.'], 'aliases': ['user']}",
    "vdc_name": "{'description': ['The name of the vdc where the gateway is located.']}",
    "verify_certs": "{'description': ['If the certificates of the authentication is to be verified.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml


#Add a set of firewall rules

- hosts: localhost
  connection: local
  tasks:
   - vca_fw:
       instance_id: 'b15ff1e5-1024-4f55-889f-ea0209726282'
       vdc_name: 'benz_ansible'
       state: 'absent'
       fw_rules:
         - description: "ben testing"
           source_ip: "Any"
           dest_ip: 192.0.2.23
         - description: "ben testing 2"
           source_ip: 192.0.2.50
           source_port: "Any"
           dest_port: "22"
           dest_ip: 192.0.2.101
           is_enable: "true"
           enable_logging: "false"
           protocol: "Tcp"
           policy: "allow"


```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
