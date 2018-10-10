# Ansible module: ansible.module_netapp_e_iscsi_interface


NetApp E-Series manage iSCSI interface configuration

## Description

Configure settings of an E-Series iSCSI interface

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The IPv4 address to assign to the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)']}",
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "config_method": "{'description': ['The configuration method type to use for this interface.', 'dhcp is mutually exclusive with I(address), I(subnet_mask), and I(gateway).'], 'choices': ['dhcp', 'static'], 'default': 'dhcp'}",
    "controller": "{'description': ['The controller that owns the port you want to configure.', 'Controller names are presented alphabetically, with the first controller as A, the second as B, and so on.', 'Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.'], 'required': True, 'choices': ['A', 'B']}",
    "gateway": "{'description': ['The IPv4 gateway address to utilize for the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)']}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False}",
    "mtu": "{'description': ['The maximum transmission units (MTU), in bytes.', 'This allows you to configure a larger value for the MTU, in order to enable jumbo frames (any value > 1500).', "Generally, it is necessary to have your host, switches, and other components not only support jumbo frames, but also have it configured properly. Therefore, unless you know what you're doing, it's best to leave this at the default."], 'default': 1500, 'aliases': ['max_frame_size']}",
    "name": "{'description': ['The channel of the port to modify the configuration of.', 'The list of choices is not necessarily comprehensive. It depends on the number of ports that are available in the system.', 'The numerical value represents the number of the channel (typically from left to right on the HIC), beginning with a value of 1.'], 'required': True, 'aliases': ['channel']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['When enabled, the provided configuration will be utilized.', 'When disabled, the IPv4 configuration will be cleared and IPv4 connectivity disabled.'], 'choices': ['enabled', 'disabled'], 'default': 'enabled'}",
    "subnet_mask": "{'description': ['The subnet mask to utilize for the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Configure the first port on the A controller with a static IPv4 address
      netapp_e_iscsi_interface:
        name: "1"
        controller: "A"
        config_method: static
        address: "192.168.1.100"
        subnet_mask: "255.255.255.0"
        gateway: "192.168.1.1"
        ssid: "1"
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

    - name: Disable ipv4 connectivity for the second port on the B controller
      netapp_e_iscsi_interface:
        name: "2"
        controller: "B"
        state: disabled
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"

    - name: Enable jumbo frames for the first 4 ports on controller A
      netapp_e_iscsi_interface:
        name: "{{ item | int }}"
        controller: "A"
        state: enabled
        mtu: 9000
        config_method: dhcp
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
      loop:
        - 1
        - 2
        - 3
        - 4

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
