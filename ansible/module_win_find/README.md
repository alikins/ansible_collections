# Ansible module: ansible.module_win_find


Return a list of files based on specific criteria

## Description

Return a list of files based on specified criteria.
Multiple criteria are AND'd together.
For non-Windows targets, use the M(find) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "age": "{'description': ['Select files or folders whose age is equal to or greater than the specified time. Use a negative age to find files equal to or less than the specified time. You can choose seconds, minutes, hours, days or weeks by specifying the first letter of an of those words (e.g., "2s", "10d", 1w").']}",
    "age_stamp": "{'description': ['Choose the file property against which we compare C(age). The default attribute we compare with is the last modification time.'], 'choices': ['atime', 'ctime', 'mtime'], 'default': 'mtime'}",
    "checksum_algorithm": "{'description': ['Algorithm to determine the checksum of a file. Will throw an error if the host is unable to use specified algorithm.'], 'choices': ['md5', 'sha1', 'sha256', 'sha384', 'sha512'], 'default': 'sha1'}",
    "file_type": "{'description': ['Type of file to search for.'], 'choices': ['directory', 'file'], 'default': 'file'}",
    "follow": "{'description': ['Set this to C(yes) to follow symlinks in the path.', 'This needs to be used in conjunction with C(recurse).'], 'type': 'bool', 'default': False}",
    "get_checksum": "{'description': ['Whether to return a checksum of the file in the return info (default sha1), use C(checksum_algorithm) to change from the default.'], 'type': 'bool', 'default': True}",
    "hidden": "{'description': ['Set this to include hidden files or folders.'], 'type': 'bool', 'default': False}",
    "paths": "{'description': ['List of paths of directories to search for files or folders in. This can be supplied as a single path or a list of paths.'], 'required': True}",
    "patterns": "{'description': ['One or more (powershell or regex) patterns to compare filenames with. The type of pattern matching is controlled by C(use_regex) option. The patterns retrict the list of files or folders to be returned based on the filenames. For a file to be matched it only has to match with one pattern in a list provided.']}",
    "recurse": "{'description': ['Will recursively descend into the directory looking for files or folders.'], 'type': 'bool', 'default': False}",
    "size": "{'description': ['Select files or folders whose size is equal to or greater than the specified size. Use a negative value to find files equal to or less than the specified size. You can specify the size with a suffix of the byte type i.e. kilo = k, mega = m... Size is not evaluated for symbolic links.']}",
    "use_regex": "{'description': ['Will set patterns to run as a regex check if set to C(yes).'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Find files in path
  win_find:
    paths: D:\Temp

- name: Find hidden files in path
  win_find:
    paths: D:\Temp
    hidden: yes

- name: Find files in multiple paths
  win_find:
    paths:
    - C:\Temp
    - D:\Temp

- name: Find files in directory while searching recursively
  win_find:
    paths: D:\Temp
    recurse: yes

- name: Find files in directory while following symlinks
  win_find:
    paths: D:\Temp
    recurse: yes
    follow: yes

- name: Find files with .log and .out extension using powershell wildcards
  win_find:
    paths: D:\Temp
    patterns: [ '*.log', '*.out' ]

- name: Find files in path based on regex pattern
  win_find:
    paths: D:\Temp
    patterns: out_\d{8}-\d{6}.log

- name: Find files older than 1 day
  win_find:
    paths: D:\Temp
    age: 86400

- name: Find files older than 1 day based on create time
  win_find:
    paths: D:\Temp
    age: 86400
    age_stamp: ctime

- name: Find files older than 1 day with unit syntax
  win_find:
    paths: D:\Temp
    age: 1d

- name: Find files newer than 1 hour
  win_find:
    paths: D:\Temp
    age: -3600

- name: Find files newer than 1 hour with unit syntax
  win_find:
    paths: D:\Temp
    age: -1h

- name: Find files larger than 1MB
  win_find:
    paths: D:\Temp
    size: 1048576

- name: Find files larger than 1GB with unit syntax
  win_find:
    paths: D:\Temp
    size: 1g

- name: Find files smaller than 1MB
  win_find:
    paths: D:\Temp
    size: -1048576

- name: Find files smaller than 1GB with unit syntax
  win_find:
    paths: D:\Temp
    size: -1g

- name: Find folders/symlinks in multiple paths
  win_find:
    paths:
    - C:\Temp
    - D:\Temp
    file_type: directory

- name: Find files and return SHA256 checksum of files found
  win_find:
    paths: C:\Temp
    get_checksum: yes
    checksum_algorithm: sha256

- name: Find files and do not return the checksum
  win_find:
    paths: C:\Temp
    get_checksum: no

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
