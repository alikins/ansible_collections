# Ansible module: ansible.module_patch


Apply patch files using the GNU patch tool

## Description

Apply patch files using the GNU patch tool.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'version_added': '2.0', 'description': ['Passes C(--backup --version-control=numbered) to patch, producing numbered backup copies.'], 'type': 'bool', 'default': False}",
    "basedir": "{'description': ['Path of a base directory in which the patch file will be applied. May be omitted when C(dest) option is specified, otherwise required.']}",
    "binary": "{'version_added': '2.0', 'description': ["Setting to C(yes) will disable patch's heuristic for transforming CRLF line endings into LF. Line endings of src and dest must match. If set to C(no), C(patch) will replace CRLF in C(src) files on POSIX."], 'type': 'bool', 'default': False}",
    "dest": "{'description': ['Path of the file on the remote machine to be patched.', "The names of the files to be patched are usually taken from the patch file, but if there's just one file to be patched it can specified with this option."], 'aliases': ['originalfile']}",
    "remote_src": "{'description': ['If C(no), it will search for src at originating/master machine, if C(yes) it will go to the remote/target machine for the C(src).'], 'type': 'bool', 'default': False}",
    "src": "{'description': ["Path of the patch file as accepted by the GNU patch tool. If C(remote_src) is 'no', the patch source file is looked up from the module's I(files) directory."], 'required': True, 'aliases': ['patchfile']}",
    "state": "{'version_added': '2.6', 'description': ['Whether the patch should be applied or reverted.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "strip": "{'description': ['Number that indicates the smallest prefix containing leading slashes that will be stripped from each file name found in the patch file. For more information see the strip parameter of the GNU patch tool.'], 'default': 0}",
}
```

## Examples


``` yaml

- name: Apply patch to one file
  patch:
    src: /tmp/index.html.patch
    dest: /var/www/index.html

- name: Apply patch to multiple files under basedir
  patch:
    src: /tmp/customize.patch
    basedir: /var/www
    strip: 1

- name: Revert patch to one file
  patch:
    src: /tmp/index.html.patch
    dest: /var/www/index.html
    state: absent

```

## License

TODO

## Author Information
  - ['Jakub Jirutka (@jirutka)', 'Luis Alberto Perez Lazaro (@luisperlaz)']
  - ['Jakub Jirutka (@jirutka)', 'Luis Alberto Perez Lazaro (@luisperlaz)']
