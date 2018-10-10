# Ansible module: ansible.module_kibana_plugin


Manage Kibana plugins

## Description

Manages Kibana plugins.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Delete and re-install the plugin. Can be useful for plugins update'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the plugin to install'], 'required': True}",
    "plugin_bin": "{'description': ['Location of the plugin binary'], 'default': '/opt/kibana/bin/kibana'}",
    "plugin_dir": "{'description': ['Your configured plugin directory specified in Kibana'], 'default': '/opt/kibana/installedPlugins/'}",
    "state": "{'description': ['Desired state of a plugin.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Timeout setting: 30s, 1m, 1h...'], 'default': '1m'}",
    "url": "{'description': ['Set exact URL to download the plugin from. For local file, prefix its absolute path with file://']}",
    "version": "{'description': ['Version of the plugin to be installed. If plugin exists with previous version, it will NOT be updated if C(force) is not set to yes']}",
}
```

## Examples


``` yaml

- name: Install Elasticsearch head plugin
  kibana_plugin:
    state: present
    name: elasticsearch/marvel

- name: Install specific version of a plugin
  kibana_plugin:
    state: present
    name: elasticsearch/marvel
    version: '2.3.3'

- name: Uninstall Elasticsearch head plugin
  kibana_plugin:
    state: absent
    name: elasticsearch/marvel

```

## License

TODO

## Author Information
  - ['Thierno IB. BARRY (@barryib)']
