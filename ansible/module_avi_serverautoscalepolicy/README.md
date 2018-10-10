# Ansible module: ansible.module_avi_serverautoscalepolicy


Module for setup of ServerAutoScalePolicy Avi RESTful Object

## Description

This module is used to configure ServerAutoScalePolicy object
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
    "intelligent_autoscale": "{'description': ['Use avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "intelligent_scalein_margin": "{'description': ['Maximum extra capacity as percentage of load used by the intelligent scheme.', 'Scalein is triggered when available capacity is more than this margin.', 'Allowed values are 1-99.', 'Default value when not specified in API or module is interpreted by Avi Controller as 40.']}",
    "intelligent_scaleout_margin": "{'description': ['Minimum extra capacity as percentage of load used by the intelligent scheme.', 'Scaleout is triggered when available capacity is less than this margin.', 'Allowed values are 1-99.', 'Default value when not specified in API or module is interpreted by Avi Controller as 20.']}",
    "max_scalein_adjustment_step": "{'description': ['Maximum number of servers to scalein simultaneously.', 'The actual number of servers to scalein is chosen such that target number of servers is always more than or equal to the min_size.', 'Default value when not specified in API or module is interpreted by Avi Controller as 1.']}",
    "max_scaleout_adjustment_step": "{'description': ['Maximum number of servers to scaleout simultaneously.', 'The actual number of servers to scaleout is chosen such that target number of servers is always less than or equal to the max_size.', 'Default value when not specified in API or module is interpreted by Avi Controller as 1.']}",
    "max_size": "{'description': ['Maximum number of servers after scaleout.', 'Allowed values are 0-400.']}",
    "min_size": "{'description': ['No scale-in happens once number of operationally up servers reach min_servers.', 'Allowed values are 0-400.']}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "scalein_alertconfig_refs": "{'description': ['Trigger scalein when alerts due to any of these alert configurations are raised.', 'It is a reference to an object of type alertconfig.']}",
    "scalein_cooldown": "{'description': ['Cooldown period during which no new scalein is triggered to allow previous scalein to successfully complete.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "scaleout_alertconfig_refs": "{'description': ['Trigger scaleout when alerts due to any of these alert configurations are raised.', 'It is a reference to an object of type alertconfig.']}",
    "scaleout_cooldown": "{'description': ['Cooldown period during which no new scaleout is triggered to allow previous scaleout to successfully complete.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "use_predicted_load": "{'description': ['Use predicted load rather than current load.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

- name: Example to create ServerAutoScalePolicy object
  avi_serverautoscalepolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_serverautoscalepolicy

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
