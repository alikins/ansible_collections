# Ansible module: ansible.module_docker_network


Manage Docker networks

## Description

Create/remove Docker networks and connect containers to them.
Performs largely the same function as the "docker network" CLI subcommand.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "appends": "{'description': ['By default the connected list is canonical, meaning containers not on the list are removed from the network. Use C(appends) to leave existing containers connected.'], 'type': 'bool', 'default': False, 'aliases': ['incremental']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "connected": "{'description': ['List of container names or container IDs to connect to a network.'], 'aliases': ['containers']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "driver": "{'description': ['Specify the type of network. Docker provides bridge and overlay drivers, but 3rd party drivers can also be used.'], 'default': 'bridge'}",
    "driver_options": "{'description': ['Dictionary of network settings. Consult docker docs for valid options and values.']}",
    "force": "{'description': ['With state I(absent) forces disconnecting all containers from the network prior to deleting the network. With state I(present) will disconnect all containers, delete the network and re-create the network.  This option is required if you have changed the IPAM or driver options and want an existing network to be updated to use the new options.'], 'type': 'bool', 'default': False}",
    "ipam_driver": "{'description': ['Specify an IPAM driver.']}",
    "ipam_options": "{'description': ['Dictionary of IPAM options.']}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "name": "{'description': ['Name of the network to operate on.'], 'required': True, 'aliases': ['network_name']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['I(absent) deletes the network. If a network has connected containers, it cannot be deleted. Use the C(force) option to disconnect all containers and delete the network.', 'I(present) creates the network, if it does not already exist with the specified parameters, and connects the list of containers provided via the connected parameter. Containers not on the list will be disconnected. An empty list will leave no containers connected to the network. Use the C(appends) option to leave existing containers connected. Use the C(force) options to force re-creation of the network.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create a network
  docker_network:
    name: network_one

- name: Remove all but selected list of containers
  docker_network:
    name: network_one
    connected:
      - container_a
      - container_b
      - container_c

- name: Remove a single container
  docker_network:
    name: network_one
    connected: "{{ fulllist|difference(['container_a']) }}"

- name: Add a container to a network, leaving existing containers connected
  docker_network:
    name: network_one
    connected:
      - container_a
    appends: yes

- name: Create a network with options
  docker_network:
    name: network_two
    driver_options:
      com.docker.network.bridge.name: net2
    ipam_options:
      subnet: '172.3.26.0/16'
      gateway: 172.3.26.1
      iprange: '192.168.1.0/24'

- name: Delete a network, disconnecting all containers
  docker_network:
    name: network_one
    state: absent
    force: yes

```

## License

TODO

## Author Information
  - ['Ben Keith (@keitwb)', 'Chris Houseknecht (@chouseknecht)']
  - ['Ben Keith (@keitwb)', 'Chris Houseknecht (@chouseknecht)']
