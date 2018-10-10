# Ansible module: ansible.module_aci_interface_policy_port_channel


Manage port channel interface policies (lacp:LagPol)

## Description

Manage port channel interface policies on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description for the port channel.'], 'aliases': ['descr']}",
    "fast_select": "{'description': ['Determines if Fast Select is enabled for Hot Standby Ports.', 'This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "graceful_convergence": "{'description': ['Determines if Graceful Convergence is enabled.', 'This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "load_defer": "{'description': ['Determines if Load Defer is enabled.', 'This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "max_links": "{'description': ['Maximum links.', 'Accepted values range between 1 and 16.', 'The APIC defaults to C(16) when unset during creation.'], 'type': 'int'}",
    "min_links": "{'description': ['Minimum links.', 'Accepted values range between 1 and 16.', 'The APIC defaults to C(1) when unset during creation.'], 'type': 'int'}",
    "mode": "{'description': ['Port channel interface policy mode.', 'Determines the LACP method to use for forming port-channels.', 'The APIC defaults to C(off) when unset during creation.'], 'choices': ['active', 'mac-pin', 'mac-pin-nicload', 'off', 'passive']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "port_channel": "{'description': ['Name of the port channel.'], 'required': True, 'aliases': ['name']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "suspend_individual": "{'description': ['Determines if Suspend Individual is enabled.', 'This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "symmetric_hash": "{'description': ['Determines if Symmetric Hashing is enabled.', 'This makes up the LACP Policy Control Policy; if one setting is defined, then all other Control Properties left undefined or set to false will not exist after the task is ran.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- aci_interface_policy_port_channel:
    host: '{{ inventory_hostname }}'
    username: '{{ username }}'
    password: '{{ password }}'
    port_channel: '{{ port_channel }}'
    description: '{{ description }}'
    min_links: '{{ min_links }}'
    max_links: '{{ max_links }}'
    mode: '{{ mode }}'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
