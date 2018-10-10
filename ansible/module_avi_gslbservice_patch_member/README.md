# Ansible module: ansible.module_avi_gslbservice_patch_member


Avi API Module

## Description

This module can be used for calling any resources defined in Avi REST API. U(https://avinetworks.com/)
This module is useful for invoking HTTP Patch methods and accessing resources that do not have an REST object associated with them.

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "data": "{'description': ['HTTP body of GSLB Service Member in YAML or JSON format.']}",
    "name": "{'description': ['Name of the GSLB Service'], 'required': True}",
    "params": "{'description': ['Query parameters passed to the HTTP API.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied to the member. Member is', 'identified using field member.ip.addr.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
}
```

## Examples


``` yaml

  - name: Patch GSLB Service to add a new member and group
    avi_gslbservice_patch_member:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      name: gs-3
      api_version: 17.2.1
      data:
        group:
          name: newfoo
          priority: 60
          members:
            - enabled: true
              ip:
                addr:  10.30.10.66
                type: V4
              ratio: 3
  - name: Patch GSLB Service to delete an existing member
    avi_gslbservice_patch_member:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      name: gs-3
      state: absent
      api_version: 17.2.1
      data:
        group:
          name: newfoo
          members:
            - enabled: true
              ip:
                addr:  10.30.10.68
                type: V4
              ratio: 3
  - name: Update priority of GSLB Service Pool
    avi_gslbservice_patch_member:
      controller: ""
      username: ""
      password: ""
      name: gs-3
      state: present
      api_version: 17.2.1
      data:
        group:
          name: newfoo
          priority: 42

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
