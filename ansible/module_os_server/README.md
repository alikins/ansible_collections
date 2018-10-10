# Ansible module: ansible.module_os_server


Create/Delete Compute Instances from OpenStack

## Description

Create or Remove compute instances from OpenStack.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "auto_ip": "{'description': ['Ensure instance has public ip however the cloud wants to do that'], 'type': 'bool', 'default': True, 'aliases': ['auto_floating_ip', 'public_ip']}",
    "availability_zone": "{'description': ['Availability zone in which to create the server.']}",
    "boot_from_volume": "{'description': ['Should the instance boot from a persistent volume created based on the image given. Mututally exclusive with boot_volume.'], 'type': 'bool', 'default': False}",
    "boot_volume": "{'description': ['Volume name or id to use as the volume to boot from. Implies boot_from_volume. Mutually exclusive with image and boot_from_volume.'], 'aliases': ['root_volume']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "config_drive": "{'description': ['Whether to boot the server with config drive enabled'], 'type': 'bool', 'default': False}",
    "delete_fip": "{'description': ['When I(state) is absent and this option is true, any floating IP associated with the instance will be deleted along with the instance.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "flavor": "{'description': ['The name or id of the flavor in which the new instance has to be created. Mutually exclusive with flavor_ram'], 'default': 1}",
    "flavor_include": "{'description': ['Text to use to filter flavor names, for the case, such as Rackspace, where there are multiple flavors that have the same ram count. flavor_include is a positive match filter - it must exist in the flavor name.']}",
    "flavor_ram": "{'description': ['The minimum amount of ram in MB that the flavor in which the new instance has to be created must have. Mutually exclusive with flavor.'], 'default': 1}",
    "floating_ip_pools": "{'description': ['Name of floating IP pool from which to choose a floating IP']}",
    "floating_ips": "{'description': ['list of valid floating IPs that pre-exist to assign to this node']}",
    "image": "{'description': ['The name or id of the base image to boot.'], 'required': True}",
    "image_exclude": "{'description': ['Text to use to filter image names, for the case, such as HP, where there are multiple image names matching the common identifying portions. image_exclude is a negative match filter - it is text that may not exist in the image name. Defaults to "(deprecated)"']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "key_name": "{'description': ['The key pair name to be used when creating a instance']}",
    "meta": "{'description': ['A list of key value pairs that should be provided as a metadata to the new instance or a string containing a list of key-value pairs. Eg:  meta: "key1=value1,key2=value2"']}",
    "name": "{'description': ['Name that has to be given to the instance. It is also possible to specify the ID of the instance instead of its name if I(state) is I(absent).'], 'required': True}",
    "network": "{'description': ['Name or ID of a network to attach this instance to. A simpler version of the nics parameter, only one of network or nics should be supplied.']}",
    "nics": "{'description': ["A list of networks to which the instance's interface should be attached. Networks may be referenced by net-id/net-name/port-id or port-name.", 'Also this accepts a string containing a list of (net/port)-(id/name) Eg: nics: "net-id=uuid-1,port-name=myport" Only one of network or nics should be supplied.']}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "reuse_ips": "{'description': ['When I(auto_ip) is true and this option is true, the I(auto_ip) code will attempt to re-use unassigned floating ips in the project before creating a new one. It is important to note that it is impossible to safely do this concurrently, so if your use case involves concurrent server creation, it is highly recommended to set this to false and to delete the floating ip associated with a server when the server is deleted using I(delete_fip).'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "scheduler_hints": "{'description': ['Arbitrary key/value pairs to the scheduler for custom use'], 'version_added': '2.1'}",
    "security_groups": "{'description': ['Names of the security groups to which the instance should be added. This may be a YAML list or a comma separated string.']}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "terminate_volume": "{'description': ['If C(yes), delete volume when deleting instance (if booted from volume)'], 'type': 'bool', 'default': False}",
    "timeout": "{'description': ['The amount of time the module should wait for the instance to get into active state.'], 'required': False, 'default': 180}",
    "userdata": "{'description': ['Opaque blob of data which is made available to the instance']}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "volume_size": "{'description': ['The size of the volume to create in GB if booting from volume based on an image.']}",
    "volumes": "{'description': ['A list of preexisting volumes names or ids to attach to the instance'], 'default': []}",
    "wait": "{'description': ['If the module should wait for the instance to be created.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

