# Ansible module: ansible.module_librato_annotation


create an annotation in librato

## Description

Create an annotation event on the given annotation stream :name. If the annotation stream does not exist, it will be created automatically

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Librato account api key'], 'required': True}",
    "description": "{'description': ['The description contains extra meta-data about a particular annotation', 'The description should contain specifics on the individual annotation e.g. Deployed 9b562b2 shipped new feature foo!'], 'required': False}",
    "end_time": "{'description': ['The unix timestamp indicating the time at which the event referenced by this annotation ended', 'For events that have a duration, this is a useful way to annotate the duration of the event'], 'required': False}",
    "links": "{'description': ['See examples'], 'required': True}",
    "name": "{'description': ['The annotation stream name', 'If the annotation stream does not exist, it will be created automatically'], 'required': False}",
    "source": "{'description': ['A string which describes the originating source of an annotation when that annotation is tracked across multiple members of a population'], 'required': False}",
    "start_time": "{'description': ['The unix timestamp indicating the time at which the event referenced by this annotation started'], 'required': False}",
    "title": "{'description': ['The title of an annotation is a string and may contain spaces', 'The title should be a short, high-level summary of the annotation e.g. v45 Deployment'], 'required': True}",
    "user": "{'description': ['Librato account username'], 'required': True}",
}
```

## Examples


``` yaml

# Create a simple annotation event with a source
- librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXX
    title: App Config Change
    source: foo.bar
    description: This is a detailed description of the config change

# Create an annotation that includes a link
- librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXXX
    name: code.deploy
    title: app code deploy
    description: this is a detailed description of a deployment
    links:
      - rel: example
        href: http://www.example.com/deploy

# Create an annotation with a start_time and end_time
- librato_annotation:
    user: user@example.com
    api_key: XXXXXXXXXXXXXXXXXX
    name: maintenance
    title: Maintenance window
    description: This is a detailed description of maintenance
    start_time: 1395940006
    end_time: 1395954406

```

## License

TODO

## Author Information
  - ['Seth Edwards (@sedward)']
