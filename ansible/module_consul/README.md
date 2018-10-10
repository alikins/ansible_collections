# Ansible module: ansible.module_consul


Add, modify & delete services within a consul cluster

## Description

Registers services and checks for an agent with a consul cluster. A service is some process running on the agent node that should be advertised by consul's discovery mechanism. It may optionally supply a check definition, a periodic service test to notify the consul cluster of service's health.
Checks may also be registered per node e.g. disk usage, or cpu usage and notify the health of the entire node to the cluster. Service level checks do not require a check name or id as these are derived by Consul from the Service name and id respectively by appending 'service:' Node level checks require a check_name and optionally a check_id.
Currently, there is no complete way to retrieve the script, interval or ttl metadata for a registered check. Without this metadata it is  not possible to tell if the data supplied with ansible represents a change to a check. As a result this does not attempt to determine changes and will always report a changed occurred. An api method is planned to supply this metadata so at that stage change management will be added.
See http://consul.io for more details.

## Requirements

TODO

## Arguments

``` json
{
    "check_id": "{'description': ['an ID for the service check, defaults to the check name, ignored if part of a service definition.']}",
    "check_name": "{'description': ['a name for the service check, defaults to the check id. required if standalone, ignored if part of service definition.']}",
    "host": "{'description': ['host of the consul agent defaults to localhost'], 'default': 'localhost'}",
    "http": "{'description': ['checks can be registered with an http endpoint. This means that consul will check that the http endpoint returns a successful http status. Interval must also be provided with this option.'], 'version_added': '2.0'}",
    "interval": "{'description': ['the interval at which the service check will be run. This is a number with a s or m suffix to signify the units of seconds or minutes e.g 15s or 1m. If no suffix is supplied, m will be used by default e.g. 1 will be 1m. Required if the script param is specified.']}",
    "notes": "{'description': ['Notes to attach to check when registering it.']}",
    "port": "{'description': ['the port on which the consul agent is running'], 'default': 8500}",
    "scheme": "{'description': ['the protocol scheme on which the consul agent is running'], 'default': 'http', 'version_added': '2.1'}",
    "script": "{'description': ['the script/command that will be run periodically to check the health of the service. Scripts require an interval and vise versa']}",
    "service_address": "{'description': ["the address to advertise that the service will be listening on. This value will be passed as the I(Address) parameter to Consul's U(/v1/agent/service/register) API method, so refer to the Consul API documentation for further details."], 'version_added': '2.1'}",
    "service_id": "{'description': ['the ID for the service, must be unique per node, defaults to the service name if the service name is supplied'], 'default': 'service_name if supplied'}",
    "service_name": "{'description': ['Unique name for the service on a node, must be unique per node, required if registering a service. May be omitted if registering a node level check']}",
    "service_port": "{'description': ['the port on which the service is listening. Can optionally be supplied for registration of a service, i.e. if service_name or service_id is set']}",
    "state": "{'description': ['register or deregister the consul service, defaults to present'], 'required': True, 'choices': ['present', 'absent']}",
    "tags": "{'description': ['a list of tags that will be attached to the service registration.']}",
    "timeout": "{'description': ['A custom HTTP check timeout. The consul default is 10 seconds. Similar to the interval this is a number with a s or m suffix to signify the units of seconds or minutes, e.g. 15s or 1m.'], 'version_added': '2.0'}",
    "token": "{'description': ['the token key indentifying an ACL rule set. May be required to register services.']}",
    "ttl": "{'description': ["checks can be registered with a ttl instead of a script and interval this means that the service will check in with the agent before the ttl expires. If it doesn't the check will be considered failed. Required if registering a check and the script an interval are missing Similar to the interval this is a number with a s or m suffix to signify the units of seconds or minutes e.g 15s or 1m. If no suffix is supplied, m will be used by default e.g. 1 will be 1m"]}",
    "validate_certs": "{'description': ['whether to verify the tls certificate of the consul agent'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

- name: register nginx service with the local consul agent
  consul:
    service_name: nginx
    service_port: 80

- name: register nginx service with curl check
  consul:
    service_name: nginx
    service_port: 80
    script: curl http://localhost
    interval: 60s

- name: register nginx with an http check
  consul:
    service_name: nginx
    service_port: 80
    interval: 60s
    http: http://localhost:80/status

- name: register external service nginx available at 10.1.5.23
  consul:
    service_name: nginx
    service_port: 80
    service_address: 10.1.5.23

- name: register nginx with some service tags
  consul:
    service_name: nginx
    service_port: 80
    tags:
      - prod
      - webservers

- name: remove nginx service
  consul:
    service_name: nginx
    state: absent

- name: register celery worker service
  consul:
    service_name: celery-worker
    tags:
      - prod
      - worker

- name: create a node level check to test disk usage
  consul:
    check_name: Disk usage
    check_id: disk_usage
    script: /opt/disk_usage.py
    interval: 5m

- name: register an http check against a service that's already registered
  consul:
    check_name: nginx-check2
    check_id: nginx-check2
    service_id: nginx
    interval: 60s
    http: http://localhost:80/morestatus

```

## License

TODO

## Author Information
  - ['Steve Gargan (@sgargan)']