- name: Create a new instance and attaches to a network and passes metadata to the instance
  os_server:
       state: present
       auth:
         auth_url: https://identity.example.com
         username: admin
         password: admin
         project_name: admin
       name: vm1
       image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
       key_name: ansible_key
       timeout: 200
       flavor: 4
       nics:
         - net-id: 34605f38-e52a-25d2-b6ec-754a13ffb723
         - net-name: another_network
       meta:
         hostname: test1
         group: uge_master

# Create a new instance in HP Cloud AE1 region availability zone az2 and
# automatically assigns a floating IP
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        state: present
        auth:
          auth_url: https://identity.example.com
          username: username
          password: Equality7-2521
          project_name: username-project1
        name: vm1
        region_name: region-b.geo-1
        availability_zone: az2
        image: 9302692b-b787-4b52-a3a6-daebb79cb498
        key_name: test
        timeout: 200
        flavor: 101
        security_groups: default
        auto_ip: yes

# Create a new instance in named cloud mordred availability zone az2
# and assigns a pre-known floating IP
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        state: present
        cloud: mordred
        name: vm1
        availability_zone: az2
        image: 9302692b-b787-4b52-a3a6-daebb79cb498
        key_name: test
        timeout: 200
        flavor: 101
        floating_ips:
          - 12.34.56.79

# Create a new instance with 4G of RAM on Ubuntu Trusty, ignoring
# deprecated images
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        state: present
        cloud: mordred
        region_name: region-b.geo-1
        image: Ubuntu Server 14.04
        image_exclude: deprecated
        flavor_ram: 4096

# Create a new instance with 4G of RAM on Ubuntu Trusty on a Performance node
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        cloud: rax-dfw
        state: present
        image: Ubuntu 14.04 LTS (Trusty Tahr) (PVHVM)
        flavor_ram: 4096
        flavor_include: Performance

# Creates a new instance and attaches to multiple network
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance with a string
      os_server:
        auth:
           auth_url: https://identity.example.com
           username: admin
           password: admin
           project_name: admin
        name: vm1
        image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
        key_name: ansible_key
        timeout: 200
        flavor: 4
        nics: "net-id=4cb08b20-62fe-11e5-9d70-feff819cdc9f,net-id=542f0430-62fe-11e5-9d70-feff819cdc9f..."

- name: Creates a new instance and attaches to a network and passes metadata to the instance
  os_server:
       state: present
       auth:
         auth_url: https://identity.example.com
         username: admin
         password: admin
         project_name: admin
       name: vm1
       image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
       key_name: ansible_key
       timeout: 200
       flavor: 4
       nics:
         - net-id: 34605f38-e52a-25d2-b6ec-754a13ffb723
         - net-name: another_network
       meta: "hostname=test1,group=uge_master"

- name:  Creates a new instance and attaches to a specific network
  os_server:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: vm1
    image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
    key_name: ansible_key
    timeout: 200
    flavor: 4
    network: another_network

# Create a new instance with 4G of RAM on a 75G Ubuntu Trusty volume
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        state: present
        cloud: mordred
        region_name: ams01
        image: Ubuntu Server 14.04
        flavor_ram: 4096
        boot_from_volume: True
        volume_size: 75

# Creates a new instance with 2 volumes attached
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        state: present
        cloud: mordred
        region_name: ams01
        image: Ubuntu Server 14.04
        flavor_ram: 4096
        volumes:
        - photos
        - music

# Creates a new instance with provisioning userdata using Cloud-Init
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        state: present
        image: "Ubuntu Server 14.04"
        flavor: "P-1"
        network: "Production"
        userdata: |
          #cloud-config
          chpasswd:
            list: |
              ubuntu:{{ default_password }}
            expire: False
          packages:
            - ansible
          package_upgrade: true

# Creates a new instance with provisioning userdata using Bash Scripts
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      os_server:
        name: vm1
        state: present
        image: "Ubuntu Server 14.04"
        flavor: "P-1"
        network: "Production"
        userdata: |
          {%- raw -%}#!/bin/bash
          echo "  up ip route add 10.0.0.0/8 via {% endraw -%}{{ intra_router }}{%- raw -%}" >> /etc/network/interfaces.d/eth0.conf
          echo "  down ip route del 10.0.0.0/8" >> /etc/network/interfaces.d/eth0.conf
          ifdown eth0 && ifup eth0
          {% endraw %}

# Deletes an instance via its ID
- name: remove an instance
  hosts: localhost
  tasks:
    - name: remove an instance
      os_server:
        name: abcdef01-2345-6789-0abc-def0123456789
        state: absent


```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
