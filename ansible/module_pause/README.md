# Ansible module: ansible.module_pause


Pause playbook execution

## Description

Pauses playbook execution for a set amount of time, or until a prompt is acknowledged. All parameters are optional. The default behavior is to pause with a prompt.
To pause/wait/sleep per host, use the M(wait_for) module.
You can use C(ctrl+c) if you wish to advance a pause earlier than it is set to expire or if you need to abort a playbook run entirely. To continue early press C(ctrl+c) and then C(c). To abort a playbook press C(ctrl+c) and then C(a).
The pause module integrates into async/parallelized playbooks without any special considerations (see Rolling Updates). When using pauses with the C(serial) playbook parameter (as in rolling updates) you are only prompted once for the current group of hosts.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "echo": "{'description': ['Controls whether or not keyboard input is shown when typing.', "Has no effect if 'seconds' or 'minutes' is set."], 'type': 'bool', 'default': True, 'version_added': 2.5}",
    "minutes": "{'description': ['A positive number of minutes to pause for.']}",
    "prompt": "{'description': ['Optional text to use for the prompt message.']}",
    "seconds": "{'description': ['A positive number of seconds to pause for.']}",
}
```

## Examples


``` yaml

# Pause for 5 minutes to build app cache.
- pause:
    minutes: 5

# Pause until you can verify updates to an application were successful.
- pause:

# A helpful reminder of what to look out for post-update.
- pause:
    prompt: "Make sure org.foo.FooOverload exception is not present"

# Pause to get some sensitive input.
- pause:
    prompt: "Enter a secret"
    echo: no

```

## License

TODO

## Author Information
  - ['Tim Bielawa (@tbielawa)']
