# Ansible module: ansible.module_avi_gslbhealthmonitor


Module for setup of GslbHealthMonitor Avi RESTful Object

## Description

This module is used to configure GslbHealthMonitor object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "dns_monitor": "{'description': ['Healthmonitordns settings for gslbhealthmonitor.']}",
    "external_monitor": "{'description': ['Healthmonitorexternal settings for gslbhealthmonitor.']}",
    "failed_checks": "{'description': ['Number of continuous failed health checks before the server is marked down.', 'Allowed values are 1-50.', 'Default value when not specified in API or module is interpreted by Avi Controller as 2.']}",
    "http_monitor": "{'description': ['Healthmonitorhttp settings for gslbhealthmonitor.']}",
    "https_monitor": "{'description': ['Healthmonitorhttp settings for gslbhealthmonitor.']}",
    "monitor_port": "{'description': ['Use this port instead of the port defined for the server in the pool.', 'If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the pool.', 'Allowed values are 1-65535.', "Special values are 0 - 'use server port'."]}",
    "name": "{'description': ['A user friendly name for this health monitor.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "receive_timeout": "{'description': ['A valid response from the server is expected within the receive timeout window.', 'This timeout must be less than the send interval.', 'If server status is regularly flapping up and down, consider increasing this value.', 'Allowed values are 1-300.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.']}",
    "send_interval": "{'description': ['Frequency, in seconds, that monitors are sent to a server.', 'Allowed values are 1-3600.', 'Default value when not specified in API or module is interpreted by Avi Controller as 5.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "successful_checks": "{'description': ['Number of continuous successful health checks before server is marked up.', 'Allowed values are 1-50.', 'Default value when not specified in API or module is interpreted by Avi Controller as 2.']}",
    "tcp_monitor": "{'description': ['Healthmonitortcp settings for gslbhealthmonitor.']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Type of the health monitor.', 'Enum options - HEALTH_MONITOR_PING, HEALTH_MONITOR_TCP, HEALTH_MONITOR_HTTP, HEALTH_MONITOR_HTTPS, HEALTH_MONITOR_EXTERNAL, HEALTH_MONITOR_UDP,', 'HEALTH_MONITOR_DNS, HEALTH_MONITOR_GSLB.'], 'required': True}",
    "udp_monitor": "{'description': ['Healthmonitorudp settings for gslbhealthmonitor.']}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the health monitor.']}",
}
```

## Examples


``` yaml

- name: Example to create GslbHealthMonitor object
  avi_gslbhealthmonitor:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_gslbhealthmonitor

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
