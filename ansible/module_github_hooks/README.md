# Ansible module: ansible.module_github_hooks


Manages GitHub service hooks

## Description

Adds service hooks and removes service hooks that have an error status.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['This tells the githooks module what you want it to do.'], 'required': True, 'choices': ['create', 'cleanall', 'list', 'clean504']}",
    "content_type": "{'description': ['Content type to use for requests made to the webhook'], 'required': False, 'default': 'json', 'choices': ['json', 'form']}",
    "hookurl": "{'description': ['When creating a new hook, this is the url that you want GitHub to post to. It is only required when creating a new hook.'], 'required': False}",
    "oauthkey": "{'description': ['The oauth key provided by GitHub. It can be found/generated on GitHub under "Edit Your Profile" >> "Developer settings" >> "Personal Access Tokens"'], 'required': True}",
    "repo": "{'description': ['This is the API url for the repository you want to manage hooks for. It should be in the form of: https://api.github.com/repos/user:/repo:. Note this is different than the normal repo url.\n'], 'required': True}",
    "user": "{'description': ['Github username.'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target repo will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Example creating a new service hook. It ignores duplicates.
- github_hooks:
    action: create
    hookurl: http://11.111.111.111:2222
    user: '{{ gituser }}'
    oauthkey: '{{ oauthkey }}'
    repo: https://api.github.com/repos/pcgentry/Github-Auto-Deploy

# Cleaning all hooks for this repo that had an error on the last update. Since this works for all hooks in a repo it is probably best that this would
# be called from a handler.
- github_hooks:
    action: cleanall
    user: '{{ gituser }}'
    oauthkey: '{{ oauthkey }}'
    repo: '{{ repo }}'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Phillip Gentry, CX Inc (@pcgentry)']
