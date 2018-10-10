# Ansible module: ansible.module_puppet


Runs puppet

## Description

Runs I(puppet) agent or apply in a reliable manner.

## Requirements

TODO

## Arguments

``` json
{
    "certname": "{'description': ['The name to use when handling certificates.'], 'version_added': '2.1'}",
    "debug": "{'description': ['Enable full debugging'], 'version_added': '2.7'}",
    "environment": "{'description': ['Puppet environment to be used.']}",
    "execute": "{'description': ['Execute a specific piece of Puppet code.', 'It has no effect with a puppetmaster.'], 'version_added': '2.1'}",
    "facter_basename": "{'description': ['Basename of the facter output file.'], 'default': 'ansible'}",
    "facts": "{'description': ['A dict of values to pass in as persistent external facter facts.']}",
    "logdest": "{'description': ['Where the puppet logs should go, if puppet apply is being used. C(all)\nwill go to both C(stdout) and C(syslog).\n'], 'choices': ['stdout', 'syslog', 'all'], 'default': 'stdout', 'version_added': '2.1'}",
    "manifest": "{'description': ['Path to the manifest file to run puppet apply on.']}",
    "modulepath": "{'description': ['Path to an alternate location for puppet modules.'], 'version_added': '2.4'}",
    "puppetmaster": "{'description': ['The hostname of the puppetmaster to contact.']}",
    "summarize": "{'description': ['Whether to print a transaction summary'], 'version_added': '2.7'}",
    "tags": "{'description': ['A comma-separated list of puppet tags to be used.'], 'version_added': '2.1'}",
    "timeout": "{'description': ['How long to wait for I(puppet) to finish.'], 'default': '30m'}",
    "verbose": "{'description': ['Print extra information'], 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: Run puppet agent and fail if anything goes wrong
  puppet:

- name: Run puppet and timeout in 5 minutes
  puppet:
    timeout: 5m

- name: Run puppet using a different environment
  puppet:
    environment: testing

- name: Run puppet using a specific certname
  puppet:
    certname: agent01.example.com

- name: Run puppet using a specific piece of Puppet code. Has no effect with a puppetmaster
  puppet:
    execute: include ::mymodule

- name: Run puppet using a specific tags
  puppet:
    tags: update,nginx

- name: Run a manifest with debug, log to both syslog and stdout, specify module path
  puppet:
    modulepath: /etc/puppet/modules:/opt/stack/puppet-modules:/usr/share/openstack-puppet/modules
    logdest: all
    manifest: /var/lib/example/puppet_step_config.pp

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
