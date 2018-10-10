# Ansible module: ansible.module_one_image


Manages OpenNebula images

## Description

Manages OpenNebula images

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['Password of the user to login into OpenNebula RPC server. If not set', 'then the value of the C(ONE_PASSWORD) environment variable is used.']}",
    "api_url": "{'description': ['URL of the OpenNebula RPC server.', 'It is recommended to use HTTPS so that the username/password are not', 'transferred over the network unencrypted.', 'If not set then the value of the C(ONE_URL) environment variable is used.']}",
    "api_username": "{'description': ['Name of the user to login into the OpenNebula RPC server. If not set', 'then the value of the C(ONE_USERNAME) environment variable is used.']}",
    "enabled": "{'description': ['Whether the image should be enabled or disabled.'], 'type': 'bool'}",
    "id": "{'description': ['A C(id) of the image you would like to manage.']}",
    "name": "{'description': ['A C(name) of the image you would like to manage.']}",
    "new_name": "{'description': ['A name that will be assigned to the existing or new image.', "In the case of cloning, by default C(new_name) will take the name of the origin image with the prefix 'Copy of'."]}",
    "state": "{'description': ['C(present) - state that is used to manage the image', 'C(absent) - delete the image', 'C(cloned) - clone the image', 'C(renamed) - rename the image to the C(new_name)'], 'choices': ['present', 'absent', 'cloned', 'renamed'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Fetch the IMAGE by id
- one_image:
    id: 45
  register: result

# Print the IMAGE properties
- debug:
    msg: result

# Rename existing IMAGE
- one_image:
    id: 34
    state: renamed
    new_name: bar-image

# Disable the IMAGE by id
- one_image:
    id: 37
    enabled: no

# Enable the IMAGE by name
- one_image:
    name: bar-image
    enabled: yes

# Clone the IMAGE by name
- one_image:
    name: bar-image
    state: cloned
    new_name: bar-image-clone
  register: result

# Delete the IMAGE by id
- one_image:
    id: '{{ result.id }}'
    state: absent

```

## License

TODO

## Author Information
  - ['Milan Ilic (@ilicmilan)']
