# Ansible lookup: ansible.lookup_chef_databag


fetches data from a Chef Databag

## Description

This is a lookup plugin to provide access to chef data bags using the pychef package. It interfaces with the chef server api using the same methods to find a knife or chef-client config file to load parameters from, starting from either the given base path or the current working directory. The lookup order mirrors the one from Chef, all folders in the base path are walked back looking for the following configuration file in order : .chef/knife.rb, ~/.chef/knife.rb, /etc/chef/client.rb

## Requirements

TODO

## Arguments

``` json
{
    "item": "{'description': ['Item to fetch'], 'required': True}",
    "name": "{'description': ['Name of the databag'], 'required': True}",
}
```

## Examples


``` yaml

    - debug:
        msg: "{{ lookup('chef_databag', 'name=data_bag_name item=data_bag_item') }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
