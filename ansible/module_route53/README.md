# Ansible module: ansible.module_route53


add or delete entries in Amazons Route53 DNS service

## Description

Creates and deletes DNS records in Amazons Route53 service

## Requirements

TODO

## Arguments

``` json
{
    "alias": "{'description': ['Indicates if this is an alias record.'], 'version_added': '1.9', 'type': 'bool', 'default': False}",
    "alias_evaluate_target_health": "{'description': ['Whether or not to evaluate an alias target health. Useful for aliases to Elastic Load Balancers.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "alias_hosted_zone_id": "{'description': ['The hosted zone identifier.'], 'version_added': '1.9'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "failover": "{'description': ['Failover resource record sets only. Whether this is the primary or secondary resource record set. Allowed values are PRIMARY and SECONDARY'], 'version_added': '2.0'}",
    "health_check": "{'description': ['Health check to associate with this record'], 'version_added': '2.0'}",
    "hosted_zone_id": "{'description': ['The Hosted Zone ID of the DNS zone to modify'], 'version_added': '2.0'}",
    "identifier": "{'description': ['Have to be specified for Weighted, latency-based and failover resource record sets only. An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type.'], 'version_added': '2.0'}",
    "overwrite": "{'description': ['Whether an existing record should be overwritten on create if values do not match']}",
    "private_zone": "{'description': ['If set to C(yes), the private zone matching the requested name within the domain will be used if there are both public and private zones. The default is to use the public zone.'], 'type': 'bool', 'default': False, 'version_added': '1.9'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "record": "{'description': ['The full DNS record to create or delete'], 'required': True}",
    "region": "{'description': ['Latency-based resource record sets only Among resource record sets that have the same combination of DNS name and type, a value that determines which region this should be associated with for the latency-based routing'], 'version_added': '2.0'}",
    "retry_interval": "{'description': ['In the case that route53 is still servicing a prior request, this module will wait and try again after this many seconds. If you have many domain names, the default of 500 seconds may be too long.'], 'default': 500}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ["Specifies the state of the resource record. As of Ansible 2.4, the I(command) option has been changed to I(state) as default and the choices 'present' and 'absent' have been added, but I(command) still works as well."], 'required': True, 'aliases': ['command'], 'choices': ['present', 'absent', 'get', 'create', 'delete']}",
    "ttl": "{'description': ['The TTL to give the new record'], 'default': '3600 (one hour)'}",
    "type": "{'description': ['The type of DNS record to create'], 'required': True, 'choices': ['A', 'CNAME', 'MX', 'AAAA', 'TXT', 'PTR', 'SRV', 'SPF', 'CAA', 'NS', 'SOA']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "value": "{'description': ['The new value when creating a DNS record.  YAML lists or multiple comma-spaced values are allowed for non-alias records.', 'When deleting a record all values for the record must be specified or Route53 will not delete it.']}",
    "vpc_id": "{'description': ['When used in conjunction with private_zone: true, this will only modify records in the private hosted zone attached to this VPC.', 'This allows you to have multiple private hosted zones, all with the same name, attached to different VPCs.'], 'version_added': '2.0'}",
    "wait": "{'description': ['Wait until the changes have been replicated to all Amazon Route 53 DNS servers.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "wait_timeout": "{'description': ['How long to wait for the changes to be replicated, in seconds.'], 'default': 300, 'version_added': '2.1'}",
    "weight": "{'description': ['Weighted resource record sets only. Among resource record sets that have the same combination of DNS name and type, a value that determines what portion of traffic for the current resource record set is routed to the associated location.'], 'version_added': '2.0'}",
    "zone": "{'description': ['The DNS zone to modify'], 'required': True}",
}
```

## Examples


