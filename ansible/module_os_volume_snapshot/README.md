# Ansible module: ansible.module_os_volume_snapshot


Create/Delete Cinder Volume Snapshots

## Description

Create or Delete cinder block storage volume snapshots

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Availability zone in which to create the snapshot.']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "display_description": "{'description': ['String describing the snapshot'], 'aliases': ['description']}",
    "display_name": "{'description': ['Name of the snapshot'], 'required': True, 'aliases': ['name']}",
    "force": "{'description': ['Allows or disallows snapshot of a volume to be created when the volume is attached to an instance.'], 'type': 'bool', 'default': False}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "volume": "{'description': ['The volume name or id to create/delete the snapshot'], 'required': True}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Creates a snapshot on volume 'test_volume'
- name: create and delete snapshot
  hosts: localhost
  tasks:
  - name: create snapshot
    os_volume_snapshot:
      state: present
      cloud: mordred
      availability_zone: az2
      display_name: test_snapshot
      volume: test_volume
  - name: delete snapshot
    os_volume_snapshot:
      state: absent
      cloud: mordred
      availability_zone: az2
      display_name: test_snapshot
      volume: test_volume

```

## License

TODO

## Author Information
  - ['Mario Santos (@ruizink)']
