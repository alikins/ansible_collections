# Ansible module: ansible.module_avi_healthmonitor


Module for setup of HealthMonitor Avi RESTful Object

## Description

This module is used to configure HealthMonitor object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "dns_monitor": "{'description': ['Healthmonitordns settings for healthmonitor.']}",
    "external_monitor": "{'description': ['Healthmonitorexternal settings for healthmonitor.']}",
    "failed_checks": "{'description': ['Number of continuous failed health checks before the server is marked down.', 'Allowed values are 1-50.', 'Default value when not specified in API or module is interpreted by Avi Controller as 2.']}",
    "http_monitor": "{'description': ['Healthmonitorhttp settings for healthmonitor.']}",
    "https_monitor": "{'description': ['Healthmonitorhttp settings for healthmonitor.']}",
    "is_federated": "{'description': ["This field describes the object's replication scope.", 'If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.', 'If the field is set to true, then the object is replicated across the federation.', 'Field introduced in 17.1.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.4', 'type': 'bool'}",
    "monitor_port": "{'description': ['Use this port instead of the port defined for the server in the pool.', 'If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the pool.', 'Allowed values are 1-65535.', "Special values are 0 - 'use server port'."]}",
    "name": "{'description': ['A user friendly name for this health monitor.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "receive_timeout": "{'description': ['A valid response from the server is expected within the receive timeout window.', 'This timeout must be less than the send interval.', 'If server status is regularly flapping up and down, consider increasing this value.', 'Allowed values are 1-2400.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.', 'Units(SEC).']}",
    "send_interval": "{'description': ['Frequency, in seconds, that monitors are sent to a server.', 'Allowed values are 1-3600.', 'Default value when not specified in API or module is interpreted by Avi Controller as 10.', 'Units(SEC).']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "successful_checks": "{'description': ['Number of continuous successful health checks before server is marked up.', 'Allowed values are 1-50.', 'Default value when not specified in API or module is interpreted by Avi Controller as 2.']}",
    "tcp_monitor": "{'description': ['Healthmonitortcp settings for healthmonitor.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Type of the health monitor.', 'Enum options - HEALTH_MONITOR_PING, HEALTH_MONITOR_TCP, HEALTH_MONITOR_HTTP, HEALTH_MONITOR_HTTPS, HEALTH_MONITOR_EXTERNAL, HEALTH_MONITOR_UDP,', 'HEALTH_MONITOR_DNS, HEALTH_MONITOR_GSLB.'], 'required': True}",
    "udp_monitor": "{'description': ['Healthmonitorudp settings for healthmonitor.']}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the health monitor.']}",
}
```

## Examples


``` yaml

- name: Create a HTTPS health monitor
  avi_healthmonitor:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    https_monitor:
      http_request: HEAD / HTTP/1.0
      http_response_code:
        - HTTP_2XX
        - HTTP_3XX
    receive_timeout: 4
    failed_checks: 3
    send_interval: 10
    successful_checks: 3
    type: HEALTH_MONITOR_HTTPS
    name: MyWebsite-HTTPS

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
