# Ansible module: ansible.module_cs_project


Manages projects on Apache CloudStack based clouds

## Description

Create, update, suspend, activate and remove projects.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the project is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "display_text": "{'description': ['Display text of the project.', 'If not specified, C(name) will be used as C(display_text).']}",
    "domain": "{'description': ['Domain the project is related to.']}",
    "name": "{'description': ['Name of the project.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['State of the project.'], 'default': 'present', 'choices': ['present', 'absent', 'active', 'suspended']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'If you want to delete all tags, set a empty list e.g. C(tags: []).'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

# Create a project
- local_action:
    module: cs_project
    name: web
    tags:
      - { key: admin, value: john }
      - { key: foo,   value: bar }

# Rename a project
- local_action:
    module: cs_project
    name: web
    display_text: my web project

# Suspend an existing project
- local_action:
    module: cs_project
    name: web
    state: suspended

# Activate an existing project
- local_action:
    module: cs_project
    name: web
    state: active

# Remove a project
- local_action:
    module: cs_project
    name: web
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
