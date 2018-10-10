# Ansible module: ansible.module_cpm_user


Get various status and parameters from WTI OOB and PDU devices

## Description

Get/Add/Edit Delete Users from WTI OOB and PDU devices

## Requirements

TODO

## Arguments

``` json
{
    "cpm_action": "{'description': ['This is the Action to send the module.'], 'required': True, 'choices': ['getuser', 'adduser', 'edituser', 'deleteuser']}",
    "cpm_password": "{'description': ['This is the Basic Authentication Password of the WTI device to send the module.'], 'required': True}",
    "cpm_url": "{'description': ['This is the URL of the WTI device to send the module.'], 'required': True}",
    "cpm_username": "{'description': ['This is the Basic Authentication Username of the WTI device to send the module.'], 'required': True}",
    "use_https": "{'description': ['Designates to use an https connection or http connection.'], 'required': False, 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['Flag to control if the lookup will observe HTTP proxy environment variables when present.'], 'required': False, 'type': 'bool', 'default': False}",
    "user_accessapi": "{'description': ['If the user has access to the WTI device via RESTful APIs', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_accesslevel": "{'description': ['This is the access level that needs to be create/modified/deleted', '0 View, 1 User, 2 SuperUser, 3 Adminstrator'], 'required': False, 'choices': [0, 1, 2, 3]}",
    "user_accessmonitor": "{'description': ['If the user has ability to monitor connection sessions', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_accessoutbound": "{'description': ['If the user has ability to initiate Outbound connection', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_accessserial": "{'description': ['If the user has access to the WTI device via Serial ports', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_accessssh": "{'description': ['If the user has access to the WTI device via SSH', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_accessweb": "{'description': ['If the user has access to the WTI device via Web', '0 No , 1 Yes'], 'required': False, 'choices': [0, 1]}",
    "user_callbackphone": "{'description': ['This is the Call Back phone number used for POTS modem connections'], 'required': False}",
    "user_groupaccess": "{'description': ['If AccessLevel is lower than Administrator, which Groups the user has access'], 'required': False}",
    "user_name": "{'description': ['This is the User Name that needs to be create/modified/deleted'], 'required': True}",
    "user_pass": "{'description': ['This is the User Password that needs to be create/modified/deleted', 'If the user is being Created this parameter is required'], 'required': False}",
    "user_plugaccess": "{'description': ['If AccessLevel is lower than Administrator, which plugs the user has access'], 'required': False}",
    "user_portaccess": "{'description': ['If AccessLevel is lower than Administrator, which ports the user has access'], 'required': False}",
    "validate_certs": "{'description': ['If false, SSL certificates will not be validated. This should only be used', 'on personally controlled sites using self-signed certificates.'], 'required': False, 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Get User Parameters
- name: Get the User Parameters for the given user of a WTI device
  cpm_user:
    cpm_action: "getuser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: true
    user_name: "usernumberone"

# Create User
- name: Create a User on a given WTI device
  cpm_user:
    cpm_action: "adduser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: false
    user_name: "usernumberone"
    user_pass: "complicatedpassword"
    user_accesslevel: 2
    user_accessssh: 1
    user_accessserial: 1
    user_accessweb: 0
    user_accessapi: 1
    user_accessmonitor: 0
    user_accessoutbound: 0
    user_portaccess: "10011111"
    user_plugaccess: "00000111"
    user_groupaccess: "00000000"

# Edit User
- name: Edit a User on a given WTI device
  cpm_user:
    cpm_action: "edituser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: false
    user_name: "usernumberone"
    user_pass: "newpasswordcomplicatedpassword"

# Delete User
- name: Delete a User from a given WTI device
  cpm_user:
    cpm_action: "deleteuser"
    cpm_url: "rest.wti.com"
    cpm_username: "restuser"
    cpm_password: "restfuluserpass12"
    use_https: true
    validate_certs: true
    user_name: "usernumberone"

```

## License

TODO

## Author Information
  - ['Western Telematic Inc. (@wtinetworkgear)']
