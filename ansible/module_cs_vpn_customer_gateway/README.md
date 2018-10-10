# Ansible module: ansible.module_cs_vpn_customer_gateway


Manages site-to-site VPN customer gateway configurations on Apache CloudStack based clouds

## Description

Create, update and remove VPN customer gateways.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VPN customer gateway is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidrs": "{'description': ['List of guest CIDRs behind the gateway.', 'Required if C(state=present).'], 'aliases': ['cidr']}",
    "domain": "{'description': ['Domain the VPN customer gateway is related to.']}",
    "dpd": "{'description': ['Enable Dead Peer Detection.', 'Disabled per default by the API on creation if not set.'], 'type': 'bool'}",
    "esp_lifetime": "{'description': ['Lifetime in seconds of phase 2 VPN connection.', 'Defaulted to 3600 by the API on creation if not set.']}",
    "esp_policy": "{'description': ['ESP policy in the format e.g. C(aes256-sha1;modp1536).', 'Required if C(state=present).']}",
    "force_encap": "{'description': ['Force encapsulation for NAT traversal.', 'Disabled per default by the API on creation if not set.'], 'type': 'bool'}",
    "gateway": "{'description': ['Public IP address of the gateway.', 'Required if C(state=present).']}",
    "ike_lifetime": "{'description': ['Lifetime in seconds of phase 1 VPN connection.', 'Defaulted to 86400 by the API on creation if not set.']}",
    "ike_policy": "{'description': ['IKE policy in the format e.g. C(aes256-sha1;modp1536).', 'Required if C(state=present).']}",
    "ipsec_psk": "{'description': ['IPsec Preshared-Key.', 'Cannot contain newline or double quotes.', 'Required if C(state=present).']}",
    "name": "{'description': ['Name of the gateway.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "project": "{'description': ['Name of the project the VPN gateway is related to.']}",
    "state": "{'description': ['State of the VPN customer gateway.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Create a vpn customer gateway
  local_action:
    module: cs_vpn_customer_gateway
    name: my vpn customer gateway
    cidrs:
    - 192.168.123.0/24
    - 192.168.124.0/24
    esp_policy: aes256-sha1;modp1536
    gateway: 10.10.1.1
    ike_policy: aes256-sha1;modp1536
    ipsec_psk: "S3cr3Tk3Y"

- name: Remove a vpn customer gateway
  local_action:
    module: cs_vpn_customer_gateway
    name: my vpn customer gateway
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
