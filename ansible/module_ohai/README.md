# Ansible module: ansible.module_ohai


Returns inventory data from *Ohai*

## Description

Similar to the M(facter) module, this runs the I(Ohai) discovery program (U(https://docs.chef.io/ohai.html)) on the remote host and returns JSON inventory data. I(Ohai) data is a bit more verbose and nested than I(facter).

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

# Retrieve (ohai) data from all Web servers and store in one-file per host
ansible webservers -m ohai --tree=/tmp/ohaidata

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
