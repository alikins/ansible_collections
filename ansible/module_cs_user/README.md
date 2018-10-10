# Ansible module: ansible.module_cs_user


Manages users on Apache CloudStack based clouds

## Description

Create, update, disable, lock, enable and remove users.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the user will be created under.', 'Required on C(state=present).']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the user is related to.'], 'default': 'ROOT'}",
    "email": "{'description': ['Email of the user.', 'Required on C(state=present).']}",
    "first_name": "{'description': ['First name of the user.', 'Required on C(state=present).']}",
    "keys_registered": "{'description': ['If API keys of the user should be generated.', 'Note: Keys can not be removed by the API again.'], 'version_added': '2.4', 'type': 'bool', 'default': False}",
    "last_name": "{'description': ['Last name of the user.', 'Required on C(state=present).']}",
    "password": "{'description': ['Password of the user to be created.', 'Required on C(state=present).', 'Only considered on creation and will not be updated if user exists.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['State of the user.', 'C(unlocked) is an alias for C(enabled).'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled', 'locked', 'unlocked']}",
    "timezone": "{'description': ['Timezone of the user.']}",
    "username": "{'description': ['Username of the user.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create an user in domain 'CUSTOMERS'
  local_action:
    module: cs_user
    account: developers
    username: johndoe
    password: S3Cur3
    last_name: Doe
    first_name: John
    email: john.doe@example.com
    domain: CUSTOMERS

- name: Lock an existing user in domain 'CUSTOMERS'
  local_action:
    module: cs_user
    username: johndoe
    domain: CUSTOMERS
    state: locked

- name: Disable an existing user in domain 'CUSTOMERS'
  local_action:
    module: cs_user
    username: johndoe
    domain: CUSTOMERS
    state: disabled

- name: Enable/unlock an existing user in domain 'CUSTOMERS'
  local_action:
    module: cs_user
    username: johndoe
    domain: CUSTOMERS
    state: enabled

- name: Remove an user in domain 'CUSTOMERS'
  local_action:
    module: cs_user
    name: customer_xy
    domain: CUSTOMERS
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
