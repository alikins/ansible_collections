# Ansible module: ansible.module_avi_ipaddrgroup


Module for setup of IpAddrGroup Avi RESTful Object

## Description

This module is used to configure IpAddrGroup object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "addrs": "{'description': ['Configure ip address(es).']}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "apic_epg_name": "{'description': ['Populate ip addresses from members of this cisco apic epg.']}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "country_codes": "{'description': ['Populate the ip address ranges from the geo database for this country.']}",
    "description": "{'description': ['User defined description for the object.']}",
    "ip_ports": "{'description': ['Configure (ip address, port) tuple(s).']}",
    "marathon_app_name": "{'description': ['Populate ip addresses from tasks of this marathon app.']}",
    "marathon_service_port": "{'description': ['Task port associated with marathon service port.', 'If marathon app has multiple service ports, this is required.', 'Else, the first task port is used.']}",
    "name": "{'description': ['Name of the ip address group.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "prefixes": "{'description': ['Configure ip address prefix(es).']}",
    "ranges": "{'description': ['Configure ip address range(s).']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the ip address group.']}",
}
```

## Examples


``` yaml

  - name: Create an IP Address Group configuration
    avi_ipaddrgroup:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      name: Client-Source-Block
      prefixes:
      - ip_addr:
          addr: 10.0.0.0
          type: V4
        mask: 8
      - ip_addr:
          addr: 172.16.0.0
          type: V4
        mask: 12
      - ip_addr:
          addr: 192.168.0.0
          type: V4
        mask: 16

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
