# Ansible module: ansible.module_lxc_container


Manage LXC Containers

## Description

Management of LXC containers

## Requirements

TODO

## Arguments

``` json
{
    "archive": "{'choices': [True, False], 'description': ['Create an archive of a container. This will create a tarball of the running container.'], 'type': 'bool', 'default': False}",
    "archive_compression": "{'choices': ['gzip', 'bzip2', 'none'], 'description': ['Type of compression to use when creating an archive of a running container.'], 'default': 'gzip'}",
    "archive_path": "{'description': ['Path the save the archived container. If the path does not exist the archive method will attempt to create it.']}",
    "backing_store": "{'choices': ['dir', 'lvm', 'loop', 'btrfs', 'overlayfs', 'zfs'], 'description': ['Backend storage type for the container.'], 'default': 'dir'}",
    "clone_name": "{'description': ['Name of the new cloned server. This is only used when state is clone.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "clone_snapshot": "{'choices': [True, False], 'description': ['Create a snapshot a container when cloning. This is not supported by all container storage backends. Enabling this may fail if the backing store does not support snapshots.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "config": "{'description': ['Path to the LXC configuration file.']}",
    "container_command": "{'description': ['Run a command within a container.']}",
    "container_config": "{'description': ["list of 'key=value' options to use when configuring a container."]}",
    "container_log": "{'choices': [True, False], 'description': ['Enable a container log for host actions to the container.'], 'type': 'bool', 'default': False}",
    "container_log_level": "{'choices': ['INFO', 'ERROR', 'DEBUG'], 'description': ['Set the log level for a container where *container_log* was set.'], 'required': False, 'default': 'INFO'}",
    "directory": "{'description': ['Place rootfs directory under DIR.']}",
    "fs_size": "{'description': ['File system Size.'], 'default': '5G'}",
    "fs_type": "{'description': ['Create fstype TYPE.'], 'default': 'ext4'}",
    "lv_name": "{'description': ['Name of the logical volume, defaults to the container name.'], 'default': '$CONTAINER_NAME'}",
    "lxc_path": "{'description': ['Place container under PATH']}",
    "name": "{'description': ['Name of a container.'], 'required': True}",
    "state": "{'choices': ['started', 'stopped', 'restarted', 'absent', 'frozen'], 'description': ['Define the state of a container. If you clone a container using `clone_name` the newly cloned container created in a stopped state. The running container will be stopped while the clone operation is happening and upon completion of the clone the original container state will be restored.'], 'default': 'started'}",
    "template": "{'description': ['Name of the template to use within an LXC create.'], 'default': 'ubuntu'}",
    "template_options": "{'description': ['Template options when building the container.']}",
    "thinpool": "{'description': ['Use LVM thin pool called TP.']}",
    "vg_name": "{'description': ['If Backend store is lvm, specify the name of the volume group.'], 'default': 'lxc'}",
    "zfs_root": "{'description': ['Create zfs under given zfsroot.']}",
}
```

## Examples


