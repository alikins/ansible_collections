# Ansible module: ansible.module_rhn_register


Manage Red Hat Network registration using the ``rhnreg_ks`` command

## Description

Manage registration to the Red Hat Network.

## Requirements

TODO

## Arguments

``` json
{
    "activationkey": "{'description': ['supply an activation key for use with registration']}",
    "channels": "{'description': ['Optionally specify a list of comma-separated channels to subscribe to upon successful registration.'], 'default': []}",
    "enable_eus": "{'description': ['If C(no), extended update support will be requested.'], 'type': 'bool', 'default': False}",
    "nopackages": "{'description': ['If C(yes), the registered node will not upload its installed packages information to Satellite server'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "password": "{'description': ['Red Hat Network password']}",
    "profilename": "{'description': ['supply an profilename for use with registration'], 'version_added': '2.0'}",
    "server_url": "{'description': ['Specify an alternative Red Hat Network server URL'], 'default': 'Current value of I(serverURL) from C(/etc/sysconfig/rhn/up2date) is the default'}",
    "sslcacert": "{'description': ['supply a custom ssl CA certificate file for use with registration'], 'version_added': '2.1'}",
    "state": "{'description': ['whether to register (C(present)), or unregister (C(absent)) a system'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "systemorgid": "{'description': ['supply an organizational id for use with registration'], 'version_added': '2.1'}",
    "username": "{'description': ['Red Hat Network username']}",
}
```

## Examples


``` yaml

# Unregister system from RHN.
- rhn_register:
    state: absent
    username: joe_user
    password: somepass

# Register as user (joe_user) with password (somepass) and auto-subscribe to available content.
- rhn_register:
    state: present
    username: joe_user
    password: somepass

# Register with activationkey (1-222333444) and enable extended update support.
- rhn_register:
    state: present
    activationkey: 1-222333444
    enable_eus: true

# Register with activationkey (1-222333444) and set a profilename which may differ from the hostname.
- rhn_register:
    state: present
    activationkey: 1-222333444
    profilename: host.example.com.custom

# Register as user (joe_user) with password (somepass) against a satellite
# server specified by (server_url).
- rhn_register:
    state: present
    username: joe_user
    password: somepass'
    server_url: https://xmlrpc.my.satellite/XMLRPC

# Register as user (joe_user) with password (somepass) and enable
# channels (rhel-x86_64-server-6-foo-1) and (rhel-x86_64-server-6-bar-1).
- rhn_register:
    state: present
    username: joe_user
    password: somepass
    channels: rhel-x86_64-server-6-foo-1,rhel-x86_64-server-6-bar-1

```

## License

TODO

## Author Information
  - ['James Laska']
