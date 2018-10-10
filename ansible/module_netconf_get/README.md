# Ansible module: ansible.module_netconf_get


Fetch configuration/state data from NETCONF enabled network devices

## Description

NETCONF is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
This module allows the user to fetch configuration and state data from NETCONF enabled network devices.

## Requirements

TODO

## Arguments

``` json
{
    "display": "{'description': ['Encoding scheme to use when serializing output from the device. The option I(json) will serialize the output as JSON data. If the option value is I(json) it requires jxmlease to be installed on control node. The option I(pretty) is similar to received XML response but is using human readable format (spaces, new lines). The option value I(xml) is similar to received XML response but removes all XML namespaces.'], 'choices': ['json', 'pretty', 'xml']}",
    "filter": "{'description': ['This argument specifies the XML string which acts as a filter to restrict the portions of the data to be are retrieved from the remote device. If this option is not specified entire configuration or state data is returned in result depending on the value of C(source) option. The C(filter) value can be either XML string or XPath, if the filter is in XPath format the NETCONF server running on remote host should support xpath capability else it will result in an error.']}",
    "lock": "{'description': ['Instructs the module to explicitly lock the datastore specified as C(source). If no I(source) is defined, the I(running) datastore will be locked. By setting the option value I(always) is will explicitly lock the datastore mentioned in C(source) option. By setting the option value I(never) it will not lock the C(source) datastore. The value I(if-supported) allows better interworking with NETCONF servers, which do not support the (un)lock operation for all supported datastores.'], 'default': 'never', 'choices': ['never', 'always', 'if-supported']}",
    "source": "{'description': ['This argument specifies the datastore from which configuration data should be fetched. Valid values are I(running), I(candidate) and I(startup). If the C(source) value is not set both configuration and state information are returned in response from running datastore.'], 'choices': ['running', 'candidate', 'startup']}",
}
```

## Examples


``` yaml

- name: Get running configuration and state data
  netconf_get:

- name: Get configuration and state data from startup datastore
  netconf_get:
    source: startup

- name: Get system configuration data from running datastore state (junos)
  netconf_get:
    source: running
    filter: <configuration><system></system></configuration>

- name: Get configuration and state data in JSON format
  netconf_get:
    display: json

- name: get schema list using subtree w/ namespaces
  netconf_get:
    display: json
    filter: <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"><schemas><schema/></schemas></netconf-state>
    lock: never

- name: get schema list using xpath
  netconf_get:
    display: xml
    filter: /netconf-state/schemas/schema

- name: get interface confiugration with filter (iosxr)
  netconf_get:
    display: pretty
    filter: <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"></interface-configurations>
    lock: if-supported

- name: Get system configuration data from running datastore state (junos)
  netconf_get:
    source: running
    filter: <configuration><system></system></configuration>
    lock: if-supported

- name: Get complete configuration data from running datastore (SROS)
  netconf_get:
    source: running
    filter: <configure xmlns="urn:nokia.com:sros:ns:yang:sr:conf"/>

- name: Get complete state data (SROS)
  netconf_get:
    filter: <state xmlns="urn:nokia.com:sros:ns:yang:sr:state"/>

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)', 'Sven Wisotzky (@wisotzky)']
  - ['Ganesh Nalawade (@ganeshrn)', 'Sven Wisotzky (@wisotzky)']
