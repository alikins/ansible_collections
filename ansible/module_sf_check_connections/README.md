# Ansible module: ansible.module_sf_check_connections


Check connectivity to MVIP and SVIP

## Description

Used to test the management connection to the cluster.
The test pings the MVIP and SVIP, and executes a simple API method to verify connectivity.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "mvip": "{'description': ['Optionally, use to test connection of a different MVIP.', 'This is not needed to test the connection to the target cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "skip": "{'description': ['Skip checking connection to SVIP or MVIP.'], 'choices': ['svip', 'mvip']}",
    "svip": "{'description': ['Optionally, use to test connection of a different SVIP.', 'This is not needed to test the connection to the target cluster.']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Check connections to MVIP and SVIP
     sf_check_connections:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
