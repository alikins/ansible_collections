# Ansible module: ansible.module_docker_container


manage docker containers

## Description

Manage the life cycle of docker containers.
Supports check mode. Run with --check and --diff to view config difference and list of actions to be taken.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "auto_remove": "{'description': ["enable auto-removal of the container on daemon side when the container's process exits"], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "blkio_weight": "{'description': ['Block IO (relative weight), between 10 and 1000.']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cap_drop": "{'description': ['List of capabilities to drop from the container.'], 'version_added': '2.7'}",
    "capabilities": "{'description': ['List of capabilities to add to the container.']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "cleanup": "{'description': ['Use with I(detach=false) to remove the container after successful execution.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "command": "{'description': ['Command to execute when the container starts. A command may be either a string or a list. Prior to version 2.4, strings were split on commas.']}",
    "comparisons": "{'type': 'dict', 'description': ['Allows to specify how properties of existing containers are compared with module options to decide whether the container should be recreated / updated or not. Only options which correspond to the state of a container as handled by the Docker daemon can be specified.', 'Must be a dictionary specifying for an option one of the keys C(strict), C(ignore) and C(allow_more_present).', 'If C(strict) is specified, values are tested for equality, and changes always result in updating or restarting. If C(ignore) is specified, changes are ignored.', "C(allow_more_present) is allowed only for lists, sets and dicts. If it is specified for lists or sets, the container will only be updated or restarted if the module option contains a value which is not present in the container's options. If the option is specified for a dict, the container will only be updated or restarted if the module option contains a key which isn't present in the container's option, or if the value of a key present differs.", 'The wildcard option C(*) can be used to set one of the default values C(strict) or C(ignore) to I(all) comparisons.', 'See the examples for details.'], 'version_added': '2.8'}",
    "cpu_period": "{'description': ['Limit CPU CFS (Completely Fair Scheduler) period'], 'default': 0}",
    "cpu_quota": "{'description': ['Limit CPU CFS (Completely Fair Scheduler) quota'], 'default': 0}",
    "cpu_shares": "{'description': ['CPU shares (relative weight).']}",
    "cpuset_cpus": "{'description': ['CPUs in which to allow execution C(1,3) or C(1-3).']}",
    "cpuset_mems": "{'description': ['Memory nodes (MEMs) in which to allow execution C(0-3) or C(0,1)']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "detach": "{'description': ['Enable detached mode to leave the container running in background. If disabled, the task will reflect the status of the container run (failed if the command failed).'], 'type': 'bool', 'default': True}",
    "devices": "{'description': ['List of host device bindings to add to the container. Each binding is a mapping expressed in the format: <path_on_host>:<path_in_container>:<cgroup_permissions>']}",
    "dns_opts": "{'description': ['list of DNS options']}",
    "dns_search_domains": "{'description': ['List of custom DNS search domains.']}",
    "dns_servers": "{'description': ['List of custom DNS servers.']}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "domainname": "{'description': ['Container domainname.'], 'version_added': '2.5'}",
    "entrypoint": "{'description': ['Command that overwrites the default ENTRYPOINT of the image.']}",
    "env": "{'description': ['Dictionary of key,value pairs.']}",
    "env_file": "{'version_added': '2.2', 'description': ['Path to a file, present on the target, containing environment variables I(FOO=BAR).', 'If variable also present in C(env), then C(env) value will override.']}",
    "etc_hosts": "{'description': ["Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container's /etc/hosts file."]}",
    "exposed_ports": "{'description': ['List of additional container ports which informs Docker that the container listens on the specified network ports at runtime. If the port is already exposed using EXPOSE in a Dockerfile, it does not need to be exposed again.'], 'aliases': ['exposed', 'expose']}",
    "force_kill": "{'description': ['Use the kill command when stopping a running container.'], 'type': 'bool', 'default': False, 'aliases': ['forcekill']}",
    "groups": "{'description': ['List of additional group names and/or IDs that the container process will run as.']}",
    "hostname": "{'description': ['Container hostname.']}",
    "ignore_image": "{'description': ['When C(state) is I(present) or I(started) the module compares the configuration of an existing container to requested configuration. The evaluation includes the image version. If the image version in the registry does not match the container, the container will be recreated. Stop this behavior by setting C(ignore_image) to I(True).', 'I(Warning:) This option is ignored if C(image) or C(*) is used for the C(comparisons) option.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "image": "{'description': ['Repository path and tag used to create the container. If an image is not found or pull is true, the image will be pulled from the registry. If no tag is included, C(latest) will be used.', 'Can also be an image ID. If this is the case, the image is assumed to be available locally. The C(pull) option is ignored for this case.']}",
    "init": "{'description': ['Run an init inside the container that forwards signals and reaps processes. This option requires Docker API 1.25+.'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "interactive": "{'description': ['Keep stdin open after a container is launched, even if not attached.'], 'type': 'bool', 'default': False}",
    "ipc_mode": "{'description': ["Set the IPC mode for the container. Can be one of 'container:<name|id>' to reuse another container's IPC namespace or 'host' to use the host's IPC namespace within the container."]}",
    "keep_volumes": "{'description': ['Retain volumes associated with a removed container.'], 'type': 'bool', 'default': True}",
    "kernel_memory": "{'description': ['Kernel memory limit (format: C(<number>[<unit>])). Number is a positive integer. Unit can be C(B) (byte), C(K) (kibibyte, 1024B), C(M) (mebibyte), C(G) (gibibyte), C(T) (tebibyte), or C(P) (pebibyte). Minimum is C(4M).', 'Omitting the unit defaults to bytes.'], 'default': 0}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "kill_signal": "{'description': ['Override default signal used to kill a running container.']}",
    "labels": "{'description': ['Dictionary of key value pairs.']}",
    "links": "{'description': ['List of name aliases for linked containers in the format C(container_name:alias).', 'Setting this will force container to be restarted.']}",
    "log_driver": "{'description': ['Specify the logging driver. Docker uses I(json-file) by default.', 'See L(here,https://docs.docker.com/config/containers/logging/configure/) for possible choices.'], 'required': False}",
    "log_options": "{'description': ['Dictionary of options specific to the chosen log_driver. See https://docs.docker.com/engine/admin/logging/overview/ for details.'], 'aliases': ['log_opt']}",
    "mac_address": "{'description': ['Container MAC address (e.g. 92:d0:c6:0a:29:33)']}",
    "memory": "{'description': ['Memory limit (format: C(<number>[<unit>])). Number is a positive integer. Unit can be C(B) (byte), C(K) (kibibyte, 1024B), C(M) (mebibyte), C(G) (gibibyte), C(T) (tebibyte), or C(P) (pebibyte).', 'Omitting the unit defaults to bytes.'], 'default': '0'}",
    "memory_reservation": "{'description': ['Memory soft limit (format: C(<number>[<unit>])). Number is a positive integer. Unit can be C(B) (byte), C(K) (kibibyte, 1024B), C(M) (mebibyte), C(G) (gibibyte), C(T) (tebibyte), or C(P) (pebibyte).', 'Omitting the unit defaults to bytes.'], 'default': 0}",
    "memory_swap": "{'description': ['Total memory limit (memory + swap, format: C(<number>[<unit>])). Number is a positive integer. Unit can be C(B) (byte), C(K) (kibibyte, 1024B), C(M) (mebibyte), C(G) (gibibyte), C(T) (tebibyte), or C(P) (pebibyte).', 'Omitting the unit defaults to bytes.'], 'default': 0}",
    "memory_swappiness": "{'description': ["Tune a container's memory swappiness behavior. Accepts an integer between 0 and 100."], 'default': 0}",
    "name": "{'description': ['Assign a name to a new container or match an existing container.', 'When identifying an existing container name may be a name or a long or short container ID.'], 'required': True}",
    "network_mode": "{'description': ['Connect the container to a network. Choices are "bridge", "host", "none" or "container:<name|id>"']}",
    "networks": "{'description': ['List of networks the container belongs to.', 'Each network is a dict with keys C(name), C(ipv4_address), C(ipv6_address), C(links), C(aliases).', 'For each network C(name) is required, all other keys are optional.', 'If included, C(links) or C(aliases) are lists.', 'For examples of the data structure and usage see EXAMPLES below.', 'To remove a container from one or more networks, use the C(purge_networks) option.', 'Note that as opposed to C(docker run ...), M(docker_container) does not remove the default network if C(networks) is specified. You need to explicity use C(purge_networks) to enforce the removal of the default network (and all other networks not explicitly mentioned in C(networks)).'], 'version_added': '2.2'}",
    "oom_killer": "{'description': ['Whether or not to disable OOM Killer for the container.'], 'type': 'bool', 'default': False}",
    "oom_score_adj": "{'description': ['An integer value containing the score given to the container in order to tune OOM killer preferences.'], 'default': 0, 'version_added': '2.2'}",
    "output_logs": "{'description': ['If set to true, output of the container command will be printed (only effective when log_driver is set to json-file or journald.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "paused": "{'description': ['Use with the started state to pause running processes inside the container.'], 'type': 'bool', 'default': False}",
    "pid_mode": "{'description': ["Set the PID namespace mode for the container. Currently only supports 'host'."]}",
    "privileged": "{'description': ['Give extended privileges to the container.'], 'type': 'bool', 'default': False}",
    "published_ports": "{'description': ['List of ports to publish from the container to the host.', 'Use docker CLI syntax: C(8000), C(9000:8000), or C(0.0.0.0:9000:8000), where 8000 is a container port, 9000 is a host port, and 0.0.0.0 is a host interface.', 'Port ranges can be used for source and destination ports. If two ranges with different lengths are specified, the shorter range will be used.', 'Bind addresses must be either IPv4 or IPv6 addresses. Hostnames are I(not) allowed. This is different from the C(docker) command line utility. Use the L(dig lookup,../lookup/dig.html) to resolve hostnames.', 'Container ports must be exposed either in the Dockerfile or via the C(expose) option.', 'A value of C(all) will publish all exposed container ports to random host ports, ignoring any other mappings.', 'If C(networks) parameter is provided, will inspect each network to see if there exists a bridge network with optional parameter com.docker.network.bridge.host_binding_ipv4. If such a network is found, then published ports where no host IP address is specified will be bound to the host IP pointed to by com.docker.network.bridge.host_binding_ipv4. Note that the first bridge network with a com.docker.network.bridge.host_binding_ipv4 value encountered in the list of C(networks) is the one that will be used.'], 'aliases': ['ports']}",
    "pull": "{'description': ['If true, always pull the latest version of an image. Otherwise, will only pull an image when missing.', 'I(Note) that images are only pulled when specified by name. If the image is specified as a image ID (hash), it cannot be pulled.'], 'type': 'bool', 'default': False}",
    "purge_networks": "{'description': ['Remove the container from ALL networks not included in C(networks) parameter.', 'Any default networks such as I(bridge), if not found in C(networks), will be removed as well.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "read_only": "{'description': ["Mount the container's root file system as read-only."], 'type': 'bool', 'default': False}",
    "recreate": "{'description': ['Use with present and started states to force the re-creation of an existing container.'], 'type': 'bool', 'default': False}",
    "restart": "{'description': ['Use with started state to force a matching container to be stopped and restarted.'], 'type': 'bool', 'default': False}",
    "restart_policy": "{'description': ['Container restart policy. Place quotes around I(no) option.'], 'choices': ['no', 'on-failure', 'always', 'unless-stopped']}",
    "restart_retries": "{'description': ['Use with restart policy to control maximum number of restart attempts.'], 'default': 0}",
    "security_opts": "{'description': ['List of security options in the form of C("label:user:User")']}",
    "shm_size": "{'description': ['Size of C(/dev/shm) (format: C(<number>[<unit>])). Number is positive integer. Unit can be C(B) (byte), C(K) (kibibyte, 1024B), C(M) (mebibyte), C(G) (gibibyte), C(T) (tebibyte), or C(P) (pebibyte).', 'Omitting the unit defaults to bytes. If you omit the size entirely, the system uses C(64M).']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['I(absent) - A container matching the specified name will be stopped and removed. Use force_kill to kill the container rather than stopping it. Use keep_volumes to retain volumes associated with the removed container.', 'I(present) - Asserts the existence of a container matching the name and any provided configuration parameters. If no container matches the name, a container will be created. If a container matches the name but the provided configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be removed and re-created with the requested config. Image version will be taken into account when comparing configuration. To ignore image version use the ignore_image option. Use the recreate option to force the re-creation of the matching container. Use force_kill to kill the container rather than stopping it. Use keep_volumes to retain volumes associated with a removed container.', 'I(started) - Asserts there is a running container matching the name and any provided configuration. If no container matches the name, a container will be created and started. If a container matching the name is found but the configuration does not match, the container will be updated, if it can be. If it cannot be updated, it will be removed and a new container will be created with the requested configuration and started. Image version will be taken into account when comparing configuration. To ignore image version use the ignore_image option. Use recreate to always re-create a matching container, even if it is running. Use restart to force a matching container to be stopped and restarted. Use force_kill to kill a container rather than stopping it. Use keep_volumes to retain volumes associated with a removed container.', 'I(stopped) - Asserts that the container is first I(present), and then if the container is running moves it to a stopped state. Use force_kill to kill a container rather than stopping it.'], 'default': 'started', 'choices': ['absent', 'present', 'stopped', 'started']}",
    "stop_signal": "{'description': ['Override default signal used to stop the container.']}",
    "stop_timeout": "{'description': ['Number of seconds to wait for the container to stop before sending SIGKILL. When the container is created by this module, its C(StopTimeout) configuration will be set to this value.', "When the container is stopped, will be used as a timeout for stopping the container. In case the container has a custom C(StopTimeout) configuration, the behavior depends on the version of docker. New versions of docker will always use the container's configured C(StopTimeout) value if it has been configured."]}",
    "sysctls": "{'description': ['Dictionary of key,value pairs.'], 'version_added': 2.4}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tmpfs": "{'description': ['Mount a tmpfs directory'], 'version_added': 2.4}",
    "trust_image_content": "{'description': ['If C(yes), skip image verification.'], 'type': 'bool', 'default': False}",
    "tty": "{'description': ['Allocate a pseudo-TTY.'], 'type': 'bool', 'default': False}",
    "ulimits": "{'description': ['List of ulimit options. A ulimit is specified as C(nofile:262144:262144)']}",
    "user": "{'description': ['Sets the username or UID used and optionally the groupname or GID for the specified command.', 'Can be [ user | user:group | uid | uid:gid | user:gid | uid:group ]']}",
    "userns_mode": "{'description': ['User namespace to use'], 'version_added': '2.5'}",
    "uts": "{'description': ['Set the UTS namespace mode for the container.']}",
    "volume_driver": "{'description': ['The container volume driver.']}",
    "volumes": "{'description': ['List of volumes to mount within the container.', 'Use docker CLI-style syntax: C(/host:/container[:mode])', 'Mount modes can be a comma-separated list of various modes such as C(ro), C(rw), C(consistent), C(delegated), C(cached), C(rprivate), C(private), C(rshared), C(shared), C(rslave), C(slave). Note that docker might not support all modes and combinations of such modes.', 'SELinux hosts can additionally use C(z) or C(Z) to use a shared or private label for the volume.', 'Note that Ansible 2.7 and earlier only supported one mode, which had to be one of C(ro), C(rw), C(z), and C(Z).']}",
    "volumes_from": "{'description': ['List of container names or Ids to get volumes from.']}",
    "working_dir": "{'description': ['Path to the working directory.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Create a data container
  docker_container:
    name: mydata
    image: busybox
    volumes:
      - /data

- name: Re-create a redis container
  docker_container:
    name: myredis
    image: redis
    command: redis-server --appendonly yes
    state: present
    recreate: yes
    exposed_ports:
      - 6379
    volumes_from:
      - mydata

- name: Restart a container
  docker_container:
    name: myapplication
    image: someuser/appimage
    state: started
    restart: yes
    links:
     - "myredis:aliasedredis"
    devices:
     - "/dev/sda:/dev/xvda:rwm"
    ports:
     - "8080:9000"
     - "127.0.0.1:8081:9001/udp"
    env:
        SECRET_KEY: ssssh

- name: Container present
  docker_container:
    name: mycontainer
    state: present
    image: ubuntu:14.04
    command: sleep infinity

- name: Stop a container
  docker_container:
    name: mycontainer
    state: stopped

- name: Start 4 load-balanced containers
  docker_container:
    name: "container{{ item }}"
    recreate: yes
    image: someuser/anotherappimage
    command: sleep 1d
  with_sequence: count=4

- name: remove container
  docker_container:
    name: ohno
    state: absent

- name: Syslogging output
  docker_container:
    name: myservice
    image: busybox
    log_driver: syslog
    log_options:
      syslog-address: tcp://my-syslog-server:514
      syslog-facility: daemon
      # NOTE: in Docker 1.13+ the "syslog-tag" option was renamed to "tag" for
      # older docker installs, use "syslog-tag" instead
      tag: myservice

- name: Create db container and connect to network
  docker_container:
    name: db_test
    image: "postgres:latest"
    networks:
      - name: "{{ docker_network_name }}"

- name: Start container, connect to network and link
  docker_container:
    name: sleeper
    image: ubuntu:14.04
    networks:
      - name: TestingNet
        ipv4_address: "172.1.1.100"
        aliases:
          - sleepyzz
        links:
          - db_test:db
      - name: TestingNet2

- name: Start a container with a command
  docker_container:
    name: sleepy
    image: ubuntu:14.04
    command: ["sleep", "infinity"]

- name: Add container to networks
  docker_container:
    name: sleepy
    networks:
      - name: TestingNet
        ipv4_address: 172.1.1.18
        links:
          - sleeper
      - name: TestingNet2
        ipv4_address: 172.1.10.20

- name: Update network with aliases
  docker_container:
    name: sleepy
    networks:
      - name: TestingNet
        aliases:
          - sleepyz
          - zzzz

- name: Remove container from one network
  docker_container:
    name: sleepy
    networks:
      - name: TestingNet2
    purge_networks: yes

- name: Remove container from all networks
  docker_container:
    name: sleepy
    purge_networks: yes

- name: Start a container and use an env file
  docker_container:
    name: agent
    image: jenkinsci/ssh-slave
    env_file: /var/tmp/jenkins/agent.env

- name: Create a container with limited capabilities
  docker_container:
    name: sleepy
    image: ubuntu:16.04
    command: sleep infinity
    capabilities:
      - sys_time
    cap_drop:
      - all

- name: Finer container restart/update control
  docker_container:
    name: test
    image: ubuntu:18.04
    env:
      - arg1: true
      - arg2: whatever
    volumes:
      - /tmp:/tmp
    comparisons:
      image: ignore   # don't restart containers with older versions of the image
      env: strict   # we want precisely this environment
      volumes: allow_more_present   # if there are more volumes, that's ok, as long as `/tmp:/tmp` is there

- name: Finer container restart/update control II
  docker_container:
    name: test
    image: ubuntu:18.04
    env:
      - arg1: true
      - arg2: whatever
    comparisons:
      '*': ignore  # by default, ignore *all* options (including image)
      env: strict   # except for environment variables; there, we want to be strict

```

## License

TODO

## Author Information
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
  - ['Cove Schneider (@cove)', 'Joshua Conner (@joshuaconner)', 'Pavel Antonov (@softzilla)', 'Thomas Steinbach (@ThomasSteinbach)', 'Philippe Jandot (@zfil)', 'Daan Oosterveld (@dusdanig)', 'Chris Houseknecht (@chouseknecht)', 'Kassian Sun (@kassiansun)']
