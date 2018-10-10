# Ansible module: ansible.module_bigip_device_facts


Collect facts from F5 BIG-IP devices

## Description

Collect facts from F5 BIG-IP devices.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts returned to a given subset.', 'Can specify a list of values to include a larger subset.', 'Values can also be used with an initial C(!) to specify that a specific subset should not be collected.'], 'required': True, 'choices': ['all', 'monitors', 'profiles', 'asm-policy-stats', 'client-ssl-profiles', 'devices', 'device-groups', 'external-monitors', 'fasthttp-profiles', 'fastl4-profiles', 'gateway-icmp-monitors', 'gtm-pools', 'gtm-servers', 'gtm-wide-ips', 'gtm-a-pools', 'gtm-a-wide-ips', 'gtm-aaaa-pools', 'gtm-aaaa-wide-ips', 'gtm-cname-pools', 'gtm-cname-wide-ips', 'gtm-mx-pools', 'gtm-mx-wide-ips', 'gtm-naptr-pools', 'gtm-naptr-wide-ips', 'gtm-srv-pools', 'gtm-srv-wide-ips', 'http-monitors', 'https-monitors', 'http-profiles', 'iapp-services', 'iapplx-packages', 'icmp-monitors', 'interfaces', 'internal-data-groups', 'irules', 'ltm-pools', 'nodes', 'oneconnect-profiles', 'partitions', 'provision-info', 'self-ips', 'server-ssl-profiles', 'software-volumes', 'software-images', 'software-hotfixes', 'ssl-certs', 'ssl-keys', 'system-db', 'system-info', 'tcp-monitors', 'tcp-half-open-monitors', 'tcp-profiles', 'traffic-groups', 'trunks', 'udp-profiles', 'vcmp-guests', 'virtual-addresses', 'virtual-servers', 'vlans', '!all', '!monitors', '!profiles', '!asm-policy-stats', '!client-ssl-profiles', '!devices', '!device-groups', '!external-monitors', '!fasthttp-profiles', '!fastl4-profiles', '!gateway-icmp-monitors', '!gtm-pools', '!gtm-servers', '!gtm-wide-ips', '!gtm-a-pools', '!gtm-a-wide-ips', '!gtm-aaaa-pools', '!gtm-aaaa-wide-ips', '!gtm-cname-pools', '!gtm-cname-wide-ips', '!gtm-mx-pools', '!gtm-mx-wide-ips', '!gtm-naptr-pools', '!gtm-naptr-wide-ips', '!gtm-srv-pools', '!gtm-srv-wide-ips', '!http-monitors', '!https-monitors', '!http-profiles', '!iapp-services', '!iapplx-packages', '!icmp-monitors', '!interfaces', '!internal-data-groups', '!irules', '!ltm-pools', '!nodes', '!oneconnect-profiles', '!partitions', '!provision-info', '!self-ips', '!server-ssl-profiles', '!software-volumes', '!software-images', '!software-hotfixes', '!ssl-certs', '!ssl-keys', '!system-db', '!system-info', '!tcp-monitors', '!tcp-half-open-monitors', '!tcp-profiles', '!traffic-groups', '!trunks', '!udp-profiles', '!vcmp-guests', '!virtual-addresses', '!virtual-servers', '!vlans'], 'aliases': ['include']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Collect BIG-IP facts
  bigip_device_facts:
    gather_subset:
      - interfaces
      - vlans
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IP facts
  bigip_device_facts:
    gather_subset:
      - all
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IP facts except trunks
  bigip_device_facts:
    gather_subset:
      - all
      - "!trunks"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
