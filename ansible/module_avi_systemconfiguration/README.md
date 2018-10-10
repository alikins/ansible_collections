# Ansible module: ansible.module_avi_systemconfiguration


Module for setup of SystemConfiguration Avi RESTful Object

## Description

This module is used to configure SystemConfiguration object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "admin_auth_configuration": "{'description': ['Adminauthconfiguration settings for systemconfiguration.']}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "default_license_tier": "{'description': ['Specifies the default license tier which would be used by new clouds.', 'Enum options - ENTERPRISE_16, ENTERPRISE_18.', 'Field introduced in 17.2.5.', 'Default value when not specified in API or module is interpreted by Avi Controller as ENTERPRISE_18.'], 'version_added': '2.5'}",
    "dns_configuration": "{'description': ['Dnsconfiguration settings for systemconfiguration.']}",
    "dns_virtualservice_refs": "{'description': ['Dns virtualservices hosting fqdn records for applications across avi vantage.', 'If no virtualservices are provided, avi vantage will provide dns services for configured applications.', 'Switching back to avi vantage from dns virtualservices is not allowed.', 'It is a reference to an object of type virtualservice.']}",
    "docker_mode": "{'description': ['Boolean flag to set docker_mode.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "email_configuration": "{'description': ['Emailconfiguration settings for systemconfiguration.']}",
    "global_tenant_config": "{'description': ['Tenantconfiguration settings for systemconfiguration.']}",
    "linux_configuration": "{'description': ['Linuxconfiguration settings for systemconfiguration.']}",
    "mgmt_ip_access_control": "{'description': ['Configure ip access control for controller to restrict open access.']}",
    "ntp_configuration": "{'description': ['Ntpconfiguration settings for systemconfiguration.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "portal_configuration": "{'description': ['Portalconfiguration settings for systemconfiguration.']}",
    "proxy_configuration": "{'description': ['Proxyconfiguration settings for systemconfiguration.']}",
    "snmp_configuration": "{'description': ['Snmpconfiguration settings for systemconfiguration.']}",
    "ssh_ciphers": "{'description': ['Allowed ciphers list for ssh to the management interface on the controller and service engines.', 'If this is not specified, all the default ciphers are allowed.', 'Ssh -q cipher provides the list of default ciphers supported.']}",
    "ssh_hmacs": "{'description': ['Allowed hmac list for ssh to the management interface on the controller and service engines.', 'If this is not specified, all the default hmacs are allowed.', 'Ssh -q mac provides the list of default hmacs supported.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
}
```

## Examples


``` yaml

- name: Example to create SystemConfiguration object
  avi_systemconfiguration:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_systemconfiguration

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
