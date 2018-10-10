# Ansible module: ansible.module_manageiq_provider


Management of provider in ManageIQ

## Description

The manageiq_provider module supports adding, updating, and deleting provider in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "alerts": "{'description': ['Alerts endpoint connection information.'], 'suboptions': {'hostname': {'description': "The provider's api hostname.", 'required': True}, 'port': {'description': "The provider's api port."}, 'userid': {'description': "Provider's api endpoint authentication userid. defaults to None."}, 'password': {'description': "Provider's api endpoint authentication password. defaults to None."}, 'auth_key': {'description': "Provider's api endpoint authentication bearer token. defaults to None."}, 'verify_ssl': {'description': 'Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.', 'default': True}, 'security_protocol': {'choices': ['ssl-with-validation', 'ssl-with-validation-custom-ca', 'ssl-without-validation'], 'description': 'How SSL certificates should be used for HTTPS requests. defaults to None.'}, 'certificate_authority': {'description': 'The CA bundle string with custom certificates. defaults to None.'}}}",
    "api_version": "{'description': ['The OpenStack Keystone API version. defaults to None.'], 'choices': ['v2', 'v3'], 'version_added': '2.5'}",
    "azure_tenant_id": "{'description': ['Tenant ID. defaults to None.'], 'version_added': '2.5', 'aliases': ['keystone_v3_domain_id']}",
    "host_default_vnc_port_end": "{'description': ['The last port in the host VNC range. defaults to None.'], 'version_added': '2.5'}",
    "host_default_vnc_port_start": "{'description': ['The first port in the host VNC range. defaults to None.'], 'version_added': '2.5'}",
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "metrics": "{'description': ['Metrics endpoint connection information.'], 'suboptions': {'hostname': {'description': "The provider's api hostname.", 'required': True}, 'port': {'description': "The provider's api port."}, 'userid': {'description': "Provider's api endpoint authentication userid. defaults to None."}, 'password': {'description': "Provider's api endpoint authentication password. defaults to None."}, 'auth_key': {'description': "Provider's api endpoint authentication bearer token. defaults to None."}, 'verify_ssl': {'description': 'Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.', 'type': 'bool', 'default': 'yes'}, 'security_protocol': {'choices': ['ssl-with-validation', 'ssl-with-validation-custom-ca', 'ssl-without-validation', 'non-ssl'], 'description': 'How SSL certificates should be used for HTTPS requests. defaults to None.'}, 'certificate_authority': {'description': 'The CA bundle string with custom certificates. defaults to None.'}, 'path': {'description': 'Database name for oVirt metrics. Defaults to ovirt_engine_history.', 'default': 'ovirt_engine_history'}}}",
    "name": "{'description': ["The provider's name."], 'required': True}",
    "project": "{'description': ['Google Compute Engine Project ID. defaults to None.'], 'version_added': '2.5'}",
    "provider": "{'description': ['Default endpoint connection information, required if state is true.'], 'suboptions': {'hostname': {'description': "The provider's api hostname.", 'required': True}, 'port': {'description': "The provider's api port."}, 'userid': {'description': "Provider's api endpoint authentication userid. defaults to None."}, 'password': {'description': "Provider's api endpoint authentication password. defaults to None."}, 'auth_key': {'description': "Provider's api endpoint authentication bearer token. defaults to None."}, 'verify_ssl': {'description': 'Whether SSL certificates should be verified for HTTPS requests (deprecated). defaults to True.', 'type': 'bool', 'default': 'yes'}, 'security_protocol': {'description': 'How SSL certificates should be used for HTTPS requests. defaults to None.', 'choices': ['ssl-with-validation', 'ssl-with-validation-custom-ca', 'ssl-without-validation', 'non-ssl']}, 'certificate_authority': {'description': 'The CA bundle string with custom certificates. defaults to None.'}}}",
    "provider_region": "{'description': ['The provider region name to connect to (e.g. AWS region for Amazon).']}",
    "ssh_keypair": "{'description': ['SSH key pair used for SSH connections to all hosts in this provider.'], 'version_added': '2.5', 'suboptions': {'hostname': {'description': 'Director hostname.', 'required': True}, 'userid': {'description': 'SSH username.'}, 'auth_key': {'description': 'SSH private key.'}}}",
    "state": "{'description': ['absent - provider should not exist, present - provider should be present, refresh - provider will be refreshed'], 'choices': ['absent', 'present', 'refresh'], 'default': 'present'}",
    "subscription": "{'description': ['Microsoft Azure subscription ID. defaults to None.'], 'version_added': '2.5'}",
    "tenant_mapping_enabled": "{'type': 'bool', 'default': False, 'description': ['Whether to enable mapping of existing tenants. defaults to False.'], 'version_added': '2.5'}",
    "type": "{'description': ["The provider's type."], 'required': True, 'choices': ['Openshift', 'Amazon', 'oVirt', 'VMware', 'Azure', 'Director', 'OpenStack', 'GCE']}",
    "zone": "{'description': ['The ManageIQ zone name that will manage the provider.'], 'default': 'default'}",
}
```

## Examples


``` yaml

