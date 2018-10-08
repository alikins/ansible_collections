# Ansible lookup: ansible.lookup_url


return contents from URL

## Description

Returns the content of the URL requested to be used as data in play.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['urls to query']}",
    "split_lines": "{'description': ['Flag to control if content is returned as a list of lines or as a single text blob'], 'type': 'boolean', 'default': True}",
    "use_proxy": "{'description': ['Flag to control if the lookup will observe HTTP proxy environment variables when present.'], 'type': 'boolean', 'default': True}",
    "validate_certs": "{'description': ['Flag to control SSL certificate validation'], 'type': 'boolean', 'default': True}",
}
```

## Examples


``` yaml

- name: url lookup splits lines by default
  debug: msg="{{item}}"
  loop: "{{ lookup('url', 'https://github.com/gremlin.keys', wantlist=True) }}"

- name: display ip ranges
  debug: msg="{{ lookup('url', 'https://ip-ranges.amazonaws.com/ip-ranges.json', split_lines=False) }}"

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
