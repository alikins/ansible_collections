# Ansible lookup: ansible.lookup_dig


query DNS using the dnspython library

## Description

The dig lookup runs queries against DNS servers to retrieve DNS records for a specific name (FQDN - fully qualified domain name). It is possible to lookup any DNS record in this manner.
There is a couple of different syntaxes that can be used to specify what record should be retrieved, and for which name. It is also possible to explicitly specify the DNS server(s) to use for lookups.
In its simplest form, the dig lookup plugin can be used to retrieve an IPv4 address (DNS A record) associated with FQDN
In addition to (default) A record, it is also possible to specify a different record type that should be queried. This can be done by either passing-in additional parameter of format qtype=TYPE to the dig lookup, or by appending /TYPE to the FQDN being queried.
If multiple values are associated with the requested record, the results will be returned as a comma-separated list. In such cases you may want to pass option wantlist=True to the plugin, which will result in the record values being returned as a list over which you can iterate later on.
By default, the lookup will rely on system-wide configured DNS servers for performing the query. It is also possible to explicitly specify DNS servers to query using the @DNS_SERVER_1,DNS_SERVER_2,...,DNS_SERVER_N notation. This needs to be passed-in as an additional parameter to the lookup

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['domain(s) to query']}",
    "flat": "{'description': ['If 0 each record is returned as a dictionary, otherwise a string'], 'default': 1}",
    "qtype": "{'description': ['record type to query'], 'default': 'A', 'choices': ['A', 'ALL', 'AAAA', 'CNAME', 'DNAME', 'DLV', 'DNSKEY', 'DS', 'HINFO', 'LOC', 'MX', 'NAPTR', 'NS', 'NSEC3PARAM', 'PTR', 'RP', 'RRSIG', 'SOA', 'SPF', 'SRV', 'SSHFP', 'TLSA', 'TXT']}",
}
```

## Examples


``` yaml

- name: Simple A record (IPV4 address) lookup for example.com
  debug: msg="{{ lookup('dig', 'example.com.')}}"

- name: "The TXT record for example.org."
  debug: msg="{{ lookup('dig', 'example.org.', 'qtype=TXT') }}"

- name: "The TXT record for example.org, alternative syntax."
  debug: msg="{{ lookup('dig', 'example.org./TXT') }}"

- name: use in a loop
  debug: msg="MX record for gmail.com {{ item }}"
  with_items: "{{ lookup('dig', 'gmail.com./MX', wantlist=True) }}"

- debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '192.0.2.5/PTR') }}"
- debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '5.2.0.192.in-addr.arpa./PTR') }}"
- debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '5.2.0.192.in-addr.arpa.', 'qtype=PTR') }}"
- debug: msg="Querying 198.51.100.23 for IPv4 address for example.com. produces {{ lookup('dig', 'example.com', '@198.51.100.23') }}"

- debug: msg="XMPP service for gmail.com. is available at {{ item.target }} on port {{ item.port }}"
  with_items: "{{ lookup('dig', '_xmpp-server._tcp.gmail.com./SRV', 'flat=0', wantlist=True) }}"

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>']
