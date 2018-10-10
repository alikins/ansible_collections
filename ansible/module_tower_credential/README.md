# Ansible module: ansible.module_tower_credential


create, update, or destroy Ansible Tower credential

## Description

Create, update, or destroy Ansible Tower credentials. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "authorize": "{'description': ['Should use authorize for net type.'], 'type': 'bool', 'default': False}",
    "authorize_password": "{'description': ['Password for net credentials that require authorize.']}",
    "become_method": "{'description': ['Become method to Use for privledge escalation.'], 'choices': ['None', 'sudo', 'su', 'pbrun', 'pfexec', 'pmrun']}",
    "become_password": "{'description': ['Become password. Use ASK for prompting.']}",
    "become_username": "{'description': ['Become username. Use ASK for prompting.']}",
    "client": "{'description': ['Client or application ID for azure_rm type.']}",
    "description": "{'description': ['The description to use for the credential.']}",
    "domain": "{'description': ['Domain for openstack type.']}",
    "host": "{'description': ['Host for this credential.']}",
    "kind": "{'description': ['Type of credential being added.'], 'required': True, 'choices': ['ssh', 'vault', 'net', 'scm', 'aws', 'vmware', 'satellite6', 'cloudforms', 'gce', 'azure_rm', 'openstack', 'rhv', 'insights', 'tower']}",
    "name": "{'description': ['The name to use for the credential.'], 'required': True}",
    "organization": "{'description': ['Organization that should own the credential.']}",
    "password": "{'description': ['Password for this credential. Use ASK for prompting. secret_key for AWS. api_key for RAX.']}",
    "project": "{'description': ['Project that should for this credential.']}",
    "secret": "{'description': ['Secret token for azure_rm type.']}",
    "security_token": "{'description': ['STS token for aws type.'], 'version_added': '2.6'}",
    "ssh_key_data": "{'description': ['SSH private key content. To extract the content from a file path, use the lookup function (see examples).'], 'required': False}",
    "ssh_key_unlock": "{'description': ['Unlock password for ssh_key. Use ASK for prompting.']}",
    "state": "{'description': ['Desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subscription": "{'description': ['Subscription ID for azure_rm type.']}",
    "team": "{'description': ['Team that should own this credential.']}",
    "tenant": "{'description': ['Tenant ID for azure_rm type.']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "user": "{'description': ['User that should own this credential.']}",
    "username": "{'description': ['Username for this credential. access_key for AWS.']}",
    "vault_password": "{'description': ['Vault password. Use ASK for prompting.']}",
}
```

## Examples


``` yaml

- name: Add tower credential
  tower_credential:
    name: Team Name
    description: Team Description
    organization: test-org
    state: present
    tower_config_file: "~/tower_cli.cfg"

- name: Create a valid SCM credential from a private_key file
  tower_credential:
    name: SCM Credential
    organization: Default
    state: present
    kind: scm
    username: joe
    password: secret
    ssh_key_data: "{{ lookup('file', '/tmp/id_rsa') }}"
    ssh_key_unlock: "passphrase"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
