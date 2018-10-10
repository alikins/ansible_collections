# Ansible module: ansible.module_bigip_device_trust


Manage the trust relationships between BIG-IPs

## Description

Manage the trust relationships between BIG-IPs. Devices, once peered, cannot be updated. If updating is needed, the peer must first be removed before it can be re-added to the trust.

## Requirements

TODO

## Arguments

``` json
{
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "peer_hostname": "{'description': ['The hostname that you want to associate with the device. This value will be used to easily distinguish this device in BIG-IP configuration.', 'When trusting a new device, if this parameter is not specified, the value of C(peer_server) will be used as a default.']}",
    "peer_password": "{'description': ['The password of the API username of the remote peer device that you are trusting. If this value is not specified, then the value of C(password), or the environment variable C(F5_PASSWORD) will be used.']}",
    "peer_server": "{'description': ['The peer address to connect to and trust for synchronizing configuration. This is typically the management address of the remote device, but may also be a Self IP.'], 'required': True}",
    "peer_user": "{'description': ['The API username of the remote peer device that you are trusting. Note that the CLI user cannot be used unless it too has an API account. If this value is not specified, then the value of C(user), or the environment variable C(F5_USER) will be used.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures the specified devices are trusted.', 'When C(absent), removes the device trusts.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "type": "{'description': ['Specifies whether the device you are adding is a Peer or a Subordinate. The default is C(peer).', 'The difference between the two is a matter of mitigating risk of compromise.', 'A subordinate device cannot sign a certificate for another device.', 'In the case where the security of an authority device in a trust domain is compromised, the risk of compromise is minimized for any subordinate device.', 'Designating devices as subordinate devices is recommended for device groups with a large number of member devices, where the risk of compromise is high.'], 'choices': ['peer', 'subordinate'], 'default': 'peer'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add trusts for all peer devices to Active device
  bigip_device_trust:
    server: lb.mydomain.com
    user: admin
    password: secret
    peer_server: "{{ item.ansible_host }}"
    peer_hostname: "{{ item.inventory_hostname }}"
    peer_user: "{{ item.bigip_username }}"
    peer_password: "{{ item.bigip_password }}"
  with_items: hostvars
  when: inventory_hostname in groups['master']
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