``` yaml

# Add new.foo.com as an A record with 3 IPs and wait until the changes have been replicated
- route53:
      state: present
      zone: foo.com
      record: new.foo.com
      type: A
      ttl: 7200
      value: 1.1.1.1,2.2.2.2,3.3.3.3
      wait: yes

# Update new.foo.com as an A record with a list of 3 IPs and wait until the changes have been replicated
- route53:
      state: present
      zone: foo.com
      record: new.foo.com
      type: A
      ttl: 7200
      value:
        - 1.1.1.1
        - 2.2.2.2
        - 3.3.3.3
      wait: yes

# Retrieve the details for new.foo.com
- route53:
      state: get
      zone: foo.com
      record: new.foo.com
      type: A
  register: rec

# Delete new.foo.com A record using the results from the get command
- route53:
      state: absent
      zone: foo.com
      record: "{{ rec.set.record }}"
      ttl: "{{ rec.set.ttl }}"
      type: "{{ rec.set.type }}"
      value: "{{ rec.set.value }}"

# Add an AAAA record.  Note that because there are colons in the value
# that the IPv6 address must be quoted. Also shows using the old form command=create.
- route53:
      command: create
      zone: foo.com
      record: localhost.foo.com
      type: AAAA
      ttl: 7200
      value: "::1"

# Add a SRV record with multiple fields for a service on port 22222
# For more information on SRV records see:
# https://en.wikipedia.org/wiki/SRV_record
- route53:
      state: present
      zone: foo.com
      record: "_example-service._tcp.foo.com"
      type: SRV
      value: "0 0 22222 host1.foo.com,0 0 22222 host2.foo.com"

# Add a TXT record. Note that TXT and SPF records must be surrounded
# by quotes when sent to Route 53:
- route53:
      state: present
      zone: foo.com
      record: localhost.foo.com
      type: TXT
      ttl: 7200
      value: '"bar"'

# Add an alias record that points to an Amazon ELB:
- route53:
      state: present
      zone: foo.com
      record: elb.foo.com
      type: A
      value: "{{ elb_dns_name }}"
      alias: True
      alias_hosted_zone_id: "{{ elb_zone_id }}"

# Retrieve the details for elb.foo.com
- route53:
      state: get
      zone: foo.com
      record: elb.foo.com
      type: A
  register: rec

# Delete an alias record using the results from the get command
- route53:
      state: absent
      zone: foo.com
      record: "{{ rec.set.record }}"
      ttl: "{{ rec.set.ttl }}"
      type: "{{ rec.set.type }}"
      value: "{{ rec.set.value }}"
      alias: True
      alias_hosted_zone_id: "{{ rec.set.alias_hosted_zone_id }}"

# Add an alias record that points to an Amazon ELB and evaluates it health:
- route53:
    state: present
    zone: foo.com
    record: elb.foo.com
    type: A
    value: "{{ elb_dns_name }}"
    alias: True
    alias_hosted_zone_id: "{{ elb_zone_id }}"
    alias_evaluate_target_health: True

# Add an AAAA record with Hosted Zone ID.
- route53:
      state: present
      zone: foo.com
      hosted_zone_id: Z2AABBCCDDEEFF
      record: localhost.foo.com
      type: AAAA
      ttl: 7200
      value: "::1"

# Use a routing policy to distribute traffic:
- route53:
      state: present
      zone: foo.com
      record: www.foo.com
      type: CNAME
      value: host1.foo.com
      ttl: 30
      # Routing policy
      identifier: "host1@www"
      weight: 100
      health_check: "d994b780-3150-49fd-9205-356abdd42e75"

# Add a CAA record (RFC 6844):
- route53:
      state: present
      zone: example.com
      record: example.com
      type: CAA
      value:
        - 0 issue "ca.example.net"
        - 0 issuewild ";"
        - 0 iodef "mailto:security@example.com"


```

## License

TODO

## Author Information
  - ['Bruce Pennypacker (@bpennypacker)', 'Mike Buzzetti <mike.buzzetti@gmail.com>']
  - ['Bruce Pennypacker (@bpennypacker)', 'Mike Buzzetti <mike.buzzetti@gmail.com>']
