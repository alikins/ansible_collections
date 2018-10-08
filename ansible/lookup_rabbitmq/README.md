# Ansible lookup: ansible.lookup_rabbitmq


Retrieve messages from an AMQP/AMQPS RabbitMQ queue

## Description

This lookup uses a basic get to retrieve all, or a limited number C(count), messages from a RabbitMQ queue.

## Requirements

TODO

## Arguments

``` json
{
    "count": "{'description': ['How many messages to collect from the queue.', 'If not set, defaults to retrieving all the messages from the queue.']}",
    "queue": "{'description': ['The queue to get messages from.'], 'required': True}",
    "url": "{'description': ['An URI connection string to connect to the AMQP/AMQPS RabbitMQ server.', 'For more information refer to the URI spec U(https://www.rabbitmq.com/uri-spec.html).'], 'required': True}",
}
```

## Examples


``` yaml

- name: Get all messages off a queue
  debug:
    msg: "{{ lookup('rabbitmq', url='amqp://guest:guest@192.168.0.10:5672/%2F', queue='hello') }}"


# If you are intending on using the returned messages as a variable in more than
# one task (eg. debug, template), it is recommended to set_fact.

- name: Get 2 messages off a queue and set a fact for re-use
  set_fact:
    messages: "{{ lookup('rabbitmq', url='amqp://guest:guest@192.168.0.10:5672/%2F', queue='hello', count=2) }}"

- name: Dump out contents of the messages
  debug:
    var: messages


```

## License

TODO

## Author Information
  - ['John Imison <@Im0>']
