# Ansible module: ansible.module_bigip_vcmp_guest


Manages vCMP guests on a BIG-IP

## Description

Manages vCMP guests on a BIG-IP. This functionality only exists on actual hardware and must be enabled by provisioning C(vcmp) with the C(bigip_provision) module.

## Requirements

TODO

## Arguments

``` json
{
    "allowed_slots": "{'description': ['Contains those slots that the guest is allowed to be assigned to.', 'When the host determines which slots this guest should be assigned to, only slots in this list will be considered.', 'This is a good way to force guests to be assigned only to particular slots, or, by configuring disjoint C(allowed_slots) on two guests, that those guests are never assigned to the same slot.', 'By default this list includes every available slot in the cluster. This means, by default, the guest may be assigned to any slot.'], 'version_added': 2.7}",
    "cores_per_slot": "{'description': ['Specifies the number of cores that the system allocates to the guest.', 'Each core represents a portion of CPU and memory. Therefore, the amount of memory allocated per core is directly tied to the amount of CPU. This amount of memory varies per hardware platform type.', 'The number you can specify depends on the type of hardware you have.', 'In the event of a reboot, the system persists the guest to the same slot on which it ran prior to the reboot.']}",
    "delete_virtual_disk": "{'description': ['When C(state) is C(absent), will additionally delete the virtual disk associated with the vCMP guest. By default, this value is C(no).'], 'type': 'bool', 'default': False}",
    "initial_image": "{'description': ["Specifies the base software release ISO image file for installing the TMOS hypervisor instance and any licensed BIG-IP modules onto the guest's virtual disk. When creating a new guest, this parameter is required."]}",
    "mgmt_address": "{'description': ['Specifies the IP address, and subnet or subnet mask that you use to access the guest when you want to manage a module running within the guest. This parameter is required if the C(mgmt_network) parameter is C(bridged).', 'When creating a new guest, if you do not specify a network or network mask, a default of C(/24) (C(255.255.255.0)) will be assumed.']}",
    "mgmt_network": "{'description': ['Specifies the method by which the management address is used in the vCMP guest.', "When C(bridged), specifies that the guest can communicate with the vCMP host's management network.", "When C(isolated), specifies that the guest is isolated from the vCMP host's management network. In this case, the only way that a guest can communicate with the vCMP host is through the console port or through a self IP address on the guest that allows traffic through port 22.", 'When C(host only), prevents the guest from installing images and hotfixes other than those provided by the hypervisor.', 'If the guest setting is C(isolated) or C(host only), the C(mgmt_address) does not apply.', "Concerning mode changing, changing C(bridged) to C(isolated) causes the vCMP host to remove all of the guest's management interfaces from its bridged management network. This immediately disconnects the guest's VMs from the physical management network. Changing C(isolated) to C(bridged) causes the vCMP host to dynamically add the guest's management interfaces to the bridged management network. This immediately connects all of the guest's VMs to the physical management network. Changing this property while the guest is in the C(configured) or C(provisioned) state has no immediate effect."], 'choices': ['bridged', 'isolated', 'host only']}",
    "mgmt_route": "{'description': ['Specifies the gateway address for the C(mgmt_address).', 'If this value is not specified when creating a new guest, it is set to C(none).', 'The value C(none) can be used during an update to remove this value.']}",
    "min_number_of_slots": "{'description': ['Specifies the minimum number of slots that the guest must be assigned to in order to deploy.', 'This field dictates the number of slots that the guest must be assigned to.', 'If at the end of any allocation attempt the guest is not assigned to at least this many slots, the attempt fails and the change that initiated it is reverted.', "A guest's C(min_number_of_slots) value cannot be greater than its C(number_of_slots)."], 'version_added': 2.7}",
    "name": "{'description': ['The name of the vCMP guest to manage.'], 'required': True}",
    "number_of_slots": "{'description': ['Specifies the number of slots for the system to use for creating the guest.', 'This value dictates how many cores a guest is allocated from each slot that it is assigned to.', 'Possible values are dependent on the type of blades being used in this cluster.', 'The default value depends on the type of blades being used in this cluster.'], 'version_added': 2.7}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['The state of the vCMP guest on the system. Each state implies the actions of all states before it.', 'When C(configured), guarantees that the vCMP guest exists with the provided attributes. Additionally, ensures that the vCMP guest is turned off.', 'When C(disabled), behaves the same as C(configured) the name of this state is just a convenience for the user that is more understandable.', 'When C(provisioned), will ensure that the guest is created and installed. This state will not start the guest; use C(deployed) for that. This state is one step beyond C(present) as C(present) will not install the guest; only setup the configuration for it to be installed.', 'When C(present), ensures the guest is properly provisioned and starts the guest so that it is in a running state.', 'When C(absent), removes the vCMP from the system.'], 'default': 'present', 'choices': ['configured', 'disabled', 'provisioned', 'present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "vlans": "{'description': ['VLANs that the guest uses to communicate with other guests, the host, and with the external network. The available VLANs in the list are those that are currently configured on the vCMP host.', "The order of these VLANs is not important; in fact, it's ignored. This module will order the VLANs for you automatically. Therefore, if you deliberately re-order them in subsequent tasks, you will find that this module will B(not) register a change."]}",
}
```

## Examples


``` yaml

- name: Create a vCMP guest
  bigip_vcmp_guest:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    mgmt_network: bridge
    mgmt_address: 10.20.30.40/24
  delegate_to: localhost

- name: Create a vCMP guest with specific VLANs
  bigip_vcmp_guest:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    mgmt_network: bridge
    mgmt_address: 10.20.30.40/24
    vlans:
      - vlan1
      - vlan2
  delegate_to: localhost

- name: Remove vCMP guest and disk
  bigip_vcmp_guest:
    name: guest1
    state: absent
    delete_virtual_disk: yes
  register: result

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
