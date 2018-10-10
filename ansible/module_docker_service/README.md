# Ansible module: ansible.module_docker_service


Manage docker services and containers

## Description

Consumes docker compose to start, shutdown and scale services.
Works with compose versions 1 and 2.
Compose can be read from a docker-compose.yml (or .yaml) file or inline using the C(definition) option.
See the examples for more details.
Supports check mode.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "build": "{'description': ['Use with state I(present) to always build images prior to starting the application.', 'Same as running docker-compose build with the pull option.', 'Images will only be rebuilt if Docker detects a change in the Dockerfile or build directory contents.', 'Use the C(nocache) option to ignore the image cache when performing the build.', 'If an existing image is replaced, services using the image will be recreated unless C(recreate) is I(never).'], 'type': 'bool', 'default': False}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "definition": "{'description': ['Provide docker-compose yaml describing one or more services, networks and volumes.', 'Mutually exclusive with C(project_src) and C(files).']}",
    "dependencies": "{'description': ['When C(state) is I(present) specify whether or not to include linked services.'], 'type': 'bool', 'default': True}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "files": "{'description': ['List of file names relative to C(project_src). Overrides docker-compose.yml or docker-compose.yaml.', 'Files are loaded and merged in the order given.']}",
    "hostname_check": "{'description': ["Whether or not to check the Docker daemon's hostname against the name provided in the client certificate."], 'type': 'bool', 'default': False}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "nocache": "{'description': ['Use with the build option to ignore the cache during the image build process.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "project_name": "{'description': ['Provide a project name. If not provided, the project name is taken from the basename of C(project_src).', 'Required when C(definition) is provided.']}",
    "project_src": "{'description': ['Path to a directory containing a docker-compose.yml or docker-compose.yaml file.', 'Mutually exclusive with C(definition).', 'Required when no C(definition) is provided.']}",
    "pull": "{'description': ['Use with state I(present) to always pull images prior to starting the application.', 'Same as running docker-compose pull.', 'When a new image is pulled, services using the image will be recreated unless C(recreate) is I(never).'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "recreate": "{'description': ['By default containers will be recreated when their configuration differs from the service definition.', 'Setting to I(never) ignores configuration differences and leaves existing containers unchanged.', 'Setting to I(always) forces recreation of all existing containers.'], 'required': False, 'choices': ['always', 'never', 'smart'], 'default': 'smart'}",
    "remove_images": "{'description': ['Use with state I(absent) to remove the all images or only local images.'], 'choices': ['all', 'local']}",
    "remove_orphans": "{'description': ['Remove containers for services not defined in the compose file.'], 'type': 'bool', 'default': False}",
    "remove_volumes": "{'description': ['Use with state I(absent) to remove data volumes.'], 'type': 'bool', 'default': False}",
    "restarted": "{'description': ['Use with state I(present) to restart all containers.'], 'type': 'bool', 'default': False}",
    "scale": "{'description': ['When C(state) is I(present) scale services. Provide a dictionary of key/value pairs where the key is the name of the service and the value is an integer count for the number of containers.']}",
    "services": "{'description': ['When C(state) is I(present) run I(docker-compose up) on a subset of services.']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['Desired state of the project.', 'Specifying I(present) is the same as running I(docker-compose up).', 'Specifying I(absent) is the same as running I(docker-compose down).'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "stopped": "{'description': ['Use with state I(present) to leave the containers in an exited or non-running state.'], 'type': 'bool', 'default': False}",
    "timeout": "{'description': ['timeout in seconds for container shutdown when attached or when containers are already running.'], 'default': 10}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples use the django example at U(https://docs.docker.com/compose/django/). Follow it to create the flask
# directory

- name: Run using a project directory
  hosts: localhost
  connection: local
  gather_facts: no
  tasks:
    - docker_service:
        project_src: flask
        state: absent

    - docker_service:
        project_src: flask
      register: output

    - debug:
        var: output

    - docker_service:
        project_src: flask
        build: no
      register: output

    - debug:
        var: output

    - assert:
        that: "not output.changed "

    - docker_service:
        project_src: flask
        build: no
        stopped: true
      register: output

    - debug:
        var: output

    - assert:
        that:
          - "not web.flask_web_1.state.running"
          - "not db.flask_db_1.state.running"

    - docker_service:
        project_src: flask
        build: no
        restarted: true
      register: output

    - debug:
        var: output

    - assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"

- name: Scale the web service to 2
  hosts: localhost
  connection: local
  gather_facts: no
  tasks:
    - docker_service:
        project_src: flask
        scale:
          web: 2
      register: output

    - debug:
        var: output

- name: Run with inline v2 compose
  hosts: localhost
  connection: local
  gather_facts: no
  tasks:
    - docker_service:
        project_src: flask
        state: absent

    - docker_service:
        project_name: flask
        definition:
          version: '2'
          services:
            db:
              image: postgres
            web:
              build: "{{ playbook_dir }}/flask"
              command: "python manage.py runserver 0.0.0.0:8000"
              volumes:
                - "{{ playbook_dir }}/flask:/code"
              ports:
                - "8000:8000"
              depends_on:
                - db
      register: output

    - debug:
        var: output

    - assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"

- name: Run with inline v1 compose
  hosts: localhost
  connection: local
  gather_facts: no
  tasks:
    - docker_service:
        project_src: flask
        state: absent

    - docker_service:
        project_name: flask
        definition:
            db:
              image: postgres
            web:
              build: "{{ playbook_dir }}/flask"
              command: "python manage.py runserver 0.0.0.0:8000"
              volumes:
                - "{{ playbook_dir }}/flask:/code"
              ports:
                - "8000:8000"
              links:
                - db
      register: output

    - debug:
        var: output

    - assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)']
