# Ansible module: ansible.module_packet_device


Manage a bare metal server in the Packet Host

## Description

Manage a bare metal server in the Packet Host (a "device" in the API terms).
When the machine is created it can optionally wait for public IP address, or for active state.
This module has a dependency on packet >= 1.0.
API is documented at U(https://www.packet.net/developers/api/devices).

## Requirements

TODO

## Arguments

``` json
{
    "always_pxe": "{'description': ['Persist PXE as the first boot option.', 'Normally, the PXE process happens only on the first boot. Set this arg to have your device continuously boot to iPXE.'], 'default': False, 'version_added': '2.4'}",
    "auth_token": "{'description': ['Packet api token. You can also supply it in env var C(PACKET_API_TOKEN).']}",
    "count": "{'description': ['The number of devices to create. Count number can be included in hostname via the %d string formatter.'], 'default': 1}",
    "count_offset": "{'description': ['From which number to start the count.'], 'default': 1}",
    "device_ids": "{'description': ['List of device IDs on which to operate.']}",
    "facility": "{'description': ['Facility slug for device creation. See Packet API for current list - U(https://www.packet.net/developers/api/facilities/).']}",
    "features": "{'description': ['Dict with "features" for device creation. See Packet API docs for details.']}",
    "hostnames": "{'description': ['A hostname of a device, or a list of hostnames.', 'If given string or one-item list, you can use the C("%d") Python string format to expand numbers from I(count).', 'If only one hostname, it might be expanded to list if I(count)>1.'], 'aliases': ['name']}",
    "ipxe_script_url": "{'description': ['URL of custom iPXE script for provisioning.', 'More about custome iPXE for Packet devices at U(https://help.packet.net/technical/infrastructure/custom-ipxe).'], 'version_added': '2.4'}",
    "locked": "{'description': ['Whether to lock a created device.'], 'default': False, 'version_added': '2.4', 'aliases': ['lock']}",
    "operating_system": "{'description': ['OS slug for device creation. See Packet API for current list - U(https://www.packet.net/developers/api/operatingsystems/).']}",
    "plan": "{'description': ['Plan slug for device creation. See Packet API for current list - U(https://www.packet.net/developers/api/plans/).']}",
    "project_id": "{'description': ['ID of project of the device.'], 'required': True}",
    "state": "{'description': ['Desired state of the device.', 'If set to C(present) (the default), the module call will return immediately after the device-creating HTTP request successfully returns.', 'If set to C(active), the module call will block until all the specified devices are in state active due to the Packet API, or until I(wait_timeout).'], 'choices': ['present', 'absent', 'active', 'inactive', 'rebooted'], 'default': 'present'}",
    "user_data": "{'description': ['Userdata blob made available to the machine']}",
    "wait_for_public_IPv": "{'description': ['Whether to wait for the instance to be assigned a public IPv4/IPv6 address.', 'If set to 4, it will wait until IPv4 is assigned to the instance.', 'If set to 6, wait until public IPv6 is assigned to the instance.'], 'choices': [4, 6], 'version_added': '2.4'}",
    "wait_timeout": "{'description': ['How long (seconds) to wait either for automatic IP address assignment, or for the device to reach the C(active) I(state).', 'If I(wait_for_public_IPv) is set and I(state) is C(active), the module will wait for both events consequently, applying the timeout twice.'], 'default': 900}",
}
```

## Examples


``` yaml

# All the examples assume that you have your Packet api token in env var PACKET_API_TOKEN.
# You can also pass it to the auth_token parameter of the module instead.

# Creating devices

- name: create 1 device
  hosts: localhost
  tasks:
  - packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: myserver
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1

# Create the same device and wait until it is in state "active", (when it's
# ready for other API operations). Fail if the devices in not "active" in
# 10 minutes.

- name: create device and wait up to 10 minutes for active state
  hosts: localhost
  tasks:
  - packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: myserver
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1
      state: active
      wait_timeout: 600

- name: create 3 ubuntu devices called server-01, server-02 and server-03
  hosts: localhost
  tasks:
  - packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: server-%02d
      count: 3
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1

- name: Create 3 coreos devices with userdata, wait until they get IPs and then wait for SSH
  hosts: localhost
  tasks:
  - name: create 3 devices and register their facts
    packet_device:
      hostnames: [coreos-one, coreos-two, coreos-three]
      operating_system: coreos_stable
      plan: baremetal_0
      facility: ewr1
      locked: true
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      wait_for_public_IPv: 4
      user_data: |
        #cloud-config
        ssh_authorized_keys:
          - {{ lookup('file', 'my_packet_sshkey') }}
        coreos:
          etcd:
            discovery: https://discovery.etcd.io/6a28e078895c5ec737174db2419bb2f3
            addr: $private_ipv4:4001
            peer-addr: $private_ipv4:7001
          fleet:
            public-ip: $private_ipv4
          units:
            - name: etcd.service
              command: start
            - name: fleet.service
              command: start
    register: newhosts

  - name: wait for ssh
    wait_for:
      delay: 1
      host: "{{ item.public_ipv4 }}"
      port: 22
      state: started
      timeout: 500
    with_items: "{{ newhosts.devices }}"


# Other states of devices

- name: remove 3 devices by uuid
  hosts: localhost
  tasks:
  - packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      state: absent
      device_ids:
        - 1fb4faf8-a638-4ac7-8f47-86fe514c30d8
        - 2eb4faf8-a638-4ac7-8f47-86fe514c3043
        - 6bb4faf8-a638-4ac7-8f47-86fe514c301f

```

## License

TODO

## Author Information
  - ['Tomas Karasek (@t0mk) <tom.to.the.k@gmail.com>', 'Matt Baldwin <baldwin@stackpointcloud.com>', "Thibaud Morel l'Horset <teebes@gmail.com>"]
  - ['Tomas Karasek (@t0mk) <tom.to.the.k@gmail.com>', 'Matt Baldwin <baldwin@stackpointcloud.com>', "Thibaud Morel l'Horset <teebes@gmail.com>"]
  - ['Tomas Karasek (@t0mk) <tom.to.the.k@gmail.com>', 'Matt Baldwin <baldwin@stackpointcloud.com>', "Thibaud Morel l'Horset <teebes@gmail.com>"]
