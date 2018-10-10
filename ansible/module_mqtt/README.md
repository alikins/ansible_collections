# Ansible module: ansible.module_mqtt


Publish a message on an MQTT topic for the IoT

## Description

Publish a message on an MQTT topic.

## Requirements

TODO

## Arguments

``` json
{
    "ca_certs": "{'description': ['The path to the Certificate Authority certificate files that are to be treated as trusted by this client. If this is the only option given then the client will operate in a similar manner to a web browser. That is to say it will require the broker to have a certificate signed by the Certificate Authorities in ca_certs and will communicate using TLS v1, but will not attempt any form of authentication. This provides basic network encryption but may not be sufficient depending on how the broker is configured.'], 'version_added': 2.3}",
    "certfile": "{'description': ['The path pointing to the PEM encoded client certificate. If this is not None it will be used as client information for TLS based authentication. Support for this feature is broker dependent.'], 'version_added': 2.3}",
    "client_id": "{'description': ['MQTT client identifier'], 'default': 'hostname + pid'}",
    "keyfile": "{'description': ['The path pointing to the PEM encoded client private key. If this is not None it will be used as client information for TLS based authentication. Support for this feature is broker dependent.'], 'version_added': 2.3}",
    "password": "{'description': ['Password for C(username) to authenticate against the broker.']}",
    "payload": "{'description': ['Payload. The special string C("None") may be used to send a NULL (i.e. empty) payload which is useful to simply notify with the I(topic) or to clear previously retained messages.'], 'required': True}",
    "port": "{'description': ['MQTT broker port number'], 'default': 1883}",
    "qos": "{'description': ['QoS (Quality of Service)'], 'default': 0, 'choices': ['0', '1', '2']}",
    "retain": "{'description': ['Setting this flag causes the broker to retain (i.e. keep) the message so that applications that subsequently subscribe to the topic can received the last retained message immediately.'], 'type': 'bool', 'default': False}",
    "server": "{'description': ['MQTT broker address/name'], 'default': 'localhost'}",
    "topic": "{'description': ['MQTT topic name'], 'required': True}",
    "username": "{'description': ['Username to authenticate against the broker.']}",
}
```

## Examples


``` yaml

- mqtt:
    topic: 'service/ansible/{{ ansible_hostname }}'
    payload: 'Hello at {{ ansible_date_time.iso8601 }}'
    qos: 0
    retain: False
    client_id: ans001
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens)']
