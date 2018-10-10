# Ansible module: ansible.module_os_quota


Manage OpenStack Quotas

## Description

Manage OpenStack Quotas. Quotas can be created, updated or deleted using this module. A quota will be updated if matches an existing project and is present.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "backup_gigabytes": "{'description': ["Maximum size of backups in GB's."]}",
    "backups": "{'description': ['Maximum number of backups allowed.']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "cores": "{'description': ["Maximum number of CPU's per project."]}",
    "fixed_ips": "{'description': ["Number of fixed IP's to allow."]}",
    "floating_ips": "{'description': ["Number of floating IP's to allow in Compute."], 'aliases': ['compute_floating_ips']}",
    "floatingip": "{'description': ["Number of floating IP's to allow in Network."], 'aliases': ['network_floating_ips']}",
    "gigabytes": "{'description': ['Maximum volume storage allowed for project.']}",
    "gigabytes_lvm": "{'description': ["Maximum size in GB's of individual lvm volumes."]}",
    "injected_file_size": "{'description': ['Maximum file size in bytes.']}",
    "injected_files": "{'description': ['Number of injected files to allow.']}",
    "injected_path_size": "{'description': ['Maximum path size.']}",
    "instances": "{'description': ['Maximum number of instances allowed.']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "key_pairs": "{'description': ['Number of key pairs to allow.']}",
    "loadbalancer": "{'description': ['Number of load balancers to allow.'], 'version_added': '2.4'}",
    "name": "{'description': ['Name of the OpenStack Project to manage.'], 'required': True}",
    "network": "{'description': ['Number of networks to allow.']}",
    "per_volume_gigabytes": "{'description': ["Maximum size in GB's of individual volumes."]}",
    "pool": "{'description': ['Number of load balancer pools to allow.'], 'version_added': '2.4'}",
    "port": "{'description': ['Number of Network ports to allow, this needs to be greater than the instances limit.']}",
    "properties": "{'description': ['Number of properties to allow.']}",
    "ram": "{'description': ['Maximum amount of ram in MB to allow.']}",
    "rbac_policy": "{'description': ['Number of policies to allow.']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "router": "{'description': ['Number of routers to allow.']}",
    "security_group": "{'description': ['Number of security groups to allow.']}",
    "security_group_rule": "{'description': ['Number of rules per security group to allow.']}",
    "server_group_members": "{'description': ['Number of server group members to allow.']}",
    "server_groups": "{'description': ['Number of server groups to allow.']}",
    "snapshots": "{'description': ['Number of snapshots to allow.']}",
    "snapshots_lvm": "{'description': ['Number of LVM snapshots to allow.']}",
    "state": "{'description': ['A value of present sets the quota and a value of absent resets the quota to system defaults.'], 'default': 'present'}",
    "subnet": "{'description': ['Number of subnets to allow.']}",
    "subnetpool": "{'description': ['Number of subnet pools to allow.']}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "volumes": "{'description': ['Number of volumes to allow.']}",
    "volumes_lvm": "{'description': ['Number of LVM volumes to allow.']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# List a Project Quota
- os_quota:
    cloud: mycloud
    name: demoproject

# Set a Project back to the defaults
- os_quota:
    cloud: mycloud
    name: demoproject
    state: absent

# Update a Project Quota for cores
- os_quota:
    cloud: mycloud
    name: demoproject
    cores: 100

# Update a Project Quota
- os_quota:
    name: demoproject
    cores: 1000
    volumes: 20
    volumes_type:
      - volume_lvm: 10

# Complete example based on list of projects
- name: Update quotas
  os_quota:
    name: "{{ item.name }}"
    backup_gigabytes: "{{ item.backup_gigabytes }}"
    backups: "{{ item.backups }}"
    cores: "{{ item.cores }}"
    fixed_ips: "{{ item.fixed_ips }}"
    floating_ips: "{{ item.floating_ips }}"
    floatingip: "{{ item.floatingip }}"
    gigabytes: "{{ item.gigabytes }}"
    injected_file_size: "{{ item.injected_file_size }}"
    injected_files: "{{ item.injected_files }}"
    injected_path_size: "{{ item.injected_path_size }}"
    instances: "{{ item.instances }}"
    key_pairs: "{{ item.key_pairs }}"
    loadbalancer: "{{ item.loadbalancer }}"
    per_volume_gigabytes: "{{ item.per_volume_gigabytes }}"
    pool: "{{ item.pool }}"
    port: "{{ item.port }}"
    properties: "{{ item.properties }}"
    ram: "{{ item.ram }}"
    security_group_rule: "{{ item.security_group_rule }}"
    security_group: "{{ item.security_group }}"
    server_group_members: "{{ item.server_group_members }}"
    server_groups: "{{ item.server_groups }}"
    snapshots: "{{ item.snapshots }}"
    volumes: "{{ item.volumes }}"
    volumes_types:
      volumes_lvm: "{{ item.volumes_lvm }}"
    snapshots_types:
      snapshots_lvm: "{{ item.snapshots_lvm }}"
    gigabytes_types:
      gigabytes_lvm: "{{ item.gigabytes_lvm }}"
  with_items:
    - "{{ projects }}"
  when: item.state == "present"

```

## License

TODO

## Author Information
  - ['Michael Gale (gale.michael@gmail.com)']
