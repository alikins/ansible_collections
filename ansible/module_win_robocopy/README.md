# Ansible module: ansible.module_win_robocopy


Synchronizes the contents of two directories using Robocopy

## Description

Synchronizes the contents of files/directories from a source to destination.
Under the hood this just calls out to RoboCopy, since that should be available on most modern Windows systems.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['Destination file/directory to sync (Will receive contents of src).'], 'required': True, 'type': 'path'}",
    "flags": "{'description': ['Directly supply Robocopy flags. If set, C(purge) and C(recurse) will be ignored.']}",
    "purge": "{'description': ['Deletes any files/directories found in the destination that do not exist in the source.', 'Toggles the C(/purge) flag to RoboCopy. If C(flags) is set, this will be ignored.'], 'type': 'bool', 'default': False}",
    "recurse": "{'description': ['Includes all subdirectories (Toggles the C(/e) flag to RoboCopy).', 'If C(flags) is set, this will be ignored.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['Source file/directory to sync.'], 'required': True, 'type': 'path'}",
}
```

## Examples


``` yaml

- name: Sync the contents of one directory to another
  win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo

- name: Sync the contents of one directory to another, including subdirectories
  win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    recurse: yes

- name: Sync the contents of one directory to another, and remove any files/directories found in destination that do not exist in the source
  win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    purge: yes

- name: Sync content in recursive mode, removing any files/directories found in destination that do not exist in the source
  win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    recurse: yes
    purge: yes

- name: Sync two directories in recursive and purging mode, specifying additional special flags
  win_robocopy:
    src: C:\DirectoryOne
    dest: C:\DirectoryTwo
    flags: /E /PURGE /XD SOME_DIR /XF SOME_FILE /MT:32

- name: Sync one file from a remote UNC path in recursive and purging mode, specifying additional special flags
  win_robocopy:
    src: \\Server1\Directory One
    dest: C:\DirectoryTwo
    flags: file.zip /E /PURGE /XD SOME_DIR /XF SOME_FILE /MT:32

```

## License

TODO

## Author Information
  - ['Corwin Brown (@blakfeld)']
