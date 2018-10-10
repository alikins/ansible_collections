# Ansible module: ansible.module_pubnub_blocks


PubNub blocks management module

## Description

This module allows Ansible to interface with the PubNub BLOCKS infrastructure by providing the following operations: create / remove, start / stop and rename for blocks and create / modify / remove for event handlers

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Name of PubNub account for from which C(application) will be used to manage blocks.', "User's account will be used if value not set or empty."], 'required': False, 'version_added': '2.4'}",
    "application": "{'description': ['Name of target PubNub application for which blocks configuration on specific C(keyset) will be done.'], 'required': True}",
    "cache": "{'description': ["In case if single play use blocks management module few times it is preferred to enabled 'caching' by making previous module to share gathered artifacts and pass them to this parameter.\n"], 'required': False, 'default': {}}",
    "changes": "{'description': ["List of fields which should be changed by block itself (doesn't affect any event handlers).", 'Possible options for change is: C(name).'], 'required': False, 'default': {}}",
    "description": "{'description': ["Short block description which will be later visible on admin.pubnub.com. Used only if block doesn't exists and won't change description for existing block."], 'required': False, 'default': 'New block'}",
    "email": "{'description': ['Email from account for which new session should be started.', 'Not required if C(cache) contains result of previous module call (in same play).'], 'required': False}",
    "event_handlers": "{'description': ['List of event handlers which should be updated for specified block C(name).', 'Each entry for new event handler should contain: C(name), C(src), C(channels), C(event). C(name) used as event handler name which can be used later to make changes to it.', 'C(src) is full path to file with event handler code.', 'C(channels) is name of channel from which event handler is waiting for events.', 'C(event) is type of event which is able to trigger event handler: I(js-before-publish), I(js-after-publish), I(js-after-presence).', 'Each entry for existing handlers should contain C(name) (so target handler can be identified). Rest parameters (C(src), C(channels) and C(event)) can be added if changes required for them.', 'It is possible to rename event handler by adding C(changes) key to event handler payload and pass dictionary, which will contain single key C(name), where new name should be passed.', 'To remove particular event handler it is possible to set C(state) for it to C(absent) and it will be removed.'], 'required': False, 'default': []}",
    "keyset": "{'description': ["Name of application's keys set which is bound to managed blocks."], 'required': True}",
    "name": "{'description': ['Name of managed block which will be later visible on admin.pubnub.com.'], 'required': True}",
    "password": "{'description': ['Password which match to account to which specified C(email) belong.', 'Not required if C(cache) contains result of previous module call (in same play).'], 'required': False}",
    "state": "{'description': ['Intended block state after event handlers creation / update process will be completed.'], 'required': False, 'default': 'started', 'choices': ['started', 'stopped', 'present', 'absent']}",
    "validate_certs": "{'description': ['This key allow to try skip certificates check when performing REST API calls. Sometimes host may have issues with certificates on it and this will cause problems to call PubNub REST API.', 'If check should be ignored C(False) should be passed to this parameter.'], 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Event handler create example.
- name: Create single event handler
  pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    event_handlers:
      -
        src: '{{ path_to_handler_source }}'
        name: '{{ handler_name }}'
        event: 'js-before-publish'
        channels: '{{ handler_channel }}'

# Change event handler trigger event type.
- name: Change event handler 'event'
  pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    event_handlers:
      -
        name: '{{ handler_name }}'
        event: 'js-after-publish'

# Stop block and event handlers.
- name: Stopping block
  pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: stop

# Multiple module calls with cached result passing
- name: Create '{{ block_name }}' block
  register: module_cache
  pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
- name: Add '{{ event_handler_1_name }}' handler to '{{ block_name }}'
  register: module_cache
  pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
    event_handlers:
      -
        src: '{{ path_to_handler_1_source }}'
        name: '{{ event_handler_1_name }}'
        channels: '{{ event_handler_1_channel }}'
        event: 'js-before-publish'
- name: Add '{{ event_handler_2_name }}' handler to '{{ block_name }}'
  register: module_cache
  pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
    event_handlers:
      -
        src: '{{ path_to_handler_2_source }}'
        name: '{{ event_handler_2_name }}'
        channels: '{{ event_handler_2_channel }}'
        event: 'js-before-publish'
- name: Start '{{ block_name }}' block
  register: module_cache
  pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: started

```

## License

TODO

## Author Information
  - ['PubNub <support@pubnub.com> (@pubnub)', 'Sergey Mamontov <sergey@pubnub.com> (@parfeon)']
  - ['PubNub <support@pubnub.com> (@pubnub)', 'Sergey Mamontov <sergey@pubnub.com> (@parfeon)']
