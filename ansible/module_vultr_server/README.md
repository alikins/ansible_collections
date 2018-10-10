# Ansible module: ansible.module_vultr_server


Manages virtual servers on Vultr

## Description

Deploy, start, stop, update, restart, reinstall servers.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "auto_backup_enabled": "{'description': ['Whether to enable automatic backups or not.'], 'type': 'bool'}",
    "firewall_group": "{'description': ['The firewall group to assign this server to.']}",
    "force": "{'description': ['Force stop/start the server if required to apply changes', 'Otherwise a running server will not be changed.'], 'type': 'bool'}",
    "hostname": "{'description': ['Hostname to assign to this server.']}",
    "ipv6_enabled": "{'description': ['Whether to enable IPv6 or not.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the server.'], 'required': True, 'aliases': ['label']}",
    "notify_activate": "{'description': ['Whether to send an activation email when the server is ready or not.', 'Only considered on creation.'], 'type': 'bool'}",
    "os": "{'description': ['The operating system.', 'Required if the server does not yet exist.']}",
    "plan": "{'description': ['Plan to use for the server.', 'Required if the server does not yet exist.']}",
    "private_network_enabled": "{'description': ['Whether to enable private networking or not.'], 'type': 'bool'}",
    "region": "{'description': ['Region the server is deployed into.', 'Required if the server does not yet exist.']}",
    "reserved_ip_v4": "{'description': ['IP address of the floating IP to use as the main IP of this server.', 'Only considered on creation.']}",
    "ssh_keys": "{'description': ['List of SSH keys passed to the server on creation.'], 'aliases': ['ssh_key']}",
    "startup_script": "{'description': ['Name of the startup script to execute on boot.', 'Only considered while creating the server.']}",
    "state": "{'description': ['State of the server.'], 'default': 'present', 'choices': ['present', 'absent', 'restarted', 'reinstalled', 'started', 'stopped']}",
    "tag": "{'description': ['Tag for the server.']}",
    "user_data": "{'description': ['User data to be passed to the server.']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: create server
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    os: CentOS 7 x64
    plan: 1024 MB RAM,25 GB SSD,1.00 TB BW
    region: Amsterdam
    state: present

- name: ensure a server is present and started
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    os: CentOS 7 x64
    plan: 1024 MB RAM,25 GB SSD,1.00 TB BW
    region: Amsterdam
    state: started

- name: ensure a server is present and stopped
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    os: CentOS 7 x64
    plan: 1024 MB RAM,25 GB SSD,1.00 TB BW
    region: Amsterdam
    state: stopped

- name: ensure an existing server is stopped
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    state: stopped

- name: ensure an existing server is started
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    state: started

- name: ensure a server is absent
  local_action:
    module: vultr_server
    name: "{{ vultr_server_name }}"
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
