# Ansible inventory: ansible.inventory_vmware_vm_inventory


VMware Guest inventory source

## Description

Get virtual machines as inventory hosts from VMware environment.
Uses any file which ends with vmware.yml or vmware.yaml as a YAML configuration file.
The inventory_hostname is always the 'Name' and UUID of the virtual machine. UUID is added as VMware allows virtual machines with the same name.

## Requirements

TODO

## Arguments

``` json
{
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "hostname": "{'description': ['Name of vCenter or ESXi server.'], 'required': True, 'env': [{'name': 'VMWARE_SERVER'}]}",
    "password": "{'description': ['Password of vSphere admin user.'], 'required': True, 'env': [{'name': 'VMWARE_PASSWORD'}]}",
    "port": "{'description': ['Port number used to connect to vCenter or ESXi Server.'], 'default': 443, 'env': [{'name': 'VMWARE_PORT'}]}",
    "username": "{'description': ['Name of vSphere admin user.'], 'required': True, 'env': [{'name': 'VMWARE_USERNAME'}]}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.'], 'default': True, 'type': 'boolean'}",
    "with_tags": "{'description': ['Include tags and associated virtual machines.', "Requires 'vSphere Automation SDK' and 'vCloud Suite SDK' libraries to be installed on the given controller machine.", 'Please refer following URLs for installation steps', 'https://code.vmware.com/web/sdk/65/vsphere-automation-python', 'https://code.vmware.com/web/sdk/60/vcloudsuite-python'], 'default': False, 'type': 'boolean'}",
}
```

## Examples


``` yaml

    # Sample configuration file for VMware Guest dynamic inventory
    plugin: vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    with_tags: True

```

## License

TODO

## Author Information
  - ['UNKNOWN']
