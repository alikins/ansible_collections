# Ansible module: ansible.module_netscaler_gslb_service


Manage gslb service entities in Netscaler

## Description

Manage gslb service entities in Netscaler.

## Requirements

TODO

## Arguments

``` json
{
    "appflowlog": "{'choices': ['enabled', 'disabled'], 'description': ['Enable logging appflow flow information.']}",
    "cip": "{'choices': ['enabled', 'disabled'], 'description': ["In the request that is forwarded to the GSLB service, insert a header that stores the client's IP address. Client IP header insertion is used in connection-proxy based site persistence."]}",
    "cipheader": "{'description': ["Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.", 'Minimum length = 1']}",
    "clttimeout": "{'description': ['Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.', 'Minimum value = 0', 'Maximum value = 31536000']}",
    "cnameentry": "{'description': ['Canonical name of the GSLB service. Used in CNAME-based GSLB.', 'Minimum length = 1']}",
    "comment": "{'description': ['Any comments that you might want to associate with the GSLB service.']}",
    "downstateflush": "{'choices': ['enabled', 'disabled'], 'description': ['Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.']}",
    "hashid": "{'description': ['Unique hash identifier for the GSLB service, used by hash based load balancing methods.', 'Minimum value = C(1)']}",
    "healthmonitor": "{'description': ['Monitor the health of the GSLB service.'], 'type': 'bool'}",
    "ipaddress": "{'description': ['IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device.']}",
    "maxaaausers": "{'description': ['Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.', 'Minimum value = C(0)', 'Maximum value = C(65535)']}",
    "maxbandwidth": "{'description': ['Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum.']}",
    "maxclient": "{'description': ['The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.', 'Minimum value = C(0)', 'Maximum value = C(4294967294)']}",
    "monitor_bindings": "{'description': ['Bind monitors to this gslb service'], 'suboptions': {'weight': {'description': ['Weight to assign to the monitor-service binding.', 'A larger number specifies a greater weight.', 'Contributes to the monitoring threshold, which determines the state of the service.', 'Minimum value = C(1)', 'Maximum value = C(100)']}, 'monitor_name': {'description': ['Monitor name.']}}}",
    "monthreshold": "{'description': ['Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.', 'Minimum value = C(0)', 'Maximum value = C(65535)']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "port": "{'description': ['Port on which the load balancing entity represented by this GSLB service listens.', 'Minimum value = 1', 'Range 1 - 65535', '* in CLI is represented as 65535 in NITRO API']}",
    "publicip": "{'description': ["The public IP address that a NAT device translates to the GSLB service's private IP address. Optional."]}",
    "publicport": "{'description': ["The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional."]}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "servername": "{'description': ['Name of the server hosting the GSLB service.', 'Minimum length = 1']}",
    "servicename": "{'description': ['Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space, colon C(:), at C(@), equals C(=), and hyphen C(-) characters. Can be changed after the GSLB service is created.', '', 'Minimum length = 1']}",
    "servicetype": "{'choices': ['HTTP', 'FTP', 'TCP', 'UDP', 'SSL', 'SSL_BRIDGE', 'SSL_TCP', 'NNTP', 'ANY', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'RADIUS', 'RDP', 'RTSP', 'MYSQL', 'MSSQL', 'ORACLE'], 'description': ['Type of service to create.']}",
    "sitename": "{'description': ['Name of the GSLB site to which the service belongs.', 'Minimum length = 1']}",
    "sitepersistence": "{'choices': ['ConnectionProxy', 'HTTPRedirect', 'NONE'], 'description': ['Use cookie-based site persistence. Applicable only to C(HTTP) and C(SSL) GSLB services.']}",
    "siteprefix": "{'description': ["The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains."]}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

- name: Setup gslb service 2

  delegate_to: localhost
  register: result
  check_mode: "{{ check_mode }}"

  netscaler_gslb_service:
    operation: present

    servicename: gslb-service-2
    cnameentry: example.com
    sitename: gslb-site-1

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
