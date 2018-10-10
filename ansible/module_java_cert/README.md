# Ansible module: ansible.module_java_cert


Uses keytool to import/remove key from java keystore(cacerts)

## Description

This is a wrapper module around keytool, which can be used to import/remove certificates from a given java keystore.

## Requirements

TODO

## Arguments

``` json
{
    "cert_alias": "{'description': ['Imported certificate alias. The alias is used when checking for the presence of a certificate in the keystore.']}",
    "cert_path": "{'description': ['Local path to load certificate from. One of cert_url or cert_path is required to load certificate.']}",
    "cert_port": "{'description': ['Port to connect to URL. This will be used to create server URL:PORT'], 'default': 443}",
    "cert_url": "{'description': ['Basic URL to fetch SSL certificate from. One of cert_url or cert_path is required to load certificate.']}",
    "executable": "{'description': ['Path to keytool binary if not used we search in PATH for it.'], 'default': 'keytool'}",
    "keystore_create": "{'description': ["Create keystore if it doesn't exist"]}",
    "keystore_pass": "{'description': ['Keystore password.'], 'required': True}",
    "keystore_path": "{'description': ['Path to keystore.']}",
    "pkcs12_alias": "{'description': ['Alias in the PKCS12 keystore.'], 'default': 1, 'version_added': '2.4'}",
    "pkcs12_password": "{'description': ['Password for importing from PKCS12 keystore.'], 'default': '', 'version_added': '2.4'}",
    "pkcs12_path": "{'description': ['Local path to load PKCS12 keystore from.'], 'version_added': '2.4'}",
    "state": "{'description': ['Defines action which can be either certificate import or removal.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Import SSL certificate from google.com to a given cacerts keystore
  java_cert:
    cert_url: google.com
    cert_port: 443
    keystore_path: /usr/lib/jvm/jre7/lib/security/cacerts
    keystore_pass: changeit
    state: present

- name: Remove certificate with given alias from a keystore
  java_cert:
    cert_url: google.com
    keystore_path: /usr/lib/jvm/jre7/lib/security/cacerts
    keystore_pass: changeit
    executable: /usr/lib/jvm/jre7/bin/keytool
    state: absent

- name: Import SSL certificate from google.com to a keystore, create it if it doesn't exist
  java_cert:
    cert_url: google.com
    keystore_path: /tmp/cacerts
    keystore_pass: changeit
    keystore_create: yes
    state: present

- name: Import a pkcs12 keystore with a specified alias, create it if it doesn't exist
  java_cert:
    pkcs12_path: "/tmp/importkeystore.p12"
    cert_alias: default
    keystore_path: /opt/wildfly/standalone/configuration/defaultkeystore.jks
    keystore_pass: changeit
    keystore_create: yes
    state: present

```

## License

TODO

## Author Information
  - ['Adam Hamsik (@haad)']