``` yaml

- name: Create a started container
  lxc_container:
    name: test-container-started
    container_log: true
    template: ubuntu
    state: started
    template_options: --release trusty

- name: Create a stopped container
  lxc_container:
    name: test-container-stopped
    container_log: true
    template: ubuntu
    state: stopped
    template_options: --release trusty

- name: Create a frozen container
  lxc_container:
    name: test-container-frozen
    container_log: true
    template: ubuntu
    state: frozen
    template_options: --release trusty
    container_command: |
      echo 'hello world.' | tee /opt/started-frozen

# Create filesystem container, configure it, and archive it, and start it.
- name: Create filesystem container
  lxc_container:
    name: test-container-config
    backing_store: dir
    container_log: true
    template: ubuntu
    state: started
    archive: true
    archive_compression: none
    container_config:
      - "lxc.aa_profile=unconfined"
      - "lxc.cgroup.devices.allow=a *:* rmw"
    template_options: --release trusty

# Create an lvm container, run a complex command in it, add additional
# configuration to it, create an archive of it, and finally leave the container
# in a frozen state. The container archive will be compressed using bzip2
- name: Create a frozen lvm container
  lxc_container:
    name: test-container-lvm
    container_log: true
    template: ubuntu
    state: frozen
    backing_store: lvm
    template_options: --release trusty
    container_command: |
      apt-get update
      apt-get install -y vim lxc-dev
      echo 'hello world.' | tee /opt/started
      if [[ -f "/opt/started" ]]; then
          echo 'hello world.' | tee /opt/found-started
      fi
    container_config:
      - "lxc.aa_profile=unconfined"
      - "lxc.cgroup.devices.allow=a *:* rmw"
    archive: true
    archive_compression: bzip2
  register: lvm_container_info

- name: Debug info on container "test-container-lvm"
  debug:
    var: lvm_container_info

- name: Run a command in a container and ensure its in a "stopped" state.
  lxc_container:
    name: test-container-started
    state: stopped
    container_command: |
      echo 'hello world.' | tee /opt/stopped

- name: Run a command in a container and ensure its it in a "frozen" state.
  lxc_container:
    name: test-container-stopped
    state: frozen
    container_command: |
      echo 'hello world.' | tee /opt/frozen

- name: Start a container
  lxc_container:
    name: test-container-stopped
    state: started

- name: Run a command in a container and then restart it
  lxc_container:
    name: test-container-started
    state: restarted
    container_command: |
      echo 'hello world.' | tee /opt/restarted

- name: Run a complex command within a "running" container
  lxc_container:
    name: test-container-started
    container_command: |
      apt-get update
      apt-get install -y curl wget vim apache2
      echo 'hello world.' | tee /opt/started
      if [[ -f "/opt/started" ]]; then
          echo 'hello world.' | tee /opt/found-started
      fi

# Create an archive of an existing container, save the archive to a defined
# path and then destroy it.
- name: Archive container
  lxc_container:
    name: test-container-started
    state: absent
    archive: true
    archive_path: /opt/archives

# Create a container using overlayfs, create an archive of it, create a
# snapshot clone of the container and and finally leave the container
# in a frozen state. The container archive will be compressed using gzip.
- name: Create an overlayfs container archive and clone it
  lxc_container:
    name: test-container-overlayfs
    container_log: true
    template: ubuntu
    state: started
    backing_store: overlayfs
    template_options: --release trusty
    clone_snapshot: true
    clone_name: test-container-overlayfs-clone-snapshot
    archive: true
    archive_compression: gzip
  register: clone_container_info

- name: debug info on container "test-container"
  debug:
    var: clone_container_info

- name: Clone a container using snapshot
  lxc_container:
    name: test-container-overlayfs-clone-snapshot
    backing_store: overlayfs
    clone_name: test-container-overlayfs-clone-snapshot2
    clone_snapshot: true

- name: Create a new container and clone it
  lxc_container:
    name: test-container-new-archive
    backing_store: dir
    clone_name: test-container-new-archive-clone

- name: Archive and clone a container then destroy it
  lxc_container:
    name: test-container-new-archive
    state: absent
    clone_name: test-container-new-archive-destroyed-clone
    archive: true
    archive_compression: gzip

- name: Start a cloned container.
  lxc_container:
    name: test-container-new-archive-destroyed-clone
    state: started

- name: Destroy a container
  lxc_container:
    name: '{{ item }}'
    state: absent
  with_items:
    - test-container-stopped
    - test-container-started
    - test-container-frozen
    - test-container-lvm
    - test-container-config
    - test-container-overlayfs
    - test-container-overlayfs-clone
    - test-container-overlayfs-clone-snapshot
    - test-container-overlayfs-clone-snapshot2
    - test-container-new-archive
    - test-container-new-archive-clone
    - test-container-new-archive-destroyed-clone

```

## License

TODO

## Author Information
  - ['Kevin Carter (@cloudnull)']
