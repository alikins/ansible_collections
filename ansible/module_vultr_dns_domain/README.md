# Ansible module: ansible.module_vultr_dns_domain


Manages DNS domains on Vultr

## Description

Create and remove DNS domains.

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
    "name": "{'description': ['The domain name.'], 'required': True, 'aliases': ['domain']}",
    "server_ip": "{'description': ['The default server IP.', 'Use M(vultr_dns_record) to change it once the domain is created.', 'Required if C(state=present).']}",
    "state": "{'description': ['State of the DNS domain.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure a domain exists
  local_action:
    module: vultr_dns_domain
    name: example.com
    server_ip: 10.10.10.10

- name: Ensure a domain is absent
  local_action:
    module: vultr_dns_domain
    name: example.com
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
