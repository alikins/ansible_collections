# Ansible module: ansible.module_clc_server


Create, Delete, Start and Stop servers in CenturyLink Cloud

## Description

An Ansible module to Create, Delete, Start and Stop servers in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "add_public_ip": "{'description': ['Whether to add a public ip to the server'], 'type': 'bool', 'default': False}",
    "additional_disks": "{'description': ['The list of additional disks for the server'], 'default': []}",
    "alert_policy_id": "{'description': ["The alert policy to assign to the server. This is mutually exclusive with 'alert_policy_name'."]}",
    "alert_policy_name": "{'description': ["The alert policy to assign to the server. This is mutually exclusive with 'alert_policy_id'."]}",
    "alias": "{'description': ['The account alias to provision the servers under.']}",
    "anti_affinity_policy_id": "{'description': ["The anti-affinity policy to assign to the server. This is mutually exclusive with 'anti_affinity_policy_name'."]}",
    "anti_affinity_policy_name": "{'description': ["The anti-affinity policy to assign to the server. This is mutually exclusive with 'anti_affinity_policy_id'."]}",
    "configuration_id": "{'description': ['Only required for bare metal servers. Specifies the identifier for the specific configuration type of bare metal server to deploy.']}",
    "count": "{'description': ['The number of servers to build (mutually exclusive with exact_count)'], 'default': 1}",
    "count_group": "{'description': ['Required when exact_count is specified.  The Server Group use to determine how many severs to deploy.']}",
    "cpu": "{'description': ['How many CPUs to provision on the server'], 'default': 1}",
    "cpu_autoscale_policy_id": "{'description': ['The autoscale policy to assign to the server.']}",
    "custom_fields": "{'description': ['The list of custom fields to set on the server.'], 'default': []}",
    "description": "{'description': ['The description to set for the server.']}",
    "exact_count": "{'description': ['Run in idempotent mode.  Will insure that this exact number of servers are running in the provided group, creating and deleting them to reach that count.  Requires count_group to be set.']}",
    "group": "{'description': ['The Server Group to create servers under.'], 'default': 'Default Group'}",
    "ip_address": "{'description': ['The IP Address for the server. One is assigned if not provided.']}",
    "location": "{'description': ['The Datacenter to create servers in.']}",
    "managed_os": "{'description': ["Whether to create the server as 'Managed' or not."], 'type': 'bool', 'default': False, 'required': False}",
    "memory": "{'description': ['Memory in GB.'], 'default': 1}",
    "name": "{'description': ["A 1 to 6 character identifier to use for the server. This is required when state is 'present'"]}",
    "network_id": "{'description': ['The network UUID on which to create servers.']}",
    "os_type": "{'description': ['Only required for bare metal servers. Specifies the OS to provision with the bare metal server.'], 'choices': ['redHat6_64Bit', 'centOS6_64Bit', 'windows2012R2Standard_64Bit', 'ubuntu14_64Bit']}",
    "packages": "{'description': ['The list of blue print packages to run on the server after its created.'], 'default': []}",
    "password": "{'description': ['Password for the administrator / root user']}",
    "primary_dns": "{'description': ['Primary DNS used by the server.']}",
    "public_ip_ports": "{'description': ['A list of ports to allow on the firewall to the servers public ip, if add_public_ip is set to True.'], 'default': []}",
    "public_ip_protocol": "{'description': ['The protocol to use for the public ip if add_public_ip is set to True.'], 'default': 'TCP', 'choices': ['TCP', 'UDP', 'ICMP']}",
    "secondary_dns": "{'description': ['Secondary DNS used by the server.']}",
    "server_ids": "{'description': ['Required for started, stopped, and absent states. A list of server Ids to insure are started, stopped, or absent.'], 'default': []}",
    "source_server_password": "{'description': ['The password for the source server if a clone is specified.']}",
    "state": "{'description': ['The state to insure that the provided resources are in.'], 'default': 'present', 'choices': ['present', 'absent', 'started', 'stopped']}",
    "storage_type": "{'description': ['The type of storage to attach to the server.'], 'default': 'standard', 'choices': ['standard', 'hyperscale']}",
    "template": "{'description': ["The template to use for server creation.  Will search for a template if a partial string is provided. This is required when state is 'present'"]}",
    "ttl": "{'description': ['The time to live for the server in seconds.  The server will be deleted when this time expires.']}",
    "type": "{'description': ['The type of server to create.'], 'default': 'standard', 'choices': ['standard', 'hyperscale', 'bareMetal']}",
    "wait": "{'description': ['Whether to wait for the provisioning tasks to finish before returning.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Provision a single Ubuntu Server
  clc_server:
    name: test
    template: ubuntu-14-64
    count: 1
    group: Default Group
    state: present

- name: Ensure 'Default Group' has exactly 5 servers
  clc_server:
    name: test
    template: ubuntu-14-64
    exact_count: 5
    count_group: Default Group
    group: Default Group

- name: Stop a Server
  clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: stopped

- name: Start a Server
  clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: started

- name: Delete a Server
  clc_server:
    server_ids:
      - UC1ACCT-TEST01
    state: absent

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
