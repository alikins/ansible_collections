# Ansible module: ansible.module_win_template


Templates a file out to a remote server

## Description

Templates are processed by the Jinja2 templating language (U(http://jinja.pocoo.org/docs/)) - documentation on the template formatting can be found in the Template Designer Documentation (U(http://jinja.pocoo.org/docs/templates/)).
Six additional variables can be used in templates: C(ansible_managed) (configurable via the C(defaults) section of C(ansible.cfg)) contains a string which can be used to describe the template name, host, modification time of the template file and the owner uid, C(template_host) contains the node name of the template's machine, C(template_uid) the owner, C(template_path) the absolute path of the template, C(template_fullpath) is the absolute path of the template, and C(template_run_date) is the date that the template was rendered. Note that including a string that uses a date in the template will result in the template being marked 'changed' each time.

## Requirements

TODO

## Arguments

``` json
{
    "block_end_string": "{'description': ['The string marking the end of a block.'], 'default': '%}', 'version_added': '2.4'}",
    "block_start_string": "{'description': ['The string marking the beginning of a block.'], 'default': '{%', 'version_added': '2.4'}",
    "dest": "{'description': ['Location to render the template to on the remote machine.'], 'required': True}",
    "force": "{'description': ['If C(yes), will replace the remote file when contents are different from the source.', 'If C(no), the file will only be transferred if the destination does not exist.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "newline_sequence": "{'description': ['Specify the newline sequence to use for templating files.'], 'choices': ['\\n', '\\r', '\\r\\n'], 'default': '\\r\\n', 'version_added': '2.4'}",
    "src": "{'description': ['Path of a Jinja2 formatted template on the local server. This can be a relative or absolute path.'], 'required': True}",
    "trim_blocks": "{'description': ['If this is set to C(yes) the first newline after a block is removed (block, not variable tag!).'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "variable_end_string": "{'description': ['The string marking the end of a print statement.'], 'default': '}}', 'version_added': '2.4'}",
    "variable_start_string": "{'description': ['The string marking the beginning of a print statement.'], 'default': '{{', 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Create a file from a Jinja2 template
  win_template:
    src: /mytemplates/file.conf.j2
    dest: C:\Temp\file.conf

- name: Create a Unix-style file from a Jinja2 template
  win_template:
    src: unix/config.conf.j2
    dest: C:\share\unix\config.conf
    newline_sequence: '\n'

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
