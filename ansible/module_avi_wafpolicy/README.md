# Ansible module: ansible.module_avi_wafpolicy


Module for setup of WafPolicy Avi RESTful Object

## Description

This module is used to configure WafPolicy object
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
    "created_by": "{'description': ['Creator name.', 'Field introduced in 17.2.4.']}",
    "crs_groups": "{'description': ['Waf rules are categorized in to groups based on their characterization.', 'These groups are system created with crs groups.', 'Field introduced in 17.2.1.']}",
    "description": "{'description': ['Field introduced in 17.2.1.']}",
    "mode": "{'description': ['Waf policy mode.', 'This can be detection or enforcement.', 'Enum options - WAF_MODE_DETECTION_ONLY, WAF_MODE_ENFORCEMENT.', 'Field introduced in 17.2.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as WAF_MODE_DETECTION_ONLY.'], 'required': True}",
    "name": "{'description': ['Field introduced in 17.2.1.'], 'required': True}",
    "paranoia_level": "{'description': ['Waf ruleset paranoia  mode.', 'This is used to select rules based on the paranoia-level tag.', 'Enum options - WAF_PARANOIA_LEVEL_LOW, WAF_PARANOIA_LEVEL_MEDIUM, WAF_PARANOIA_LEVEL_HIGH, WAF_PARANOIA_LEVEL_EXTREME.', 'Field introduced in 17.2.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as WAF_PARANOIA_LEVEL_LOW.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "post_crs_groups": "{'description': ['Waf rules are categorized in to groups based on their characterization.', 'These groups are created by the user and will be enforced after the crs groups.', 'Field introduced in 17.2.1.']}",
    "pre_crs_groups": "{'description': ['Waf rules are categorized in to groups based on their characterization.', 'These groups are created by the user and will be  enforced before the crs groups.', 'Field introduced in 17.2.1.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.', 'Field introduced in 17.2.1.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Field introduced in 17.2.1.']}",
    "waf_profile_ref": "{'description': ['Waf profile for waf policy.', 'It is a reference to an object of type wafprofile.', 'Field introduced in 17.2.1.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Example to create WafPolicy object
  avi_wafpolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_wafpolicy

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
