# Ansible module: ansible.module_avi_gslb


Module for setup of Gslb Avi RESTful Object

## Description

This module is used to configure Gslb object
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
    "clear_on_max_retries": "{'description': ['Max retries after which the remote site is treated as a fresh start.', 'In fresh start all the configs are downloaded.', 'Allowed values are 1-1024.', 'Default value when not specified in API or module is interpreted by Avi Controller as 20.']}",
    "client_ip_addr_group": "{'description': ['Group to specify if the client ip addresses are public or private.', 'Field introduced in 17.1.2.'], 'version_added': '2.4'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "description": "{'description': ['User defined description for the object.']}",
    "dns_configs": "{'description': ['Sub domain configuration for the gslb.', "Gslb service's fqdn must be a match one of these subdomains."]}",
    "is_federated": "{'description': ['This field indicates that this object is replicated across gslb federation.', 'Field introduced in 17.1.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'version_added': '2.4', 'type': 'bool'}",
    "leader_cluster_uuid": "{'description': ['Mark this site as leader of gslb configuration.', 'This site is the one among the avi sites.'], 'required': True}",
    "maintenance_mode": "{'description': ['This field disables the configuration operations on the leader for all federated objects.', 'Cud operations on gslb, gslbservice, gslbgeodbprofile and other federated objects will be rejected.', "The rest-api disabling helps in upgrade scenarios where we don't want configuration sync operations to the gslb member when the member is being", 'upgraded.', 'This configuration programmatically blocks the leader from accepting new gslb configuration when member sites are undergoing upgrade.', 'Field introduced in 17.2.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.5', 'type': 'bool'}",
    "name": "{'description': ['Name for the gslb object.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "send_interval": "{'description': ['Frequency with which group members communicate.', 'Allowed values are 1-3600.', 'Default value when not specified in API or module is interpreted by Avi Controller as 15.', 'Units(SEC).']}",
    "sites": "{'description': ['Select avi site member belonging to this gslb.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "third_party_sites": "{'description': ['Third party site member belonging to this gslb.', 'Field introduced in 17.1.1.']}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the gslb object.']}",
    "view_id": "{'description': ['The view-id is used in change-leader mode to differentiate partitioned groups while they have the same gslb namespace.', 'Each partitioned group will be able to operate independently by using the view-id.', 'Default value when not specified in API or module is interpreted by Avi Controller as 0.']}",
}
```

## Examples


``` yaml

- name: Example to create Gslb object
  avi_gslb:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_gslb

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
