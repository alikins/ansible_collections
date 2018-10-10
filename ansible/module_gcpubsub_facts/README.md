# Ansible module: ansible.module_gcpubsub_facts


List Topics/Subscriptions and Messages from Google PubSub

## Description

List Topics/Subscriptions from Google PubSub.  Use the gcpubsub module for topic/subscription management. See U(https://cloud.google.com/pubsub/docs) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "state": "{'description': ['list is the only valid option.'], 'required': False}",
    "topic": "{'description': ['GCP pubsub topic name.  Only the name, not the full path, is required.'], 'required': False}",
    "view": "{'description': ["Choices are 'topics' or 'subscriptions'"], 'required': True}",
}
```

## Examples


``` yaml

## List all Topics in a project
- gcpubsub_facts:
    view: topics
    state: list

## List all Subscriptions in a project
- gcpubsub_facts:
    view: subscriptions
    state: list

## List all Subscriptions for a Topic in a project
- gcpubsub_facts:
    view: subscriptions
    topic: my-topic
    state: list

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
