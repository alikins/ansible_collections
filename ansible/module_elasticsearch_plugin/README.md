# Ansible module: ansible.module_elasticsearch_plugin


Manage Elasticsearch plugins

## Description

Manages Elasticsearch plugins.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Force batch mode when installing plugins. This is only necessary if a plugin requires additional permissions and console detection fails.'], 'default': False, 'version_added': '2.7'}",
    "name": "{'description': ['Name of the plugin to install.'], 'required': True}",
    "plugin_bin": "{'description': ['Location of the plugin binary. If this file is not found, the default plugin binaries will be used.', 'The default changed in Ansible 2.4 to None.']}",
    "plugin_dir": "{'description': ['Your configured plugin directory specified in Elasticsearch'], 'default': '/usr/share/elasticsearch/plugins/'}",
    "proxy_host": "{'description': ['Proxy host to use during plugin installation'], 'version_added': '2.1'}",
    "proxy_port": "{'description': ['Proxy port to use during plugin installation'], 'version_added': '2.1'}",
    "src": "{'description': ['Optionally set the source location to retrieve the plugin from. This can be a file:// URL to install from a local file, or a remote URL. If this is not set, the plugin location is just based on the name.', 'The name parameter must match the descriptor in the plugin ZIP specified.', 'Is only used if the state would change, which is solely checked based on the name parameter. If, for example, the plugin is already installed, changing this has no effect.', 'For ES 1.x use url.'], 'required': False, 'version_added': '2.7'}",
    "state": "{'description': ['Desired state of a plugin.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Timeout setting: 30s, 1m, 1h...', 'Only valid for Elasticsearch < 5.0. This option is ignored for Elasticsearch > 5.0.'], 'default': '1m'}",
    "url": "{'description': ['Set exact URL to download the plugin from (Only works for ES 1.x).', 'For ES 2.x and higher, use src.'], 'required': False}",
    "version": "{'description': ['Version of the plugin to be installed. If plugin exists with previous version, it will NOT be updated']}",
}
```

## Examples


``` yaml

# Install Elasticsearch Head plugin in Elasticsearch 2.x
- elasticsearch_plugin:
    name: mobz/elasticsearch-head
    state: present

# Install a specific version of Elasticsearch Head in Elasticsearch 2.x
- elasticsearch_plugin:
    name: mobz/elasticsearch-head
    version: 2.0.0

# Uninstall Elasticsearch head plugin in Elasticsearch 2.x
- elasticsearch_plugin:
    name: mobz/elasticsearch-head
    state: absent

# Install a specific plugin in Elasticsearch >= 5.0
- elasticsearch_plugin:
    name: analysis-icu
    state: present

# Install the ingest-geoip plugin with a forced installation
- elasticsearch_plugin:
    name: ingest-geoip
    state: present
    force: yes

```

## License

TODO

## Author Information
  - ['Mathew Davies (@ThePixelDeveloper)', 'Sam Doran (@samdoran)']
  - ['Mathew Davies (@ThePixelDeveloper)', 'Sam Doran (@samdoran)']
