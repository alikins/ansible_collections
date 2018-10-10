# Ansible module: ansible.module_consul_session


Manipulate consul sessions

## Description

Allows the addition, modification and deletion of sessions in a consul cluster. These sessions can then be used in conjunction with key value pairs to implement distributed locks. In depth documentation for working with sessions can be found at http://www.consul.io/docs/internals/sessions.html

## Requirements

TODO

## Arguments

``` json
{
    "behavior": "{'description': ['The optional behavior that can be attached to the session when it is created. This controls the behavior when a session is invalidated.'], 'choices': ['delete', 'release'], 'default': 'release', 'version_added': '2.2'}",
    "checks": "{'description': ['A list of checks that will be used to verify the session health. If all the checks fail, the session will be invalidated and any locks associated with the session will be release and can be acquired once the associated lock delay has expired.']}",
    "datacenter": "{'description': ['The name of the datacenter in which the session exists or should be created.']}",
    "delay": "{'description': ['The optional lock delay that can be attached to the session when it is created. Locks for invalidated sessions ar blocked from being acquired until this delay has expired. Durations are in seconds.'], 'default': 15}",
    "host": "{'description': ['The host of the consul agent defaults to localhost.'], 'default': 'localhost'}",
    "name": "{'description': ['The name that should be associated with the session. This is opaque to Consul and not required.']}",
    "node": "{'description': ['The name of the node that with which the session will be associated. by default this is the name of the agent.']}",
    "port": "{'description': ['The port on which the consul agent is running.'], 'default': 8500}",
    "scheme": "{'description': ['The protocol scheme on which the consul agent is running.'], 'default': 'http', 'version_added': '2.1'}",
    "state": "{'description': ["Whether the session should be present i.e. created if it doesn't exist, or absent, removed if present. If created, the ID for the session is returned in the output. If absent, the name or ID is required to remove the session. Info for a single session, all the sessions for a node or all available sessions can be retrieved by specifying info, node or list for the state; for node or info, the node name or session id is required as parameter."], 'choices': ['absent', 'info', 'list', 'node', 'present'], 'default': 'present'}",
    "validate_certs": "{'description': ['Whether to verify the tls certificate of the consul agent.'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

- name: register basic session with consul
  consul_session:
    name: session1

- name: register a session with an existing check
  consul_session:
    name: session_with_check
    checks:
      - existing_check_name

- name: register a session with lock_delay
  consul_session:
    name: session_with_delay
    delay: 20s

- name: retrieve info about session by id
  consul_session:
    id: session_id
    state: info

- name: retrieve active sessions
  consul_session:
    state: list

```

## License

TODO

## Author Information
  - ['Steve Gargan (@sgargan)']
