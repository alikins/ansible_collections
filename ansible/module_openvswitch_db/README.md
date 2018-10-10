# Ansible module: ansible.module_openvswitch_db


Configure open vswitch database

## Description

Set column values in record in database table.

## Requirements

TODO

## Arguments

``` json
{
    "col": "{'required': True, 'description': ['Identifies the column in the record.']}",
    "key": "{'required': False, 'description': ['Identifies the key in the record column, when the column is a map type.']}",
    "record": "{'required': True, 'description': ['Identifies the recoard in the table.']}",
    "state": "{'required': False, 'description': ['Configures the state of the key. When set to I(present), the I(key) and I(value) pair will be set on the I(record) and when set to I(absent) the I(key) will not be set.'], 'default': 'present', 'choices': ['present', 'absent'], 'version_added': '2.4'}",
    "table": "{'required': True, 'description': ['Identifies the table in the database.']}",
    "timeout": "{'required': False, 'default': 5, 'description': ['How long to wait for ovs-vswitchd to respond']}",
    "value": "{'required': True, 'description': ['Expected value for the table, record, column and key.']}",
}
```

## Examples


``` yaml

# Increase the maximum idle time to 50 seconds before pruning unused kernel
# rules.
- openvswitch_db:
    table: open_vswitch
    record: .
    col: other_config
    key: max-idle
    value: 50000

# Disable in band copy
- openvswitch_db:
    table: Bridge
    record: br-int
    col: other_config
    key: disable-in-band
    value: true

# Remove in band key
- openvswitch_db:
    state: present
    table: Bridge
    record: br-int
    col: other_config
    key: disable-in-band

# Mark port with tag 10
- openvswitch_db:
    table: Port
    record: port0
    col: tag
    value: 10

```

## License

TODO

## Author Information
  - ['Mark Hamilton (mhamilton@vmware.com)']
