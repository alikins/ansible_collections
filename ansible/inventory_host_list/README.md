# Ansible inventory: ansible.inventory_host_list


Parses a 'host list' string

## Description

Parses a host list string as a comma separated values of hosts
This plugin only applies to inventory strings that are not paths and contain a comma.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

    # define 2 hosts in command line
    # ansible -i '10.10.2.6, 10.10.2.4' -m ping all

    # DNS resolvable names
    # ansible -i 'host1.example.com, host2' -m user -a 'name=me state=absent' all

    # just use localhost
    # ansible-playbook -i 'localhost,' play.yml -c local

```

## License

TODO

## Author Information
  - ['UNKNOWN']