- name: Create a new provider in ManageIQ ('Hawkular' metrics)
  manageiq_provider:
    name: 'EngLab'
    type: 'OpenShift'
    state: 'present'
    provider:
      auth_key: 'topSecret'
      hostname: 'example.com'
      port: 8443
      verify_ssl: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      auth_key: 'topSecret'
      role: 'hawkular'
      hostname: 'example.com'
      port: 443
      verify_ssl: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1:80'
      username: 'admin'
      password: 'password'
      verify_ssl: true


- name: Update an existing provider named 'EngLab' (defaults to 'Prometheus' metrics)
  manageiq_provider:
    name: 'EngLab'
    type: 'Openshift'
    state: 'present'
    provider:
      auth_key: 'topSecret'
      hostname: 'next.example.com'
      port: 8443
      verify_ssl: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      auth_key: 'topSecret'
      hostname: 'next.example.com'
      port: 443
      verify_ssl: true
      security_protocol: 'ssl-with-validation-custom-ca'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      verify_ssl: true


- name: Delete a provider in ManageIQ
  manageiq_provider:
    name: 'EngLab'
    type: 'Openshift'
    state: 'absent'
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      verify_ssl: true


- name: Create a new Amazon provider in ManageIQ using token authentication
  manageiq_provider:
    name: 'EngAmazon'
    type: 'Amazon'
    state: 'present'
    provider:
      hostname: 'amazon.example.com'
      userid: 'hello'
      password: 'world'
    manageiq_connection:
      url: 'https://127.0.0.1'
      token: 'VeryLongToken'
      verify_ssl: true


- name: Create a new oVirt provider in ManageIQ
  manageiq_provider:
    name: 'RHEV'
    type: 'oVirt'
    state: 'present'
    provider:
      hostname: 'rhev01.example.com'
      userid: 'admin@internal'
      password: 'password'
      verify_ssl: true
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      hostname: 'metrics.example.com'
      path: 'ovirt_engine_history'
      userid: 'user_id_metrics'
      password: 'password_metrics'
      verify_ssl: true
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    manageiq_connection:
      url: 'https://127.0.0.1'
      username: 'admin'
      password: 'password'
      verify_ssl: true

- name: Create a new VMware provider in ManageIQ
  manageiq_provider:
    name: 'EngVMware'
    type: 'VMware'
    state: 'present'
    provider:
      hostname: 'vcenter.example.com'
      host_default_vnc_port_start: 5800
      host_default_vnc_port_end: 5801
      userid: 'root'
      password: 'password'
    manageiq_connection:
      url: 'https://127.0.0.1'
      token: 'VeryLongToken'
      verify_ssl: true

