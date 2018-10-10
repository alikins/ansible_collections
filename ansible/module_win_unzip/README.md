# Ansible module: ansible.module_win_unzip


Unzips compressed files and archives on the Windows node

## Description

Unzips compressed files and archives.
Supports .zip files natively.
Supports other formats supported by the Powershell Community Extensions (PSCX) module (basically everything 7zip supports).
For non-Windows targets, use the M(unarchive) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "creates": "{'description': ['If this file or directory exists the specified src will not be extracted.'], 'type': 'path'}",
    "delete_archive": "{'description': ['Remove the zip file, after unzipping.'], 'type': 'bool', 'default': False, 'aliases': ['rm']}",
    "dest": "{'description': ['Destination of zip file (provide absolute path of directory). If it does not exist, the directory will be created.'], 'required': True, 'type': 'path'}",
    "recurse": "{'description': ['Recursively expand zipped files within the src file.', 'Setting to a value of C(yes) requires the PSCX module to be installed.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['File to be unzipped (provide absolute path).'], 'required': True, 'type': 'path'}",
}
```

## Examples


``` yaml

# This unzips a library that was downloaded with win_get_url, and removes the file after extraction
# $ ansible -i hosts -m win_unzip -a "src=C:\LibraryToUnzip.zip dest=C:\Lib remove=true" all

- name: Unzip a bz2 (BZip) file
  win_unzip:
    src: C:\Users\Phil\Logs.bz2
    dest: C:\Users\Phil\OldLogs
    creates: C:\Users\Phil\OldLogs

- name: Unzip gz log
  win_unzip:
    src: C:\Logs\application-error-logs.gz
    dest: C:\ExtractedLogs\application-error-logs

# Unzip .zip file, recursively decompresses the contained .gz files and removes all unneeded compressed files after completion.
- name: Unzip ApplicationLogs.zip and decompress all GZipped log files
  hosts: all
  gather_facts: no
  tasks:
    - name: Recursively decompress GZ files in ApplicationLogs.zip
      win_unzip:
        src: C:\Downloads\ApplicationLogs.zip
        dest: C:\Application\Logs
        recurse: yes
        delete_archive: yes

- name: Install PSCX
  win_psmodule:
    name: Pscx
    state: present

```

## License

TODO

## Author Information
  - ['Phil Schwartz (@schwartzmx)']
