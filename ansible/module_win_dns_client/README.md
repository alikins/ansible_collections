# Ansible module: ansible.module_win_dns_client


Configures DNS lookup on Windows hosts

## Description

The C(win_dns_client) module configures the DNS client on Windows network adapters.

## Requirements

TODO

## Arguments

``` json
{
    "adapter_names": "{'description': ["Adapter name or list of adapter names for which to manage DNS settings ('*' is supported as a wildcard value). The adapter name used is the connection caption in the Network Control Panel or via C(Get-NetAdapter), eg C(Local Area Connection)."], 'required': True}",
    "ipv4_addresses": "{'description': ['Single or ordered list of DNS server IPv4 addresses to configure for lookup. An empty list will configure the adapter to use the DHCP-assigned values on connections where DHCP is enabled, or disable DNS lookup on statically-configured connections.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Set a single address on the adapter named Ethernet
  win_dns_client:
    adapter_names: Ethernet
    ipv4_addresses: 192.168.34.5

- name: Set multiple lookup addresses on all visible adapters (usually physical adapters that are in the Up state), with debug logging to a file
  win_dns_client:
    adapter_names: '*'
    ipv4_addresses:
    - 192.168.34.5
    - 192.168.34.6
    log_path: C:\dns_log.txt

- name: Configure all adapters whose names begin with Ethernet to use DHCP-assigned DNS values
  win_dns_client:
    adapter_names: 'Ethernet*'
    ipv4_addresses: []

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
