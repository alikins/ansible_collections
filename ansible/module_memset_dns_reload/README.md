# Ansible module: ansible.module_memset_dns_reload


Request reload of Memset's DNS infrastructure,

## Description

Request a reload of Memset's DNS infrastructure, and optionally poll until it finishes.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'required': True, 'description': ['The API key obtained from the Memset control panel.']}",
    "poll": "{'default': False, 'type': 'bool', 'description': ["Boolean value, if set will poll the reload job's status and return when the job has completed (unless the 30 second timeout is reached first). If the timeout is reached then the task will not be marked as failed, but stderr will indicate that the polling failed."]}",
}
```

## Examples


``` yaml

- name: submit DNS reload and poll.
  memset_dns_reload:
    api_key: 5eb86c9196ab03919abcf03857163741
    poll: True
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Simon Weald (@analbeard)']
