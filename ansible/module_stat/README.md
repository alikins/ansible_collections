# Ansible module: ansible.module_stat


Retrieve file or file system status

## Description

Retrieves facts for a file similar to the linux/unix 'stat' command.
For Windows targets, use the M(win_stat) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "checksum_algorithm": "{'description': ['Algorithm to determine checksum of file. Will throw an error if the host is unable to use specified algorithm.', 'The remote host has to support the hashing method specified, C(md5) can be unavailable if the host is FIPS-140 compliant.'], 'choices': ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'], 'default': 'sha1', 'aliases': ['checksum', 'checksum_algo'], 'version_added': '2.0'}",
    "follow": "{'description': ['Whether to follow symlinks.'], 'type': 'bool', 'default': False}",
    "get_attributes": "{'description': ['Get file attributes using lsattr tool if present.'], 'type': 'bool', 'default': True, 'version_added': '2.3', 'aliases': ['attr', 'attributes']}",
    "get_checksum": "{'description': ['Whether to return a checksum of the file (default sha1).'], 'type': 'bool', 'default': True, 'version_added': '1.8'}",
    "get_md5": "{'description': ['Whether to return the md5 sum of the file.', "Will return None if not a regular file or if we're unable to use md5 (Common for FIPS-140 compliant systems).", 'The default of this option changed from C(yes) to C(no) in Ansible 2.5 and will be removed altogether in Ansible 2.9.', 'Use C(get_checksum=true) with C(checksum_algorithm=md5) to return an md5 hash under the C(checksum) return value.'], 'type': 'bool', 'default': False}",
    "get_mime": "{'description': ["Use file magic and return data about the nature of the file. this uses the 'file' utility found on most Linux/Unix systems.", "This will add both `mime_type` and 'charset' fields to the return, if possible.", "In 2.3 this option changed from 'mime' to 'get_mime' and the default changed to 'Yes'."], 'type': 'bool', 'default': True, 'version_added': '2.1', 'aliases': ['mime', 'mime_type', 'mime-type']}",
    "path": "{'description': ['The full path of the file/object to get the facts of.'], 'required': True}",
}
```

## Examples


``` yaml

# Obtain the stats of /etc/foo.conf, and check that the file still belongs
# to 'root'. Fail otherwise.
- stat:
    path: /etc/foo.conf
  register: st
- fail:
    msg: "Whoops! file ownership has changed"
  when: st.stat.pw_name != 'root'

# Determine if a path exists and is a symlink. Note that if the path does
# not exist, and we test sym.stat.islnk, it will fail with an error. So
# therefore, we must test whether it is defined.
# Run this to understand the structure, the skipped ones do not pass the
# check performed by 'when'
- stat:
    path: /path/to/something
  register: sym

- debug:
    msg: "islnk isn't defined (path doesn't exist)"
  when: sym.stat.islnk is not defined

- debug:
    msg: "islnk is defined (path must exist)"
  when: sym.stat.islnk is defined

- debug:
    msg: "Path exists and is a symlink"
  when: sym.stat.islnk is defined and sym.stat.islnk

- debug:
    msg: "Path exists and isn't a symlink"
  when: sym.stat.islnk is defined and sym.stat.islnk == False


# Determine if a path exists and is a directory.  Note that we need to test
# both that p.stat.isdir actually exists, and also that it's set to true.
- stat:
    path: /path/to/something
  register: p
- debug:
    msg: "Path exists and is a directory"
  when: p.stat.isdir is defined and p.stat.isdir

# Don't do checksum
- stat:
    path: /path/to/myhugefile
    get_checksum: no

# Use sha256 to calculate checksum
- stat:
    path: /path/to/something
    checksum_algorithm: sha256

```

## License

TODO

## Author Information
  - ['Bruce Pennypacker (@bpennypacker)']
