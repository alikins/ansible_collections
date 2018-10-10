# Ansible module: ansible.module_avi_backupconfiguration


Module for setup of BackupConfiguration Avi RESTful Object

## Description

This module is used to configure BackupConfiguration object
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
    "backup_file_prefix": "{'description': ['Prefix of the exported configuration file.', 'Field introduced in 17.1.1.']}",
    "backup_passphrase": "{'description': ['Passphrase of backup configuration.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "maximum_backups_stored": "{'description': ['Rotate the backup files based on this count.', 'Allowed values are 1-20.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.']}",
    "name": "{'description': ['Name of backup configuration.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "remote_directory": "{'description': ['Directory at remote destination with write permission for ssh user.']}",
    "remote_hostname": "{'description': ['Remote destination.']}",
    "save_local": "{'description': ['Local backup.'], 'type': 'bool'}",
    "ssh_user_ref": "{'description': ['Access credentials for remote destination.', 'It is a reference to an object of type cloudconnectoruser.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "upload_to_remote_host": "{'description': ['Remote backup.'], 'type': 'bool'}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

- name: Example to create BackupConfiguration object
  avi_backupconfiguration:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_backupconfiguration

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
