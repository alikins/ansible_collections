# Ansible module: ansible.module_avi_autoscalelaunchconfig


Module for setup of AutoScaleLaunchConfig Avi RESTful Object

## Description

This module is used to configure AutoScaleLaunchConfig object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "image_id": "{'description': ['Unique id of the amazon machine image (ami)  or openstack vm id.']}",
    "mesos": "{'description': ['Autoscalemesossettings settings for autoscalelaunchconfig.']}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "openstack": "{'description': ['Autoscaleopenstacksettings settings for autoscalelaunchconfig.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "use_external_asg": "{'description': ['If set to true, serverautoscalepolicy will use the autoscaling group (external_autoscaling_groups) from pool to perform scale up and scale down.', 'Pool should have single autoscaling group configured.', 'Field introduced in 17.2.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

  - name: Create an Autoscale Launch configuration.
    avi_autoscalelaunchconfig:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      image_id: default
      name: default-autoscalelaunchconfig
      tenant_ref: admin

```

## License

TODO

## Author Information
  - ['Chaitanya Deshpande (chaitanya.deshpande@avinetworks.com)']
