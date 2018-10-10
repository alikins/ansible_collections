# Ansible module: ansible.module_win_acl


Set file/directory/registry permissions for a system user or group

## Description

Add or remove rights/permissions for a given user or group for the specified file, folder, registry key or AppPool identifies.
If adding ACL's for AppPool identities (available since 2.3), the Windows Feature "Web-Scripting-Tools" must be enabled.

## Requirements

TODO

## Arguments

``` json
{
    "inherit": "{'description': ['Inherit flags on the ACL rules.', 'Can be specified as a comma separated list, e.g. C(ContainerInherit), C(ObjectInherit).', 'For more information on the choices see MSDN InheritanceFlags enumeration at U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.inheritanceflags.aspx).', 'Defaults to C(ContainerInherit, ObjectInherit) for Directories.'], 'choices': ['ContainerInherit', 'ObjectInherit']}",
    "path": "{'description': ['The path to the file or directory.'], 'required': True}",
    "propagation": "{'description': ['Propagation flag on the ACL rules.', 'For more information on the choices see MSDN PropagationFlags enumeration at U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.propagationflags.aspx).'], 'choices': ['InheritOnly', 'None', 'NoPropagateInherit'], 'default': 'None'}",
    "rights": "{'description': ['The rights/permissions that are to be allowed/denied for the specified user or group for the item at C(path).', 'If C(path) is a file or directory, rights can be any right under MSDN FileSystemRights U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.filesystemrights.aspx).', 'If C(path) is a registry key, rights can be any right under MSDN RegistryRights U(https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.registryrights.aspx).'], 'required': True}",
    "state": "{'description': ['Specify whether to add C(present) or remove C(absent) the specified access rule.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "type": "{'description': ['Specify whether to allow or deny the rights specified.'], 'required': True, 'choices': ['allow', 'deny']}",
    "user": "{'description': ['User or Group to add specified rights to act on src file/folder or registry key.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Restrict write and execute access to User Fed-Phil
  win_acl:
    user: Fed-Phil
    path: C:\Important\Executable.exe
    type: deny
    rights: ExecuteFile,Write

- name: Add IIS_IUSRS allow rights
  win_acl:
    path: C:\inetpub\wwwroot\MySite
    user: IIS_IUSRS
    rights: FullControl
    type: allow
    state: present
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: set registry key right
  win_acl:
    path: HKCU:\Bovine\Key
    user: BUILTIN\Users
    rights: EnumerateSubKeys
    type: allow
    state: present
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: Remove FullControl AccessRule for IIS_IUSRS
  win_acl:
    path: C:\inetpub\wwwroot\MySite
    user: IIS_IUSRS
    rights: FullControl
    type: allow
    state: absent
    inherit: ContainerInherit, ObjectInherit
    propagation: 'None'

- name: Deny Intern
  win_acl:
    path: C:\Administrator\Documents
    user: Intern
    rights: Read,Write,Modify,FullControl,Delete
    type: deny
    state: present

```

## License

TODO

## Author Information
  - ['Phil Schwartz (@schwartzmx)', 'Trond Hindenes (@trondhindenes)', 'Hans-Joachim Kliemeck (@h0nIg)']
  - ['Phil Schwartz (@schwartzmx)', 'Trond Hindenes (@trondhindenes)', 'Hans-Joachim Kliemeck (@h0nIg)']
  - ['Phil Schwartz (@schwartzmx)', 'Trond Hindenes (@trondhindenes)', 'Hans-Joachim Kliemeck (@h0nIg)']
