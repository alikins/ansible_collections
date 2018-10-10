# Ansible module: ansible.module_avi_scheduler


Module for setup of Scheduler Avi RESTful Object

## Description

This module is used to configure Scheduler object
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
    "backup_config_ref": "{'description': ['Backup configuration to be executed by this scheduler.', 'It is a reference to an object of type backupconfiguration.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "enabled": "{'description': ['Boolean flag to set enabled.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "end_date_time": "{'description': ['Scheduler end date and time.']}",
    "frequency": "{'description': ['Frequency at which custom scheduler will run.', 'Allowed values are 0-60.']}",
    "frequency_unit": "{'description': ['Unit at which custom scheduler will run.', 'Enum options - SCHEDULER_FREQUENCY_UNIT_MIN, SCHEDULER_FREQUENCY_UNIT_HOUR, SCHEDULER_FREQUENCY_UNIT_DAY, SCHEDULER_FREQUENCY_UNIT_WEEK,', 'SCHEDULER_FREQUENCY_UNIT_MONTH.']}",
    "name": "{'description': ['Name of scheduler.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "run_mode": "{'description': ['Scheduler run mode.', 'Enum options - RUN_MODE_PERIODIC, RUN_MODE_AT, RUN_MODE_NOW.']}",
    "run_script_ref": "{'description': ['Control script to be executed by this scheduler.', 'It is a reference to an object of type alertscriptconfig.']}",
    "scheduler_action": "{'description': ['Define scheduler action.', 'Enum options - SCHEDULER_ACTION_RUN_A_SCRIPT, SCHEDULER_ACTION_BACKUP.', 'Default value when not specified in API or module is interpreted by Avi Controller as SCHEDULER_ACTION_BACKUP.']}",
    "start_date_time": "{'description': ['Scheduler start date and time.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

- name: Example to create Scheduler object
  avi_scheduler:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_scheduler

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
