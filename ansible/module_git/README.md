# Ansible module: ansible.module_git


Deploy software (or files) from git checkouts

## Description

Manage I(git) checkouts of repositories to deploy files or software.

## Requirements

TODO

## Arguments

``` json
{
    "accept_hostkey": "{'description': ['if C(yes), ensure that "-o StrictHostKeyChecking=no" is present as an ssh option.'], 'type': 'bool', 'default': False, 'version_added': '1.5'}",
    "archive": "{'description': ['Specify archive file path with extension. If specified, creates an archive file of the specified format containing the tree structure for the source tree. Allowed archive formats ["zip", "tar.gz", "tar", "tgz"]', 'This will clone and perform git archive from local directory as not all git servers support git archive.'], 'version_added': '2.4'}",
    "bare": "{'description': ['if C(yes), repository will be created as a bare repo, otherwise it will be a standard repo with a workspace.'], 'type': 'bool', 'default': False, 'version_added': '1.4'}",
    "clone": "{'description': ['If C(no), do not clone the repository if it does not exist locally'], 'type': 'bool', 'default': True, 'version_added': '1.9'}",
    "depth": "{'description': ['Create a shallow clone with a history truncated to the specified number or revisions. The minimum possible value is C(1), otherwise ignored. Needs I(git>=1.9.1) to work correctly.']}",
    "dest": "{'description': ['The path of where the repository should be checked out. This parameter is required, unless C(clone) is set to C(no).'], 'required': True}",
    "executable": "{'description': ['Path to git executable to use. If not supplied, the normal mechanism for resolving binary paths will be used.'], 'version_added': '1.4'}",
    "force": "{'description': ["If C(yes), any modified files in the working repository will be discarded.  Prior to 0.7, this was always 'yes' and could not be disabled.  Prior to 1.9, the default was `yes`"], 'type': 'bool', 'default': False}",
    "key_file": "{'description': ['Specify an optional private key file path, on the target host, to use for the checkout.'], 'version_added': '1.5'}",
    "recursive": "{'description': ['if C(no), repository will be cloned without the --recursive option, skipping sub-modules.'], 'type': 'bool', 'default': True, 'version_added': '1.6'}",
    "reference": "{'description': ['Reference repository (see "git clone --reference ...")'], 'version_added': '1.4'}",
    "refspec": "{'description': ['Add an additional refspec to be fetched. If version is set to a I(SHA-1) not reachable from any branch or tag, this option may be necessary to specify the ref containing the I(SHA-1). Uses the same syntax as the \'git fetch\' command. An example value could be "refs/meta/config".'], 'version_added': '1.9'}",
    "remote": "{'description': ['Name of the remote.'], 'default': 'origin'}",
    "repo": "{'description': ['git, SSH, or HTTP(S) protocol address of the git repository.'], 'required': True, 'aliases': ['name']}",
    "separate_git_dir": "{'description': ['The path to place the cloned repository. If specified, Git repository can be separated from working tree.'], 'version_added': '2.7'}",
    "ssh_opts": "{'description': ['Creates a wrapper script and exports the path as GIT_SSH which git then automatically uses to override ssh arguments. An example value could be "-o StrictHostKeyChecking=no"'], 'version_added': '1.5'}",
    "track_submodules": "{'description': ['if C(yes), submodules will track the latest commit on their master branch (or other branch specified in .gitmodules).  If C(no), submodules will be kept at the revision specified by the main project. This is equivalent to specifying the --remote flag to git submodule update.'], 'type': 'bool', 'default': False, 'version_added': '1.8'}",
    "umask": "{'description': ['The umask to set before doing any checkouts, or any other repository maintenance.'], 'version_added': '2.2'}",
    "update": "{'description': ['If C(no), do not retrieve new revisions from the origin repository', 'Operations like archive will work on the existing (old) repository and might not respond to changes to the options version or remote.'], 'type': 'bool', 'default': True}",
    "verify_commit": "{'description': ['if C(yes), when cloning or checking out a C(version) verify the signature of a GPG signed commit. This requires C(git) version>=2.1.0 to be installed. The commit MUST be signed and the public key MUST be present in the GPG keyring.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "version": "{'description': ['What version of the repository to check out.  This can be the literal string C(HEAD), a branch name, a tag name. It can also be a I(SHA-1) hash, in which case C(refspec) needs to be specified if the given revision is not already available.'], 'default': 'HEAD'}",
}
```

## Examples


``` yaml

# Example git checkout from Ansible Playbooks
- git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    version: release-0.22

# Example read-write git checkout from github
- git:
    repo: ssh://git@github.com/mylogin/hello.git
    dest: /home/mylogin/hello

# Example just ensuring the repo checkout exists
- git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    update: no

# Example just get information about the repository whether or not it has
# already been cloned locally.
- git:
    repo: 'https://foosball.example.org/path/to/repo.git'
    dest: /srv/checkout
    clone: no
    update: no

# Example checkout a github repo and use refspec to fetch all pull requests
- git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    refspec: '+refs/pull/*:refs/heads/*'

# Example Create git archive from repo
- git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    archive: /tmp/ansible-examples.zip

# Example clone a repo with separate git directory
- git:
    repo: https://github.com/ansible/ansible-examples.git
    dest: /src/ansible-examples
    separate_git_dir: /src/ansible-examples.git

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
