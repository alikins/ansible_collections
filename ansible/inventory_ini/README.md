# Ansible inventory: ansible.inventory_ini


Uses an Ansible INI file as inventory source

## Description

INI file based inventory, sections are groups or group related with special `:modifiers`.
Entries in sections C([group_1]) are hosts, members of the group.
Hosts can have variables defined inline as key/value pairs separated by C(=).
The C(children) modifier indicates that the section contains groups.
The C(vars) modifier indicates that the section contains variables assigned to members of the group.
Anything found outside a section is considered an 'ungrouped' host.
Values passed in using the C(key=value) syntax are interpreted as Python literal structure (strings, numbers, tuples, lists, dicts, booleans, None), alternatively as string. For example C(var=FALSE) would create a string equal to 'FALSE'. Do not rely on types set during definition, always make sure you specify type with a filter when needed when consuming the variable.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

  example1: |
      # example cfg file
      [web]
      host1
      host2 ansible_port=222

      [web:vars]
      http_port=8080 # all members of 'web' will inherit these
      myvar=23

      [web:children] # child groups will automatically add their hosts to partent group
      apache
      nginx

      [apache]
      tomcat1
      tomcat2 myvar=34 # host specific vars override group vars
      tomcat3 mysecret="'03#pa33w0rd'" # proper quoting to prevent value changes

      [nginx]
      jenkins1

      [nginx:vars]
      has_java = True # vars in child groups override same in parent

      [all:vars]
      has_java = False # 'all' is 'top' parent

  example2: |
      # other example config
      host1 # this is 'ungrouped'

      # both hosts have same IP but diff ports, also 'ungrouped'
      host2 ansible_host=127.0.0.1 ansible_port=44
      host3 ansible_host=127.0.0.1 ansible_port=45

      [g1]
      host4

      [g2]
      host4 # same host as above, but member of 2 groups, will inherit vars from both
            # inventory hostnames are unique

```

## License

TODO

## Author Information
  - ['UNKNOWN']
