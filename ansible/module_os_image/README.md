# Ansible module: ansible.module_os_image


Add/Delete images from OpenStack Cloud

## Description

Add or Remove images from the OpenStack Image Repository

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "checksum": "{'version_added': '2.5', 'description': ['The checksum of the image']}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "container_format": "{'description': ['The format of the container'], 'default': 'bare'}",
    "disk_format": "{'description': ['The format of the disk that is getting uploaded'], 'default': 'qcow2'}",
    "filename": "{'description': ['The path to the file which has to be uploaded']}",
    "id": "{'version_added': '2.4', 'description': ['The Id of the image']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "is_public": "{'description': ['Whether the image can be accessed publicly. Note that publicizing an image requires admin role by default.'], 'type': 'bool', 'default': True}",
    "kernel": "{'description': ['The name of an existing kernel image that will be associated with this image']}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "min_disk": "{'description': ['The minimum disk space (in GB) required to boot this image']}",
    "min_ram": "{'description': ['The minimum ram (in MB) required to boot this image']}",
    "name": "{'description': ['Name that has to be given to the image'], 'required': True}",
    "owner": "{'description': ['The owner of the image']}",
    "properties": "{'description': ['Additional properties to be associated with this image'], 'default': {}}",
    "ramdisk": "{'description': ['The name of an existing ramdisk image that will be associated with this image']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Upload an image from a local file named cirros-0.3.0-x86_64-disk.img
- os_image:
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: passme
      project_name: admin
    name: cirros
    container_format: bare
    disk_format: qcow2
    state: present
    filename: cirros-0.3.0-x86_64-disk.img
    kernel: cirros-vmlinuz
    ramdisk: cirros-initrd
    properties:
      cpu_arch: x86_64
      distro: ubuntu

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
