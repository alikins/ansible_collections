# Ansible module: ansible.module_cs_sshkeypair


Manages SSH keys on Apache CloudStack based clouds

## Description

Create, register and remove SSH keys.
If no key was found and no public key was provided and a new SSH private/public key pair will be created and the private key will be returned.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the public key is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the public key is related to.']}",
    "name": "{'description': ['Name of public key.'], 'required': True}",
    "project": "{'description': ['Name of the project the public key to be registered in.']}",
    "public_key": "{'description': ['String of the public key.']}",
    "state": "{'description': ['State of the public key.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# create a new private / public key pair:
- cs_sshkeypair:
    name: linus@example.com
  delegate_to: localhost
  register: key
- debug:
    msg: 'Private key is {{ key.private_key }}'

# remove a public key by its name:
- cs_sshkeypair:
    name: linus@example.com
    state: absent
  delegate_to: localhost

# register your existing local public key:
- cs_sshkeypair:
    name: linus@example.com
    public_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
