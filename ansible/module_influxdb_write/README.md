# Ansible module: ansible.module_influxdb_write


Write data points into InfluxDB

## Description

Write data points into InfluxDB.

## Requirements

TODO

## Arguments

``` json
{
    "data_points": "{'description': ['Data points as dict to write into the database.'], 'required': True}",
    "database_name": "{'description': ['Name of the database.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address on which InfluxDB server is listening.', 'Since version 2.5, defaulted to localhost.'], 'default': 'localhost'}",
    "password": "{'description': ['Password that will be used to authenticate against InfluxDB server.', 'Alias C(login_password) added in version 2.5.'], 'default': 'root', 'aliases': ['login_password']}",
    "port": "{'description': ['The port on which InfluxDB server is listening'], 'default': 8086}",
    "proxies": "{'description': ['HTTP(S) proxy to use for Requests to connect to InfluxDB server.'], 'version_added': '2.5'}",
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

- name: Write points into database
  influxdb_write:
      hostname: "{{influxdb_ip_address}}"
      database_name: "{{influxdb_database_name}}"
      data_points:
        - measurement: connections
          tags:
            host: server01
            region: us-west
          time: "{{ ansible_date_time.iso8601 }}"
          fields:
            value: 2000
        - measurement: connections
          tags:
            host: server02
            region: us-east
          time: "{{ ansible_date_time.iso8601 }}"
          fields:
            value: 3000

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
