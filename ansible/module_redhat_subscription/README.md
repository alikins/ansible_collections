# Ansible module: ansible.module_redhat_subscription


Manage registration and subscriptions to RHSM using the ``subscription-manager`` command

## Description

Manage registration and subscription to the Red Hat Subscription Management entitlement platform using the C(subscription-manager) command

## Requirements

TODO

## Arguments

``` json
{
    "activationkey": "{'description': ['supply an activation key for use with registration']}",
    "auto_attach": "{'description': ['Upon successful registration, auto-consume available subscriptions', 'Added in favor of deprecated autosubscribe in 2.5.'], 'type': 'bool', 'default': False, 'version_added': '2.5', 'aliases': ['autosubscribe']}",
    "consumer_id": "{'description': ["References an existing consumer ID to resume using a previous registration\nfor this system. If the  system's identity certificate is lost or corrupted,\nthis option allows it to resume using its previous identity and subscriptions.\nThe default is to not specify a consumer ID so a new ID is created.\n"], 'version_added': '2.1'}",
    "consumer_name": "{'description': ['Name of the system to register, defaults to the hostname'], 'version_added': '2.1'}",
    "consumer_type": "{'description': ['The type of unit to register, defaults to system'], 'version_added': '2.1'}",
    "environment": "{'description': ['Register with a specific environment in the destination org. Used with Red Hat Satellite 6.x or Katello'], 'version_added': '2.2'}",
    "force_register": "{'description': ['Register the system even if it is already registered'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "org_id": "{'description': ['Organization ID to use in conjunction with activationkey'], 'version_added': '2.0'}",
    "password": "{'description': ['access.redhat.com or Sat6 password']}",
    "pool": "{'description': ['Specify a subscription pool name to consume.  Regular expressions accepted. Use I(pool_ids) instead if\npossible, as it is much faster. Mutually exclusive with I(pool_ids).\n'], 'default': '^$'}",
    "pool_ids": "{'description': ['Specify subscription pool IDs to consume. Prefer over I(pool) when possible as it is much faster.\nA pool ID may be specified as a C(string) - just the pool ID (ex. C(0123456789abcdef0123456789abcdef)),\nor as a C(dict) with the pool ID as the key, and a quantity as the value (ex.\nC(0123456789abcdef0123456789abcdef: 2). If the quantity is provided, it is used to consume multiple\nentitlements from a pool (the pool must support this). Mutually exclusive with I(pool).\n'], 'default': [], 'version_added': '2.4'}",
    "rhsm_baseurl": "{'description': ['Specify CDN baseurl']}",
    "rhsm_repo_ca_cert": "{'description': ['Specify an alternative location for a CA certificate for CDN'], 'version_added': '2.7'}",
    "server_hostname": "{'description': ['Specify an alternative Red Hat Subscription Management or Sat6 server']}",
    "server_insecure": "{'description': ['Enable or disable https server certificate verification when connecting to C(server_hostname)']}",
    "server_proxy_hostname": "{'description': ['Specify a HTTP proxy hostname'], 'version_added': '2.4'}",
    "server_proxy_password": "{'description': ['Specify a password for HTTP proxy with basic authentication'], 'version_added': '2.4'}",
    "server_proxy_port": "{'description': ['Specify a HTTP proxy port'], 'version_added': '2.4'}",
    "server_proxy_user": "{'description': ['Specify a user for HTTP proxy with basic authentication'], 'version_added': '2.4'}",
    "state": "{'description': ['whether to register and subscribe (C(present)), or unregister (C(absent)) a system'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'description': ['access.redhat.com or Sat6  username']}",
}
```

## Examples


``` yaml

- name: Register as user (joe_user) with password (somepass) and auto-subscribe to available content.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    auto_attach: true

- name: Same as above but subscribe to a specific pool by ID.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids: 0123456789abcdef0123456789abcdef

- name: Register and subscribe to multiple pools.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids:
      - 0123456789abcdef0123456789abcdef
      - 1123456789abcdef0123456789abcdef

- name: Same as above but consume multiple entitlements.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids:
      - 0123456789abcdef0123456789abcdef: 2
      - 1123456789abcdef0123456789abcdef: 4

- name: Register and pull existing system data.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    consumer_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Register with activationkey and consume subscriptions matching Red Hat Enterprise Server or Red Hat Virtualization
  redhat_subscription:
    state: present
    activationkey: 1-222333444
    org_id: 222333444
    pool: '^(Red Hat Enterprise Server|Red Hat Virtualization)$'

- name: Update the consumed subscriptions from the previous example (remove Red Hat Virtualization subscription)
  redhat_subscription:
    state: present
    activationkey: 1-222333444
    org_id: 222333444
    pool: '^Red Hat Enterprise Server$'

- name: Register as user credentials into given environment (against Red Hat Satellite 6.x), and auto-subscribe.
  redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    environment: Library
    auto_attach: true

```

## License

TODO

## Author Information
  - ['Barnaby Court (@barnabycourt)']
