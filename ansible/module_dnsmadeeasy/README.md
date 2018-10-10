# Ansible module: ansible.module_dnsmadeeasy


Interface with dnsmadeeasy.com (a DNS hosting service)

## Description

Manages DNS records via the v2 REST API of the DNS Made Easy service.  It handles records only; there is no manipulation of domains or monitor/account support yet. See: U(https://www.dnsmadeeasy.com/integration/restapi/)


## Requirements

TODO

## Arguments

``` json
{
    "account_key": "{'description': ['Account API Key.'], 'required': True}",
    "account_secret": "{'description': ['Account Secret Key.'], 'required': True}",
    "autoFailover": "{'description': ['If true, fallback to the primary IP address is manual after a failover.', 'If false, fallback to the primary IP address is automatic after a failover.'], 'type': 'bool', 'default': False, 'version_added': 2.4}",
    "contactList": "{'description': ['Name or id of the contact list that the monitor will notify.', "The default C('') means the Account Owner."], 'required': True, 'default': '', 'version_added': 2.4}",
    "domain": "{'description': ['Domain to work with. Can be the domain name (e.g. "mydomain.com") or the numeric ID of the domain in DNS Made Easy (e.g. "839989") for faster resolution'], 'required': True}",
    "failover": "{'description': ['If C(yes), add or change the failover.  This is applicable only for A records.'], 'type': 'bool', 'default': False, 'version_added': 2.4}",
    "httpFile": "{'description': ['The file at the Fqdn that the monitor queries for HTTP or HTTPS.'], 'version_added': 2.4}",
    "httpFqdn": "{'description': ['The fully qualified domain name used by the monitor.'], 'version_added': 2.4}",
    "httpQueryString": "{'description': ['The string in the httpFile that the monitor queries for HTTP or HTTPS.'], 'version_added': 2.4}",
    "ip1": "{'description': ['Primary IP address for the failover.', 'Required if adding or changing the monitor or failover.'], 'version_added': 2.4}",
    "ip2": "{'description': ['Secondary IP address for the failover.', 'Required if adding or changing the failover.'], 'version_added': 2.4}",
    "ip3": "{'description': ['Tertiary IP address for the failover.'], 'version_added': 2.4}",
    "ip4": "{'description': ['Quaternary IP address for the failover.'], 'version_added': 2.4}",
    "ip5": "{'description': ['Quinary IP address for the failover.'], 'version_added': 2.4}",
    "maxEmails": "{'description': ['Number of emails sent to the contact list by the monitor.'], 'required': True, 'default': 1, 'version_added': 2.4}",
    "monitor": "{'description': ['If C(yes), add or change the monitor.  This is applicable only for A records.'], 'type': 'bool', 'default': False, 'version_added': 2.4}",
    "port": "{'description': ['Port used by the monitor.'], 'required': True, 'default': 80, 'version_added': 2.4}",
    "protocol": "{'description': ['Protocol used by the monitor.'], 'required': True, 'default': 'HTTP', 'choices': ['TCP', 'UDP', 'HTTP', 'DNS', 'SMTP', 'HTTPS'], 'version_added': 2.4}",
    "record_name": "{'description': ['Record name to get/create/delete/update. If record_name is not specified; all records for the domain will be returned in "result" regardless of the state argument.']}",
    "record_ttl": "{'description': ['record\'s "Time to live".  Number of seconds the record remains cached in DNS servers.'], 'default': 1800}",
    "record_type": "{'description': ['Record type.'], 'choices': ['A', 'AAAA', 'CNAME', 'ANAME', 'HTTPRED', 'MX', 'NS', 'PTR', 'SRV', 'TXT']}",
    "record_value": "{'description': ['Record value. HTTPRED: <redirection URL>, MX: <priority> <target name>, NS: <name server>, PTR: <target name>, SRV: <priority> <weight> <port> <target name>, TXT: <text value>"\n', "If record_value is not specified; no changes will be made and the record will be returned in 'result' (in other words, this module can be used to fetch a record's current id, type, and ttl)\n"]}",
    "sandbox": "{'description': ['Decides if the sandbox API should be used. Otherwise (default) the production API of DNS Made Easy is used.'], 'type': 'bool', 'default': False, 'version_added': 2.7}",
    "sensitivity": "{'description': ['Number of checks the monitor performs before a failover occurs where Low = 8, Medium = 5,and High = 3.'], 'required': True, 'default': 'Medium', 'choices': ['Low', 'Medium', 'High'], 'version_added': 2.4}",
    "state": "{'description': ['whether the record should exist or not'], 'required': True, 'choices': ['present', 'absent']}",
    "systemDescription": "{'description': ['Description used by the monitor.'], 'required': True, 'default': '', 'version_added': 2.4}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

# fetch my.com domain records
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
  register: response

# create / ensure the presence of a record
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1

# update the previously created record
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_value: 192.0.2.23

# fetch a specific record
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
  register: response

# delete a record / ensure it is absent
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    record_type: A
    state: absent
    record_name: test

# Add a failover
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: True
    ip1: 127.0.0.2
    ip2: 127.0.0.3

- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: True
    ip1: 127.0.0.2
    ip2: 127.0.0.3
    ip3: 127.0.0.4
    ip4: 127.0.0.5
    ip5: 127.0.0.6

# Add a monitor
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: yes
    ip1: 127.0.0.2
    protocol: HTTP  # default
    port: 80  # default
    maxEmails: 1
    systemDescription: Monitor Test A record
    contactList: my contact list

# Add a monitor with http options
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: yes
    ip1: 127.0.0.2
    protocol: HTTP  # default
    port: 80  # default
    maxEmails: 1
    systemDescription: Monitor Test A record
    contactList: 1174  # contact list id
    httpFqdn: http://my.com
    httpFile: example
    httpQueryString: some string

# Add a monitor and a failover
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: True
    ip1: 127.0.0.2
    ip2: 127.0.0.3
    monitor: yes
    protocol: HTTPS
    port: 443
    maxEmails: 1
    systemDescription: monitoring my.com status
    contactList: emergencycontacts

# Remove a failover
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: no

# Remove a monitor
- dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: no

```

## License

TODO

## Author Information
  - ['Brice Burgess (@briceburg)']
