# Ansible module: ansible.module_win_audit_rule


Adds an audit rule to files, folders, or registry keys

## Description

Used to apply audit rules to files, folders or registry keys.
Once applied, it will begin recording the user who performed the operation defined into the Security Log in the Event viewer.
The behavior is designed to ignore inherited rules since those cannot be adjusted without first disabling the inheritance behavior. It will still print inherited rules in the output though for debugging purposes.

## Requirements

TODO

## Arguments

``` json
{
    "audit_flags": "{'description': ['Defines whether to log on failure, success, or both.', 'To log both define as comma separated list "Success, Failure".'], 'required': True, 'type': 'list', 'choices': ['Failure', 'Success']}",
    "inheritance_flags": "{'description': ['Defines what objects inside of a folder or registry key will inherit the settings.', 'If you are setting a rule on a file, this value has to be changed to C(none).', 'For more information on the choices see MSDN PropagationFlags enumeration at U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.inheritanceflags.aspx).'], 'type': 'list', 'default': 'ContainerInherit,ObjectInherit', 'choices': ['ContainerInherit', 'ObjectInherit']}",
    "path": "{'description': ['Path to the file, folder, or registry key.', "Registry paths should be in Powershell format, beginning with an abbreviation for the root such as, 'hklm:\\software'."], 'required': True, 'type': 'path', 'aliases': ['dest', 'destination']}",
    "propagation_flags": "{'description': ['Propagation flag on the audit rules.', 'This value is ignored when the path type is a file.', 'For more information on the choices see MSDN PropagationFlags enumeration at U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.propagationflags.aspx).'], 'default': 'None', 'choices': ['None', 'InherityOnly', 'NoPropagateInherit']}",
    "rights": "{'description': ['Comma separated list of the rights desired. Only required for adding a rule.', 'If I(path) is a file or directory, rights can be any right under MSDN FileSystemRights U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.filesystemrights.aspx).', 'If I(path) is a registry key, rights can be any right under MSDN RegistryRights U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.registryrights.aspx).'], 'required': True, 'type': 'list'}",
    "state": "{'description': ['Whether the rule should be C(present) or C(absent).', 'For absent, only I(path), I(user), and I(state) are required.', 'Specifying C(absent) will remove all rules matching the defined I(user).'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "user": "{'description': ['The user or group to adjust rules for.'], 'required': True}",
}
```

## Examples


``` yaml

- name: add filesystem audit rule for a folder
  win_audit_rule:
    path: C:\inetpub\wwwroot\website
    user: BUILTIN\Users
    rights: write,delete,changepermissions
    audit_flags: success,failure
    inheritance_flags: ContainerInherit,ObjectInherit

- name: add filesystem audit rule for a file
  win_audit_rule:
    path: C:\inetpub\wwwroot\website\web.config
    user: BUILTIN\Users
    rights: write,delete,changepermissions
    audit_flags: success,failure
    inheritance_flags: None

- name: add registry audit rule
  win_audit_rule:
    path: HKLM:\software
    user: BUILTIN\Users
    rights: delete
    audit_flags: 'success'

- name: remove filesystem audit rule
  win_audit_rule:
    path: C:\inetpub\wwwroot\website
    user: BUILTIN\Users
    state: absent

- name: remove registry audit rule
  win_audit_rule:
    path: HKLM:\software
    user: BUILTIN\Users
    state: absent

```

## License

TODO

## Author Information
  - ['Noah Sparks (@nwsparks)']
