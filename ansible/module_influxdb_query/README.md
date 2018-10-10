# Ansible module: ansible.module_influxdb_query


Query data points from InfluxDB

## Description

Query data points from InfluxDB.

## Requirements

TODO

## Arguments

``` json
{
    "database_name": "{'description': ['Name of the database.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address on which InfluxDB server is listening.', 'Since version 2.5, defaulted to localhost.'], 'default': 'localhost'}",
    "password": "{'description': ['Password that will be used to authenticate against InfluxDB server.', 'Alias C(login_password) added in version 2.5.'], 'default': 'root', 'aliases': ['login_password']}",
    "port": "{'description': ['The port on which InfluxDB server is listening'], 'default': 8086}",
    "proxies": "{'description': ['HTTP(S) proxy to use for Requests to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "query": "{'description': ['Query to be executed.'], 'required': True}",
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

- name: Query connections
  influxdb_query:
    hostname: "{{ influxdb_ip_address }}"
    database_name: "{{ influxdb_database_name }}"
    query: "select mean(value) from connections"
  register: connection

- name: Query connections with tags filters
  influxdb_query:
    hostname: "{{ influxdb_ip_address }}"
    database_name: "{{ influxdb_database_name }}"
    query: "select mean(value) from connections where region='zue01' and host='server01'"
  register: connection

- name: Print results from the query
  debug:
    var: connection.query_results

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
