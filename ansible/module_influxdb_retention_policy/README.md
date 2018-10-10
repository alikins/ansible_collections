# Ansible module: ansible.module_influxdb_retention_policy


Manage InfluxDB retention policies

## Description

Manage InfluxDB retention policies

## Requirements

TODO

## Arguments

``` json
{
    "database_name": "{'description': ['Name of the database.'], 'required': True}",
    "default": "{'description': ['Sets the retention policy as default retention policy'], 'required': True}",
    "duration": "{'description': ['Determines how long InfluxDB should keep the data'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address on which InfluxDB server is listening.', 'Since version 2.5, defaulted to localhost.'], 'default': 'localhost'}",
    "password": "{'description': ['Password that will be used to authenticate against InfluxDB server.', 'Alias C(login_password) added in version 2.5.'], 'default': 'root', 'aliases': ['login_password']}",
    "policy_name": "{'description': ['Name of the retention policy'], 'required': True}",
    "port": "{'description': ['The port on which InfluxDB server is listening'], 'default': 8086}",
    "proxies": "{'description': ['HTTP(S) proxy to use for Requests to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "replication": "{'description': ['Determines how many independent copies of each point are stored in the cluster'], 'required': True}",
    "retries": "{'description': ['Number of retries client will try before aborting.', 'C(0) indicates try until success.'], 'default': 3, 'version_added': '2.5'}",
    "ssl": "{'description': ['Use https instead of http to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "timeout": "{'description': ['Number of seconds Requests will wait for client to establish a connection.'], 'version_added': '2.5'}",
    "udp_port": "{'description': ['UDP port to connect to InfluxDB server.'], 'default': 4444, 'version_added': '2.5'}",
    "use_udp": "{'description': ['Use UDP to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "username": "{'description': ['Username that will be used to authenticate against InfluxDB server.', 'Alias C(login_username) added in version 2.5.'], 'default': 'root', 'aliases': ['login_username']}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Example influxdb_retention_policy command from Ansible Playbooks
- name: create 1 hour retention policy
  influxdb_retention_policy:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      policy_name: test
      duration: 1h
      replication: 1
      ssl: yes
      validate_certs: yes

- name: create 1 day retention policy
  influxdb_retention_policy:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      policy_name: test
      duration: 1d
      replication: 1

- name: create 1 week retention policy
  influxdb_retention_policy:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      policy_name: test
      duration: 1w
      replication: 1

- name: create infinite retention policy
  influxdb_retention_policy:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      policy_name: test
      duration: INF
      replication: 1
      ssl: no
      validate_certs: no

```

## License

TODO

## Author Information
  - ['Kamil Szczygiel (@kamsz)']
