# Ansible module: ansible.module_apache2_mod_proxy


Set and/or get members' attributes of an Apache httpd 2.4 mod_proxy balancer pool

## Description

Set and/or get members' attributes of an Apache httpd 2.4 mod_proxy balancer pool, using HTTP POST and GET requests. The httpd mod_proxy balancer-member status page has to be enabled and accessible, as this module relies on parsing this page. This module supports ansible check_mode, and requires BeautifulSoup python module.

## Requirements

TODO

## Arguments

``` json
{
    "balancer_url_suffix": "{'description': ['Suffix of the balancer pool url required to access the balancer pool status page (e.g. balancer_vhost[:port]/balancer_url_suffix).'], 'default': '/balancer-manager/'}",
    "balancer_vhost": "{'description': ['(ipv4|ipv6|fqdn):port of the Apache httpd 2.4 mod_proxy balancer pool.'], 'required': True}",
    "member_host": "{'description': ["(ipv4|ipv6|fqdn) of the balancer member to get or to set attributes to. Port number is autodetected and should not be specified here. If undefined, apache2_mod_proxy module will return a members list of dictionaries of all the current balancer pool members' attributes."]}",
    "state": "{'description': ['Desired state of the member host. (absent|disabled),drained,hot_standby,ignore_errors can be simultaneously invoked by separating them with a comma (e.g. state=drained,ignore_errors).'], 'choices': ['present', 'absent', 'enabled', 'disabled', 'drained', 'hot_standby', 'ignore_errors']}",
    "tls": "{'description': ['Use https to access balancer management page.'], 'type': 'bool', 'default': False}",
    "validate_certs": "{'description': ['Validate ssl/tls certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Get all current balancer pool members' attributes:
- apache2_mod_proxy:
    balancer_vhost: 10.0.0.2

# Get a specific member's attributes:
- apache2_mod_proxy:
    balancer_vhost: myws.mydomain.org
    balancer_suffix: /lb/
    member_host: node1.myws.mydomain.org

# Enable all balancer pool members:
- apache2_mod_proxy:
    balancer_vhost: '{{ myloadbalancer_host }}'
  register: result
- apache2_mod_proxy:
    balancer_vhost: '{{ myloadbalancer_host }}'
    member_host: '{{ item.host }}'
    state: present
  with_items: '{{ result.members }}'

# Gracefully disable a member from a loadbalancer node:
- apache2_mod_proxy:
    balancer_vhost: '{{ vhost_host }}'
    member_host: '{{ member.host }}'
    state: drained
  delegate_to: myloadbalancernode
- wait_for:
    host: '{{ member.host }}'
    port: '{{ member.port }}'
    state: drained
  delegate_to: myloadbalancernode
- apache2_mod_proxy:
    balancer_vhost: '{{ vhost_host }}'
    member_host: '{{ member.host }}'
    state: absent
  delegate_to: myloadbalancernode

```

## License

TODO

## Author Information
  - ['Olivier Boukili (@oboukili)"']
