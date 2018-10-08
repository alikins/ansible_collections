# Ansible lookup: ansible.lookup_config


Lookup current Ansible configuration values

## Description

Retrieves the value of an Ansible configuration setting.
You can use C(ansible-config list) to see all available settings.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The key(s) to look up'], 'required': True}",
    "on_missing": "{'description': ['action to take if term is missing from config', 'Error will raise a fatal error', 'Skip will just ignore the term', 'Warn will skip over it but issue a warning'], 'default': 'error', 'type': 'string', 'choices': ['error', 'skip', 'warn']}",
}
```

## Examples


``` yaml

    - name: Show configured default become user
      debug: msg="{{ lookup('config', 'DEFAULT_BECOME_USER')}}"

    - name: print out role paths
      debug:
        msg: "These are the configured role paths: {{lookup('config', 'DEFAULT_ROLES_PATH')}}"

    - name: find retry files, skip if missing that key
      find:
        paths: "{{lookup('config', 'RETRY_FILES_SAVE_PATH')|default(playbook_dir, True)}}"
        patterns: "*.retry"

    - name: see the colors
      debug: msg="{{item}}"
      loop: "{{lookup('config', 'COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP', wantlist=True)}}"

    - name: skip if bad value in var
      debug: msg="{{ lookup('config', config_in_var, on_missing='skip')}}"
      var:
        config_in_var: UNKNOWN

```

## License

TODO

## Author Information
  - ['Ansible Core']
