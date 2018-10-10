# Ansible module: ansible.module_deploy_helper


Manages some of the steps common in deploying projects

## Description

The Deploy Helper manages some of the steps common in deploying software. It creates a folder structure, manages a symlink for the current release and cleans up old releases.
Running it with the C(state=query) or C(state=present) will return the C(deploy_helper) fact. C(project_path), whatever you set in the path parameter, C(current_path), the path to the symlink that points to the active release, C(releases_path), the path to the folder to keep releases in, C(shared_path), the path to the folder to keep shared resources in, C(unfinished_filename), the file to check for to recognize unfinished builds, C(previous_release), the release the 'current' symlink is pointing to, C(previous_release_path), the full path to the 'current' symlink target, C(new_release), either the 'release' parameter or a generated timestamp, C(new_release_path), the path to the new release folder (not created by the module).

## Requirements

TODO

## Arguments

``` json
{
    "clean": "{'description': ['Whether to run the clean procedure in case of C(state=finalize).'], 'type': 'bool', 'default': True}",
    "current_path": "{'description': ['the name of the symlink that is created when the deploy is finalized. Used in C(finalize) and C(clean). Returned in the C(deploy_helper.current_path) fact.'], 'default': 'current'}",
    "keep_releases": "{'description': ['the number of old releases to keep when cleaning. Used in C(finalize) and C(clean). Any unfinished builds will be deleted first, so only correct releases will count. The current version will not count.'], 'default': 5}",
    "path": "{'required': True, 'aliases': ['dest'], 'description': ['the root path of the project. Alias I(dest). Returned in the C(deploy_helper.project_path) fact.']}",
    "release": "{'description': ["the release version that is being deployed. Defaults to a timestamp format %Y%m%d%H%M%S (i.e. '20141119223359'). This parameter is optional during C(state=present), but needs to be set explicitly for C(state=finalize). You can use the generated fact C(release={{ deploy_helper.new_release }})."]}",
    "releases_path": "{'description': ['the name of the folder that will hold the releases. This can be relative to C(path) or absolute. Returned in the C(deploy_helper.releases_path) fact.'], 'default': 'releases'}",
    "shared_path": "{'description': ['the name of the folder that will hold the shared resources. This can be relative to C(path) or absolute. If this is set to an empty string, no shared folder will be created. Returned in the C(deploy_helper.shared_path) fact.'], 'default': 'shared'}",
    "state": "{'description': ['the state of the project. C(query) will only gather facts, C(present) will create the project I(root) folder, and in it the I(releases) and I(shared) folders, C(finalize) will remove the unfinished_filename file, create a symlink to the newly deployed release and optionally clean old releases, C(clean) will remove failed & old releases, C(absent) will remove the project folder (synonymous to the M(file) module with C(state=absent))'], 'choices': ['present', 'finalize', 'absent', 'clean', 'query'], 'default': 'present'}",
    "unfinished_filename": "{'description': ['the name of the file that indicates a deploy has not finished. All folders in the releases_path that contain this file will be deleted on C(state=finalize) with clean=True, or C(state=clean). This file is automatically deleted from the I(new_release_path) during C(state=finalize).'], 'default': 'DEPLOY_UNFINISHED'}",
}
```

## Examples


``` yaml


# General explanation, starting with an example folder structure for a project:

# root:
#     releases:
#         - 20140415234508
#         - 20140415235146
#         - 20140416082818
#
#     shared:
#         - sessions
#         - uploads
#
#     current: releases/20140416082818


# The 'releases' folder holds all the available releases. A release is a complete build of the application being
# deployed. This can be a clone of a repository for example, or a sync of a local folder on your filesystem.
# Having timestamped folders is one way of having distinct releases, but you could choose your own strategy like
# git tags or commit hashes.
#
# During a deploy, a new folder should be created in the releases folder and any build steps required should be
# performed. Once the new build is ready, the deploy procedure is 'finalized' by replacing the 'current' symlink
# with a link to this build.
#
# The 'shared' folder holds any resource that is shared between releases. Examples of this are web-server
# session files, or files uploaded by users of your application. It's quite common to have symlinks from a release
# folder pointing to a shared/subfolder, and creating these links would be automated as part of the build steps.
#
# The 'current' symlink points to one of the releases. Probably the latest one, unless a deploy is in progress.
# The web-server's root for the project will go through this symlink, so the 'downtime' when switching to a new
# release is reduced to the time it takes to switch the link.
#
# To distinguish between successful builds and unfinished ones, a file can be placed in the folder of the release
# that is currently in progress. The existence of this file will mark it as unfinished, and allow an automated
# procedure to remove it during cleanup.


# Typical usage
- name: Initialize the deploy root and gather facts
  deploy_helper:
    path: /path/to/root
- name: Clone the project to the new release folder
  git:
    repo: git://foosball.example.org/path/to/repo.git
    dest: '{{ deploy_helper.new_release_path }}'
    version: v1.1.1
- name: Add an unfinished file, to allow cleanup on successful finalize
  file:
    path: '{{ deploy_helper.new_release_path }}/{{ deploy_helper.unfinished_filename }}'
    state: touch
- name: Perform some build steps, like running your dependency manager for example
  composer:
    command: install
    working_dir: '{{ deploy_helper.new_release_path }}'
- name: Create some folders in the shared folder
  file:
    path: '{{ deploy_helper.shared_path }}/{{ item }}'
    state: directory
  with_items:
    - sessions
    - uploads
- name: Add symlinks from the new release to the shared folder
  file:
    path: '{{ deploy_helper.new_release_path }}/{{ item.path }}'
    src: '{{ deploy_helper.shared_path }}/{{ item.src }}'
    state: link
  with_items:
      - path: app/sessions
        src: sessions
      - path: web/uploads
        src: uploads
- name: Finalize the deploy, removing the unfinished file and switching the symlink
  deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Retrieving facts before running a deploy
- name: Run 'state=query' to gather facts without changing anything
  deploy_helper:
    path: /path/to/root
    state: query
# Remember to set the 'release' parameter when you actually call 'state=present' later
- name: Initialize the deploy root
  deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: present

# all paths can be absolute or relative (to the 'path' parameter)
- deploy_helper:
    path: /path/to/root
    releases_path: /var/www/project/releases
    shared_path: /var/www/shared
    current_path: /var/www/active

# Using your own naming strategy for releases (a version tag in this case):
- deploy_helper:
    path: /path/to/root
    release: v1.1.1
    state: present
- deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Using a different unfinished_filename:
- deploy_helper:
    path: /path/to/root
    unfinished_filename: README.md
    release: '{{ deploy_helper.new_release }}'
    state: finalize

# Postponing the cleanup of older builds:
- deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize
    clean: False
- deploy_helper:
    path: /path/to/root
    state: clean
# Or running the cleanup ahead of the new deploy
- deploy_helper:
    path: /path/to/root
    state: clean
- deploy_helper:
    path: /path/to/root
    state: present

# Keeping more old releases:
- deploy_helper:
    path: /path/to/root
    release: '{{ deploy_helper.new_release }}'
    state: finalize
    keep_releases: 10
# Or, if you use 'clean=false' on finalize:
- deploy_helper:
    path: /path/to/root
    state: clean
    keep_releases: 10

# Removing the entire project root folder
- deploy_helper:
    path: /path/to/root
    state: absent

# Debugging the facts returned by the module
- deploy_helper:
    path: /path/to/root
- debug:
    var: deploy_helper

```

## License

TODO

## Author Information
  - ['Ramon de la Fuente (@ramondelafuente)']
