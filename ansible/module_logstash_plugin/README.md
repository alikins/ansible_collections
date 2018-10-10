# Ansible module: ansible.module_logstash_plugin


Manage Logstash plugins

## Description

Manages Logstash plugins.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Install plugin with that name.'], 'required': True}",
    "plugin_bin": "{'description': ['Specify logstash-plugin to use for plugin management.'], 'default': '/usr/share/logstash/bin/logstash-plugin'}",
    "proxy_host": "{'description': ['Proxy host to use during plugin installation.']}",
    "proxy_port": "{'description': ['Proxy port to use during plugin installation.']}",
    "state": "{'description': ['Apply plugin state.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "version": "{'description': ['Specify plugin Version of the plugin to install. If plugin exists with previous version, it will NOT be updated.']}",
}
```

## Examples


``` yaml

- name: Install Logstash beats input plugin
  logstash_plugin:
    state: present
    name: logstash-input-beats

- name: Install specific version of a plugin
  logstash_plugin:
    state: present
    name: logstash-input-syslog
    version: '3.2.0'

- name: Uninstall Logstash plugin
  logstash_plugin:
    state: absent
    name: logstash-filter-multiline

- name: install Logstash plugin with alternate heap size
  logstash_plugin:
    state: present
    name: logstash-input-beats
  environment:
    LS_JAVA_OPTS: "-Xms256m -Xmx256m"

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
