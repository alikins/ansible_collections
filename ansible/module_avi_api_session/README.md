# Ansible module: ansible.module_avi_api_session


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
    "data": "{'description': ['HTTP body in YAML or JSON format.']}",
    "http_method": "{'description': ['Allowed HTTP methods for RESTful services and are supported by Avi Controller.'], 'choices': ['get', 'put', 'post', 'patch', 'delete'], 'required': True}",
    "params": "{'description': ['Query parameters passed to the HTTP API.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "path": "{'description': ['Path for Avi API resource. For example, C(path: virtualservice) will translate to C(api/virtualserivce).']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "timeout": "{'description': ['Timeout (in seconds) for Avi API calls.'], 'default': 60}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
}
```

## Examples


``` yaml


  - name: Get Pool Information using avi_api_session
    avi_api_session:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      http_method: get
      path: pool
      params:
        name: "{{ pool_name }}"
      api_version: 16.4
    register: pool_results

  - name: Patch Pool with list of servers
    avi_api_session:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      http_method: patch
      path: "{{ pool_path }}"
      api_version: 16.4
      data:
        add:
          servers:
            - ip:
                addr: 10.10.10.10
                type: V4
            - ip:
                addr: 20.20.20.20
                type: V4
    register: updated_pool

  - name: Fetch Pool metrics bandwidth and connections rate
    avi_api_session:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      http_method: get
      path: analytics/metrics/pool
      api_version: 16.4
      params:
        name: "{{ pool_name }}"
        metric_id: l4_server.avg_bandwidth,l4_server.avg_complete_conns
        step: 300
        limit: 10
    register: pool_metrics


```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
