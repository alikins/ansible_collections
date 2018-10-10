# Ansible module: ansible.module_proxmox


management of instances in Proxmox VE cluster

## Description

allows you to create/delete/stop instances in Proxmox VE cluster
Starting in Ansible 2.1, it automatically detects containerization type (lxc for PVE 4, openvz for older)

## Requirements

TODO

## Arguments

``` json
{
    "api_host": "{'description': ['the host of the Proxmox VE cluster'], 'required': True}",
    "api_password": "{'description': ['the password to authenticate with', 'you can use PROXMOX_PASSWORD environment variable']}",
    "api_user": "{'description': ['the user to authenticate with'], 'required': True}",
    "cores": "{'description': ['Specify number of cores per socket.'], 'default': 1, 'version_added': 2.4}",
    "cpus": "{'description': ['numbers of allocated cpus for instance'], 'default': 1}",
    "cpuunits": "{'description': ['CPU weight for a VM'], 'default': 1000}",
    "disk": "{'description': ['hard disk size in GB for instance'], 'default': 3}",
    "force": "{'description': ['forcing operations', 'can be used only with states C(present), C(stopped), C(restarted)', 'with C(state=present) force option allow to overwrite existing container', 'with states C(stopped) , C(restarted) allow to force stop instance'], 'type': 'bool', 'default': False}",
    "hostname": "{'description': ['the instance hostname', 'required only for C(state=present)', 'must be unique if vmid is not passed']}",
    "ip_address": "{'description': ['specifies the address the container will be assigned']}",
    "memory": "{'description': ['memory size in MB for instance'], 'default': 512}",
    "mounts": "{'description': ['specifies additional mounts (separate disks) for the container. As a hash/dictionary defining mount points'], 'version_added': '2.2'}",
    "nameserver": "{'description': ['sets DNS server IP address for a container']}",
    "netif": "{'description': ['specifies network interfaces for the container. As a hash/dictionary defining interfaces.']}",
    "node": "{'description': ['Proxmox VE node, when new VM will be created', 'required only for C(state=present)', 'for another states will be autodiscovered']}",
    "onboot": "{'description': ['specifies whether a VM will be started during system bootup'], 'type': 'bool', 'default': False}",
    "ostemplate": "{'description': ['the template for VM creating', 'required only for C(state=present)']}",
    "password": "{'description': ['the instance root password', 'required only for C(state=present)']}",
    "pool": "{'description': ['Proxmox VE resource pool'], 'version_added': '2.3'}",
    "pubkey": "{'description': ['Public key to add to /root/.ssh/authorized_keys. This was added on Proxmox 4.2, it is ignored for earlier versions'], 'version_added': '2.3'}",
    "searchdomain": "{'description': ['sets DNS search domain for a container']}",
    "state": "{'description': ['Indicate desired state of the instance'], 'choices': ['present', 'started', 'absent', 'stopped', 'restarted'], 'default': 'present'}",
    "storage": "{'description': ['target storage'], 'default': 'local'}",
    "swap": "{'description': ['swap memory size in MB for instance'], 'default': 0}",
    "timeout": "{'description': ['timeout for operations'], 'default': 30}",
    "unprivileged": "{'version_added': '2.3', 'description': ['Indicate if the container should be unprivileged'], 'type': 'bool', 'default': False}",
    "validate_certs": "{'description': ['enable / disable https certificate verification'], 'type': 'bool', 'default': False}",
    "vmid": "{'description': ['the instance id', 'if not set, the next available VM ID will be fetched from ProxmoxAPI.', 'if not set, will be fetched from PromoxAPI based on the hostname']}",
}
```

## Examples


``` yaml

# Create new container with minimal options
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

# Create new container automatically selecting the next available vmid.
- proxmox:
    node: 'uk-mc02'
    api_user: 'root@pam'
    api_password: '1q2w3e'
    api_host: 'node1'
    password: '123456'
    hostname: 'example.org'
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

# Create new container with minimal options with force(it will rewrite existing container)
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    force: yes

# Create new container with minimal options use environment PROXMOX_PASSWORD variable(you should export it before)
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

# Create new container with minimal options defining network interface with dhcp
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    netif: '{"net0":"name=eth0,ip=dhcp,ip6=dhcp,bridge=vmbr0"}'

# Create new container with minimal options defining network interface with static ip
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    netif: '{"net0":"name=eth0,gw=192.168.0.1,ip=192.168.0.2/24,bridge=vmbr0"}'

# Create new container with minimal options defining a mount with 8GB
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    mounts: '{"mp0":"local:8,mp=/mnt/test/"}'

# Create new container with minimal options defining a cpu core limit
- proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    cores: 2

# Start container
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: started

# Start container with mount. You should enter a 90-second timeout because servers with additional disks take longer to boot.
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: started
    timeout: 90

# Stop container
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: stopped

# Stop container with force
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    force: yes
    state: stopped

# Restart container(stopped or mounted container you can't restart)
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: restarted

# Remove container
- proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: absent

```

## License

TODO

## Author Information
  - ['Sergei Antipov (@UnderGreen)']
