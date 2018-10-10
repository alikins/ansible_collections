# Ansible module: ansible.module_one_image_facts


Gather facts about OpenNebula images

## Description

Gather facts about OpenNebula images

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['Password of the user to login into OpenNebula RPC server. If not set', 'then the value of the C(ONE_PASSWORD) environment variable is used.']}",
    "api_url": "{'description': ['URL of the OpenNebula RPC server.', 'It is recommended to use HTTPS so that the username/password are not', 'transferred over the network unencrypted.', 'If not set then the value of the C(ONE_URL) environment variable is used.']}",
    "api_username": "{'description': ['Name of the user to login into the OpenNebula RPC server. If not set', 'then the value of the C(ONE_USERNAME) environment variable is used.']}",
    "ids": "{'description': ['A list of images ids whose facts you want to gather.'], 'aliases': ['id']}",
    "name": "{'description': ['A C(name) of the image whose facts will be gathered.', "If the C(name) begins with '~' the C(name) will be used as regex pattern", 'which restricts the list of images (whose facts will be returned) whose names match specified regex.', "Also, if the C(name) begins with '~*' case-insensitive matching will be performed.", 'See examples for more details.']}",
}
```

## Examples


``` yaml

# Gather facts about all images
- one_image_facts:
  register: result

# Print all images facts
- debug:
    msg: result

# Gather facts about an image using ID
- one_image_facts:
    ids:
      - 123

# Gather facts about an image using the name
- one_image_facts:
    name: 'foo-image'
  register: foo_image

# Gather facts about all IMAGEs whose name matches regex 'app-image-.*'
- one_image_facts:
    name: '~app-image-.*'
  register: app_images

# Gather facts about all IMAGEs whose name matches regex 'foo-image-.*' ignoring cases
- one_image_facts:
    name: '~*foo-image-.*'
  register: foo_images

```

## License

TODO

## Author Information
  - ['Milan Ilic (@ilicmilan)']
