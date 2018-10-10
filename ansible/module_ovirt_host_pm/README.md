# Ansible module: ansible.module_ovirt_host_pm


Module to manage power management of hosts in oVirt/RHV

## Description

Module to manage power management of hosts in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Address of the power management interface.']}",
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "encrypt_options": "{'description': ['If I(true) options will be encrypted when send to agent.'], 'aliases': ['encrypt']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "name": "{'description': ['Name of the host to manage.'], 'required': True, 'aliases': ['host']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "options": "{'description': ['Dictionary of additional fence agent options (including Power Management slot).', 'Additional information about options can be found at U(https://github.com/ClusterLabs/fence-agents/blob/master/doc/FenceAgentAPI.md).']}",
    "order": "{'description': ["Integer value specifying, by default it's added at the end."], 'version_added': '2.5'}",
    "password": "{'description': ['Password of the user specified in C(username) parameter.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "port": "{'description': ['Power management interface port.']}",
    "state": "{'description': ['Should the host be present/absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "type": "{'description': ['Type of the power management. oVirt/RHV predefined values are I(drac5), I(ipmilan), I(rsa), I(bladecenter), I(alom), I(apc), I(apc_snmp), I(eps), I(wti), I(rsb), I(cisco_ucs), I(drac7), I(hpblade), I(ilo), I(ilo2), I(ilo3), I(ilo4), I(ilo_ssh), but user can have defined custom type.']}",
    "username": "{'description': ['Username to be used to connect to power management interface.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add fence agent to host 'myhost'
- ovirt_host_pm:
    name: myhost
    address: 1.2.3.4
    options:
      myoption1: x
      myoption2: y
    username: admin
    password: admin
    port: 3333
    type: ipmilan

# Add fence agent to host 'myhost' using 'slot' option
- ovirt_host_pm:
    name: myhost
    address: 1.2.3.4
    options:
      myoption1: x
      myoption2: y
      slot: myslot
    username: admin
    password: admin
    port: 3333
    type: ipmilan


# Remove ipmilan fence agent with address 1.2.3.4 on host 'myhost'
- ovirt_host_pm:
    state: absent
    name: myhost
    address: 1.2.3.4
    type: ipmilan

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
