# Ansible module: ansible.module_netscaler_service


Manage service configuration in Netscaler

## Description

Manage service configuration in Netscaler.
This module allows the creation, deletion and modification of Netscaler services.
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.
This module supports check mode.

## Requirements

TODO

## Arguments

``` json
{
    "accessdown": "{'description': ['Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.'], 'default': False}",
    "appflowlog": "{'choices': ['enabled', 'disabled'], 'description': ['Enable logging of AppFlow information.']}",
    "cacheable": "{'description': ['Use the transparent cache redirection virtual server to forward requests to the cache server.', 'Note: Do not specify this parameter if you set the Cache Type parameter.'], 'default': False}",
    "cachetype": "{'choices': ['TRANSPARENT', 'REVERSE', 'FORWARD'], 'description': ['Cache type supported by the cache server.']}",
    "cip": "{'choices': ['enabled', 'disabled'], 'description': ["Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option."]}",
    "cipheader": "{'description': ['Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".', 'Minimum length = 1']}",
    "cka": "{'description': ['Enable client keep-alive for the service.']}",
    "cleartextport": "{'description': ['Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.', 'Minimum value = 1']}",
    "clttimeout": "{'description': ['Time, in seconds, after which to terminate an idle client connection.', 'Minimum value = 0', 'Maximum value = 31536000']}",
    "cmp": "{'description': ['Enable compression for the service.']}",
    "comment": "{'description': ['Any information about the service.']}",
    "customserverid": "{'description': ['Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.'], 'default': 'None'}",
    "disabled": "{'description': ['When set to C(yes) the service state will be set to DISABLED.', 'When set to C(no) the service state will be set to ENABLED.', 'Note that due to limitations of the underlying NITRO API a C(disabled) state change alone does not cause the module result to report a changed status.'], 'type': 'bool', 'default': False}",
    "dnsprofilename": "{'description': ['Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.', 'Minimum length = 1', 'Maximum length = 127']}",
    "downstateflush": "{'choices': ['enabled', 'disabled'], 'description': ['Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.']}",
    "graceful": "{'description': ['Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.'], 'default': False}",
    "hashid": "{'description': ['A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.', 'Minimum value = 1']}",
    "healthmonitor": "{'description': ['Monitor the health of this service'], 'default': True}",
    "httpprofilename": "{'description': ['Name of the HTTP profile that contains HTTP configuration settings for the service.', 'Minimum length = 1', 'Maximum length = 127']}",
    "ip": "{'description': ['IP to assign to the service.', 'Minimum length = 1']}",
    "ipaddress": "{'description': ['The new IP address of the service.']}",
    "maxbandwidth": "{'description': ['Maximum bandwidth, in Kbps, allocated to the service.', 'Minimum value = 0', 'Maximum value = 4294967287']}",
    "maxclient": "{'description': ['Maximum number of simultaneous open connections to the service.', 'Minimum value = 0', 'Maximum value = 4294967294']}",
    "maxreq": "{'description': ['Maximum number of requests that can be sent on a persistent connection to the service.', 'Note: Connection requests beyond this value are rejected.', 'Minimum value = 0', 'Maximum value = 65535']}",
    "monitor_bindings": "{'description': ['A list of load balancing monitors to bind to this service.', 'Each monitor entry is a dictionary which may contain the following options.', 'Note that if not using the built in monitors they must first be setup.'], 'suboptions': {'monitorname': {'description': ['Name of the monitor.']}, 'weight': {'description': ['Weight to assign to the binding between the monitor and service.']}, 'dup_state': {'choices': ['enabled', 'disabled'], 'description': ['State of the monitor.', 'The state setting for a monitor of a given type affects all monitors of that type.', 'For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled.', 'If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.']}, 'dup_weight': {'description': ['Weight to assign to the binding between the monitor and service.']}}}",
    "monthreshold": "{'description': ['Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.', 'Minimum value = 0', 'Maximum value = 65535']}",
    "name": "{'description': ['Name for the service. Must begin with an ASCII alphabetic or underscore C(_) character, and must contain only ASCII alphanumeric, underscore C(_), hash C(#), period C(.), space C( ), colon C(:), at C(@), equals C(=), and hyphen C(-) characters. Cannot be changed after the service has been created.', 'Minimum length = 1']}",
    "netprofile": "{'description': ['Network profile to use for the service.', 'Minimum length = 1', 'Maximum length = 127']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. 192.168.1.1:555.'], 'required': True}",
    "pathmonitor": "{'description': ['Path monitoring for clustering.']}",
    "pathmonitorindv": "{'description': ['Individual Path monitoring decisions.']}",
    "port": "{'description': ['Port number of the service.', 'Range 1 - 65535', '* in CLI is represented as 65535 in NITRO API']}",
    "processlocal": "{'choices': ['enabled', 'disabled'], 'description': ['By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.']}",
    "rtspsessionidremap": "{'description': ['Enable RTSP session ID mapping for the service.'], 'default': False}",
    "save_config": "{'description': ['If true the module will save the configuration on the netscaler node if it makes any changes.', 'The module will not save the configuration on the netscaler node if it made no changes.'], 'type': 'bool', 'default': True}",
    "serverid": "{'description': ['The identifier for the service. This is used when the persistency type is set to Custom Server ID.']}",
    "servername": "{'description': ['Name of the server that hosts the service.', 'Minimum length = 1']}",
    "servicetype": "{'choices': ['HTTP', 'FTP', 'TCP', 'UDP', 'SSL', 'SSL_BRIDGE', 'SSL_TCP', 'DTLS', 'NNTP', 'RPCSVR', 'DNS', 'ADNS', 'SNMP', 'RTSP', 'DHCPRA', 'ANY', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'DNS_TCP', 'ADNS_TCP', 'MYSQL', 'MSSQL', 'ORACLE', 'RADIUS', 'RADIUSListener', 'RDP', 'DIAMETER', 'SSL_DIAMETER', 'TFTP', 'SMPP', 'PPTP', 'GRE', 'SYSLOGTCP', 'SYSLOGUDP', 'FIX', 'SSL_FIX'], 'description': ['Protocol in which data is exchanged with the service.']}",
    "sp": "{'description': ['Enable surge protection for the service.']}",
    "state": "{'choices': ['present', 'absent'], 'default': 'present', 'description': ['The state of the resource being configured by the module on the netscaler node.', "When present the resource will be created if needed and configured according to the module's parameters.", 'When absent the resource will be deleted from the netscaler node.']}",
    "svrtimeout": "{'description': ['Time, in seconds, after which to terminate an idle server connection.', 'Minimum value = 0', 'Maximum value = 31536000']}",
    "tcpb": "{'description': ['Enable TCP buffering for the service.']}",
    "tcpprofilename": "{'description': ['Name of the TCP profile that contains TCP configuration settings for the service.', 'Minimum length = 1', 'Maximum length = 127']}",
    "td": "{'description': ['Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.', 'Minimum value = 0', 'Maximum value = 4094']}",
    "useproxyport": "{'description': ['Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.', 'Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.']}",
    "usip": "{'description': ["Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service."]}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

# Monitor monitor-1 must have been already setup

- name: Setup http service
  gather_facts: False
  delegate_to: localhost
  netscaler_service:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    name: service-http-1
    servicetype: HTTP
    ipaddress: 10.78.0.1
    port: 80

    monitor_bindings:
      - monitor-1

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
