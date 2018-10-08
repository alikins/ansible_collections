# Ansible inventory: ansible.inventory_auto


Loads and executes an inventory plugin specified in a YAML config

## Description

By whitelisting C(auto) as the final inventory plugin, any YAML inventory config file with a C(plugin) key at its root will automatically cause the named plugin to be loaded and executed with that config. This effectively provides automatic whitelisting of all installed/accessible inventory plugins.
To disable this behavior, remove C(auto) from the C(INVENTORY_ENABLED) config element.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

# This plugin is not intended for direct use; it is a fallback mechanism for automatic whitelisting of
# all installed inventory plugins.

```

## License

TODO

## Author Information
  - ['Matt Davis <@nitzmahone>']
