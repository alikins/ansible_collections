# Ansible module: ansible.module_netscaler_gslb_site


Manage gslb site entities in Netscaler

## Description

Manage gslb site entities in Netscaler.

## Requirements

TODO

## Arguments

``` json
{
    "clip": "{'description': ['Cluster IP address. Specify this parameter to connect to the remote cluster site for GSLB auto-sync. Note: The cluster IP address is defined when creating the cluster.']}",
    "metricexchange": "{'choices': ['enabled', 'disabled'], 'description': ['Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second.', 'If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.']}",
    "naptrreplacementsuffix": "{'description': ['The naptr replacement suffix configured here will be used to construct the naptr replacement field in NAPTR record.', 'Minimum length = 1']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "nwmetricexchange": "{'choices': ['enabled', 'disabled'], 'description': ['Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.']}",
    "parentsite": "{'description': ['Parent site of the GSLB site, in a parent-child topology.']}",
    "publicclip": "{'description': ['IP address to be used to globally access the remote cluster when it is deployed behind a NAT. It can be same as the normal cluster IP address.']}",
    "publicip": "{'description': ['Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.', 'Minimum length = 1']}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "sessionexchange": "{'choices': ['enabled', 'disabled'], 'description': ['Exchange persistent session entries with other GSLB sites every five seconds.']}",
    "siteipaddress": "{'description': ['IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).', 'Minimum length = 1']}",
    "sitename": "{'description': ['Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at C(@), equals C(=), and hyphen C(-) characters. Cannot be changed after the virtual server is created.', 'Minimum length = 1']}",
    "sitetype": "{'choices': ['REMOTE', 'LOCAL'], 'description': ['Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.']}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "triggermonitor": "{'choices': ['ALWAYS', 'MEPDOWN', 'MEPDOWN_SVCDOWN'], 'description': ['Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:', '* C(ALWAYS) - Monitor the GSLB service at all times.', '* C(MEPDOWN) - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.', 'C(MEPDOWN_SVCDOWN) - Monitor the service in either of the following situations:', '* The exchange of metrics through MEP is disabled.', '* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

- name: Setup gslb site
  delegate_to: localhost
  netscaler_gslb_site:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    sitename: gslb-site-1
    siteipaddress: 192.168.1.1
    sitetype: LOCAL
    publicip: 192.168.1.1
    metricexchange: enabled
    nwmetricexchange: enabled
    sessionexchange: enabled
    triggermonitor: ALWAYS


```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
