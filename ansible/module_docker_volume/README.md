# Ansible module: ansible.module_docker_volume


Manage Docker volumes

## Description

Create/remove Docker volumes.
Performs largely the same function as the "docker volume" CLI subcommand.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "driver": "{'description': ['Specify the type of volume. Docker provides the C(local) driver, but 3rd party drivers can also be used.'], 'default': 'local'}",
    "driver_options": "{'description': ['Dictionary of volume settings. Consult docker docs for valid options and values: U(https://docs.docker.com/engine/reference/commandline/volume_create/#driver-specific-options)']}",
    "force": "{'description': ['With state C(present) causes the volume to be deleted and recreated if the volume already exist and the driver, driver options or labels differ. This will cause any data in the existing volume to be lost.'], 'type': 'bool', 'default': False}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "labels": "{'description': ['List of labels to set for the volume']}",
    "name": "{'description': ['Name of the volume to operate on.'], 'required': True, 'aliases': ['volume_name']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['C(absent) deletes the volume.', 'C(present) creates the volume, if it does not already exist.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create a volume
  docker_volume:
    name: volume_one

- name: Remove a volume
  docker_volume:
    name: volume_one
    state: absent

- name: Create a volume with options
  docker_volume:
    name: volume_two
    driver_options:
      type: btrfs
      device: /dev/sda2

```

## License

TODO

## Author Information
  - ['Alex Grönholm (@agronholm)']
