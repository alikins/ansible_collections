# Ansible module: ansible.module_gcpubsub


Create and Delete Topics/Subscriptions, Publish and pull messages on PubSub

## Description

Create and Delete Topics/Subscriptions, Publish and pull messages on PubSub. See U(https://cloud.google.com/pubsub/docs) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "ack_deadline": "{'description': ['Subfield of subscription. Not required. Default deadline for subscriptions to ACK the message before it is resent. See examples.']}",
    "name": "{'description': ['Subfield of subscription. Required if subscription is specified. See examples.']}",
    "publish": "{'description': ['List of dictionaries describing messages and attributes to be published.  Dictionary is in message(str):attributes(dict) format. Only message is required.']}",
    "pull": "{'description': ["Subfield of subscription. Not required. If specified, messages will be retrieved from topic via the provided subscription name. max_messages (int; default None; max number of messages to pull), message_ack (bool; default False; acknowledge the message) and return_immediately (bool; default True, don't wait for messages to appear). If the messages are acknowledged, changed is set to True, otherwise, changed is False."]}",
    "push_endpoint": "{'description': ['Subfield of subscription.  Not required.  If specified, message will be sent to an endpoint. See U(https://cloud.google.com/pubsub/docs/advanced#push_endpoints) for more information.']}",
    "state": "{'description': ['State of the topic or queue.', 'Applies to the most granular resource.', 'If subscription isspecified we remove it.', 'If only topic is specified, that is what is removed.', 'NOTE - A topic can be removed without first removing the subscription.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "subscription": "{'description': ['Dictionary containing a subscripton name associated with a topic (required), along with optional ack_deadline, push_endpoint and pull. For pulling from a subscription, message_ack (bool), max_messages (int) and return_immediate are available as subfields. See subfields name, push_endpoint and ack_deadline for more information.']}",
    "topic": "{'description': ['GCP pubsub topic name.', 'Only the name, not the full path, is required.'], 'required': True}",
}
```

## Examples


``` yaml

# (Message will be pushed; there is no check to see if the message was pushed before
- name: Create a topic and publish a message to it
  gcpubsub:
    topic: ansible-topic-example
    state: present

# Subscriptions associated with topic are not deleted.
- name: Delete Topic
  gcpubsub:
    topic: ansible-topic-example
    state: absent

# Setting absent will keep the messages from being sent
- name: Publish multiple messages, with attributes (key:value available with the message)
  gcpubsub:
    topic: '{{ topic_name }}'
    state: present
    publish:
      - message: this is message 1
        attributes:
          mykey1: myvalue
          mykey2: myvalu2
          mykey3: myvalue3
      - message: this is message 2
        attributes:
          server: prod
          sla: "99.9999"
          owner: fred

- name: Create Subscription (pull)
  gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
    state: present

# pull is default, ack_deadline is not required
- name: Create Subscription with ack_deadline and push endpoint
  gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
      ack_deadline: "60"
      push_endpoint: http://pushendpoint.example.com
    state: present

# Setting push_endpoint to "None" converts subscription to pull.
- name: Subscription change from push to pull
  gcpubsub:
    topic: ansible-topic-example
    subscription:
      name: mysub
      push_endpoint: "None"

### Topic will not be deleted
- name: Delete subscription
  gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
    state: absent

# only pull keyword is required.
- name: Pull messages from subscription
  gcpubsub:
    topic: ansible-topic-example
    subscription:
      name: ansible-topic-example-sub
      pull:
        message_ack: yes
        max_messages: "100"

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
