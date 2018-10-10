# Ansible module: ansible.module_ce_netconf


Run an arbitrary netconf command on HUAWEI CloudEngine switches

## Description

Sends an arbitrary netconf command on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "cfg_xml": "{'description': ['The config xml string.'], 'required': True}",
    "rpc": "{'description': ['The type of rpc.'], 'required': True, 'choices': ['get', 'edit-config', 'execute-action', 'execute-cli']}",
}
```

## Examples


``` yaml


- name: CloudEngine netconf test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Netconf get operation"
    ce_netconf:
      rpc: get
      cfg_xml: '<filter type="subtree">
                  <vlan xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                    <vlans>
                      <vlan>
                        <vlanId>10</vlanId>
                        <vlanif>
                          <ifName></ifName>
                          <cfgBand></cfgBand>
                          <dampTime></dampTime>
                        </vlanif>
                      </vlan>
                    </vlans>
                  </vlan>
                </filter>'
      provider: "{{ cli }}"

  - name: "Netconf edit-config operation"
    ce_netconf:
      rpc: edit-config
      cfg_xml: '<config>
                    <aaa xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                      <authenticationSchemes>
                        <authenticationScheme operation="create">
                          <authenSchemeName>default_wdz</authenSchemeName>
                          <firstAuthenMode>local</firstAuthenMode>
                          <secondAuthenMode>invalid</secondAuthenMode>
                        </authenticationScheme>
                      </authenticationSchemes>
                    </aaa>
                   </config>'
      provider: "{{ cli }}"

  - name: "Netconf execute-action operation"
    ce_netconf:
      rpc: execute-action
      cfg_xml: '<action>
                     <l2mc xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
                       <l2McResetAllVlanStatis>
                         <addrFamily>ipv4unicast</addrFamily>
                       </l2McResetAllVlanStatis>
                     </l2mc>
                   </action>'
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
