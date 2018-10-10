# Ansible module: ansible.module_find


Return a list of files based on specific criteria

## Description

Return a list of files based on specific criteria. Multiple criteria are AND'd together.
For Windows targets, use the M(win_find) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "age": "{'description': ['Select files whose age is equal to or greater than the specified time. Use a negative age to find files equal to or less than the specified time. You can choose seconds, minutes, hours, days, or weeks by specifying the first letter of any of those words (e.g., "1w").']}",
    "age_stamp": "{'default': 'mtime', 'choices': ['atime', 'ctime', 'mtime'], 'description': ['Choose the file property against which we compare age.']}",
    "contains": "{'description': ['One or more regex patterns which should be matched against the file content.']}",
    "depth": "{'description': ['Set the maximum number of levels to decend into. Setting recurse to false will override this value, which is effectively depth 1. Default is unlimited depth.'], 'version_added': '2.6'}",
    "excludes": "{'description': ['One or more (shell or regex) patterns, which type is controlled by C(use_regex) option.', 'Items matching an C(excludes) pattern are culled from C(patterns) matches. Multiple patterns can be specified using a list.'], 'type': 'list', 'aliases': ['exclude'], 'version_added': '2.5'}",
    "file_type": "{'description': ['Type of file to select.', "The 'link' and 'any' choices were added in version 2.3."], 'choices': ['any', 'directory', 'file', 'link'], 'default': 'file'}",
    "follow": "{'description': ['Set this to true to follow symlinks in path for systems with python 2.6+.'], 'type': 'bool', 'default': False}",
    "get_checksum": "{'description': ["Set this to true to retrieve a file's sha1 checksum."], 'type': 'bool', 'default': False}",
    "hidden": "{'description': ["Set this to true to include hidden files, otherwise they'll be ignored."], 'type': 'bool', 'default': False}",
    "paths": "{'required': True, 'aliases': ['name', 'path'], 'description': ['List of paths of directories to search. All paths must be fully qualified.'], 'type': 'list'}",
    "patterns": "{'default': '*', 'description': ['One or more (shell or regex) patterns, which type is controlled by C(use_regex) option.', 'The patterns restrict the list of files to be returned to those whose basenames match at least one of the patterns specified. Multiple patterns can be specified using a list.', 'This parameter expects a list, which can be either comma separated or YAML. If any of the patterns contain a comma, make sure to put them in a list to avoid splitting the patterns in undesirable ways.'], 'type': 'list', 'aliases': ['pattern']}",
    "recurse": "{'description': ['If target is a directory, recursively descend into the directory looking for files.'], 'type': 'bool', 'default': False}",
    "size": "{'description': ['Select files whose size is equal to or greater than the specified size. Use a negative size to find files equal to or less than the specified size. Unqualified values are in bytes but b, k, m, g, and t can be appended to specify bytes, kilobytes, megabytes, gigabytes, and terabytes, respectively. Size is not evaluated for directories.']}",
    "use_regex": "{'description': ['If false, the patterns are file globs (shell). If true, they are python regexes.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Recursively find /tmp files older than 2 days
  find:
    paths: /tmp
    age: 2d
    recurse: yes

- name: Recursively find /tmp files older than 4 weeks and equal or greater than 1 megabyte
  find:
    paths: /tmp
    age: 4w
    size: 1m
    recurse: yes

- name: Recursively find /var/tmp files with last access time greater than 3600 seconds
  find:
    paths: /var/tmp
    age: 3600
    age_stamp: atime
    recurse: yes

- name: Find /var/log files equal or greater than 10 megabytes ending with .old or .log.gz
  find:
    paths: /var/log
    patterns: '*.old,*.log.gz'
    size: 10m

# Note that YAML double quotes require escaping backslashes but yaml single quotes do not.
- name: Find /var/log files equal or greater than 10 megabytes ending with .old or .log.gz via regex
  find:
    paths: /var/log
    patterns: "^.*?\\.(?:old|log\\.gz)$"
    size: 10m
    use_regex: yes

- name: Find /var/log all directories, exclude nginx and mysql
  find:
    paths: /var/log
    recurse: no
    file_type: directory
    excludes: 'nginx,mysql'

# When using patterns that contain a comma, make sure they are formatted as lists to avoid splitting the pattern
- name: Use a single pattern that contains a comma formatted as a list
  find:
    paths: /var/log
    file_type: file
    use_regex: yes
    patterns: ['^_[0-9]{2,4}_.*.log$']

- name: Use multiple patterns that contain a comma formatted as a YAML list
  find:
    paths: /var/log
    file_type: file
    use_regex: yes
    patterns:
      - '^_[0-9]{2,4}_.*.log$'
      - '^[a-z]{1,5}_.*log$'


```

## License

TODO

## Author Information
  - ["Brian Coca (based on Ruggero Marchei's Tidy)"]
