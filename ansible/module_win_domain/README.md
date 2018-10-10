# Ansible module: ansible.module_win_domain


Ensures the existence of a Windows domain

## Description

Ensure that the domain named by C(dns_domain_name) exists and is reachable.
If the domain is not reachable, the domain is created in a new forest on the target Windows Server 2012R2+ host.
This module may require subsequent use of the M(win_reboot) action if changes are made.

## Requirements

TODO

## Arguments

``` json
{
    "database_path": "{'description': ['The path to a directory on a fixed disk of the Windows host where the domain database will be created.', 'If not set then the default path is C(%SYSTEMROOT%\\NTDS).'], 'type': 'path', 'version_added': '2.5'}",
    "dns_domain_name": "{'description': ['The DNS name of the domain which should exist and be reachable or reside on the target Windows host.'], 'required': True}",
    "domain_netbios_name": "{'description': ['The netbios name of the domain.', 'If not set, then the default netbios name will be the first section of dns_domain_name, up to, but not including the first period.'], 'version_added': '2.6'}",
    "safe_mode_password": "{'description': ['Safe mode password for the domain controller.'], 'required': True}",
    "sysvol_path": "{'description': ['The path to a directory on a fixed disk of the Windows host where the Sysvol file will be created.', 'If not set then the default path is C(%SYSTEMROOT%\\SYSVOL).'], 'type': 'path', 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Ensure the named domain is reachable from the target host; if not, create the domain in a new forest residing on the target host
  win_domain:
    dns_domain_name: ansible.vagrant
    safe_mode_password: password123!

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
