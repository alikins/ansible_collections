# Ansible module: ansible.module_vultr_startup_script


Manages startup scripts on Vultr

## Description

Create, update and remove startup scripts.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "name": "{'description': ['The script name.'], 'required': True}",
    "script": "{'description': ['The script source code.', 'Required if (state=present).']}",
    "script_type": "{'description': ['The script type, can not be changed once created.'], 'default': 'boot', 'choices': ['boot', 'pxe'], 'aliases': ['type']}",
    "state": "{'description': ['State of the script.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: ensure a pxe script exists, source from a file
  local_action:
    module: vultr_startup_script
    name: my_web_script
    script_type: pxe
    script: "{{ lookup('file', 'path/to/script') }}"

- name: ensure a boot script exists
  local_action:
    module: vultr_startup_script
    name: vultr_startup_script
    script: "#!/bin/bash\necho Hello World > /root/hello"

- name: ensure a script is absent
  local_action:
    module: vultr_startup_script
    name: my_web_script
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
