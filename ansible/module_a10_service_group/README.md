# Ansible module: ansible.module_a10_service_group


Manage A10 Networks AX/SoftAX/Thunder/vThunder devices' service groups

## Description

Manage SLB (Server Load Balancing) service-group objects on A10 Networks devices via aXAPIv2.

## Requirements

TODO

## Arguments

``` json
{
    "client_cert": "{'description': ['PEM formatted certificate chain file to be used for SSL client authentication. This file can also include the key as well, and if the key is included, C(client_key) is not required.']}",
    "client_key": "{'description': ['PEM formatted file that contains your private key to be used for SSL client authentication. If C(client_cert) contains both the certificate and key, this option is not required.']}",
    "force": "{'description': ['If C(yes) do not get a cached copy.'], 'aliases': ['thirsty'], 'type': 'bool', 'default': False}",
    "force_basic_auth": "{'description': ['Credentials specified with I(url_username) and I(url_password) should be passed in HTTP Header.'], 'default': False, 'type': 'bool'}",
    "host": "{'description': ['Hostname or IP of the A10 Networks device.'], 'required': True}",
    "http_agent": "{'description': ['Header to identify as, generally appears in web server logs.'], 'default': 'ansible-httpget'}",
    "partition": "{'version_added': '2.3', 'description': ['set active-partition']}",
    "password": "{'description': ['Password for the C(username) account.'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "servers": "{'description': ['A list of servers to add to the service group. Each list item should be a dictionary which specifies the C(server:) and C(port:), but can also optionally specify the C(status:). See the examples below for details.'], 'aliases': ['server', 'member']}",
    "service_group": "{'description': ['The SLB (Server Load Balancing) service-group name'], 'required': True, 'aliases': ['service', 'pool', 'group']}",
    "service_group_method": "{'description': ['The SLB service-group load balancing method, such as round-robin or weighted-rr.'], 'default': 'round-robin', 'aliases': ['method'], 'choices': ['round-robin', 'weighted-rr', 'least-connection', 'weighted-least-connection', 'service-least-connection', 'service-weighted-least-connection', 'fastest-response', 'least-request', 'round-robin-strict', 'src-ip-only-hash', 'src-ip-hash']}",
    "service_group_protocol": "{'description': ['The SLB service-group protocol of TCP or UDP.'], 'default': 'tcp', 'aliases': ['proto', 'protocol'], 'choices': ['tcp', 'udp']}",
    "state": "{'description': ['If the specified service group should exists.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "url": "{'description': ['HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path']}",
    "url_password": "{'description': ['The password for use in HTTP basic authentication.', 'If the I(url_username) parameter is not specified, the I(url_password) parameter will not be used.']}",
    "url_username": "{'description': ['The username for use in HTTP basic authentication.', 'This parameter can be used without I(url_password) for sites that allow empty passwords']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['An account with administrator privileges.'], 'required': True, 'aliases': ['user', 'admin']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.'], 'default': True, 'type': 'bool', 'version_added': 2.2}",
    "write_config": "{'description': ['If C(yes), any changes will cause a write of the running configuration to non-volatile memory. This will save I(all) configuration changes, including those that may have been made manually or through other modules, so care should be taken when specifying C(yes).'], 'version_added': 2.2, 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Create a new service-group
- a10_service_group:
    host: a10.mydomain.com
    username: myadmin
    password: mypassword
    partition: mypartition
    service_group: sg-80-tcp
    servers:
      - server: foo1.mydomain.com
        port: 8080
      - server: foo2.mydomain.com
        port: 8080
      - server: foo3.mydomain.com
        port: 8080
      - server: foo4.mydomain.com
        port: 8080
        status: disabled


```

## License

TODO

## Author Information
  - ['Eric Chou (@ericchou) 2016, Mischa Peters (@mischapeters) 2014']
