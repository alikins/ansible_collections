# Ansible module: ansible.module_docker_swarm_service


docker swarm service

## Description

M
a
n
a
g
e
 
d
o
c
k
e
r
 
s
e
r
v
i
c
e
s
.
 
A
l
l
o
w
s
 
l
i
v
e
 
a
l
t
e
r
i
n
g
 
o
f
 
a
l
r
e
a
d
y
 
d
e
f
i
n
e
d
 
s
e
r
v
i
c
e
s



## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "args": "{'required': False, 'default': [], 'description': ['List comprised of the command and the arguments to be run inside', 'the container']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "configs": "{'required': False, 'description': ['List of dictionaries describing the service configs.', 'Every item must be a dictionary exposing the keys config_id, config_name, filename, uid (defaults to 0), gid (defaults to 0), mode (defaults to 0o444)', 'Maps docker service --config option.'], 'default': []}",
    "constraints": "{'required': False, 'default': [], 'description': ['List of the service constraints.', 'Maps docker service --constraint option.']}",
    "container_labels": "{'required': False, 'description': ['List of the service containers labels.', 'Maps docker service --container-label option.'], 'default': []}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "dns": "{'required': False, 'default': [], 'description': ['List of custom DNS servers.', 'Maps docker service --dns option.', 'Requires api_version >= 1.25']}",
    "dns_options": "{'required': False, 'default': [], 'description': ['List of custom DNS options.', 'Maps docker service --dns-option option.', 'Requires api_version >= 1.25']}",
    "dns_search": "{'required': False, 'default': [], 'description': ['List of custom DNS search domains.', 'Maps docker service --dns-search option.', 'Requires api_version >= 1.25']}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "endpoint_mode": "{'required': False, 'description': ['Service endpoint mode.', 'Maps docker service --endpoint-mode option.'], 'default': 'vip', 'choices': ['vip', 'dnsrr']}",
    "env": "{'required': False, 'default': [], 'description': ['List of the service environment variables.', 'Maps docker service --env option.']}",
    "force_update": "{'required': False, 'type': 'bool', 'default': False, 'description': ['Force update even if no changes require it.', 'Maps to docker service update --force option.', 'Requires api_version >= 1.25']}",
    "hostname": "{'required': False, 'default': '', 'description': ['Container hostname', 'Maps docker service --hostname option.', 'Requires api_version >= 1.25']}",
    "image": "{'required': True, 'description': ['Service image path and tag. Maps docker service IMAGE parameter.']}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "labels": "{'required': False, 'description': ['List of the service labels.', 'Maps docker service --label option.']}",
    "limit_cpu": "{'required': False, 'default': 0.0, 'description': ['Service CPU limit. 0 equals no limit.', 'Maps docker service --limit-cpu option.']}",
    "limit_memory": "{'required': False, 'default': 0, 'description': ['Service memory limit in MB. 0 equals no limit.', 'Maps docker service --limit-memory option.']}",
    "log_driver": "{'required': False, 'default': 'json-file', 'description': ['Configure the logging driver for a service']}",
    "log_driver_options": "{'required': False, 'default': [], 'description': ['Options for service logging driver']}",
    "mode": "{'required': False, 'default': 'replicated', 'description': ['Service replication mode.', 'Maps docker service --mode option.']}",
    "mounts": "{'required': False, 'description': ['List of dictionaries describing the service mounts.', "Every item must be a dictionary exposing the keys source, target, type (defaults to 'bind'), readonly (defaults to false)", 'Maps docker service --mount option.'], 'default': []}",
    "name": "{'required': True, 'description': ['Service name']}",
    "networks": "{'required': False, 'default': [], 'description': ['List of the service networks names.', 'Maps docker service --network option.']}",
    "publish": "{'default': [], 'required': False, 'description': ['List of dictionaries describing the service published ports.', "Every item must be a dictionary exposing the keys published_port, target_port, protocol (defaults to 'tcp'), mode <ingress|host>, default to ingress.", 'Only used with api_version >= 1.25']}",
    "replicas": "{'required': False, 'default': -1, 'description': ["Number of containers instantiated in the service. Valid only if ``mode=='replicated'``.", 'If set to -1, and service is not present, service replicas will be set to 1.', 'If set to -1, and service is present, service replicas will be unchanged.', 'Maps docker service --replicas option.']}",
    "reserve_cpu": "{'required': False, 'default': 0.0, 'description': ['Service CPU reservation. 0 equals no reservation.', 'Maps docker service --reserve-cpu option.']}",
    "reserve_memory": "{'required': False, 'default': 0, 'description': ['Service memory reservation in MB. 0 equals no reservation.', 'Maps docker service --reserve-memory option.']}",
    "restart_policy": "{'required': False, 'default': 'none', 'description': ['Restart condition of the service.', 'Maps docker service --restart-condition option.'], 'choices': ['none', 'on-failure', 'any']}",
    "restart_policy_attempts": "{'required': False, 'default': 0, 'description': ['Maximum number of service restarts.', 'Maps docker service --restart-max-attempts option.']}",
    "restart_policy_delay": "{'required': False, 'default': 0, 'description': ['Delay between restarts.', 'Maps docker service --restart-delay option.']}",
    "restart_policy_window": "{'required': False, 'default': 0, 'description': ['Restart policy evaluation window.', 'Maps docker service --restart-window option.']}",
    "secrets": "{'required': False, 'description': ['List of dictionaries describing the service secrets.', 'Every item must be a dictionary exposing the keys secret_id, secret_name, filename, uid (defaults to 0), gid (defaults to 0), mode (defaults to 0o444)', 'Maps docker service --secret option.'], 'default': []}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'required': True, 'default': 'present', 'description': ['Service state.'], 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tty": "{'required': False, 'type': 'bool', 'default': False, 'description': ['Allocate a pseudo-TTY', 'Maps docker service --tty option.', 'Requires api_version >= 1.25']}",
    "update_delay": "{'required': False, 'default': 10, 'description': ['Rolling update delay', 'Maps docker service --update-delay option']}",
    "update_failure_action": "{'required': False, 'default': 'continue', 'description': ['Action to take in case of container failure', 'Maps to docker service --update-failure-action option'], 'choices': ['continue', 'pause']}",
    "update_max_failure_ratio": "{'required': False, 'default': 0.0, 'description': ['Fraction of tasks that may fail during an update before the failure action is invoked', 'Maps to docker service --update-max-failure-ratio']}",
    "update_monitor": "{'required': False, 'default': 5000000000, 'description': ['Time to monitor updated tasks for failures, in nanoseconds.', 'Maps to docker service --update-monitor option']}",
    "update_order": "{'required': False, 'default': 'stop-first', 'description': ['Specifies the order of operations when rolling out an updated task.', 'Maps to docker service --update-order'], 'choices': ['stop-first', 'start-first']}",
    "update_parallelism": "{'required': False, 'default': 1, 'description': ['Rolling update parallelism', 'Maps docker service --update-parallelism option']}",
    "user": "{'required': False, 'default': 'root', 'description': ['username or UID']}",
}
```

## Examples


``` yaml

