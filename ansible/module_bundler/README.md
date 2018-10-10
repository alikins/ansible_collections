# Ansible module: ansible.module_bundler


Manage Ruby Gem dependencies with Bundler

## Description

Manage installation and Gem version dependencies for Ruby using the Bundler gem

## Requirements

TODO

## Arguments

``` json
{
    "binstub_directory": "{'description': ['Only applies if state is C(present). Specifies the directory to install any gem bins files to. When executed the bin files will run within the context of the Gemfile and fail if any required gem dependencies are not installed. If C(chdir) is set then this path is relative to C(chdir)']}",
    "chdir": "{'description': ['The directory to execute the bundler commands from. This directoy needs to contain a valid Gemfile or .bundle/ directory'], 'default': 'temporary working directory'}",
    "clean": "{'description': ['Only applies if state is C(present). If set removes any gems on the target host that are not in the gemfile'], 'type': 'bool', 'default': False}",
    "deployment_mode": "{'description': ['Only applies if state is C(present). If set it will install gems in ./vendor/bundle instead of the default location. Requires a Gemfile.lock file to have been created prior'], 'type': 'bool', 'default': False}",
    "exclude_groups": "{'description': ["A list of Gemfile groups to exclude during operations. This only applies when state is C(present). Bundler considers this a 'remembered' property for the Gemfile and will automatically exclude groups in future operations even if C(exclude_groups) is not set"]}",
    "executable": "{'description': ['The path to the bundler executable']}",
    "extra_args": "{'description': ['A space separated string of additional commands that can be applied to the Bundler command. Refer to the Bundler documentation for more information']}",
    "gem_path": "{'description': ['Only applies if state is C(present). Specifies the directory to install the gems into. If C(chdir) is set then this path is relative to C(chdir)'], 'default': 'RubyGems gem paths'}",
    "gemfile": "{'description': ['Only applies if state is C(present). The path to the gemfile to use to install gems.'], 'default': 'Gemfile in current directory'}",
    "local": "{'description': ['If set only installs gems from the cache on the target host'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['The desired state of the Gem bundle. C(latest) updates gems to the most recent, acceptable version'], 'choices': ['present', 'latest'], 'default': 'present'}",
    "user_install": "{'description': ["Only applies if state is C(present). Installs gems in the local user's cache or for all users"], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Installs gems from a Gemfile in the current directory
- bundler:
    state: present
    executable: ~/.rvm/gems/2.1.5/bin/bundle

# Excludes the production group from installing
- bundler:
    state: present
    exclude_groups: production

# Install gems into ./vendor/bundle
- bundler:
    state: present
    deployment_mode: yes

# Installs gems using a Gemfile in another directory
- bundler:
    state: present
    gemfile: ../rails_project/Gemfile

# Updates Gemfile in another directory
- bundler:
    state: latest
    chdir: ~/rails_project

```

## License

TODO

## Author Information
  - ['Tim Hoiberg (@thoiberg)']
