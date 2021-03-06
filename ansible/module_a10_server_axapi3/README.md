# Ansible module: ansible.module_a10_server_axapi3


Manage A10 Networks AX/SoftAX/Thunder/vThunder devices

## Description

Manage SLB (Server Load Balancer) server objects on A10 Networks devices via aXAPIv3.

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
    "operation": "{'description': ['Create, Update or Remove SLB server. For create and update operation, we use the IP address and server name specified in the POST message. For delete operation, we use the server name in the request URI.'], 'default': 'create', 'choices': ['create', 'update', 'remove']}",
    "password": "{'description': ['Password for the C(username) account.'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "server_ip": "{'description': ['The SLB (Server Load Balancer) server IPv4 address.'], 'required': True, 'aliases': ['ip', 'address']}",
    "server_name": "{'description': ['The SLB (Server Load Balancer) server name.'], 'required': True, 'aliases': ['server']}",
    "server_ports": "{'description': ['A list of ports to create for the server. Each list item should be a dictionary which specifies the C(port:) and C(protocol:).'], 'aliases': ['port']}",
    "server_status": "{'description': ['The SLB (Server Load Balancer) virtual server status.'], 'default': 'enable', 'aliases': ['action'], 'choices': ['enable', 'disable']}",
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

# Create a new server
- a10_server:
    host: a10.mydomain.com
    username: myadmin
    password: mypassword
    server: test
    server_ip: 1.1.1.100
    validate_certs: false
    server_status: enable
    write_config: yes
    operation: create
    server_ports:
      - port-number: 8080
        protocol: tcp
        action: enable
      - port-number: 8443
        protocol: TCP


```

## License

TODO

## Author Information
  - ['Eric Chou (@ericchou) based on previous work by Mischa Peters (@mischapeters)']
