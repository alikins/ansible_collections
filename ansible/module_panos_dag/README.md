# Ansible module: ansible.module_panos_dag


create a dynamic address group

## Description

Create a dynamic address group object in the firewall used for policy rules

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "dag_filter": "{'description': ['dynamic filter user by the dynamic address group'], 'required': True}",
    "dag_name": "{'description': ['name of the dynamic address group'], 'required': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: dag
  panos_dag:
    ip_address: "192.168.1.1"
    password: "admin"
    dag_name: "dag-1"
    dag_filter: "'aws-tag.aws:cloudformation:logical-id.ServerInstance' and 'instanceState.running'"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
