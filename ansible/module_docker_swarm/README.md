# Ansible module: ansible.module_docker_swarm


Manage Swarm cluster

## Description

Create a new Swarm cluster.
Add/Remove nodes or managers to an existing cluster.

## Requirements

TODO

## Arguments

``` json
{
    "advertise_addr": "{'description': ['Externally reachable address advertised to other nodes.', 'This can either be an address/port combination in the form C(192.168.1.1:4567), or an interface followed by a port number, like C(eth0:4567).', 'If the port number is omitted, the port number from the listen address is used.', 'If C(advertise_addr) is not specified, it will be automatically detected when possible.']}",
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "autolock_managers": "{'description': ['If set, generate a key and use it to lock data stored on the managers.', 'Docker default value is C(no).'], 'type': 'bool'}",
    "ca_force_rotate": "{'description': ['An integer whose purpose is to force swarm to generate a new signing CA certificate and key, if none have been specified.', 'Docker default value is C(0).']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "dispatcher_heartbeat_period": "{'description': ['The delay for an agent to send a heartbeat to the dispatcher.', 'Docker default value is C(5s).']}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "election_tick": "{'description': ['Amount of ticks (in seconds) needed without a leader to trigger a new election.', 'Docker default value is C(10s).']}",
    "force": "{'description': ['Use with state C(present) to force creating a new Swarm, even if already part of one.', 'Use with state C(absent) to Leave the swarm even if this node is a manager.'], 'type': 'bool', 'default': False}",
    "heartbeat_tick": "{'description': ['Amount of ticks (in seconds) between each heartbeat.', 'Docker default value is C(1s).']}",
    "join_token": "{'description': ['Swarm token used to join a swarm cluster.', 'Used with I(state=join).']}",
    "keep_old_snapshots": "{'description': ['Number of snapshots to keep beyond the current snapshot.', 'Docker default value is C(0).']}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "labels": "{'description': ['User-defined key/value metadata.']}",
    "listen_addr": "{'description': ['Listen address used for inter-manager communication.', 'This can either be an address/port combination in the form C(192.168.1.1:4567), or an interface followed by a port number, like C(eth0:4567).', 'If the port number is omitted, the default swarm listening port is used.'], 'default': '0.0.0.0:2377'}",
    "log_entries_for_slow_followers": "{'description': ['Number of log entries to keep around to sync up slow followers after a snapshot is created.']}",
    "name": "{'description': ['The name of the swarm.']}",
    "node_cert_expiry": "{'description': ['Automatic expiry for nodes certificates.', 'Docker default value is C(3months).']}",
    "node_id": "{'description': ['Swarm id of the node to remove.', 'Used with I(state=remove).']}",
    "remote_addrs": "{'description': ['Remote address of a manager to connect to.', 'Used with I(state=join).']}",
    "rotate_manager_token": "{'description': ['Rotate the manager join token.'], 'type': 'bool', 'default': False}",
    "rotate_worker_token": "{'description': ['Rotate the worker join token.'], 'type': 'bool', 'default': False}",
    "signing_ca_cert": "{'description': ['The desired signing CA certificate for all swarm node TLS leaf certificates, in PEM format.']}",
    "signing_ca_key": "{'description': ['The desired signing CA key for all swarm node TLS leaf certificates, in PEM format.']}",
    "snapshot_interval": "{'description': ['Number of logs entries between snapshot.', 'Docker default value is C(10000).']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['Set to C(present), to create/update a new cluster.', 'Set to C(join), to join an existing cluster.', 'Set to C(absent), to leave an existing cluster.', 'Set to C(remove), to remove an absent node from the cluster.', 'Set to C(inspect) to display swarm informations.'], 'required': True, 'default': 'present', 'choices': ['present', 'join', 'absent', 'remove', 'inspect']}",
    "task_history_retention_limit": "{'description': ['Maximum number of tasks history stored.', 'Docker default value is C(5).']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml


- name: Init a new swarm with default parameters
  docker_swarm:
    state: present
    advertise_addr: 192.168.1.1

- name: Update swarm configuration
  docker_swarm:
    state: present
    election_tick: 5

- name: Add nodes
  docker_swarm:
    state: join
    advertise_addr: 192.168.1.2
    join_token: SWMTKN-1--xxxxx
    remote_addrs: [ '192.168.1.1:2377' ]

- name: Leave swarm for a node
  docker_swarm:
    state: absent

- name: Remove a swarm manager
  docker_swarm:
    state: absent
    force: true

- name: Remove node from swarm
  docker_swarm:
    state: remove
    node_id: mynode

- name: Inspect swarm
  docker_swarm:
    state: inspect
  register: swarm_info

```

## License

TODO

## Author Information
  - ['Thierry Bouvet (@tbouvet)']
