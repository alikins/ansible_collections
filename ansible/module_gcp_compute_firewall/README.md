# Ansible module: ansible.module_gcp_compute_firewall


Creates a GCP Firewall

## Description

Each network has its own firewall controlling access to and from the instances.
All traffic to instances, even from other instances, is blocked by the firewall unless firewall rules are created to allow it.
The default network has automatically created firewall rules that are shown in default firewall rules. No manually created network has automatically created firewall rules except for a default "allow" rule for outgoing traffic and a default "deny" for incoming traffic. For all networks except the default network, you must create any firewall rules you need.

## Requirements

TODO

## Arguments

``` json
{
    "allowed": "{'description': ['The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection.'], 'required': False, 'suboptions': {'ip_protocol': {'description': ['The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol number.'], 'required': True}, 'ports': {'description': ['An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.', 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'], 'required': False}}}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': False}",
    "network": "{'description': ['URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default If you choose to specify this property, you can specify the network as a full or partial URL. For example, the following are all valid URLs: U(https://www.googleapis.com/compute/v1/projects/myproject/global/) networks/my-network projects/myproject/global/networks/my-network global/networks/default .'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "source_ranges": "{'description': ['If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. Only IPv4 is supported.'], 'required': False}",
    "source_tags": "{'description': ["If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply."], 'required': False}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "target_tags": "{'description': ['A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[].', 'If no targetTags are specified, the firewall rule applies to all instances on the specified network.'], 'required': False}",
}
```

## Examples


``` yaml

- name: create a firewall
  gcp_compute_firewall:
      name: "test_object"
      allowed:
      - ip_protocol: tcp
        ports:
        - '22'
      target_tags:
      - test-ssh-server
      - staging-ssh-server
      source_tags:
      - test-ssh-clients
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