- name: Create a new Azure provider in ManageIQ
  manageiq_provider:
    name: 'EngAzure'
    type: 'Azure'
    provider_region: 'northeurope'
    subscription: 'e272bd74-f661-484f-b223-88dd128a4049'
    azure_tenant_id: 'e272bd74-f661-484f-b223-88dd128a4048'
    state: 'present'
    provider:
      hostname: 'azure.example.com'
      userid: 'e272bd74-f661-484f-b223-88dd128a4049'
      password: 'password'
    manageiq_connection:
      url: 'https://cf-6af0.rhpds.opentlc.com'
      username: 'admin'
      password: 'password'
      verify_ssl: false

- name: Create a new OpenStack Director provider in ManageIQ with rsa keypair
  manageiq_provider:
    name: 'EngDirector'
    type: 'Director'
    api_version: 'v3'
    state: 'present'
    provider:
      hostname: 'director.example.com'
      userid: 'admin'
      password: 'password'
      security_protocol: 'ssl-with-validation'
      verify_ssl: 'true'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    ssh_keypair:
      hostname: director.example.com
      userid: heat-admin
      auth_key: 'SecretSSHPrivateKey'

- name: Create a new OpenStack provider in ManageIQ with amqp metrics
  manageiq_provider:
    name: 'EngOpenStack'
    type: 'OpenStack'
    api_version: 'v3'
    state: 'present'
    provider_region: 'europe'
    tenant_mapping_enabled: 'False'
    keystone_v3_domain_id: 'mydomain'
    provider:
      hostname: 'openstack.example.com'
      userid: 'admin'
      password: 'password'
      security_protocol: 'ssl-with-validation'
      verify_ssl: 'true'
      certificate_authority: |
        -----BEGIN CERTIFICATE-----
        FAKECERTsdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu
        c2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkwHhcNMTcwODIxMTI1NTE5WhcNMjIwODIw
        MTI1NTIwWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MDMzMjAxMTkw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUDnL2tQ2xf/zO7F7hmZ4S
        ZuwKENdI4IYuWSxye4i3hPhKg6eKPzGzmDNWkIMDOrDAj1EgVSNPtPwsOL8OWvJm
        AaTjr070D7ZGWWnrrDrWEClBx9Rx/6JAM38RT8Pu7c1hXBm0J81KufSLLYiZ/gOw
        Znks5v5RUSGcAXvLkBJeATbsbh6fKX0RgQ3fFTvqQaE/r8LxcTN1uehPX1g5AaRa
        z/SNDHaFtQlE3XcqAAukyMn4N5kdNcuwF3GlQ+tJnJv8SstPkfQcZbTMUQ7I2KpJ
        ajXnMxmBhV5fCN4rb0QUNCrk2/B+EUMBY4MnxIakqNxnN1kvgI7FBbFgrHUe6QvJ
        AgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG
        SIb3DQEBCwUAA4IBAQAYRV57LUsqznSLZHA77o9+0fQetIE115DYP7wea42PODJI
        QJ+JETEfoCr0+YOMAbVmznP9GH5cMTKEWHExcIpbMBU7nMZp6A3htcJgF2fgPzOA
        aTUtzkuVCSrV//mbbYVxoFOc6sR3Br0wBs5+5iz3dBSt7xmgpMzZvqsQl655i051
        gGSTIY3z5EJmBZBjwuTjal9mMoPGA4eoTPqlITJDHQ2bdCV2oDbc7zqupGrUfZFA
        qzgieEyGzdCSRwjr1/PibA3bpwHyhD9CGD0PRVVTLhw6h6L5kuN1jA20OfzWxf/o
        XUsdmRaWiF+l4s6Dcd56SuRp5SGNa2+vP9Of/FX5
        -----END CERTIFICATE-----
    metrics:
      role: amqp
      hostname: 'amqp.example.com'
      security_protocol: 'non-ssl'
      port: 5666
      userid: admin
      password: password


- name: Create a new GCE provider in ManageIQ
  manageiq_provider:
    name: 'EngGoogle'
    type: 'GCE'
    provider_region: 'europe-west1'
    project: 'project1'
    state: 'present'
    provider:
      hostname: 'gce.example.com'
      auth_key: 'google_json_key'
      verify_ssl: 'false'

```

## License

TODO

## Author Information
  - ['Daniel Korn (@dkorn)']
