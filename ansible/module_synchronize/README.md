# Ansible module: ansible.module_synchronize


A wrapper around rsync to make common tasks in your playbooks quick and easy

## Description

C(synchronize) is a wrapper around rsync to make common tasks in your playbooks quick and easy. It is run and originates on the local host where Ansible is being run. Of course, you could just use the C(command) action to call rsync yourself, but you also have to add a fair number of boilerplate options and host facts. C(synchronize) is not intended to provide access to the full power of rsync, but does make the most common invocations easier to implement. You `still` may need to call rsync directly via C(command) or C(shell) depending on your use case.

## Requirements

TODO

## Arguments

``` json
{
    "archive": "{'description': ['Mirrors the rsync archive flag, enables recursive, links, perms, times, owner, group flags and -D.'], 'type': 'bool', 'default': True}",
    "checksum": "{'description': ['Skip based on checksum, rather than mod-time & size; Note that that "archive" option is still enabled by default - the "checksum" option will not disable it.'], 'type': 'bool', 'default': False, 'version_added': '1.6'}",
    "compress": "{'description': ['Compress file data during the transfer. In most cases, leave this enabled unless it causes problems.'], 'type': 'bool', 'default': True, 'version_added': '1.7'}",
    "copy_links": "{'description': ['Copy symlinks as the item that they point to (the referent) is copied, rather than the symlink.'], 'type': 'bool', 'default': False}",
    "delete": "{'description': ["Delete files in C(dest) that don't exist (after transfer, not before) in the C(src) path. This option requires C(recursive=yes)."], 'type': 'bool', 'default': False}",
    "dest": "{'description': ['Path on the destination host that will be synchronized from the source; The path can be absolute or relative.'], 'required': True}",
    "dest_port": "{'description': ['Port number for ssh on the destination host. Prior to ansible 2.0, the ansible_ssh_port inventory var took precedence over this value.'], 'default': 'Value of ansible_ssh_port for this host, remote_port config setting, or the value from ssh client configuration if none of those are set', 'version_added': '1.5'}",
    "dirs": "{'description': ['Transfer directories without recursing'], 'type': 'bool', 'default': False}",
    "existing_only": "{'description': ['Skip creating new files on receiver.'], 'type': 'bool', 'default': False, 'version_added': '1.5'}",
    "group": "{'description': ['Preserve group'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "link_dest": "{'description': ['add a destination to hard link against during the rsync.'], 'default': None, 'version_added': '2.5'}",
    "links": "{'description': ['Copy symlinks as symlinks.'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "mode": "{'description': ['Specify the direction of the synchronization. In push mode the localhost or delegate is the source; In pull mode the remote host in context is the source.'], 'choices': ['pull', 'push'], 'default': 'push'}",
    "owner": "{'description': ['Preserve owner (super user only)'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "partial": "{'description': ['Tells rsync to keep the partial file which should make a subsequent transfer of the rest of the file much faster.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "perms": "{'description': ['Preserve permissions.'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "private_key": "{'description': ['Specify the private key to use for SSH-based rsync connections (e.g. C(~/.ssh/id_rsa))'], 'version_added': '1.6'}",
    "recursive": "{'description': ['Recurse into directories.'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "rsync_opts": "{'description': ['Specify additional rsync options by passing in an array.'], 'default': None, 'version_added': '1.6'}",
    "rsync_path": "{'description': ['Specify the rsync command to run on the remote host. See C(--rsync-path) on the rsync man page.', 'To specify the rsync command to run on the local host, you need to set this your task var C(ansible_rsync_path).']}",
    "rsync_timeout": "{'description': ['Specify a C(--timeout) for the rsync command in seconds.'], 'default': 0}",
    "set_remote_user": "{'description': ['put user@ for the remote paths. If you have a custom ssh config to define the remote user for a host that does not match the inventory user, you should set this parameter to "no".'], 'default': True}",
    "src": "{'description': ['Path on the source host that will be synchronized to the destination; The path can be absolute or relative.'], 'required': True}",
    "times": "{'description': ['Preserve modification times'], 'type': 'bool', 'default': 'the value of the archive option'}",
    "use_ssh_args": "{'description': ['Use the ssh_args specified in ansible.cfg'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "verify_host": "{'description': ['Verify destination host key.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Synchronization of src on the control machine to dest on the remote hosts
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path

- name: Synchronization using rsync protocol (push)
  synchronize:
    src: some/relative/path/
    dest: rsync://somehost.com/path/

- name: Synchronization using rsync protocol (pull)
  synchronize:
    mode: pull
    src: rsync://somehost.com/path/
    dest: /some/absolute/path/

- name:  Synchronization using rsync protocol on delegate host (push)
  synchronize:
    src: /some/absolute/path/
    dest: rsync://somehost.com/path/
  delegate_to: delegate.host

- name: Synchronization using rsync protocol on delegate host (pull)
  synchronize:
    mode: pull
    src: rsync://somehost.com/path/
    dest: /some/absolute/path/
  delegate_to: delegate.host

- name: Synchronization without any --archive options enabled
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    archive: no

- name: Synchronization with --archive options enabled except for --recursive
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    recursive: no

- name: Synchronization with --archive options enabled except for --times, with --checksum option enabled
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    checksum: yes
    times: no

- name: Synchronization without --archive options enabled except use --links
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    archive: no
    links: yes

- name: Synchronization of two paths both on the control machine
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
  delegate_to: localhost

- name: Synchronization of src on the inventory host to the dest on the localhost in pull mode
  synchronize:
    mode: pull
    src: some/relative/path
    dest: /some/absolute/path

- name: Synchronization of src on delegate host to dest on the current inventory host.
  synchronize:
    src: /first/absolute/path
    dest: /second/absolute/path
  delegate_to: delegate.host

- name: Synchronize two directories on one remote host.
  synchronize:
    src: /first/absolute/path
    dest: /second/absolute/path
  delegate_to: "{{ inventory_hostname }}"

- name: Synchronize and delete files in dest on the remote host that are not found in src of localhost.
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    delete: yes
    recursive: yes

# This specific command is granted su privileges on the destination
- name: Synchronize using an alternate rsync command
  synchronize:
    src: some/relative/path
    dest: /some/absolute/path
    rsync_path: "su -c rsync"

# Example .rsync-filter file in the source directory
# - var       # exclude any path whose last part is 'var'
# - /var      # exclude any path starting with 'var' starting at the source directory
# + /var/conf # include /var/conf even though it was previously excluded

- name: Synchronize passing in extra rsync options
  synchronize:
    src: /tmp/helloworld
    dest: /var/www/helloworld
    rsync_opts:
      - "--no-motd"
      - "--exclude=.git"

# Hardlink files if they didn't change
- name: Use hardlinks when synchronizing filesystems
  synchronize:
    src: /tmp/path_a/foo.txt
    dest: /tmp/path_b/foo.txt
    link_dest: /tmp/path_a/

# Specify the rsync binary to use on remote host and on local host
- hosts: groupofhosts
  vars:
        ansible_rsync_path: "/usr/gnu/bin/rsync"

  tasks:
    - name: copy /tmp/localpath/ to remote location /tmp/remotepath
      synchronize:
        src: "/tmp/localpath/"
        dest: "/tmp/remotepath"
        rsync_path: "/usr/gnu/bin/rsync"


```

## License

TODO

## Author Information
  - ['Timothy Appnel (@tima)']
