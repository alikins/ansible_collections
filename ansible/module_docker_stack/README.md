# Ansible module: ansible.module_docker_stack


docker stack module

## Description

Manage docker stacks using the 'docker stack' command on the target node (see examples)

## Requirements

TODO

## Arguments

``` json
{
    "absent_retries": "{'required': False, 'default': 0, 'description': ['If C(>0) and C(state==absent) the module will retry up to C(absent_retries) times to delete the stack until all the resources have been effectively deleted. If the last try still reports the stack as not completely removed the module will fail.']}",
    "absent_retries_interval": "{'required': False, 'default': 1, 'description': ['Interval in seconds between C(absent_retries)']}",
    "compose": "{'required': True, 'default': [], 'description': ['List of compose definitions. Any element may be a string referring to the path of the compose file on the target host or the YAML contents of a compose file nested as dictionary.']}",
    "name": "{'required': True, 'description': ['Stack name']}",
    "prune": "{'required': False, 'default': False, 'description': ['If true will add the C(--prune) option to the C(docker stack deploy) command. This will have docker remove the services not present in the current stack definition.'], 'type': 'bool'}",
    "resolve_image": "{'required': False, 'choices': ['always', 'changed', 'never'], 'description': ['If set will add the C(--resolve-image) option to the C(docker stack deploy) command. This will have docker query the registry to resolve image digest and supported platforms. If not set, docker use "always" by default.']}",
    "state": "{'description': ['Service state.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "with_registry_auth": "{'required': False, 'default': False, 'description': ['If true will add the C(--with-registry-auth) option to the C(docker stack deploy) command. This will have docker send registry authentication details to Swarm agents.'], 'type': 'bool'}",
}
```

## Examples


``` yaml

-   name: deploy 'stack1' stack from file
    docker_stack:
        state: present
        name: stack1
        compose:
        -   /opt/stack.compose

-   name: deploy 'stack2' from base file and yaml overrides
    docker_stack:
        state: present
        name: stack2
        compose:
        -   /opt/stack.compose
        -   version: '3'
            services:
                web:
                    image: nginx:latest
                    environment:
                        ENVVAR: envvar

-   name: deprovision 'stack1'
    docker_stack:
        state: absent

```

## License

TODO

## Author Information
  - ['Dario Zanzico (@dariko)']
