# Ansible module: ansible.module_netapp_e_flashcache


NetApp E-Series manage SSD caches

## Description

Create or remove SSD caches on a NetApp E-Series storage array.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "cache_size_min": "{'description': ['The minimum size (in size_units) of the ssd cache. The cache will be expanded if this exceeds the current size of the cache.']}",
    "disk_count": "{'description': ['The minimum number of disks to use for building the cache. The cache will be expanded if this number exceeds the number of disks already in place']}",
    "io_type": "{'description': ['The type of workload to optimize the cache for.'], 'choices': ['filesystem', 'database', 'media'], 'default': 'filesystem'}",
    "name": "{'required': True, 'description': ['The name of the SSD cache to manage']}",
    "size_unit": "{'description': ['The unit to be applied to size arguments'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage (as configured on the web services proxy).']}",
    "state": "{'required': True, 'description': ['Whether the specified SSD cache should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

    - name: Flash Cache
      netapp_e_flashcache:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
        name: SSDCacheBuiltByAnsible

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
