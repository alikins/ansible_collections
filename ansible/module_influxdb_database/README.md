# Ansible module: ansible.module_influxdb_database


Manage InfluxDB databases

## Description

Manage InfluxDB databases.

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
    "retries": "{'description': ['Number of retries client will try before aborting.', 'C(0) indicates try until success.'], 'default': 3, 'version_added': '2.5'}",
    "ssl": "{'description': ['Use https instead of http to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "state": "{'description': ['Determines if the database should be created or destroyed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Number of seconds Requests will wait for client to establish a connection.'], 'version_added': '2.5'}",
    "udp_port": "{'description': ['UDP port to connect to InfluxDB server.'], 'default': 4444, 'version_added': '2.5'}",
    "use_udp": "{'description': ['Use UDP to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "username": "{'description': ['Username that will be used to authenticate against InfluxDB server.', 'Alias C(login_username) added in version 2.5.'], 'default': 'root', 'aliases': ['login_username']}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Example influxdb_database command from Ansible Playbooks
- name: Create database
  influxdb_database:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"

- name: Destroy database
  influxdb_database:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      state: absent

- name: Create database using custom credentials
  influxdb_database:
      hostname: "{{influxdb_ip_address}}"
      username: "{{influxdb_username}}"
      password: "{{influxdb_password}}"
      database_name: "{{influxdb_database_name}}"
      ssl: yes
      validate_certs: yes

```

## License

TODO

## Author Information
  - ['Kamil Szczygiel (@kamsz)']
