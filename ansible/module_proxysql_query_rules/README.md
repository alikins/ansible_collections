# Ansible module: ansible.module_proxysql_query_rules


Modifies query rules using the proxysql admin interface

## Description

The M(proxysql_query_rules) module modifies query rules using the proxysql admin interface.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['A rule with I(active) set to C(False) will be tracked in the database, but will be never loaded in the in-memory data structures.']}",
    "apply": "{'description': ['Used in combination with I(flagIN) and I(flagOUT) to create chains of rules. Setting apply to True signifies the last rule to be applied.']}",
    "cache_ttl": "{'description': ['The number of milliseconds for which to cache the result of the query. Note in ProxySQL 1.1 I(cache_ttl) was in seconds.']}",
    "client_addr": "{'description': ['Match traffic from a specific source.']}",
    "comment": "{'description': ['Free form text field, usable for a descriptive comment of the query rule.']}",
    "config_file": "{'description': ['Specify a config file from which I(login_user) and I(login_password) are to be read.'], 'default': ''}",
    "delay": "{'description': ['Number of milliseconds to delay the execution of the query. This is essentially a throttling mechanism and QoS, and allows a way to give priority to queries over others. This value is added to the mysql-default_query_delay global variable that applies to all queries.']}",
    "destination_hostgroup": "{'description': ['Route matched queries to this hostgroup. This happens unless there is a started transaction and the logged in user has I(transaction_persistent) set to C(True) (see M(proxysql_mysql_users)).']}",
    "digest": "{'description': ['Match queries with a specific digest, as returned by stats_mysql_query_digest.digest.']}",
    "error_msg": "{'description': ['Query will be blocked, and the specified error_msg will be returned to the client.']}",
    "flagIN": "{'description': ['Used in combination with I(flagOUT) and I(apply) to create chains of rules.']}",
    "flagOUT": "{'description': ['Used in combination with I(flagIN) and apply to create chains of rules. When set, I(flagOUT) signifies the I(flagIN) to be used in the next chain of rules.']}",
    "force_delete": "{'description': ["By default we avoid deleting more than one schedule in a single batch, however if you need this behaviour and you're not concerned about the schedules deleted, you can set I(force_delete) to C(True)."], 'default': False}",
    "load_to_runtime": "{'description': ['Dynamically load config to runtime memory.'], 'type': 'bool', 'default': True}",
    "log": "{'description': ['Query will be logged.']}",
    "login_host": "{'description': ['The host used to connect to ProxySQL admin interface.'], 'default': '127.0.0.1'}",
    "login_password": "{'description': ['The password used to authenticate to ProxySQL admin interface.']}",
    "login_port": "{'description': ['The port used to connect to ProxySQL admin interface.'], 'default': 6032}",
    "login_user": "{'description': ['The username used to authenticate to ProxySQL admin interface.']}",
    "match_digest": "{'description': ['Regular expression that matches the query digest. The dialect of regular expressions used is that of re2 - https://github.com/google/re2']}",
    "match_pattern": "{'description': ['Regular expression that matches the query text. The dialect of regular expressions used is that of re2 - https://github.com/google/re2']}",
    "mirror_flagOUT": "{'description': ['Enables query mirroring. If set I(mirror_flagOUT) can be used to evaluates the mirrored query against the specified chain of rules.']}",
    "mirror_hostgroup": "{'description': ['Enables query mirroring. If set I(mirror_hostgroup) can be used to mirror queries to the same or different hostgroup.']}",
    "negate_match_pattern": "{'description': ['If I(negate_match_pattern) is set to C(True), only queries not matching the query text will be considered as a match. This acts as a NOT operator in front of the regular expression matching against match_pattern.']}",
    "proxy_addr": "{'description': ['Match incoming traffic on a specific local IP.']}",
    "proxy_port": "{'description': ['Match incoming traffic on a specific local port.']}",
    "replace_pattern": "{'description': ['This is the pattern with which to replace the matched pattern. Note that this is optional, and when omitted, the query processor will only cache, route, or set other parameters without rewriting.']}",
    "retries": "{'description': ['The maximum number of times a query needs to be re-executed in case of detected failure during the execution of the query. If retries is not specified, the global variable mysql-query_retries_on_failure applies.']}",
    "rule_id": "{'description': ['The unique id of the rule. Rules are processed in rule_id order.']}",
    "save_to_disk": "{'description': ['Save config to sqlite db on disk to persist the configuration.'], 'type': 'bool', 'default': True}",
    "schemaname": "{'description': ['Filtering criteria matching schemaname. If I(schemaname) is non-NULL, a query will match only if the connection uses schemaname as its default schema.']}",
    "state": "{'description': ['When C(present) - adds the rule, when C(absent) - removes the rule.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The maximum timeout in milliseconds with which the matched or rewritten query should be executed. If a query run for longer than the specific threshold, the query is automatically killed. If timeout is not specified, the global variable mysql-default_query_timeout applies.']}",
    "username": "{'description': ['Filtering criteria matching username.  If I(username) is non-NULL, a query will match only if the connection is made with the correct username.']}",
}
```

## Examples


``` yaml

---
# This example adds a rule to redirect queries from a specific user to another
# hostgroup, it saves the mysql query rule config to disk, but avoids loading
# the mysql query config config to runtime (this might be because several
# rules are being added and the user wants to push the config to runtime in a
# single batch using the M(proxysql_manage_config) module). It uses supplied
# credentials to connect to the proxysql admin interface.

- proxysql_query_rules:
    login_user: admin
    login_password: admin
    username: 'guest_ro'
    match_pattern: "^SELECT.*"
    destination_hostgroup: 1
    active: 1
    retries: 3
    state: present
    load_to_runtime: False

# This example removes all rules that use the username 'guest_ro', saves the
# mysql query rule config to disk, and dynamically loads the mysql query rule
# config to runtime.  It uses credentials in a supplied config file to connect
# to the proxysql admin interface.

- proxysql_query_rules:
    config_file: '~/proxysql.cnf'
    username: 'guest_ro'
    state: absent
    force_delete: true

```

## License

TODO

## Author Information
  - ['Ben Mildren (@bmildren)']
