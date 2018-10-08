# Ansible lookup: ansible.lookup_sequence


generate a list based on a number sequence

## Description

generates a sequence of items. You can specify a start value, an end value, an optional "stride" value that specifies the number of steps to increment the sequence, and an optional printf-style format string.
Arguments can be specified as key=value pair strings or as a shortcut form of the arguments string is also accepted: [start-]end[/stride][:format].
Numerical values can be specified in decimal, hexadecimal (0x3f8) or octal (0600).
Starting at version 1.9.2, negative strides are allowed.

## Requirements

TODO

## Arguments

``` json
{
    "count": "{'description': ['number of elements in the sequence, this is not to be used with end'], 'type': 'number', 'default': 0}",
    "end": "{'description': ['number at which to end the sequence, dont use this with count'], 'type': 'number', 'default': 0}",
    "format": "{'description': ['return a string with the generated number formatted in']}",
    "start": "{'description': ['number at which to start the sequence'], 'default': 0, 'type': 'number'}",
    "stride": "{'description': ['increments between sequence numbers, the default is 1 unless the end is less than the start, then it is -1.'], 'type': 'number'}",
}
```

## Examples


``` yaml

- name: create some test users
  user:
    name: "{{ item }}"
    state: present
    groups: "evens"
  with_sequence: start=0 end=32 format=testuser%02x

- name: create a series of directories with even numbers for some reason
  file:
    dest: "/var/stuff/{{ item }}"
    state: directory
  with_sequence: start=4 end=16 stride=2

- name: a simpler way to use the sequence plugin create 4 groups
  group:
    name: "group{{ item }}"
    state: present
  with_sequence: count=4

- name: the final countdown
  debug: msg={{item}} seconds to detonation
  with_sequence: end=0 start=10

```

## License

TODO

## Author Information
  - ['Jayson Vantuyl <jayson@aggressive.ly>']
