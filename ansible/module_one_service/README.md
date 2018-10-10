# Ansible module: ansible.module_one_service


Deploy and manage OpenNebula services

## Description

Manage OpenNebula services

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['Password of the user to login into OpenNebula OneFlow API server. If not set then the value of the C(ONEFLOW_PASSWORD) environment variable is used.']}",
    "api_url": "{'description': ['URL of the OpenNebula OneFlow API server.', 'It is recommended to use HTTPS so that the username/password are not transferred over the network unencrypted.', 'If not set then the value of the ONEFLOW_URL environment variable is used.']}",
    "api_username": "{'description': ['Name of the user to login into the OpenNebula OneFlow API server. If not set then the value of the C(ONEFLOW_USERNAME) environment variable is used.']}",
    "cardinality": "{'description': ['Number of VMs for the specified role']}",
    "custom_attrs": "{'description': ['Dictionary of key/value custom attributes which will be used when instantiating a new service.'], 'default': {}}",
    "force": "{'description': ['Force the new cardinality even if it is outside the limits'], 'type': 'bool', 'default': False}",
    "group_id": "{'description': ['ID of the group which will be set as the group of the service']}",
    "mode": "{'description': ['Set permission mode of a service instance in octet format, e.g. C(600) to give owner C(use) and C(manage) and nothing to group and others.']}",
    "owner_id": "{'description': ['ID of the user which will be set as the owner of the service']}",
    "role": "{'description': ['Name of the role whose cardinality should be changed']}",
    "service_id": "{'description': ['ID of a service instance that you would like to manage']}",
    "service_name": "{'description': ['Name of a service instance that you would like to manage']}",
    "state": "{'description': ['C(present) - instantiate a service from a template specified with C(template_id)/C(template_name).', 'C(absent) - terminate an instance of a service specified with C(service_id)/C(service_name).'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "template_id": "{'description': ['ID of a service template to use to create a new instance of a service']}",
    "template_name": "{'description': ['Name of service template to use to create a new instace of a service']}",
    "unique": "{'description': ['Setting C(unique=yes) will make sure that there is only one service instance running with a name set with C(service_name) when', 'instantiating a service from a template specified with C(template_id)/C(template_name). Check examples below.'], 'type': 'bool', 'default': False}",
    "wait": "{'description': ['Wait for the instance to reach RUNNING state after DEPLOYING or COOLDOWN state after SCALING'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

# Instantiate a new service
- one_service:
    template_id: 90
  register: result

# Print service properties
- debug:
    msg: result

# Instantiate a new service with specified service_name, service group and mode
- one_service:
    template_name: 'app1_template'
    service_name: 'app1'
    group_id: 1
    mode: '660'

# Instantiate a new service with template_id and pass custom_attrs dict
- one_service:
    template_id: 90
    custom_attrs:
      public_network_id: 21
      private_network_id: 26

# Instiate a new service 'foo' if the service doesn't already exist, otherwise do nothing
- one_service:
    template_id: 53
    service_name: 'foo'
    unique: yes

# Delete a service by ID
- one_service:
    service_id: 153
    state: absent

# Get service info
- one_service:
    service_id: 153
  register: service_info

# Change service owner, group and mode
- one_service:
    service_name: 'app2'
    owner_id: 34
    group_id: 113
    mode: '600'

# Instantiate service and wait for it to become RUNNING
-  one_service:
    template_id: 43
    service_name: 'foo1'

# Wait service to become RUNNING
- one_service:
    service_id: 112
    wait: yes

# Change role cardinality
- one_service:
    service_id: 153
    role: bar
    cardinality: 5

# Change role cardinality and wait for it to be applied
- one_service:
    service_id: 112
    role: foo
    cardinality: 7
    wait: yes

```

## License

TODO

## Author Information
  - ['Milan Ilic (@ilicmilan)']
