# Ansible module: ansible.module_smartos_image_facts


Get SmartOS image details

## Description

Retrieve facts about all installed images on SmartOS. Facts will be inserted to the ansible_facts key.

## Requirements

TODO

## Arguments

``` json
{
    "filters": "{'description': ["Criteria for selecting image. Can be any value from image manifest and 'published_date', 'published', 'source', 'clones', and 'size'. More informaton can be found at U(https://smartos.org/man/1m/imgadm) under 'imgadm list'."]}",
}
```

## Examples


``` yaml

# Return facts about all installed images.
- smartos_image_facts:

# Return all private active Linux images.
- smartos_image_facts: filters="os=linux state=active public=false"

# Show, how many clones does every image have.
- smartos_image_facts:

- debug: msg="{{ smartos_images[item]['name'] }}-{{smartos_images[item]['version'] }}
            has {{ smartos_images[item]['clones'] }} VM(s)"
  with_items: "{{ smartos_images.keys() }}"

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
