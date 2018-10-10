# Ansible module: ansible.module_docker_image


Manage docker images

## Description

Build, load or pull an image, making the image available for creating containers. Also supports tagging an image into a repository and archiving an image to a .tar file.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "archive_path": "{'description': ['Use with state C(present) to archive an image to a .tar file.'], 'required': False, 'version_added': '2.1'}",
    "buildargs": "{'description': ['Provide a dictionary of C(key:value) build arguments that map to Dockerfile ARG directive.', 'Docker expects the value to be a string. For convenience any non-string values will be converted to strings.', 'Requires Docker API >= 1.21.'], 'required': False, 'version_added': '2.2'}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "container_limits": "{'description': ['A dictionary of limits applied to each container created by the build process.'], 'required': False, 'version_added': '2.1', 'suboptions': {'memory': {'description': ['Set memory limit for build.']}, 'memswap': {'description': ['Total memory (memory + swap), -1 to disable swap.']}, 'cpushares': {'description': ['CPU shares (relative weight).']}, 'cpusetcpus': {'description': ['CPUs in which to allow execution, e.g., "0-3", "0,1".']}}}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "dockerfile": "{'description': ['Use with state C(present) to provide an alternate name for the Dockerfile to use when building an image.'], 'required': False, 'version_added': '2.0'}",
    "force": "{'description': ['Use with state I(absent) to un-tag and remove all images matching the specified name. Use with state C(present) to build, load or pull an image when the image already exists.'], 'default': False, 'required': False, 'version_added': '2.1', 'type': 'bool'}",
    "http_timeout": "{'description': ['Timeout for HTTP requests during the image build operation. Provide a positive integer value for the number of seconds.'], 'required': False, 'version_added': '2.1'}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "load_path": "{'description': ['Use with state C(present) to load an image from a .tar file.'], 'required': False, 'version_added': '2.2'}",
    "name": "{'description': ["Image name. Name format will be one of: name, repository/name, registry_server:port/name. When pushing or pulling an image the name can optionally include the tag by appending ':tag_name'.", 'Note that image IDs (hashes) are not supported.'], 'required': True}",
    "nocache": "{'description': ['Do not use cache when building an image.'], 'default': False, 'required': False, 'type': 'bool'}",
    "path": "{'description': ["Use with state 'present' to build an image. Will be the path to a directory containing the context and Dockerfile for building an image."], 'aliases': ['build_path'], 'required': False}",
    "pull": "{'description': ['When building an image downloads any updates to the FROM image in Dockerfile.'], 'default': True, 'required': False, 'version_added': '2.1', 'type': 'bool'}",
    "push": "{'description': ['Push the image to the registry. Specify the registry as part of the I(name) or I(repository) parameter.'], 'default': False, 'required': False, 'version_added': '2.2', 'type': 'bool'}",
    "repository": "{'description': ['Full path to a repository. Use with state C(present) to tag the image into the repository. Expects format I(repository:tag). If no tag is provided, will use the value of the C(tag) parameter or I(latest).'], 'required': False, 'version_added': '2.1'}",
    "rm": "{'description': ['Remove intermediate containers after build.'], 'default': True, 'required': False, 'version_added': '2.1', 'type': 'bool'}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['Make assertions about the state of an image.', 'When C(absent) an image will be removed. Use the force option to un-tag and remove all images matching the provided name.', 'When C(present) check if an image exists using the provided name and tag. If the image is not found or the force option is used, the image will either be pulled, built or loaded. By default the image will be pulled from Docker Hub. To build the image, provide a path value set to a directory containing a context and Dockerfile. To load an image, specify load_path to provide a path to an archive file. To tag an image to a repository, provide a repository path. If the name contains a repository path, it will be pushed.', 'NOTE: C(build) is DEPRECATED and will be removed in release 2.3. Specifying C(build) will behave the same as C(present).'], 'required': False, 'default': 'present', 'choices': ['absent', 'present', 'build']}",
    "tag": "{'description': ['Used to select an image when pulling. Will be added to the image when pushing, tagging or building. Defaults to I(latest).', 'If C(name) parameter format is I(name:tag), then tag value from C(name) will take precedence.'], 'default': 'latest', 'required': False}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "use_tls": "{'description': ["DEPRECATED. Whether to use tls to connect to the docker server. Set to C(no) when TLS will not be used. Set to C(encrypt) to use TLS. And set to C(verify) to use TLS and verify that the server's certificate is valid for the server. NOTE: If you specify this option, it will set the value of the tls or tls_verify parameters."], 'choices': ['no', 'encrypt', 'verify'], 'default': 'no', 'required': False, 'version_added': '2.0'}",
}
```

## Examples


``` yaml


- name: pull an image
  docker_image:
    name: pacur/centos-7

- name: Tag and push to docker hub
  docker_image:
    name: pacur/centos-7
    repository: dcoppenhagan/myimage
    tag: 7.0
    push: yes

- name: Tag and push to local registry
  docker_image:
     name: centos
     repository: localhost:5000/centos
     tag: 7
     push: yes

- name: Remove image
  docker_image:
    state: absent
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1

- name: Build an image and push it to a private repo
  docker_image:
    path: ./sinatra
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1
    push: yes

- name: Archive image
  docker_image:
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1
    archive_path: my_sinatra.tar

- name: Load image from archive and push to a private registry
  docker_image:
    name: localhost:5000/myimages/sinatra
    tag: v1
    push: yes
    load_path: my_sinatra.tar

- name: Build image and with buildargs
  docker_image:
     path: /path/to/build/dir
     name: myimage
     buildargs:
       log_volume: /var/log/myapp
       listen_port: 8080

```

## License

TODO

## Author Information
  - ['Pavel Antonov (@softzilla)', 'Chris Houseknecht (@chouseknecht)']
  - ['Pavel Antonov (@softzilla)', 'Chris Houseknecht (@chouseknecht)']
