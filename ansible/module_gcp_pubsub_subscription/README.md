# Ansible module: ansible.module_gcp_pubsub_subscription


Creates a GCP Subscription

## Description

A named resource representing the stream of messages from a single, specific topic, to be delivered to the subscribing application.

## Requirements

TODO

## Arguments

``` json
{
    "ack_deadline_seconds": "{'description': ['This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an outstanding message and will not be delivered again during that time (on a best-effort basis).', 'For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes).', 'If this parameter is 0, a default value of 10 seconds is used.', 'For push delivery, this value is also used to set the request timeout for the call to the push endpoint.', 'If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message.'], 'required': False}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "name": "{'description': ['Name of the subscription.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "push_config": "{'description': ['If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that the subscriber will pull and ack messages using API methods.'], 'required': False, 'suboptions': {'push_endpoint': {'description': ['A URL locating the endpoint to which messages should be pushed.', 'For example, a Webhook endpoint might use "U(https://example.com/push".)'], 'required': False}}}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "topic": "{'description': ['A reference to a Topic resource.'], 'required': False}",
}
```

## Examples


``` yaml

- name: create a topic
  gcp_pubsub_topic:
      name: "topic-subscription"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: topic

- name: create a subscription
  gcp_pubsub_subscription:
      name: "test_object"
      topic: "{{ topic }}"
      push_config:
        push_endpoint: https://myapp.graphite.cloudnativeapp.com/webhook/sub1
      ack_deadline_seconds: 300
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
