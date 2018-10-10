# Ansible module: ansible.module_grafana_datasource


Manage Grafana datasources

## Description

Create/update/delete Grafana datasources via API.

## Requirements

TODO

## Arguments

``` json
{
    "access": "{'description': ['The access mode for this datasource.'], 'choices': ['direct', 'proxy'], 'default': 'proxy'}",
    "basic_auth_password": "{'description': ['The datasource basic auth password, when C(basic auth) is C(yes).']}",
    "basic_auth_user": "{'description': ['The datasource basic auth user.', 'Setting this option with basic_auth_password will enable basic auth.']}",
    "client_cert": "{'required': False, 'description': ['TLS certificate path used by ansible to query grafana api'], 'version_added': 2.8}",
    "client_key": "{'required': False, 'description': ['TLS private key path used by ansible to query grafana api'], 'version_added': 2.8}",
    "database": "{'description': ['Name of the database for the datasource.', 'This options is required when the C(ds_type) is C(influxdb), C(elasticsearch) (index name), C(mysql) or C(postgres).'], 'required': False}",
    "ds_type": "{'description': ['The type of the datasource.'], 'required': True, 'choices': ['graphite', 'prometheus', 'elasticsearch', 'influxdb', 'opentsdb', 'mysql', 'postgres', 'alexanderzobnin-zabbix-datasource']}",
    "es_version": "{'description': ['Elasticsearch version (for C(ds_type = elasticsearch) only)', 'Version 56 is for elasticsearch 5.6+ where tou can specify the C(max_concurrent_shard_requests) option.'], 'choices': [2, 5, 56], 'default': 5}",
    "grafana_api_key": "{'description': ['The Grafana API key.', 'If set, C(grafana_user) and C(grafana_password) will be ignored.']}",
    "grafana_url": "{'description': ['The Grafana URL.'], 'required': True}",
    "interval": "{'description': ['For elasticsearch C(ds_type), this is the index pattern used.'], 'choices': ['', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Yearly']}",
    "is_default": "{'description': ['Make this datasource the default one.'], 'type': 'bool', 'default': False}",
    "max_concurrent_shard_requests": "{'description': ['Starting with elasticsearch 5.6, you can specify the max concurrent shard per requests.'], 'default': 256}",
    "name": "{'description': ['The name of the datasource.'], 'required': True}",
    "org_id": "{'description': ['Grafana Organisation ID in which the datasource should be created.', 'Not used when C(grafana_api_key) is set, because the C(grafana_api_key) only belong to one organisation.'], 'default': 1}",
    "password": "{'description': ['The datasource password']}",
    "sslmode": "{'description': ['SSL mode for C(postgres) datasoure type.'], 'choices': ['disable', 'require', 'verify-ca', 'verify-full']}",
    "state": "{'description': ['Status of the datasource'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "time_field": "{'description': ['Name of the time field in elasticsearch ds.', 'For example C(@timestamp)'], 'default': 'timestamp'}",
    "time_interval": "{'description': ['Minimum group by interval for C(influxdb) or C(elasticsearch) datasources.', 'for example C(>10s)']}",
    "tls_ca_cert": "{'description': ['The TLS CA certificate for self signed certificates.', 'Only used when C(tls_client_cert) and C(tls_client_key) are set.']}",
    "tls_client_cert": "{'description': ['The client TLS certificate.', 'If C(tls_client_cert) and C(tls_client_key) are set, this will enable TLS authentication.', 'Starts with ----- BEGIN CERTIFICATE -----']}",
    "tls_client_key": "{'description': ['The client TLS private key', 'Starts with ----- BEGIN RSA PRIVATE KEY -----']}",
    "tls_skip_verify": "{'description': ['Skip the TLS datasource certificate verification.'], 'type': 'bool', 'default': False, 'version_added': 2.6}",
    "trends": "{'required': False, 'description': ['Use trends or not for zabbix datasource type'], 'type': 'bool', 'version_added': 2.6}",
    "tsdb_resolution": "{'description': ['The opentsdb time resolution.'], 'choices': ['millisecond', 'second'], 'default': 'second'}",
    "tsdb_version": "{'description': ['The opentsdb version.', 'Use C(1) for <=2.1, C(2) for ==2.2, C(3) for ==2.3.'], 'choices': [1, 2, 3], 'default': 1}",
    "url": "{'description': ['The URL of the datasource.'], 'required': True, 'aliases': ['ds_url']}",
    "url_password": "{'description': ['The Grafana API password.'], 'default': 'admin', 'aliases': ['grafana_password'], 'version_added': 2.7}",
    "url_username": "{'description': ['The Grafana API user.'], 'default': 'admin', 'aliases': ['grafana_user'], 'version_added': 2.7}",
    "use_proxy": "{'description': ['Boolean of whether or not to use proxy.'], 'default': True, 'type': 'bool', 'version_added': 2.8}",
    "user": "{'description': ['The datasource login user for influxdb datasources.']}",
    "validate_certs": "{'description': ['Whether to validate the Grafana certificate.'], 'type': 'bool', 'default': True}",
    "with_credentials": "{'description': ['Whether credentials such as cookies or auth headers should be sent with cross-site requests.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

---
- name: Create elasticsearch datasource
  grafana_datasource:
    name: "datasource-elastic"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "elasticisearch"
    ds_url: "https://elastic.company.com:9200"
    database: "[logstash_]YYYY.MM.DD"
    basic_auth_user: "grafana"
    basic_auth_password: "******"
    time_field: "@timestamp"
    time_interval: "1m"
    interval: "Daily"
    es_version: 56
    max_concurrent_shard_requests: 42
    tls_ca_cert: "/etc/ssl/certs/ca.pem"

- name: Create influxdb datasource
  grafana_datasource:
    name: "datasource-influxdb"
    grafana_url: "https://grafana.company.com"
    grafana_user: "admin"
    grafana_password: "xxxxxx"
    org_id: "1"
    ds_type: "influxdb"
    ds_url: "https://influx.company.com:8086"
    database: "telegraf"
    time_interval: ">10s"
    tls_ca_cert: "/etc/ssl/certs/ca.pem"

```

## License

TODO

## Author Information
  - ['Thierry Sallé (@seuf)']
