# Ansible module: ansible.module_gunicorn


Run gunicorn with various settings

## Description

Starts gunicorn with the parameters specified. Common settings for gunicorn configuration are supported. For additional configuration use a config file See U(https://gunicorn-docs.readthedocs.io/en/latest/settings.html) for more options. It's recommended to always use the chdir option to avoid problems with the location of the app.

## Requirements

TODO

## Arguments

``` json
{
    "app": "{'required': True, 'aliases': ['name'], 'description': ['The app module. A name refers to a WSGI callable that should be found in the specified module.']}",
    "chdir": "{'description': ['Chdir to specified directory before apps loading.']}",
    "config": "{'description': ['Path to the gunicorn configuration file.']}",
    "pid": "{'description': ['A filename to use for the PID file. If not set and not found on the configuration file a tmp pid file will be created to check a successful run of gunicorn.']}",
    "user": "{'description': ['Switch worker processes to run as this user.']}",
    "venv": "{'aliases': ['virtualenv'], 'description': ['Path to the virtualenv directory.']}",
    "worker": "{'choices': ['sync', 'eventlet', 'gevent', 'tornado ', 'gthread', 'gaiohttp'], 'description': ['The type of workers to use. The default class (sync) should handle most "normal" types of workloads.']}",
}
```

## Examples


``` yaml

- name: simple gunicorn run example
  gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'

- name: run gunicorn on a virtualenv
  gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    venv: '/workspace/example/venv'

- name: run gunicorn with a config file
  gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    conf: '/workspace/example/gunicorn.cfg'

- name: run gunicorn as ansible user with specified pid and config file
  gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    conf: '/workspace/example/gunicorn.cfg'
    venv: '/workspace/example/venv'
    pid: '/workspace/example/gunicorn.pid'
    user: 'ansible'

```

## License

TODO

## Author Information
  - ['Alejandro Gomez (@agmezr)']
