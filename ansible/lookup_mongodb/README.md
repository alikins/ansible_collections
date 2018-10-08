# Ansible lookup: ansible.lookup_mongodb


lookup info from MongoDB

## Description

The ``MongoDB`` lookup runs the *find()* command on a given *collection* on a given *MongoDB* server.
The result is a list of jsons, so slightly different from what PyMongo returns. In particular, *timestamps* are converted to epoch integers.

## Requirements

TODO

## Arguments

``` json
{
    "collection": "{'description': ['Name of the collection which the query will be made'], 'required': True}",
    "connect_string": "{'description': ['Can be any valid MongoDB connection string, supporting authentication, replicasets, etc.', 'More info at U(https://docs.mongodb.org/manual/reference/connection-string/)'], 'default': 'mongodb://localhost/'}",
    "database": "{'description': ['Name of the database which the query will be made'], 'required': True}",
    "filter": "{'description': ['Criteria of the output'], 'type': 'dict', 'default': '{}'}",
    "limit": "{'description': ['How many results should be shown'], 'type': 'integer'}",
    "projection": "{'description': ['Fields you want returned'], 'type': 'dict', 'default': '{}'}",
    "skip": "{'description': ['How many results should be skipped'], 'type': 'integer'}",
    "sort": "{'description': ['Sorting rules. Please notice the constats are replaced by strings.'], 'type': 'list', 'default': '[]'}",
}
```

## Examples


``` yaml

- hosts: all
  gather_facts: false
  vars:
    mongodb_parameters:
      #mandatory parameters
      database: 'local'
      #optional
      collection: "startup_log"
      connection_string: "mongodb://localhost/"
      extra_connection_parameters: { "ssl" : True , "ssl_certfile": /etc/self_signed_certificate.pem" }
      #optional query  parameters, we accept any parameter from the normal mongodb query.
      filter:  { "hostname": "batman" }
      projection: { "pid": True    , "_id" : False , "hostname" : True }
      skip: 0
      limit: 1
      sort:  [ [ "startTime" , "ASCENDING" ] , [ "age", "DESCENDING" ] ]
  tasks:
    - debug: msg="Mongo has already started with the following PID [{{ item.pid }}]"
      with_mongodb: "{{mongodb_parameters}}"

```

## License

TODO

## Author Information
  - ['Marcos Diez <marcos (at) unitron.com.br>']
