# Ansible module: ansible.module_win_dsc


Invokes a PowerShell DSC configuration

## Description

Configures a resource using PowerShell DSC.
Requires PowerShell version 5.0 or newer.
Most of the options for this module are dynamic and will vary depending on the DSC Resource specified in I(resource_name).
See :doc:`/user_guide/windows_dsc` for more information on how to use this module.

## Requirements

TODO

## Arguments

``` json
{
    "free_form": "{'description': ['The M(win_dsc) module takes in multiple free form options based on the DSC resource being invoked by I(resource_name).', 'There is no option actually named C(free_form) so see the examples.', 'This module will try and convert the option to the correct type required by the DSC resource and throw a warning if it fails.', 'If the type of the DSC resource option is a C(CimInstance) or C(CimInstance[]), this means the value should be a dictionary or list of dictionaries based on the values required by that option.', 'If the type of the DSC resource option is a C(PSCredential) then there needs to be 2 options set in the Ansible task definition suffixed with C(_username) and C(_password).', 'If the type of the DSC resource option is an array, then a list should be provided but a comma separated string also work. Use a list where possible as no escaping is required and it works with more complex types list C(CimInstance[]).'], 'required': True}",
    "module_version": "{'description': ['Can be used to configure the exact version of the DSC resource to be invoked.', 'Useful if the target node has multiple versions installed of the module containing the DSC resource.', 'If not specified, the module will follow standard PowerShell convention and use the highest version available.'], 'default': 'latest'}",
    "resource_name": "{'description': ['The name of the DSC Resource to use.', 'Must be accessible to PowerShell using any of the default paths.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Extract zip file
  win_dsc:
    resource_name: Archive
    Ensure: Present
    Path: C:\Temp\zipfile.zip
    Destination: C:\Temp\Temp2

- name: Install a Windows feature with the WindowsFeature resource
  win_dsc:
    resource_name: WindowsFeature
    Name: telnet-client

- name: Edit HKCU reg key under specific user
  win_regedit:
    resource_name: Registry
    Ensure: Present
    Key: HKEY_CURRENT_USER\ExampleKey
    ValueName: TestValue
    ValueData: TestData
    PsDscRunAsCredential_username: '{{ansible_user}}'
    PsDscRunAsCredentual_password: '{{ansible_password}}'
  no_log: true

- name: Create file with multiple attributes
  win_dsc:
    resource_name: File
    DestinationPath: C:\ansible\dsc
    Attributes: # can also be a comma separated string, e.g. 'Hidden, System'
    - Hidden
    - System
    Ensure: Present
    Type: Directory

# more complex example using custom DSC resource and dict values
- name: Setup the xWebAdministration module
  win_psmodule:
    name: xWebAdministration
    state: present

- name: Create IIS Website with Binding and Authentication options
  win_dsc:
    resource_name: xWebsite
    Ensure: Present
    Name: DSC Website
    State: Started
    PhysicalPath: C:\inetpub\wwwroot
    BindingInfo: # Example of a CimInstance[] DSC parameter (list of dicts)
    - Protocol: https
      Port: 1234
      CertificateStoreName: MY
      CertificateThumbprint: C676A89018C4D5902353545343634F35E6B3A659
      HostName: DSCTest
      IPAddress: '*'
      SSLFlags: '1'
    - Protocol: http
      Port: 4321
      IPAddress: '*'
    AuthenticationInfo: # Example of a CimInstance DSC parameter (dict)
      Anonymous: no
      Basic: true
      Digest: false
      Windows: yes

```

## License

TODO

## Author Information
  - ['Trond Hindenes (@trondhindenes)']
