# Ansible module: ansible.module_netapp_e_mgmt_interface


NetApp E-Series management interface configuration

## Description

Configure the E-Series management interfaces

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The IPv4 address to assign to the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)'], 'required': False}",
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "channel": "{'description': ['The port to modify the configuration for.', 'The channel represents the port number (typically from left to right on the controller), beginning with a value of 1.', 'Mutually exclusive with I(name).']}",
    "config_method": "{'description': ['The configuration method type to use for network interface ports.', 'dhcp is mutually exclusive with I(address), I(subnet_mask), and I(gateway).'], 'choices': ['dhcp', 'static'], 'required': False}",
    "controller": "{'description': ['The controller that owns the port you want to configure.', 'Controller names are represented alphabetically, with the first controller as A, the second as B, and so on.', 'Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.'], 'required': True, 'choices': ['A', 'B']}",
    "dns_address": "{'description': ['Primary IPv4 DNS server address'], 'required': False}",
    "dns_address_backup": "{'description': ['Backup IPv4 DNS server address', 'Queried when primary DNS server fails'], 'required': False}",
    "dns_config_method": "{'description': ['The configuration method type to use for DNS services.', 'dhcp is mutually exclusive with I(dns_address), and I(dns_address_backup).'], 'choices': ['dhcp', 'static'], 'required': False}",
    "gateway": "{'description': ['The IPv4 gateway address to utilize for the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)'], 'required': False}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False}",
    "name": "{'description': ['The port to modify the configuration for.', 'The list of choices is not necessarily comprehensive. It depends on the number of ports that are present in the system.', 'The name represents the port number (typically from left to right on the controller), beginning with a value of 1.', 'Mutually exclusive with I(channel).'], 'aliases': ['port', 'iface']}",
    "ntp_address": "{'description': ['Primary IPv4 NTP server address'], 'required': False}",
    "ntp_address_backup": "{'description': ['Backup IPv4 NTP server address', 'Queried when primary NTP server fails'], 'required': False}",
    "ntp_config_method": "{'description': ['The configuration method type to use for NTP services.', 'disable is mutually exclusive with I(ntp_address) and I(ntp_address_backup).', 'dhcp is mutually exclusive with I(ntp_address) and I(ntp_address_backup).'], 'choices': ['disable', 'dhcp', 'static'], 'required': False}",
    "ssh": "{'type': 'bool', 'description': ['Enable ssh access to the controller for debug purposes.', 'This is a controller-level setting.', 'rlogin/telnet will be enabled for ancient equipment where ssh is not available.'], 'required': False}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Enable or disable IPv4 network interface configuration.', 'Either IPv4 or IPv6 must be enabled otherwise error will occur.', 'Only required when enabling or disabling IPv4 network interface'], 'choices': ['enable', 'disable'], 'required': False, 'aliases': ['enable_interface']}",
    "subnet_mask": "{'description': ['The subnet mask to utilize for the interface.', 'Should be specified in xx.xx.xx.xx form.', 'Mutually exclusive with I(config_method=dhcp)'], 'required': False}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Configure the first port on the A controller with a static IPv4 address
      netapp_e_mgmt_interface:
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
      netapp_e_mgmt_interface:
        name: "2"
        controller: "B"
        enable_interface: no
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"

    - name: Enable ssh access for ports one and two on controller A
      netapp_e_mgmt_interface:
        name: "{{ item }}"
        controller: "A"
        ssh: yes
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
      loop:
        - 1
        - 2

    - name: Configure static DNS settings for the first port on controller A
      netapp_e_mgmt_interface:
        name: "1"
        controller: "A"
        dns_config_method: static
        dns_address: "192.168.1.100"
        dns_address_backup: "192.168.1.1"
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"

    - name: Configure static NTP settings for ports one and two on controller B
      netapp_e_mgmt_interface:
        name: "{{ item }}"
        controller: "B"
        ntp_config_method: static
        ntp_address: "129.100.1.100"
        ntp_address_backup: "127.100.1.1"
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
      loop:
        - 1
        - 2

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)', 'Nathan Swartz (@ndswartz)']
  - ['Michael Price (@lmprice)', 'Nathan Swartz (@ndswartz)']
