# Ansible module: ansible.module_user


Manage user accounts

## Description

Manage user accounts and user attributes.
For Windows targets, use the M(win_user) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "append": "{'description': ['If C(yes), add the user to the groups specified in C(groups).', 'If C(no), user will only be added to the groups specified in C(groups), removing them from all other groups.'], 'type': 'bool', 'default': False}",
    "comment": "{'description': ['Optionally sets the description (aka I(GECOS)) of user account.']}",
    "create_home": "{'description': ['Unless set to C(no), a home directory will be made for the user when the account is created or if the home directory does not exist.', 'Changed from C(createhome) to C(create_home) in version 2.5.'], 'type': 'bool', 'default': True, 'aliases': ['createhome']}",
    "expires": "{'description': ['An expiry time for the user in epoch, it will be ignored on platforms that do not support this. Currently supported on GNU/Linux, FreeBSD, and DragonFlyBSD.', 'Since version 2.6 you can remove the expiry time specify a negative value. Currently supported on GNU/Linux and FreeBSD.'], 'version_added': '1.9'}",
    "force": "{'description': ['This only affects C(state=absent), it forces removal of the user and associated directories on supported platforms. The behavior is the same as C(userdel --force), check the man page for C(userdel) on your system for details and support.'], 'type': 'bool', 'default': False}",
    "generate_ssh_key": "{'description': ['Whether to generate a SSH key for the user in question. This will B(not) overwrite an existing SSH key.'], 'type': 'bool', 'default': False}",
    "group": "{'description': ["Optionally sets the user's primary group (takes a group name)."]}",
    "groups": "{'description': ["List of groups user will be added to. When set to an empty string C(''), C(null), or C(~), the user is removed from all groups except the primary group. (C(~) means C(null) in YAML)", 'Before version 2.3, the only input format allowed was a comma separated string. Now this parameter accepts a list as well as a comma separated string.']}",
    "hidden": "{'required': False, 'type': 'bool', 'description': ['macOS only, optionally hide the user from the login window and system preferences.', "The default will be 'True' if the I(system) option is used."], 'version_added': '2.6'}",
    "home": "{'description': ["Optionally set the user's home directory."]}",
    "local": "{'description': ['Forces the use of "local" command alternatives on platforms that implement it. This is useful in environments that use centralized authentification when you want to manipulate the local users. I.E. it uses `luseradd` instead of `useradd`.', 'This requires that these commands exist on the targeted host, otherwise it will be a fatal error.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "login_class": "{'description': ["Optionally sets the user's login class, a feature of most BSD OSs."]}",
    "move_home": "{'description': ["If set to C(yes) when used with C(home=), attempt to move the user's old home directory to the specified directory if it isn't there already and the old home exists."], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the user to create, remove or modify.'], 'required': True, 'aliases': ['user']}",
    "non_unique": "{'description': ['Optionally when used with the -u option, this option allows to change the user ID to a non-unique value.'], 'type': 'bool', 'default': False}",
    "password": "{'description': ["Optionally set the user's password to this crypted value.", 'On macOS systems, this value has to be cleartext. Beware of security issues.', 'See U(https://docs.ansible.com/ansible/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module) for details on various ways to generate these password values.']}",
    "password_lock": "{'description': ['Lock the password (usermod -L, pw lock, usermod -C). BUT implementation differs on different platforms, this option does not always mean the user cannot login via other methods. This option does not disable the user, only lock the password. Do not change the password in the same task. Currently supported on Linux, FreeBSD, DragonFlyBSD, NetBSD.'], 'type': 'bool', 'version_added': '2.6'}",
    "remove": "{'description': ['This only affects C(state=absent), it attempts to remove directories associated with the user. The behavior is the same as C(userdel --remove), check the man page for details and support.'], 'type': 'bool', 'default': False}",
    "seuser": "{'description': ['Optionally sets the seuser type (user_u) on selinux enabled systems.'], 'version_added': '2.1'}",
    "shell": "{'description': ["Optionally set the user's shell.", 'On macOS, before version 2.5, the default shell for non-system users was /usr/bin/false. Since 2.5, the default shell for non-system users on macOS is /bin/bash.', 'On other operating systems, the default shell is determined by the underlying tool being used. See Notes for details.']}",
    "skeleton": "{'description': ['Optionally set a home skeleton directory. Requires create_home option!'], 'version_added': '2.0'}",
    "ssh_key_bits": "{'description': ['Optionally specify number of bits in SSH key to create.'], 'default': 'default set by ssh-keygen'}",
    "ssh_key_comment": "{'description': ['Optionally define the comment for the SSH key.'], 'default': 'ansible-generated on $HOSTNAME'}",
    "ssh_key_file": "{'description': ["Optionally specify the SSH key filename. If this is a relative filename then it will be relative to the user's home directory."], 'default': '.ssh/id_rsa'}",
    "ssh_key_passphrase": "{'description': ['Set a passphrase for the SSH key.  If no passphrase is provided, the SSH key will default to having no passphrase.']}",
    "ssh_key_type": "{'description': ['Optionally specify the type of SSH key to generate. Available SSH key types will depend on implementation present on target host.'], 'default': 'rsa'}",
    "state": "{'description': ['Whether the account should exist or not, taking action if the state is different from what is stated.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "system": "{'description': ['When creating an account C(state=present), setting this to C(yes) makes the user a system account. This setting cannot be changed on existing users.'], 'type': 'bool', 'default': False}",
    "uid": "{'description': ['Optionally sets the I(UID) of the user.']}",
    "update_password": "{'description': ['C(always) will update passwords if they differ.  C(on_create) will only set the password for newly created users.'], 'choices': ['always', 'on_create'], 'default': 'always', 'version_added': '1.3'}",
}
```

## Examples


``` yaml

- name: Add the user 'johnd' with a specific uid and a primary group of 'admin'
  user:
    name: johnd
    comment: John Doe
    uid: 1040
    group: admin

- name: Add the user 'james' with a bash shell, appending the group 'admins' and 'developers' to the user's groups
  user:
    name: james
    shell: /bin/bash
    groups: admins,developers
    append: yes

- name: Remove the user 'johnd'
  user:
    name: johnd
    state: absent
    remove: yes

- name: Create a 2048-bit SSH key for user jsmith in ~jsmith/.ssh/id_rsa
  user:
    name: jsmith
    generate_ssh_key: yes
    ssh_key_bits: 2048
    ssh_key_file: .ssh/id_rsa

- name: Added a consultant whose account you want to expire
  user:
    name: james18
    shell: /bin/zsh
    groups: developers
    expires: 1422403387

- name: starting at version 2.6, modify user, remove expiry time
  user:
    name: james18
    expires: -1

```

## License

TODO

## Author Information
  - ['Stephen Fromm (@sfromm)']
