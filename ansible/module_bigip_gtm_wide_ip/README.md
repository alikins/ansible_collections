# Ansible module: ansible.module_bigip_gtm_wide_ip


Manages F5 BIG-IP GTM wide ip

## Description

Manages F5 BIG-IP GTM wide ip.

## Requirements

TODO

## Arguments

``` json
{
    "aliases": "{'description': ['Specifies alternate domain names for the web site content you are load balancing.', 'You can use the same wildcard characters for aliases as you can for actual wide IP names.'], 'version_added': 2.7}",
    "irules": "{'description': ['List of rules to be applied.', 'If you want to remove all existing iRules, specify a single empty value; C(""). See the documentation for an example.'], 'version_added': 2.6}",
    "name": "{'description': ['Wide IP name. This name must be formatted as a fully qualified domain name (FQDN). You can also use the alias C(wide_ip) but this is deprecated and will be removed in a future Ansible version.'], 'required': True, 'aliases': ['wide_ip']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool_lb_method": "{'description': ['Specifies the load balancing method used to select a pool in this wide IP. This setting is relevant only when multiple pools are configured for a wide IP.', 'The C(round_robin) value is deprecated and will be removed in Ansible 2.9.', 'The C(global_availability) value is deprecated and will be removed in Ansible 2.9.'], 'required': True, 'aliases': ['lb_method'], 'choices': ['round-robin', 'ratio', 'topology', 'global-availability', 'global_availability', 'round_robin'], 'version_added': 2.5}",
    "pools": "{'description': ['The pools that you want associated with the Wide IP.', 'If C(ratio) is not provided when creating a new Wide IP, it will default to 1.'], 'suboptions': {'name': {'description': ['The name of the pool to include.'], 'required': True}, 'ratio': {'description': ['Ratio for the pool.', 'The system uses this number with the Ratio load balancing method.']}}, 'version_added': 2.5}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present) or C(enabled), ensures that the Wide IP exists and is enabled.', 'When C(absent), ensures that the Wide IP has been removed.', 'When C(disabled), ensures that the Wide IP exists and is disabled.'], 'default': 'present', 'choices': ['present', 'absent', 'disabled', 'enabled'], 'version_added': 2.4}",
    "type": "{'description': ['Specifies the type of wide IP. GTM wide IPs need to be keyed by query type in addition to name, since pool members need different attributes depending on the response RDATA they are meant to supply. This value is required if you are using BIG-IP versions >= 12.0.0.'], 'choices': ['a', 'aaaa', 'cname', 'mx', 'naptr', 'srv'], 'version_added': 2.4}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Set lb method
  bigip_gtm_wide_ip:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
  delegate_to: localhost

- name: Add iRules to the Wide IP
  bigip_gtm_wide_ip:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    irules:
      - irule1
      - irule2
  delegate_to: localhost

- name: Remove one iRule from the Virtual Server
  bigip_gtm_wide_ip:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    irules:
      - irule1
  delegate_to: localhost

- name: Remove all iRules from the Virtual Server
  bigip_gtm_wide_ip:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    irules: ""
  delegate_to: localhost

- name: Assign a pool with ratio to the Wide IP
  bigip_gtm_wide_ip:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    pools:
      - name: pool1
        ratio: 100
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
