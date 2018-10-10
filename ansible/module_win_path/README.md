# Ansible module: ansible.module_win_path


Manage Windows path environment variables

## Description

Allows element-based ordering, addition, and removal of Windows path environment variables.

## Requirements

TODO

## Arguments

``` json
{
    "elements": "{'description': ['A single path element, or a list of path elements (ie, directories) to add or remove.', 'When multiple elements are included in the list (and C(state) is C(present)), the elements are guaranteed to appear in the same relative order in the resultant path value.', 'Variable expansions (eg, C(%VARNAME%)) are allowed, and are stored unexpanded in the target path element.', 'Any existing path elements not mentioned in C(elements) are always preserved in their current order.', 'New path elements are appended to the path, and existing path elements may be moved closer to the end to satisfy the requested ordering.', 'Paths are compared in a case-insensitive fashion, and trailing backslashes are ignored for comparison purposes. However, note that trailing backslashes in YAML require quotes.'], 'required': True}",
    "name": "{'description': ['Target path environment variable name.'], 'default': 'PATH'}",
    "scope": "{'description': ['The level at which the environment variable specified by C(name) should be managed (either for the current user or global machine scope).'], 'choices': ['machine', 'user'], 'default': 'machine'}",
    "state": "{'description': ['Whether the path elements specified in C(elements) should be present or absent.'], 'choices': ['absent', 'present']}",
}
```

## Examples


``` yaml

- name: Ensure that system32 and Powershell are present on the global system path, and in the specified order
  win_path:
    elements:
    - '%SystemRoot%\system32'
    - '%SystemRoot%\system32\WindowsPowerShell\v1.0'

- name: Ensure that C:\Program Files\MyJavaThing is not on the current user's CLASSPATH
  win_path:
    name: CLASSPATH
    elements: C:\Program Files\MyJavaThing
    scope: user
    state: absent

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
