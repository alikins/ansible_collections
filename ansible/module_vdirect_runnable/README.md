# Ansible module: ansible.module_vdirect_runnable


Runs templates and workflow actions in Radware vDirect server

## Description

Runs configuration templates, creates workflows and runs workflow actions in Radware vDirect server.

## Requirements

TODO

## Arguments

``` json
{
    "action_name": "{'description': ['Workflow action name to run.', 'Required if I(runnable_type=Workflow).']}",
    "parameters": "{'description': ['Action parameters dictionary. In case of C(ConfigurationTemplate) runnable type,', 'the device connection details should always be passed as a parameter.']}",
    "runnable_name": "{'description': ['vDirect runnable name to run.', 'May be configuration template name, workflow template name or workflow instance name.'], 'required': True}",
    "runnable_type": "{'description': ['vDirect runnable type.'], 'required': True, 'choices': ['ConfigurationTemplate', 'Workflow', 'WorkflowTemplate']}",
    "vdirect_http_port": "{'description': ['vDirect server HTTP port number, may be set as C(VDIRECT_HTTP_PORT) environment variable.'], 'default': 2188}",
    "vdirect_https_port": "{'description': ['vDirect server HTTPS port number, may be set as C(VDIRECT_HTTPS_PORT) environment variable.'], 'default': 2189}",
    "vdirect_ip": "{'description': ['Primary vDirect server IP address, may be set as C(VDIRECT_IP) environment variable.'], 'required': True}",
    "vdirect_password": "{'description': ['vDirect server password, may be set as C(VDIRECT_PASSWORD) environment variable.'], 'required': True}",
    "vdirect_secondary_ip": "{'description': ['Secondary vDirect server IP address, may be set as C(VDIRECT_SECONDARY_IP) environment variable.']}",
    "vdirect_timeout": "{'description': ['Amount of time to wait for async operation completion [seconds],', 'may be set as C(VDIRECT_TIMEOUT) environment variable.'], 'default': 60}",
    "vdirect_use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection,', 'may be set as C(VDIRECT_HTTPS) or C(VDIRECT_USE_SSL) environment variable.'], 'type': 'bool', 'default': True}",
    "vdirect_user": "{'description': ['vDirect server username, may be set as C(VDIRECT_USER) environment variable.'], 'required': True}",
    "vdirect_validate_certs": "{'description': ['If C(no), SSL certificates will not be validated,', 'may be set as C(VDIRECT_VALIDATE_CERTS) or C(VDIRECT_VERIFY) environment variable.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vdirect_wait": "{'description': ['Wait for async operation to complete, may be set as C(VDIRECT_WAIT) environment variable.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: vdirect_runnable
  vdirect_runnable:
      vdirect_ip: 10.10.10.10
      vdirect_user: vDirect
      vdirect_password: radware
      runnable_type: ConfigurationTemplate
      runnable_name: get_vlans
      parameters: {'vlans_needed':1,'adc':[{'type':'Adc','name':'adc-1'}]}

```

## License

TODO

## Author Information
  - ['Evgeny Fedoruk @ Radware LTD (@evgenyfedoruk)']