-   name: define myservice
    docker_swarm_service:
        name: myservice
        image: "alpine"
        args:
        - "sleep"
        - "3600"
        mounts:
        -   source: /tmp/
            target: /remote_tmp/
            type: bind
        env:
        -   "ENVVAR1=envvar1"
        log_driver: fluentd
        log_driver_options:
          fluentd-address: "127.0.0.1:24224"
          fluentd-async-connect: true
          tag: "{{.Name}}/{{.ID}}"
        restart_policy: any
        restart_policy_attempts: 5
        restart_policy_window: 30
    register: dss_out1
-   name: change myservice.env
    docker_swarm_service:
        name: myservice
        image: "alpine"
        args:
        -   "sleep"
        -   "7200"
        mounts:
        -   source: /tmp/
            target: /remote_tmp/
            type: bind
        env:
        -   "ENVVAR1=envvar1"
        restart_policy: any
        restart_policy_attempts: 5
        restart_policy_window: 30
    register: dss_out2
-   name: test for changed myservice facts
    fail:
        msg: unchanged service
    when: "{{ dss_out1 == dss_out2 }}"
-   name: change myservice.image
    docker_swarm_service:
        name: myservice
        image: "alpine:edge"
        args:
        -   "sleep"
        -   "7200"
        mounts:
        -   source: /tmp/
            target: /remote_tmp/
            type: bind
        env:
        -   "ENVVAR1=envvar1"
        restart_policy: any
        restart_policy_attempts: 5
        restart_policy_window: 30
    register: dss_out3
-   name: test for changed myservice facts
    fail:
        msg: unchanged service
    when: "{{ dss_out2 == dss_out3 }}"
-   name: remove mount
    docker_swarm_service:
        name: myservice
        image: "alpine:edge"
        args:
        -   "sleep"
        -   "7200"
        env:
        -   "ENVVAR1=envvar1"
        restart_policy: any
        restart_policy_attempts: 5
        restart_policy_window: 30
    register: dss_out4
-   name: test for changed myservice facts
    fail:
        msg: unchanged service
    when: "{{ dss_out3 == dss_out4 }}"
-   name: keep service as it is
    docker_swarm_service:
        name: myservice
        image: "alpine:edge"
        args:
        -   "sleep"
        -   "7200"
        env:
        -   "ENVVAR1=envvar1"
        restart_policy: any
        restart_policy_attempts: 5
        restart_policy_window: 30
    register: dss_out5
-   name: test for changed service facts
    fail:
        msg: changed service
    when: "{{ dss_out5 != dss_out5 }}"
-   name: remove myservice
    docker_swarm_service:
        name: myservice
        state: absent

```

## License

TODO

## Author Information
  - ['Dario Zanzico (@dariko), Jason Witkowski (@jwitko)']
