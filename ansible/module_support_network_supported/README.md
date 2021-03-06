# Ansible module: ansible.module_support_network_supported


module maintained by Ansible Network Team

## Description

These are :doc:`modules maintained by the Ansible Network Team<network_maintained>` in a relationship similar to how the Ansible Core Team maintains the Core modules.

This will pull in as requirements:
- ansible.module_netconf_get
- ansible.module_netconf_config
- ansible.module_netconf_rpc
- ansible.module_iosxr_netconf
- ansible.module_iosxr_command
- ansible.module_iosxr_banner
- ansible.module_iosxr_user
- ansible.module_iosxr_facts
- ansible.module_iosxr_system
- ansible.module_iosxr_config
- ansible.module_iosxr_logging
- ansible.module_iosxr_interface
- ansible.module_net_static_route
- ansible.module_nxos_igmp_snooping
- ansible.module_nxos_udld_interface
- ansible.module_nxos_ping
- ansible.module_nxos_vtp_version
- ansible.module_nxos_bgp_neighbor
- ansible.module_nxos_vlan
- ansible.module_nxos_static_route
- ansible.module_nxos_ntp_options
- ansible.module_nxos_snmp_location
- ansible.module_nxos_rollback
- ansible.module_nxos_vtp_domain
- ansible.module_nxos_evpn_global
- ansible.module_nxos_reboot
- ansible.module_nxos_igmp_interface
- ansible.module_nxos_ntp
- ansible.module_nxos_ntp_auth
- ansible.module_nxos_snmp_host
- ansible.module_nxos_vrf
- ansible.module_nxos_system
- ansible.module_nxos_gir
- ansible.module_nxos_snmp_contact
- ansible.module_nxos_acl_interface
- ansible.module_nxos_install_os
- ansible.module_nxos_snapshot
- ansible.module_nxos_nxapi
- ansible.module_nxos_bgp_af
- ansible.module_nxos_ospf_vrf
- ansible.module_nxos_vrf_interface
- ansible.module_nxos_portchannel
- ansible.module_nxos_l3_interface
- ansible.module_nxos_vpc
- ansible.module_nxos_linkagg
- ansible.module_nxos_user
- ansible.module_nxos_snmp_user
- ansible.module_nxos_snmp_traps
- ansible.module_nxos_vxlan_vtep
- ansible.module_nxos_ip_interface
- ansible.module_nxos_igmp
- ansible.module_nxos_file_copy
- ansible.module_nxos_interface
- ansible.module_nxos_vrrp
- ansible.module_nxos_facts
- ansible.module_nxos_pim
- ansible.module_nxos_command
- ansible.module_nxos_acl
- ansible.module_nxos_vxlan_vtep_vni
- ansible.module_nxos_smu
- ansible.module_nxos_udld
- ansible.module_nxos_pim_interface
- ansible.module_nxos_hsrp
- ansible.module_nxos_vrf_af
- ansible.module_nxos_rpm
- ansible.module_nxos_evpn_vni
- ansible.module_nxos_gir_profile_management
- ansible.module_nxos_aaa_server
- ansible.module_nxos_l2_interface
- ansible.module_nxos_config
- ansible.module_nxos_banner
- ansible.module_nxos_bgp
- ansible.module_nxos_lldp
- ansible.module_nxos_ospf
- ansible.module_nxos_aaa_server_host
- ansible.module_nxos_feature
- ansible.module_nxos_vtp_password
- ansible.module_nxos_interface_ospf
- ansible.module_nxos_bgp_neighbor_af
- ansible.module_nxos_switchport
- ansible.module_nxos_overlay_global
- ansible.module_nxos_snmp_community
- ansible.module_nxos_vpc_interface
- ansible.module_nxos_logging
- ansible.module_nxos_pim_rp_address
- ansible.module_net_user
- ansible.module_net_logging
- ansible.module_net_banner
- ansible.module_net_system
- ansible.module_openvswitch_port
- ansible.module_openvswitch_db
- ansible.module_openvswitch_bridge
- ansible.module_net_vrf
- ansible.module_net_l3_interface
- ansible.module_vyos_static_route
- ansible.module_vyos_lldp
- ansible.module_vyos_l3_interface
- ansible.module_vyos_vlan
- ansible.module_vyos_config
- ansible.module_vyos_linkagg
- ansible.module_vyos_lldp_interface
- ansible.module_vyos_banner
- ansible.module_vyos_command
- ansible.module_vyos_user
- ansible.module_vyos_interface
- ansible.module_vyos_logging
- ansible.module_vyos_system
- ansible.module_vyos_facts
- ansible.module_net_l2_interface
- ansible.module_net_vlan
- ansible.module_eos_vlan
- ansible.module_eos_eapi
- ansible.module_eos_interface
- ansible.module_eos_system
- ansible.module_eos_command
- ansible.module_eos_facts
- ansible.module_eos_static_route
- ansible.module_eos_user
- ansible.module_eos_l3_interface
- ansible.module_eos_banner
- ansible.module_eos_lldp
- ansible.module_eos_l2_interface
- ansible.module_eos_logging
- ansible.module_eos_vrf
- ansible.module_eos_config
- ansible.module_eos_linkagg
- ansible.module_cli_command
- ansible.module_cli_config
- ansible.module_net_lldp
- ansible.module_ios_user
- ansible.module_ios_system
- ansible.module_ios_vrf
- ansible.module_ios_config
- ansible.module_ios_lldp
- ansible.module_ios_vlan
- ansible.module_ios_facts
- ansible.module_ios_static_route
- ansible.module_ios_command
- ansible.module_ios_linkagg
- ansible.module_ios_l3_interface
- ansible.module_ios_interface
- ansible.module_ios_logging
- ansible.module_ios_l2_interface
- ansible.module_ios_banner
- ansible.module_net_lldp_interface
- ansible.module_net_interface
- ansible.module_net_linkagg
- ansible.module_junos_banner
- ansible.module_junos_lldp
- ansible.module_junos_netconf
- ansible.module_junos_static_route
- ansible.module_junos_lldp_interface
- ansible.module_junos_vrf
- ansible.module_junos_user
- ansible.module_junos_rpc
- ansible.module_junos_package
- ansible.module_junos_facts
- ansible.module_junos_linkagg
- ansible.module_junos_l2_interface
- ansible.module_junos_l3_interface
- ansible.module_junos_scp
- ansible.module_junos_interface
- ansible.module_junos_logging
- ansible.module_junos_command
- ansible.module_junos_system
- ansible.module_junos_config
- ansible.module_junos_vlan
- ansible.module_ftd_file_upload
- ansible.module_ftd_configuration
- ansible.module_ftd_file_download
- ansible.module_net_put
- ansible.module_net_get
- ansible.module_slxos_l3_interface

## Requirements

TODO

## Arguments

}
```

## Examples



## License

TODO

## Author Information
  - ['ansible_galaxy_meta_collection@invalid.com']
