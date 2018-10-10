# Ansible module: ansible.module_gcp_sql_instance


Creates a GCP Instance

## Description

Represents a Cloud SQL instance. Cloud SQL instances are SQL databases hosted in Google's cloud. The Instances resource provides methods for common configuration and management tasks.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "backend_type": "{'description': ['* FIRST_GEN: First Generation instance. MySQL only.', '* SECOND_GEN: Second Generation instance or PostgreSQL instance.', '* EXTERNAL: A database server that is not managed by Google.'], 'required': False, 'choices': ['FIRST_GEN', 'SECOND_GEN', 'EXTERNAL']}",
    "connection_name": "{'description': ['Connection name of the Cloud SQL instance used in connection strings.'], 'required': False}",
    "database_version": "{'description': ['The database engine type and version. For First Generation instances, can be MYSQL_5_5, or MYSQL_5_6. For Second Generation instances, can be MYSQL_5_6 or MYSQL_5_7. Defaults to MYSQL_5_6.', 'PostgreSQL instances: POSTGRES_9_6  The databaseVersion property can not be changed after instance creation.'], 'required': False, 'choices': ['MYSQL_5_5', 'MYSQL_5_6', 'MYSQL_5_7', 'POSTGRES_9_6']}",
    "failover_replica": "{'description': ['The name and status of the failover replica. This property is applicable only to Second Generation instances.'], 'required': False, 'suboptions': {'available': {'description': ['The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The master can only failover to the falover replica when the status is true.'], 'required': False, 'type': 'bool'}, 'name': {'description': ["The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID. This property is applicable only to Second Generation instances."], 'required': False}}}",
    "instance_type": "{'description': ['The instance type. This can be one of the following.', '* CLOUD_SQL_INSTANCE: A Cloud SQL instance that is not replicating   from a master.', "* ON_PREMISES_INSTANCE: An instance running on the customer's   premises.", '* READ_REPLICA_INSTANCE: A Cloud SQL instance configured as a   read-replica.'], 'required': False, 'choices': ['CLOUD_SQL_INSTANCE', 'ON_PREMISES_INSTANCE', 'READ_REPLICA_INSTANCE']}",
    "ipv6_address": "{'description': ['The IPv6 address assigned to the instance. This property is applicable only to First Generation instances.'], 'required': False}",
    "master_instance_name": "{'description': ['The name of the instance which will act as master in the replication setup.'], 'required': False}",
    "max_disk_size": "{'description': ['The maximum disk size of the instance in bytes.'], 'required': False}",
    "name": "{'description': ['Name of the Cloud SQL instance. This does not include the project ID.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['The geographical region. Defaults to us-central or us-central1 depending on the instance type (First Generation or Second Generation/PostgreSQL).'], 'required': False}",
    "replica_configuration": "{'description': ['Configuration specific to failover replicas and read replicas.'], 'required': False, 'suboptions': {'failover_target': {'description': ['Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica.', 'In case the master instance fails, the replica instance will be promoted as the new master instance.', 'Only one replica can be specified as failover target, and the replica has to be in different zone with the master instance.'], 'required': False, 'type': 'bool'}, 'mysql_replica_configuration': {'description': ['MySQL specific configuration when replicating from a MySQL on-premises master. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata.  The configuration information is used only to set up the replication connection and is stored by MySQL in a file named master.info in the data directory.'], 'required': False, 'suboptions': {'ca_certificate': {'description': ["PEM representation of the trusted CA's x509 certificate."], 'required': False}, 'client_certificate': {'description': ["PEM representation of the slave's x509 certificate ."], 'required': False}, 'client_key': {'description': ["PEM representation of the slave's private key. The corresponsing public key is encoded in the client's asf asd certificate."], 'required': False}, 'connect_retry_interval': {'description': ["Seconds to wait between connect retries. MySQL's default is 60 seconds."], 'required': False}, 'dump_file_path': {'description': ['Path to a SQL dump file in Google Cloud Storage from which the slave instance is to be created. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. Dumps should have the binlog co-ordinates from which replication should begin. This can be accomplished by setting --master-data to 1 when using mysqldump.'], 'required': False}, 'master_heartbeat_period': {'description': ['Interval in milliseconds between replication heartbeats.'], 'required': False}, 'password': {'description': ['The password for the replication connection.'], 'required': False}, 'ssl_cipher': {'description': ['A list of permissible ciphers to use for SSL encryption.'], 'required': False}, 'username': {'description': ['The username for the replication connection.'], 'required': False}, 'verify_server_certificate': {'description': ["Whether or not to check the master's Common Name value in the certificate that it sends during the SSL handshake."], 'required': False, 'type': 'bool'}}}, 'replica_names': {'description': ['The replicas of the instance.'], 'required': False}, 'service_account_email_address': {'description': ['The service account email address assigned to the instance. This property is applicable only to Second Generation instances.'], 'required': False}}}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "settings": "{'description': ['The user settings.'], 'required': False, 'suboptions': {'ip_configuration': {'description': ['The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled for Second Generation instances.'], 'required': False, 'suboptions': {'ipv4_enabled': {'description': ['Whether the instance should be assigned an IP address or not.'], 'required': False, 'type': 'bool'}, 'authorized_networks': {'description': ["The list of external networks that are allowed to connect to the instance using the IP. In CIDR notation, also known as 'slash' notation (e.g. 192.168.100.0/24)."], 'required': False, 'suboptions': {'expiration_time': {'description': ['The time when this access control entry expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.'], 'required': False}, 'name': {'description': ['An optional label to identify this entry.'], 'required': False}, 'value': {'description': ['The whitelisted value for the access control list. For example, to grant access to a client from an external IP (IPv4 or IPv6) address or subnet, use that address or subnet here.'], 'required': False}}}, 'require_ssl': {'description': ["Whether the mysqld should default to 'REQUIRE X509' for users connecting over IP."], 'required': False, 'type': 'bool'}}}, 'tier': {'description': ['The tier or machine type for this instance, for example db-n1-standard-1. For MySQL instances, this field determines whether the instance is Second Generation (recommended) or First Generation.'], 'required': False}}}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a instance
  gcp_sql_instance:
      name: "test_object"
      settings:
        ip_configuration:
          authorized_networks:
          - name: google dns server
            value: 8.8.8.8/32
        tier: db-n1-standard-1
      region: us-central1
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
