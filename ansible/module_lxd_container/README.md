# Ansible module: ansible.module_lxd_container


Manage LXD Containers

## Description

Management of LXD containers

## Requirements

TODO

## Arguments

``` json
{
    "architecture": "{'description': ['The architecture for the container (e.g. "x86_64" or "i686"). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1)'], 'required': False}",
    "cert_file": "{'description': ['The client certificate file path.'], 'required': False, 'default': '"{}/.config/lxc/client.crt" .format(os.environ["HOME"])'}",
    "config": "{'description': ['The config for the container (e.g. {"limits.cpu": "2"}). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1)', 'If the container already exists and its "config" value in metadata obtained from GET /1.0/containers/<name> U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#10containersname) are different, they this module tries to apply the configurations.', "The key starts with 'volatile.' are ignored for this comparison.", 'Not all config values are supported to apply the existing container. Maybe you need to delete and recreate a container.'], 'required': False}",
    "devices": "{'description': ['The devices for the container (e.g. { "rootfs": { "path": "/dev/kvm", "type": "unix-char" }). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1)'], 'required': False}",
    "ephemeral": "{'description': ['Whether or not the container is ephemeral (e.g. true or false). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1)'], 'required': False}",
    "force_stop": "{'description': ['If this is true, the C(lxd_container) forces to stop the container when it stops or restarts the container.'], 'required': False, 'default': False}",
    "key_file": "{'description': ['The client certificate key file path.'], 'required': False, 'default': '"{}/.config/lxc/client.key" .format(os.environ["HOME"])'}",
    "name": "{'description': ['Name of a container.'], 'required': True}",
    "source": "{'description': ['The source for the container (e.g. { "type": "image", "mode": "pull", "server": "https://images.linuxcontainers.org", "protocol": "lxd", "alias": "ubuntu/xenial/amd64" }). See U(https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1)'], 'required': False}",
    "state": "{'choices': ['started', 'stopped', 'restarted', 'absent', 'frozen'], 'description': ['Define the state of a container.'], 'required': False, 'default': 'started'}",
    "timeout": "{'description': ['A timeout for changing the state of the container.', 'This is also used as a timeout for waiting until IPv4 addresses are set to the all network interfaces in the container after starting or restarting.'], 'required': False, 'default': 30}",
    "trust_password": "{'description': ['The client trusted password.', 'You need to set this password on the LXD server before running this module using the following command. lxc config set core.trust_password <some random password> See U(https://www.stgraber.org/2016/04/18/lxd-api-direct-interaction/)', 'If trust_password is set, this module send a request for authentication before sending any requests.'], 'required': False}",
    "url": "{'description': ['The unix domain socket path or the https URL for the LXD server.'], 'required': False, 'default': 'unix:/var/lib/lxd/unix.socket'}",
    "wait_for_ipv4_addresses": "{'description': ['If this is true, the C(lxd_container) waits until IPv4 addresses are set to the all network interfaces in the container after starting or restarting.'], 'required': False, 'default': False}",
}
```

## Examples


``` yaml

# An example for creating a Ubuntu container and install python
- hosts: localhost
  connection: local
  tasks:
    - name: Create a started container
      lxd_container:
        name: mycontainer
        state: started
        source:
          type: image
          mode: pull
          server: https://images.linuxcontainers.org
          protocol: lxd
          alias: ubuntu/xenial/amd64
        profiles: ["default"]
        wait_for_ipv4_addresses: true
        timeout: 600

    - name: check python is installed in container
      delegate_to: mycontainer
      raw: dpkg -s python
      register: python_install_check
      failed_when: python_install_check.rc not in [0, 1]
      changed_when: false

    - name: install python in container
      delegate_to: mycontainer
      raw: apt-get install -y python
      when: python_install_check.rc == 1

# An example for deleting a container
- hosts: localhost
  connection: local
  tasks:
    - name: Delete a container
      lxd_container:
        name: mycontainer
        state: absent

# An example for restarting a container
- hosts: localhost
  connection: local
  tasks:
    - name: Restart a container
      lxd_container:
        name: mycontainer
        state: restarted

# An example for restarting a container using https to connect to the LXD server
- hosts: localhost
  connection: local
  tasks:
    - name: Restart a container
      lxd_container:
        url: https://127.0.0.1:8443
        # These cert_file and key_file values are equal to the default values.
        #cert_file: "{{ lookup('env', 'HOME') }}/.config/lxc/client.crt"
        #key_file: "{{ lookup('env', 'HOME') }}/.config/lxc/client.key"
        trust_password: mypassword
        name: mycontainer
        state: restarted

# Note your container must be in the inventory for the below example.
#
# [containers]
# mycontainer ansible_connection=lxd
#
- hosts:
    - mycontainer
  tasks:
    - name: copy /etc/hosts in the created container to localhost with name "mycontainer-hosts"
      fetch:
        src: /etc/hosts
        dest: /tmp/mycontainer-hosts
        flat: true

```

## License

TODO

## Author Information
  - ['Hiroaki Nakamura (@hnakamur)']
