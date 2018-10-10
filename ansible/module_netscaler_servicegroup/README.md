# Ansible module: ansible.module_netscaler_servicegroup


Manage service group configuration in Netscaler

## Description

Manage service group configuration in Netscaler.
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

## Requirements

TODO

## Arguments

``` json
{
    "appflowlog": "{'choices': ['enabled', 'disabled'], 'description': ['Enable logging of AppFlow information for the specified service group.']}",
    "autoscale": "{'choices': ['DISABLED', 'DNS', 'POLICY'], 'description': ['Auto scale option for a servicegroup.']}",
    "cacheable": "{'description': ['Use the transparent cache redirection virtual server to forward the request to the cache server.', 'Note: Do not set this parameter if you set the Cache Type.'], 'type': 'bool'}",
    "cachetype": "{'choices': ['TRANSPARENT', 'REVERSE', 'FORWARD'], 'description': ['Cache type supported by the cache server.']}",
    "cip": "{'choices': ['enabled', 'disabled'], 'description': ['Insert the Client IP header in requests forwarded to the service.']}",
    "cipheader": "{'description': ["Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.", 'Minimum length = 1']}",
    "cka": "{'description': ['Enable client keep-alive for the service group.'], 'type': 'bool'}",
    "clttimeout": "{'description': ['Time, in seconds, after which to terminate an idle client connection.', 'Minimum value = C(0)', 'Maximum value = C(31536000)']}",
    "cmp": "{'description': ['Enable compression for the specified service.'], 'type': 'bool'}",
    "comment": "{'description': ['Any information about the service group.']}",
    "disabled": "{'description': ['When set to C(yes) the service group state will be set to DISABLED.', 'When set to C(no) the service group state will be set to ENABLED.', 'Note that due to limitations of the underlying NITRO API a C(disabled) state change alone does not cause the module result to report a changed status.'], 'type': 'bool', 'default': False}",
    "downstateflush": "{'choices': ['enabled', 'disabled'], 'description': ['Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.']}",
    "graceful": "{'description': ['Wait for all existing connections to the service to terminate before shutting down the service.'], 'type': 'bool'}",
    "healthmonitor": "{'description': ['Monitor the health of this service. Available settings function as follows:', 'C(yes) - Send probes to check the health of the service.', 'C(no) - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.'], 'type': 'bool'}",
    "httpprofilename": "{'description': ['Name of the HTTP profile that contains HTTP configuration settings for the service group.', 'Minimum length = 1', 'Maximum length = 127']}",
    "maxbandwidth": "{'description': ['Maximum bandwidth, in Kbps, allocated for all the services in the service group.', 'Minimum value = C(0)', 'Maximum value = C(4294967287)']}",
    "maxclient": "{'description': ['Maximum number of simultaneous open connections for the service group.', 'Minimum value = C(0)', 'Maximum value = C(4294967294)']}",
    "maxreq": "{'description': ['Maximum number of requests that can be sent on a persistent connection to the service group.', 'Note: Connection requests beyond this value are rejected.', 'Minimum value = C(0)', 'Maximum value = C(65535)']}",
    "memberport": "{'description': ['member port.']}",
    "monitorbindings": "{'description': ['A list of monitornames to bind to this service', 'Note that the monitors must have already been setup possibly using the M(netscaler_lb_monitor) module or some other method'], 'suboptions': {'monitorname': {'description': ['The monitor name to bind to this servicegroup.']}, 'weight': {'description': ['Weight to assign to the binding between the monitor and servicegroup.']}}}",
    "monthreshold": "{'description': ['Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.', 'Minimum value = C(0)', 'Maximum value = C(65535)']}",
    "netprofile": "{'description': ['Network profile for the service group.', 'Minimum length = 1', 'Maximum length = 127']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "pathmonitor": "{'description': ['Path monitoring for clustering.']}",
    "pathmonitorindv": "{'description': ['Individual Path monitoring decisions.']}",
    "rtspsessionidremap": "{'description': ['Enable RTSP session ID mapping for the service group.'], 'type': 'bool'}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "servicegroupname": "{'description': ['Name of the service group. Must begin with an ASCII alphabetic or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at C(@), equals C(=), and hyphen C(-) characters. Can be changed after the name is created.', 'Minimum length = 1']}",
    "servicemembers": "{'description': ['A list of dictionaries describing each service member of the service group.'], 'suboptions': {'ip': {'description': ['IP address of the service. Must not overlap with an existing server entity defined by name.']}, 'port': {'description': ['Server port number.', 'Range C(1) - C(65535)', '* in CLI is represented as 65535 in NITRO API']}, 'state': {'choices': ['enabled', 'disabled'], 'description': ['Initial state of the service after binding.']}, 'hashid': {'description': ['The hash identifier for the service.', 'This must be unique for each service.', 'This parameter is used by hash based load balancing methods.', 'Minimum value = C(1)']}, 'serverid': {'description': ['The identifier for the service.', 'This is used when the persistency type is set to Custom Server ID.']}, 'servername': {'description': ['Name of the server to which to bind the service group.', 'The server must already be configured as a named server.', 'Minimum length = 1']}, 'customserverid': {'description': ['The identifier for this IP:Port pair.', 'Used when the persistency type is set to Custom Server ID.']}, 'weight': {'description': ['Weight to assign to the servers in the service group.', 'Specifies the capacity of the servers relative to the other servers in the load balancing configuration.', 'The higher the weight, the higher the percentage of requests sent to the service.', 'Minimum value = C(1)', 'Maximum value = C(100)']}}}",
    "servicetype": "{'choices': ['HTTP', 'FTP', 'TCP', 'UDP', 'SSL', 'SSL_BRIDGE', 'SSL_TCP', 'DTLS', 'NNTP', 'RPCSVR', 'DNS', 'ADNS', 'SNMP', 'RTSP', 'DHCPRA', 'ANY', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'DNS_TCP', 'ADNS_TCP', 'MYSQL', 'MSSQL', 'ORACLE', 'RADIUS', 'RADIUSListener', 'RDP', 'DIAMETER', 'SSL_DIAMETER', 'TFTP', 'SMPP', 'PPTP', 'GRE', 'SYSLOGTCP', 'SYSLOGUDP', 'FIX', 'SSL_FIX'], 'description': ['Protocol used to exchange data with the service.']}",
    "sp": "{'description': ['Enable surge protection for the service group.'], 'type': 'bool'}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "svrtimeout": "{'description': ['Time, in seconds, after which to terminate an idle server connection.', 'Minimum value = C(0)', 'Maximum value = C(31536000)']}",
    "tcpb": "{'description': ['Enable TCP buffering for the service group.'], 'type': 'bool'}",
    "tcpprofilename": "{'description': ['Name of the TCP profile that contains TCP configuration settings for the service group.', 'Minimum length = 1', 'Maximum length = 127']}",
    "useproxyport": "{'description': ['Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.', 'Note: This parameter is available only when the Use Source IP C(usip) parameter is set to C(yes).'], 'type': 'bool'}",
    "usip": "{'description': ["Use client's IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections."]}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

# The LB Monitors monitor-1 and monitor-2 must already exist
# Service members defined by C(ip) must not redefine an existing server's ip address.
# Service members defined by C(servername) must already exist.

- name: Setup http service with ip members
  delegate_to: localhost
  netscaler_servicegroup:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    servicegroupname: service-group-1
    servicetype: HTTP
    servicemembers:
      - ip: 10.78.78.78
        port: 80
        weight: 50
      - ip: 10.79.79.79
        port: 80
        weight: 40
      - servername: server-1
        port: 80
        weight: 10

    monitorbindings:
      - monitorname: monitor-1
        weight: 50
      - monitorname: monitor-2
        weight: 50


```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
