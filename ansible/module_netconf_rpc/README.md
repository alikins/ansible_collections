# Ansible module: ansible.module_netconf_rpc


Execute operations on NETCONF enabled network devices

## Description

NETCONF is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
This module allows the user to execute NETCONF RPC requests as defined by IETF RFC standards as well as proprietary requests.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ['This argument specifies the optional request content (all RPC attributes). The I(content) value can either be provided as XML formatted string or as dictionary.']}",
    "display": "{'description': ['Encoding scheme to use when serializing output from the device. The option I(json) will serialize the output as JSON data. If the option value is I(json) it requires jxmlease to be installed on control node. The option I(pretty) is similar to received XML response but is using human readable format (spaces, new lines). The option value I(xml) is similar to received XML response but removes all XML namespaces.'], 'choices': ['json', 'pretty', 'xml']}",
    "rpc": "{'description': ['This argument specifies the request (name of the operation) to be executed on the remote NETCONF enabled device.']}",
    "xmlns": "{'description': ['NETCONF operations not defined in rfc6241 typically require the appropriate XML namespace to be set. In the case the I(request) option is not already provided in XML format, the namespace can be defined by the I(xmlns) option.']}",
}
```

## Examples


``` yaml

- name: lock candidate
  netconf_rpc:
    rpc: lock
    content:
      target:
        candidate:

- name: unlock candidate
  netconf_rpc:
    rpc: unlock
    xmlns: "urn:ietf:params:xml:ns:netconf:base:1.0"
    content: "{'target': {'candidate': None}}"

- name: discard changes
  netconf_rpc:
    rpc: discard-changes

- name: get-schema
  netconf_rpc:
    rpc: get-schema
    xmlns: urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring
    content:
      identifier: ietf-netconf
      version: "2011-06-01"

- name: copy running to startup
  netconf_rpc:
    rpc: copy-config
    content:
      source:
        running:
      target:
        startup:

- name: get schema list with JSON output
  netconf_rpc:
    rpc: get
    content: |
      <filter>
        <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
          <schemas/>
        </netconf-state>
      </filter>
    display: json

- name: get schema using XML request
  netconf_rpc:
    rpc: "get-schema"
    xmlns: "urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"
    content: |
      <identifier>ietf-netconf-monitoring</identifier>
      <version>2010-10-04</version>
    display: json

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)', 'Sven Wisotzky (@wisotzky)']
  - ['Ganesh Nalawade (@ganeshrn)', 'Sven Wisotzky (@wisotzky)']
