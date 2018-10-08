# Ansible inventory: ansible.inventory_advanced_host_list


Parses a 'host list' with ranges

## Description

Parses a host list string as a comma separated values of hosts and supports host ranges.
This plugin only applies to inventory sources that are not paths and contain at least one comma.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

    # simple range
    # ansible -i 'host[1:10],' -m ping

    # still supports w/o ranges also
    # ansible-playbook -i 'localhost,' play.yml

```

## License

TODO

## Author Information
  - ['UNKNOWN']
