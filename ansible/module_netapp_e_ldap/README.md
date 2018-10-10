# Ansible module: ansible.module_netapp_e_ldap


NetApp E-Series manage LDAP integration to use for authentication

## Description

Configure an E-Series system to allow authentication via an LDAP server

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "attributes": "{'description': ['The user attributes that should be considered for the group to role mapping.', "Typically this is used with something like 'memberOf', and a user's access is tested against group membership or lack thereof."], 'default': 'memberOf'}",
    "identifier": "{'description': ['This is a unique identifier for the configuration (for cases where there are multiple domains configured).', "If this is not specified, but I(state=present), we will utilize a default value of 'default'."]}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False}",
    "name": "{'description': ['The domain name[s] that will be utilized when authenticating to identify which domain to utilize.', 'Default to use the DNS name of the I(server).', 'The only requirement is that the name[s] be resolvable.', 'Example: user@example.com'], 'required': False}",
    "password": "{'description': ['This is the password for the bind user account.'], 'required': True, 'aliases': ['bind_password']}",
    "role_mappings": "{'description': ['This is where you specify which groups should have access to what permissions for the storage-system.', 'For example, all users in group A will be assigned all 4 available roles, which will allow access to all the management functionality of the system (super-user). Those in group B only have the storage.monitor role, which will allow only read-only acess.', 'This is specified as a mapping of regular expressions to a list of roles. See the examples.', 'The roles that will be assigned to to the group/groups matching the provided regex.', 'storage.admin allows users full read/write access to storage objects and operations.', 'storage.monitor allows users read-only access to storage objects and operations.', 'support.admin allows users access to hardware, diagnostic information, the Major Event Log, and other critical support-related functionality, but not the storage configuration.', 'security.admin allows users access to authentication/authorization configuration, as well as the audit log configuration, and certification management.'], 'required': True}",
    "search_base": "{'description': ['The search base is used to find group memberships of the user.', 'Example: ou=users,dc=example,dc=com'], 'required': True}",
    "server": "{'description': ['This is the LDAP server url.', 'The connection string should be specified as using the ldap or ldaps protocol along with the port information.'], 'aliases': ['server_url'], 'required': True}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Enable/disable LDAP support on the system. Disabling will clear out any existing defined domains.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "user_attribute": "{'description': ['This is the attribute we will use to match the provided username when a user attempts to authenticate.'], 'default': 'sAMAccountName'}",
    "username": "{'description': ['This is the user account that will be used for querying the LDAP server.', 'Example: CN=MyBindAcct,OU=ServiceAccounts,DC=example,DC=com'], 'required': True, 'aliases': ['bind_username']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Disable LDAP authentication
      netapp_e_ldap:
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"
        ssid: "1"
        state: absent

    - name: Remove the 'default' LDAP domain configuration
      netapp_e_ldap:
        state: absent
        identifier: default

    - name: Define a new LDAP domain, utilizing defaults where possible
      netapp_e_ldap:
        state: present
        bind_username: "CN=MyBindAccount,OU=ServiceAccounts,DC=example,DC=com"
        bind_password: "mySecretPass"
        server: "ldap://example.com:389"
        search_base: 'OU=Users,DC=example,DC=com'
        role_mappings:
          ".*dist-dev-storage.*":
            - storage.admin
            - security.admin
            - support.admin
            - storage.monitor

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
