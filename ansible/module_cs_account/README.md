# Ansible module: ansible.module_cs_account


Manages accounts on Apache CloudStack based clouds

## Description

Create, disable, lock, enable and remove accounts.

## Requirements

TODO

## Arguments

``` json
{
    "account_type": "{'description': ['Type of the account.'], 'default': 'user', 'choices': ['user', 'root_admin', 'domain_admin']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the account is related to.'], 'default': 'ROOT'}",
    "email": "{'description': ['Email of the user to be created if account did not exist.', 'Required on C(state=present).']}",
    "first_name": "{'description': ['First name of the user to be created if account did not exist.', 'Required on C(state=present).']}",
    "last_name": "{'description': ['Last name of the user to be created if account did not exist.', 'Required on C(state=present).']}",
    "name": "{'description': ['Name of account.'], 'required': True}",
    "network_domain": "{'description': ['Network domain of the account.']}",
    "password": "{'description': ['Password of the user to be created if account did not exist.', 'Required on C(state=present).']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "role": "{'description': ['Creates the account under the specified role name or id.'], 'version_added': 2.8}",
    "state": "{'description': ['State of the account.', 'C(unlocked) is an alias for C(enabled).'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled', 'locked', 'unlocked']}",
    "timezone": "{'description': ['Timezone of the user to be created if account did not exist.']}",
    "username": "{'description': ['Username of the user to be created if account did not exist.', 'Required on C(state=present).']}",
}
```

## Examples


``` yaml

# create an account in domain 'CUSTOMERS'
- local_action:
    module: cs_account
    name: customer_xy
    username: customer_xy
    password: S3Cur3
    last_name: Doe
    first_name: John
    email: john.doe@example.com
    domain: CUSTOMERS
    role: Domain Admin

# Lock an existing account in domain 'CUSTOMERS'
- local_action:
    module: cs_account
    name: customer_xy
    domain: CUSTOMERS
    state: locked

# Disable an existing account in domain 'CUSTOMERS'
- local_action:
    module: cs_account
    name: customer_xy
    domain: CUSTOMERS
    state: disabled

# Enable an existing account in domain 'CUSTOMERS'
- local_action:
    module: cs_account
    name: customer_xy
    domain: CUSTOMERS
    state: enabled

# Remove an account in domain 'CUSTOMERS'
- local_action:
    module: cs_account
    name: customer_xy
    domain: CUSTOMERS
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
