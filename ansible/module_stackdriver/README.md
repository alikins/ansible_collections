# Ansible module: ansible.module_stackdriver


Send code deploy and annotation events to stackdriver

## Description

Send code deploy and annotation events to Stackdriver

## Requirements

TODO

## Arguments

``` json
{
    "annotated_by": "{'description': ['The person or robot\xa0who the annotation should be attributed to.'], 'default': 'Ansible'}",
    "deployed_by": "{'description': ['The person or robot responsible for deploying the code'], 'default': 'Ansible'}",
    "deployed_to": "{'description': ['The environment code was deployed to. (ie: development, staging, production)']}",
    "event": "{'description': ['The type of event to send, either annotation or deploy'], 'choices': ['annotation', 'deploy']}",
    "event_epoch": "{'description': ['Unix timestamp of where the event should appear in the timeline, defaults to now. Be careful with this.']}",
    "instance_id": "{'description': ['id of an EC2 instance that this event should be attached to, which will limit the contexts where this event is shown']}",
    "key": "{'description': ['API key.'], 'required': True}",
    "level": "{'description': ['one of INFO/WARN/ERROR, defaults to INFO if not supplied. \xa0May affect display.'], 'choices': ['INFO', 'WARN', 'ERROR'], 'default': 'INFO'}",
    "msg": "{'description': ['The contents of the annotation message, in plain text. \xa0Limited to 256 characters. Required for annotation.']}",
    "repository": "{'description': ['The repository (or project) deployed']}",
    "revision_id": "{'description': ['The revision of the code that was deployed. Required for deploy events']}",
}
```

## Examples


``` yaml

- stackdriver:
    key: AAAAAA
    event: deploy
    deployed_to: production
    deployed_by: leeroyjenkins
    repository: MyWebApp
    revision_id: abcd123

- stackdriver:
    key: AAAAAA
    event: annotation
    msg: Greetings from Ansible
    annotated_by: leeroyjenkins
    level: WARN
    instance_id: i-abcd1234

```

## License

TODO

## Author Information
  - ['Ben Whaley (@bwhaley)']
