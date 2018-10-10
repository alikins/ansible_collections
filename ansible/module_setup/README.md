# Ansible module: ansible.module_setup


Gathers facts about remote hosts

## Description

This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks. It can also be executed directly by C(/usr/bin/ansible) to check what variables are available to a host. Ansible provides many I(facts) about the system, automatically.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "fact_path": "{'version_added': '1.3', 'description': ['path used for local ansible facts (C(*.fact)) - files in this dir will be run (if executable) and their results be added to C(ansible_local) facts if a file is not executable it is read. Check notes for Windows options. (from 2.1 on) File/results format can be json or ini-format'], 'required': False, 'default': '/etc/ansible/facts.d'}",
    "filter": "{'description': ['if supplied, only return facts that match this shell-style (fnmatch) wildcard.'], 'required': False, 'default': '*'}",
    "gather_subset": "{'version_added': '2.1', 'description': ['if supplied, restrict the additional facts collected to the given subset. Possible values: C(all), C(min), C(hardware), C(network), C(virtual), C(ohai), and C(facter). Can specify a list of values to specify a larger subset. Values can also be used with an initial C(!) to specify that that specific subset should not be collected.  For instance: C(!hardware,!network,!virtual,!ohai,!facter). If C(!all) is specified then only the min subset is collected. To avoid collecting even the min subset, specify C(!all,!min). To collect only specific facts, use C(!all,!min), and specify the particular fact subsets. Use the filter parameter if you do not want to display some collected facts.'], 'required': False, 'default': 'all'}",
    "gather_timeout": "{'version_added': '2.2', 'description': ['Set the default timeout in seconds for individual fact gathering'], 'required': False, 'default': 10}",
}
```

## Examples


``` yaml

# Display facts from all hosts and store them indexed by I(hostname) at C(/tmp/facts).
# ansible all -m setup --tree /tmp/facts

# Display only facts regarding memory found by ansible on all hosts and output them.
# ansible all -m setup -a 'filter=ansible_*_mb'

# Display only facts returned by facter.
# ansible all -m setup -a 'filter=facter_*'

# Collect only facts returned by facter.
# ansible all -m setup -a 'gather_subset=!all,!any,facter'

- name: Collect only facts returned by facter
  setup:
    gather_subset:
      - '!all'
      - '!any'
      - facter

# Display only facts about certain interfaces.
# ansible all -m setup -a 'filter=ansible_eth[0-2]'

# Restrict additional gathered facts to network and virtual (includes default minimum facts)
# ansible all -m setup -a 'gather_subset=network,virtual'

# Collect only network and virtual (excludes default minimum facts)
# ansible all -m setup -a 'gather_subset=!all,!any,network,virtual'

# Do not call puppet facter or ohai even if present.
# ansible all -m setup -a 'gather_subset=!facter,!ohai'

# Only collect the default minimum amount of facts:
# ansible all -m setup -a 'gather_subset=!all'

# Collect no facts, even the default minimum subset of facts:
# ansible all -m setup -a 'gather_subset=!all,!min'

# Display facts from Windows hosts with custom facts stored in C(C:\custom_facts).
# ansible windows -m setup -a "fact_path='c:\custom_facts'"

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan', "David O'Brien @david_obrien davidobrien1985"]
  - ['Ansible Core Team', 'Michael DeHaan', "David O'Brien @david_obrien davidobrien1985"]
  - ['Ansible Core Team', 'Michael DeHaan', "David O'Brien @david_obrien davidobrien1985"]
