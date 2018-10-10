# Ansible module: ansible.module_circonus_annotation


create an annotation in circonus

## Description

Create an annotation event with a given category, title and description. Optionally start, end or durations can be provided

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Circonus API key'], 'required': True}",
    "category": "{'description': ['Annotation Category'], 'required': True}",
    "description": "{'description': ['Description of annotation'], 'required': True}",
    "duration": "{'description': ['Duration in seconds of annotation'], 'default': 0}",
    "start": "{'description': ['Unix timestamp of event start'], 'default': 'I(now)'}",
    "stop": "{'description': ['Unix timestamp of event end'], 'default': 'I(now) + I(duration)'}",
    "title": "{'description': ['Title of annotation'], 'required': True}",
}
```

## Examples


``` yaml

# Create a simple annotation event with a source, defaults to start and end time of now
- circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations
# Create an annotation with a duration of 5 minutes and a default start time of now
- circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations
    duration: 300
# Create an annotation with a start_time and end_time
- circonus_annotation:
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    description: This is a detailed description of the config change
    category: This category groups like annotations
    start_time: 1395940006
    end_time: 1395954407

```

## License

TODO

## Author Information
  - ['Nick Harring (@NickatEpic)']
