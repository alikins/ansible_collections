# Ansible lookup: ansible.lookup_random_choice


return random element from list

## Description

The 'random_choice' feature can be used to pick something at random. While it's not a load balancer (there are modules for those), it can somewhat be used as a poor man's load balancer in a MacGyver like situation.
At a more basic level, they can be used to add chaos and excitement to otherwise predictable automation environments.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: Magic 8 ball for MUDs
  debug:
    msg: "{{ item }}"
  with_random_choice:
     - "go through the door"
     - "drink from the goblet"
     - "press the red button"
     - "do nothing"

```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>']
