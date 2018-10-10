# Ansible module: ansible.module_lxd_profile


Manage LXD profiles

## Description

Management of LXD profiles

## Requirements

TODO

## Arguments

``` json
{
    "cert_file": "{'description': ['The client certificate file path.'], 'required': False, 'default': '"{}/.config/lxc/client.crt" .format(os.environ["HOME"])'}",
    "config": "{'description': ['The config for the container (e.g. {"limits.memory": "4GB"}). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#patch-3)', 'If the profile already exists and its "config" value in metadata obtained from GET /1.0/profiles/<name> U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#get-19) are different, they this module tries to apply the configurations.', 'Not all config values are supported to apply the existing profile. Maybe you need to delete and recreate a profile.'], 'required': False}",
    "description": "{'description': ['Description of the profile.'], 'version_added': '2.5'}",
    "devices": "{'description': ['The devices for the profile (e.g. {"rootfs": {"path": "/dev/kvm", "type": "unix-char"}). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#patch-3)'], 'required': False}",
    "key_file": "{'description': ['The client certificate key file path.'], 'required': False, 'default': '"{}/.config/lxc/client.key" .format(os.environ["HOME"])'}",
    "name": "{'description': ['Name of a profile.'], 'required': True}",
    "new_name": "{'description': ['A new name of a profile.', 'If this parameter is specified a profile will be renamed to this name. See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-11)'], 'required': False}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Define the state of a profile.'], 'required': False, 'default': 'present'}",
    "trust_password": "{'description': ['The client trusted password.', 'You need to set this password on the LXD server before running this module using the following command. lxc config set core.trust_password <some random password> See U(https://www.stgraber.org/2016/04/18/lxd-api-direct-interaction/)', 'If trust_password is set, this module send a request for authentication before sending any requests.'], 'required': False}",
    "url": "{'description': ['The unix domain socket path or the https URL for the LXD server.'], 'required': False, 'default': 'unix:/var/lib/lxd/unix.socket'}",
}
```

## Examples


``` yaml

# An example for creating a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Create a profile
      lxd_profile:
        name: macvlan
        state: present
        config: {}
        description: my macvlan profile
        devices:
          eth0:
            nictype: macvlan
            parent: br0
            type: nic

# An example for creating a profile via http connection
- hosts: localhost
  connection: local
  tasks:
  - name: create macvlan profile
    lxd_profile:
      url: https://127.0.0.1:8443
      # These cert_file and key_file values are equal to the default values.
      #cert_file: "{{ lookup('env', 'HOME') }}/.config/lxc/client.crt"
      #key_file: "{{ lookup('env', 'HOME') }}/.config/lxc/client.key"
      trust_password: mypassword
      name: macvlan
      state: present
      config: {}
      description: my macvlan profile
      devices:
        eth0:
          nictype: macvlan
          parent: br0
          type: nic

# An example for deleting a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Delete a profile
      lxd_profile:
        name: macvlan
        state: absent

# An example for renaming a profile
- hosts: localhost
  connection: local
  tasks:
    - name: Rename a profile
      lxd_profile:
        name: macvlan
        new_name: macvlan2
        state: present

```

## License

TODO

## Author Information
  - ['Hiroaki Nakamura (@hnakamur)']
