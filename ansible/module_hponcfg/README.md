# Ansible module: ansible.module_hponcfg


Configure HP iLO interface using hponcfg

## Description

This modules configures the HP iLO interface using hponcfg.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['Path to the hponcfg executable (`hponcfg` which uses $PATH).'], 'default': 'hponcfg', 'version_added': '2.4'}",
    "minfw": "{'description': ['The minimum firmware level needed.'], 'required': False}",
    "path": "{'description': ['The XML file as accepted by hponcfg.'], 'required': True, 'aliases': ['src']}",
    "verbose": "{'description': ['Run hponcfg in verbose mode (-v).'], 'default': False, 'type': 'bool', 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Example hponcfg configuration XML
  copy:
    content: |
      <ribcl VERSION="2.0">
        <login USER_LOGIN="user" PASSWORD="password">
          <rib_info MODE="WRITE">
            <mod_global_settings>
              <session_timeout value="0"/>
              <ssh_status value="Y"/>
              <ssh_port value="22"/>
              <serial_cli_status value="3"/>
              <serial_cli_speed value="5"/>
            </mod_global_settings>
          </rib_info>
        </login>
      </ribcl>
    dest: /tmp/enable-ssh.xml

- name: Configure HP iLO using enable-ssh.xml
  hponcfg:
    src: /tmp/enable-ssh.xml

- name: Configure HP iLO on VMware ESXi hypervisor
  hponcfg:
    src: /tmp/enable-ssh.xml
    executable: /opt/hp/tools/hponcfg

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
