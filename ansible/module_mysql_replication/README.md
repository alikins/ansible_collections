# Ansible module: ansible.module_mysql_replication


Manage MySQL replication

## Description

Manages MySQL server replication, slave, master status get and change master host.

## Requirements

TODO

## Arguments

``` json
{
    "config_file": "{'description': ['Specify a config file from which user and password are to be read.'], 'default': '~/.my.cnf', 'version_added': '2.0'}",
    "connect_timeout": "{'description': ['The connection timeout when connecting to the MySQL server.'], 'default': 30, 'version_added': '2.1'}",
    "login_host": "{'description': ['Host running the database.'], 'default': 'localhost'}",
    "login_password": "{'description': ['The password used to authenticate with.']}",
    "login_port": "{'description': ['Port of the MySQL server. Requires I(login_host) be defined as other then localhost if login_port is used.'], 'default': 3306}",
    "login_unix_socket": "{'description': ['The path to a Unix domain socket for local connections.']}",
    "login_user": "{'description': ['The username used to authenticate with.']}",
    "master_auto_position": "{'description': ['does the host uses GTID based replication or not'], 'version_added': '2.0'}",
    "master_connect_retry": "{'description': ['same as mysql variable']}",
    "master_host": "{'description': ['same as mysql variable']}",
    "master_log_file": "{'description': ['same as mysql variable']}",
    "master_log_pos": "{'description': ['same as mysql variable']}",
    "master_password": "{'description': ['same as mysql variable']}",
    "master_port": "{'description': ['same as mysql variable']}",
    "master_ssl": "{'description': ['same as mysql variable'], 'choices': [0, 1]}",
    "master_ssl_ca": "{'description': ['same as mysql variable']}",
    "master_ssl_capath": "{'description': ['same as mysql variable']}",
    "master_ssl_cert": "{'description': ['same as mysql variable']}",
    "master_ssl_cipher": "{'description': ['same as mysql variable']}",
    "master_ssl_key": "{'description': ['same as mysql variable']}",
    "master_user": "{'description': ['same as mysql variable']}",
    "mode": "{'description': ['module operating mode. Could be getslave (SHOW SLAVE STATUS), getmaster (SHOW MASTER STATUS), changemaster (CHANGE MASTER TO), startslave (START SLAVE), stopslave (STOP SLAVE), resetslave (RESET SLAVE), resetslaveall (RESET SLAVE ALL)'], 'choices': ['getslave', 'getmaster', 'changemaster', 'stopslave', 'startslave', 'resetslave', 'resetslaveall'], 'default': 'getslave'}",
    "relay_log_file": "{'description': ['same as mysql variable']}",
    "relay_log_pos": "{'description': ['same as mysql variable']}",
    "ssl_ca": "{'version_added': '2.0', 'description': ['The path to a Certificate Authority (CA) certificate. This option, if used, must specify the same certificate as used by the server.']}",
    "ssl_cert": "{'version_added': '2.0', 'description': ['The path to a client public key certificate.']}",
    "ssl_key": "{'version_added': '2.0', 'description': ['The path to the client private key.']}",
}
```

## Examples


``` yaml

# Stop mysql slave thread
- mysql_replication:
    mode: stopslave

# Get master binlog file name and binlog position
- mysql_replication:
    mode: getmaster

# Change master to master server 192.0.2.1 and use binary log 'mysql-bin.000009' with position 4578
- mysql_replication:
    mode: changemaster
    master_host: 192.0.2.1
    master_log_file: mysql-bin.000009
    master_log_pos: 4578

# Check slave status using port 3308
- mysql_replication:
    mode: getslave
    login_host: ansible.example.com
    login_port: 3308

```

## License

TODO

## Author Information
  - ['Balazs Pocze (@banyek)']
