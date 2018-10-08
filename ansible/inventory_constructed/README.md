# Ansible inventory: ansible.inventory_constructed


Uses Jinja2 to construct vars and groups based on existing inventory

## Description

Uses a YAML configuration file with a valid YAML or C(.config) extension to define var expressions and group conditionals
The Jinja2 conditionals that qualify a host for membership.
The JInja2 exprpessions are calculated and assigned to the variables
Only variables already available from previous inventories or the fact cache can be used for templating.
When I(strict) is False, failed expressions will be ignored (assumes vars were missing).

## Requirements

TODO

## Arguments

``` json
{
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'constructed' plugin."], 'required': True, 'choices': ['constructed']}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
}
```

## Examples


``` yaml

    # inventory.config file in YAML format
    plugin: constructed
    strict: False
    compose:
        var_sum: var1 + var2

        # this variable will only be set if I have a persistent fact cache enabled (and have non expired facts)
        # `strict: False` will skip this instead of producing an error if it is missing facts.
        server_type: "ansible_hostname | regex_replace ('(.{6})(.{2}).*', '\\2')"
    groups:
        # simple name matching
        webservers: inventory_hostname.startswith('web')

        # using ec2 'tags' (assumes aws inventory)
        development: "'devel' in (ec2_tags|list)"

        # using other host properties populated in inventory
        private_only: not (public_dns_name is defined or ip_address is defined)

        # complex group membership
        multi_group: (group_names|intersection(['alpha', 'beta', 'omega']))|length >= 2

    keyed_groups:
        # this creates a group per distro (distro_CentOS, distro_Debian) and assigns the hosts that have matching values to it,
        # using the default separator "_"
        - prefix: distro
          key: ansible_distribution

        # this creates a group per ec2 architecture and assign hosts to the matching ones (arch_x86_64, arch_sparc, etc)
        - prefix: arch
          key: ec2_architecture

```

## License

TODO

## Author Information
  - ['UNKNOWN']
