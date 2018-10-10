# Ansible module: ansible.module_influxdb_user


Manage InfluxDB users

## Description

Manage InfluxDB users

## Requirements

TODO

## Arguments

``` json
{
    "admin": "{'description': ['Whether the user should be in the admin role or not.'], 'default': False, 'type': 'bool'}",
    "hostname": "{'description': ['The hostname or IP address on which InfluxDB server is listening.', 'Since version 2.5, defaulted to localhost.'], 'default': 'localhost'}",
    "password": "{'description': ['Password that will be used to authenticate against InfluxDB server.', 'Alias C(login_password) added in version 2.5.'], 'default': 'root', 'aliases': ['login_password']}",
    "port": "{'description': ['The port on which InfluxDB server is listening'], 'default': 8086}",
    "proxies": "{'description': ['HTTP(S) proxy to use for Requests to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "retries": "{'description': ['Number of retries client will try before aborting.', 'C(0) indicates try until success.'], 'default': 3, 'version_added': '2.5'}",
    "ssl": "{'description': ['Use https instead of http to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "state": "{'description': ['State of the user.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['Number of seconds Requests will wait for client to establish a connection.'], 'version_added': '2.5'}",
    "udp_port": "{'description': ['UDP port to connect to InfluxDB server.'], 'default': 4444, 'version_added': '2.5'}",
    "use_udp": "{'description': ['Use UDP to connect to InfluxDB server.'], 'version_added': '2.5'}",
    "user_name": "{'description': ['Name of the user.'], 'required': True}",
    "user_password": "{'description': ['Password to be set for the user.'], 'required': False}",
    "username": "{'description': ['Username that will be used to authenticate against InfluxDB server.', 'Alias C(login_username) added in version 2.5.'], 'default': 'root', 'aliases': ['login_username']}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Create a user on localhost using default login credentials
  influxdb_user:
    user_name: john
    user_password: s3cr3t

- name: Create a user on localhost using custom login credentials
  influxdb_user:
    user_name: john
    user_password: s3cr3t
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"

- name: Create an admin user on a remote host using custom login credentials
  influxdb_user:
    user_name: john
    user_password: s3cr3t
    admin: yes
    hostname: "{{ influxdb_hostname }}"
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"

- name: Destroy a user using custom login credentials
  influxdb_user:
    user_name: john
    login_username: "{{ influxdb_username }}"
    login_password: "{{ influxdb_password }}"
    state: absent

```

## License

TODO

## Author Information
  - ['Vitaliy Zhhuta (@zhhuta)']
