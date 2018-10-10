# Ansible module: ansible.module_linode


Manage instances on the Linode Public Cloud

## Description

Manage Linode Public Cloud instances and optionally wait for it to be 'running'.

## Requirements

TODO

## Arguments

``` json
{
    "additional_disks": "{'description': ['List of dictionaries for creating additional disks that are added to the Linode configuration settings.', 'Dictionary takes Size, Label, Type. Size is in MB.'], 'version_added': '2.3'}",
    "alert_bwin_enabled": "{'description': ['Set status of bandwidth in alerts.'], 'type': 'bool', 'version_added': '2.3'}",
    "alert_bwin_threshold": "{'description': ['Set threshold in MB of bandwidth in alerts.'], 'version_added': '2.3'}",
    "alert_bwout_enabled": "{'description': ['Set status of bandwidth out alerts.'], 'type': 'bool', 'version_added': '2.3'}",
    "alert_bwout_threshold": "{'description': ['Set threshold in MB of bandwidth out alerts.'], 'version_added': '2.3'}",
    "alert_bwquota_enabled": "{'description': ['Set status of bandwidth quota alerts as percentage of network transfer quota.'], 'type': 'bool', 'version_added': '2.3'}",
    "alert_bwquota_threshold": "{'description': ['Set threshold in MB of bandwidth quota alerts.'], 'version_added': '2.3'}",
    "alert_cpu_enabled": "{'description': ['Set status of receiving CPU usage alerts.'], 'type': 'bool', 'version_added': '2.3'}",
    "alert_cpu_threshold": "{'description': ['Set percentage threshold for receiving CPU usage alerts. Each CPU core adds 100% to total.'], 'version_added': '2.3'}",
    "alert_diskio_enabled": "{'description': ['Set status of receiving disk IO alerts.'], 'type': 'bool', 'version_added': '2.3'}",
    "alert_diskio_threshold": "{'description': ['Set threshold for average IO ops/sec over 2 hour period.'], 'version_added': '2.3'}",
    "api_key": "{'description': ['Linode API key']}",
    "backupweeklyday": "{'description': ['Integer value for what day of the week to store weekly backups.'], 'version_added': '2.3'}",
    "datacenter": "{'description': ['datacenter to create an instance in (Linode Datacenter)']}",
    "displaygroup": "{'description': ['Add the instance to a Display Group in Linode Manager.'], 'version_added': '2.3'}",
    "distribution": "{'description': ['distribution to use for the instance (Linode Distribution)']}",
    "kernel_id": "{'description': ['kernel to use for the instance (Linode Kernel)'], 'version_added': '2.4'}",
    "linode_id": "{'description': ['Unique ID of a linode server. This value is read-only in the sense that if you specify it on creation of a Linode it will not be used. The Linode API generates these IDs and we can those generated value here to reference a Linode more specifically. This is useful for idempotence.'], 'aliases': ['lid']}",
    "name": "{'description': ['Name to give the instance (alphanumeric, dashes, underscore).', 'To keep sanity on the Linode Web Console, name is prepended with C(LinodeID-).'], 'required': True}",
    "password": "{'description': ['root password to apply to a new server (auto generated if missing)']}",
    "payment_term": "{'description': ['payment term to use for the instance (payment term in months)'], 'default': 1, 'choices': [1, 12, 24]}",
    "plan": "{'description': ['plan to use for the instance (Linode plan)']}",
    "private_ip": "{'description': ['Add private IPv4 address when Linode is created.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "ssh_pub_key": "{'description': ['SSH public key applied to root user']}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['absent', 'active', 'deleted', 'present', 'restarted', 'started', 'stopped'], 'default': 'present'}",
    "swap": "{'description': ['swap size in MB'], 'default': 512}",
    "wait": "{'description': ['wait for the instance to be in state C(running) before returning'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
    "watchdog": "{'description': ['Set status of Lassie watchdog.'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
}
```

## Examples


``` yaml


- name: Create a new Linode
  linode:
    name: linode-test1
    plan: 1
    datacenter: 7
    distribution: 129
    state: present
  register: linode_creation

- name: Create a server with a private IP Address
  linode:
     module: linode
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 1
     datacenter: 2
     distribution: 99
     password: 'superSecureRootPassword'
     private_ip: yes
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: yes
     wait_timeout: 600
     state: present
  delegate_to: localhost
  register: linode_creation

- name: Fully configure new server
  linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 4
     datacenter: 2
     distribution: 99
     kernel_id: 138
     password: 'superSecureRootPassword'
     private_ip: yes
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: yes
     wait_timeout: 600
     state: present
     alert_bwquota_enabled: True
     alert_bwquota_threshold: 80
     alert_bwin_enabled: True
     alert_bwin_threshold: 10
     alert_cpu_enabled: True
     alert_cpu_threshold: 210
     alert_bwout_enabled: True
     alert_bwout_threshold: 10
     alert_diskio_enabled: True
     alert_diskio_threshold: 10000
     backupweeklyday: 1
     backupwindow: 2
     displaygroup: 'test'
     additional_disks:
      - {Label: 'disk1', Size: 2500, Type: 'raw'}
      - {Label: 'newdisk', Size: 2000}
     watchdog: True
  delegate_to: localhost
  register: linode_creation

- name: Ensure a running server (create if missing)
  linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 1
     datacenter: 2
     distribution: 99
     password: 'superSecureRootPassword'
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: yes
     wait_timeout: 600
     state: present
  delegate_to: localhost
  register: linode_creation

- name: Delete a server
  linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: absent
  delegate_to: localhost

- name: Stop a server
  linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: stopped
  delegate_to: localhost

- name: Reboot a server
  linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: restarted
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Vincent Viallet (@zbal)']
