# Ansible module: ansible.module_meraki_ssid


Manage wireless SSIDs in the Meraki cloud

## Description

Allows for management of SSIDs in a Meraki wireless environment.

## Requirements

TODO

## Arguments

``` json
{
    "ap_tags_vlan_ids": "{'description': ['List of VLAN tags.'], 'suboptions': {'tags': {'description': ['List of AP tags.']}, 'vlan_id': {'description': ['Numerical identifier that is assigned to the VLAN.']}}}",
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "auth_mode": "{'description': ['Set authentication mode of network.'], 'choices': ['open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius']}",
    "band_selection": "{'description': ['Set band selection mode.'], 'choices': ['Dual band operation', '5 GHz band only', 'Dual band operation with Band Steering']}",
    "concentrator_network_id": "{'description': ["The concentrator to use for 'Layer 3 roaming with a concentrator' or 'VPN'."]}",
    "default_vlan_id": "{'description': ['Default VLAN ID.']}",
    "enabled": "{'description': ['Enable or disable SSID network.'], 'type': 'bool'}",
    "encryption_mode": "{'description': ['Set encryption mode of network.'], 'choices': ['wpa', 'eap', 'wpa-eap']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "ip_assignment_mode": "{'description': ['Method of which SSID uses to assign IP addresses.'], 'choices': ['NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a concentrator', 'VPN']}",
    "min_bitrate": "{'description': ['Minimum bitrate (Mbps) allowed on SSID.'], 'choices': [1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54]}",
    "name": "{'description': ['Name of SSID.']}",
    "net_id": "{'description': ['ID of network.']}",
    "net_name": "{'description': ['Name of network.']}",
    "number": "{'description': ['SSID number within network.'], 'aliases': ['ssid_number']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "per_client_bandwidth_limit_down": "{'description': ['Maximum bandwidth in Mbps devices on SSID can download.']}",
    "per_client_bandwidth_limit_up": "{'description': ['Maximum bandwidth in Mbps devices on SSID can upload.']}",
    "psk": "{'description': ['Password for wireless network.', 'Requires auth_mode to be set to psk.']}",
    "radius_accounting_enabled": "{'description': ['Enable or disable RADIUS accounting.'], 'type': 'bool'}",
    "radius_accounting_servers": "{'description': ['List of RADIUS servers for RADIUS accounting.'], 'suboptions': {'host': {'description': ['IP addres or hostname of RADIUS server.']}, 'port': {'description': ['Port number RADIUS server is listening to.']}, 'secret': {'description': ['RADIUS password.']}}}",
    "radius_coa_enabled": "{'description': ['Enable or disable RADIUS CoA (Change of Authorization) on SSID.'], 'type': 'bool'}",
    "radius_failover_policy": "{'description': ["Set client access policy in case RADIUS servers aren't available."], 'choices': ['Deny access', 'Allow access']}",
    "radius_load_balancing_policy": "{'description': ['Set load balancing policy when multiple RADIUS servers are specified.'], 'choices': ['Strict priority order', 'Round robin']}",
    "radius_servers": "{'description': ['List of RADIUS servers.'], 'suboptions': {'host': {'description': ['IP addres or hostname of RADIUS server.']}, 'port': {'description': ['Port number RADIUS server is listening to.']}, 'secret': {'description': ['RADIUS password.']}}}",
    "splash_page": "{'description': ['Set to enable splash page and specify type of splash.'], 'choices': ['None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest']}",
    "state": "{'description': ['Specifies whether SNMP information should be queried or modified.'], 'choices': ['absent', 'query', 'present'], 'default': 'present'}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "use_vlan_tagging": "{'description': ['Set whether to use VLAN tagging.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
    "vlan_id": "{'description': ['ID number of VLAN on SSID.']}",
    "walled_garden_enabled": "{'description': ['Enable or disable walled garden functionality.'], 'type': 'bool'}",
    "walled_garden_ranges": "{'description': ['List of walled garden ranges.']}",
    "wpa_encryption_mode": "{'description': ['Encryption mode within WPA2 specification.'], 'choices': ['WPA1 and WPA2', 'WPA2 only']}",
}
```

## Examples


``` yaml


```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
