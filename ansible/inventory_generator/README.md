# Ansible inventory: ansible.inventory_generator


Uses Jinja2 to construct hosts and groups from patterns

## Description

Uses a YAML configuration file with a valid YAML or C(.config) extension to define var expressions and group conditionals
Create a template pattern that describes each host, and then use independent configuration layers
Every element of every layer is combined to create a host for every layer combination
Parent groups can be defined with reference to hosts and other groups using the same template variables

## Requirements

TODO

## Arguments

``` json
{
    "hosts": "{'description': ['The C(name) key is a template used to generate hostnames based on the C(layers) option. Each variable in the name is expanded to create a cartesian product of all possible layer combinations.', 'The C(parents) are a list of parent groups that the host belongs to. Each C(parent) item contains a C(name) key, again expanded from the template, and an optional C(parents) key that lists its parents.', 'Parents can also contain C(vars), which is a dictionary of vars that is then always set for that variable. This can provide easy access to the group name. E.g set an C(application) variable that is set to the value of the C(application) layer name.']}",
    "layers": "{'description': ['A dictionary of layers, with the key being the layer name, used as a variable name in the C(host) C(name) and C(parents) keys. Each layer value is a list of possible values for that layer.']}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'generator' plugin."], 'required': True, 'choices': ['generator']}",
}
```

## Examples


``` yaml

    # inventory.config file in YAML format
    plugin: generator
    strict: False
    hosts:
        name: "{{ operation }}-{{ application }}-{{ environment }}-runner"
        parents:
          - name: "{{ operation }}-{{ application }}-{{ environment }}"
            parents:
              - name: "{{ operation }}-{{ application }}"
                parents:
                  - name: "{{ operation }}"
                  - name: "{{ application }}"
              - name: "{{ application }}-{{ environment }}"
                parents:
                  - name: "{{ application }}"
                    vars:
                      application: "{{ application }}"
                  - name: "{{ environment }}"
                    vars:
                      environment: "{{ environment }}"
          - name: runner
    layers:
        operation:
            - build
            - launch
        environment:
            - dev
            - test
            - prod
        application:
            - web
            - api

```

## License

TODO

## Author Information
  - ['UNKNOWN']
