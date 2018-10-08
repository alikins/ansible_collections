# Ansible inventory: ansible.inventory_openstack


OpenStack inventory source

## Description

Get inventory hosts from OpenStack clouds
Uses openstack.(yml|yaml) YAML configuration file to configure the inventory plugin
Uses standard clouds.yaml YAML configuration file to configure cloud credentials

## Requirements

TODO

## Arguments

``` json
{
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "clouds_yaml_path": "{'description': ['Override path to clouds.yaml file. If this value is given it\nwill be searched first. The default path for the\nansible inventory adds /etc/ansible/openstack.yaml and\n/etc/ansible/openstack.yml to the regular locations documented\nat https://docs.openstack.org/os-client-config/latest/user/configuration.html#config-files\n'], 'type': 'string'}",
    "compose": "{'description': ['Create vars from jinja2 expressions.'], 'type': 'dictionary', 'default': {}}",
    "expand_hostvars": "{'description': ["Run extra commands on each host to fill in additional\ninformation about the host. May interrogate cinder and\nneutron and can be expensive for people with many hosts.\n(Note, the default value of this is opposite from the default\nold openstack.py inventory script's option expand_hostvars)\n"], 'type': 'bool', 'default': False}",
    "fail_on_errors": "{'description': ["Causes the inventory to fail and return no hosts if one cloud\nhas failed (for example, bad credentials or being offline).\nWhen set to False, the inventory will return as many hosts as\nit can from as many clouds as it can contact. (Note, the\ndefault value of this is opposite from the old openstack.py\ninventory script's option fail_on_errors)\n"], 'type': 'bool', 'default': False}",
    "groups": "{'description': ['Add hosts to group based on Jinja2 conditionals.'], 'type': 'dictionary', 'default': {}}",
    "inventory_hostname": "{'description': ["What to register as the inventory hostname.\nIf set to 'uuid' the uuid of the server will be used and a\ngroup will be created for the server name.\nIf set to 'name' the name of the server will be used unless\nthere are more than one server with the same name in which\ncase the 'uuid' logic will be used.\nDefault is to do 'name', which is the opposite of the old\nopenstack.py inventory script's option use_hostnames)\n"], 'type': 'string', 'choices': ['name', 'uuid'], 'default': 'name'}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "only_clouds": "{'description': ['List of clouds from clouds.yaml to use, instead of using\nthe whole list.\n'], 'type': 'list', 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'openstack' plugin."], 'required': True, 'choices': ['openstack']}",
    "private": "{'description': ["Use the private interface of each server, if it has one, as\nthe host's IP in the inventory. This can be useful if you are\nrunning ansible inside a server in the cloud and would rather\ncommunicate to your servers over the private network.\n"], 'type': 'bool', 'default': False}",
    "show_all": "{'description': ['toggles showing all vms vs only those with a working IP'], 'type': 'bool', 'default': False}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
}
```

## Examples


``` yaml

# file must be named openstack.yaml or openstack.yml
# Make the plugin behave like the default behavior of the old script
plugin: openstack
expand_hostvars: yes
fail_on_errors: yes

```

## License

TODO

## Author Information
  - ['Marco Vito Moscaritolo <marco@agavee.com>', 'Jesse Keating <jesse.keating@rackspace.com>']
  - ['Marco Vito Moscaritolo <marco@agavee.com>', 'Jesse Keating <jesse.keating@rackspace.com>']
