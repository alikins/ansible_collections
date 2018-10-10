# Ansible module: ansible.module_imc_rest


Manage Cisco IMC hardware through its REST API

## Description

Provides direct access to the Cisco IMC REST API.
Perform any configuration changes and actions that the Cisco IMC supports.
More information about the IMC REST API is available from U(http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/3_0/b_Cisco_IMC_api_301.html)

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ['When used instead of C(path), sets the content of the API requests directly.', 'This may be convenient to template simple requests, for anything complex use the M(template) module.', 'You can collate multiple IMC XML fragments and they will be processed sequentially in a single stream, the Cisco IMC output is subsequently merged.', 'Parameter C(content) is mutual exclusive with parameter C(path).']}",
    "hostname": "{'description': ['IP Address or hostname of Cisco IMC, resolvable by Ansible control host.'], 'required': True, 'aliases': ['host', 'ip']}",
    "password": "{'description': ['The password to use for authentication.'], 'default': 'password'}",
    "path": "{'description': ['Name of the absolute path of the filename that includes the body of the http request being sent to the Cisco IMC REST API.', 'Parameter C(path) is mutual exclusive with parameter C(content).'], 'aliases': ['src', 'config_file']}",
    "protocol": "{'description': ['Connection protocol to use.'], 'default': 'https', 'choices': ['http', 'https']}",
    "timeout": "{'description': ['The socket level timeout in seconds.', 'This is the time that every single connection (every fragment) can spend. If this C(timeout) is reached, the module will fail with a C(Connection failure) indicating that C(The read operation timed out).'], 'default': 60}",
    "username": "{'description': ['Username used to login to the switch.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Power down server
  imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    content: |
      <configConfMo><inConfig>
        <computeRackUnit dn="sys/rack-unit-1" adminPower="down"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Configure IMC using multiple XML fragments
  imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    timeout: 120
    content: |
      <!-- Configure Serial-on-LAN -->
      <configConfMo><inConfig>
        <solIf dn="sys/rack-unit-1/sol-if" adminState="enable" speed=="115200" comport="com0"/>
      </inConfig></configConfMo>

      <!-- Configure Console Redirection -->
      <configConfMo><inConfig>
        <biosVfConsoleRedirection dn="sys/rack-unit-1/bios/bios-settings/Console-redirection"
          vpBaudRate="115200"
          vpConsoleRedirection="com-0"
          vpFlowControl="none"
          vpTerminalType="vt100"
          vpPuttyKeyPad="LINUX"
          vpRedirectionAfterPOST="Always Enable"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Enable PXE boot and power-cycle server
  imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    content: |
      <!-- Configure PXE boot -->
      <configConfMo><inConfig>
        <lsbootLan dn="sys/rack-unit-1/boot-policy/lan-read-only" access="read-only" order="1" prot="pxe" type="lan"/>
      </inConfig></configConfMo>

      <!-- Power cycle server -->
      <configConfMo><inConfig>
        <computeRackUnit dn="sys/rack-unit-1" adminPower="cycle-immediate"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Reconfigure IMC to boot from storage
  imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    content: |
      <configConfMo><inConfig>
        <lsbootStorage dn="sys/rack-unit-1/boot-policy/storage-read-write" access="read-write" order="1" type="storage"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Add customer description to server
  imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    content: |
        <configConfMo><inConfig>
          <computeRackUnit dn="sys/rack-unit-1" usrLbl="Customer Lab - POD{{ pod_id }} - {{ inventory_hostname_short }}"/>
        </inConfig></configConfMo>
    delegate_to: localhost

- name: Disable HTTP and increase session timeout to max value 10800 secs
  imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: no
    timeout: 120
    content: |
        <configConfMo><inConfig>
          <commHttp dn="sys/svc-ext/http-svc" adminState="disabled"/>
        </inConfig></configConfMo>

        <configConfMo><inConfig>
          <commHttps dn="sys/svc-ext/https-svc" adminState="enabled" sessionTimeout="10800"/>
        </inConfig></configConfMo>
    delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
