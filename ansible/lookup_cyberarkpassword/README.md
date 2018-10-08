# Ansible lookup: ansible.lookup_cyberarkpassword


get secrets from CyberArk AIM

## Description

Get secrets from CyberArk AIM.

## Requirements

TODO

## Arguments

``` json
{
    "_command": "{'description': ['Cyberark CLI utility.'], 'env': [{'name': 'AIM_CLIPASSWORDSDK_CMD'}], 'default': '/opt/CARKaim/sdk/clipasswordsdk'}",
    "_extra": "{'description': ['for extra_parms values please check parameters for clipasswordsdk in CyberArk\'s "Credential Provider and ASCP Implementation Guide"']}",
    "appid": "{'description': ['Defines the unique ID of the application that is issuing the password request.'], 'required': True}",
    "output": "{'description': ['Specifies the desired output fields separated by commas.', 'They could be: Password, PassProps.<property>, PasswordChangeInProcess'], 'default': 'password'}",
    "query": "{'description': ['Describes the filter criteria for the password retrieval.'], 'required': True}",
}
```

## Examples


``` yaml

  - name: passing options to the lookup
    debug: msg={{ lookup("cyberarkpassword", cyquery)}}
    vars:
      cyquery:
        appid: "app_ansible"
        query": "safe=CyberArk_Passwords;folder=root;object=AdminPass"
        output: "Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess"


  - name: used in a loop
    debug: msg={{item}}
    with_cyberarkpassword:
        appid: 'app_ansible'
        query: 'safe=CyberArk_Passwords;folder=root;object=AdminPass'
        output: 'Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess'

```

## License

TODO

## Author Information
  - ['UNKNOWN']
