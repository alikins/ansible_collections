# Ansible module: ansible.module_xml


Manage bits and pieces of XML files or strings

## Description

A CRUD-like interface to managing bits of XML files.
You might also be interested in a brief tutorial from U(https://www.w3schools.com/xml/xpath_intro.asp) and U(https://developer.mozilla.org/en-US/docs/Web/XPath).

## Requirements

TODO

## Arguments

``` json
{
    "add_children": "{'description': ['Add additional child-element(s) to a selected element for a given C(xpath).', 'Child elements must be given in a list and each item may be either a string (eg. C(children=ansible) to add an empty C(<ansible/>) child element), or a hash where the key is an element name and the value is the element value.', 'This parameter requires C(xpath) to be set.']}",
    "attribute": "{'description': ['The attribute to select when using parameter C(value).', 'This is a string, not prepended with C(@).']}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "content": "{'description': ['Search for a given C(xpath) and get content.', 'This parameter requires C(xpath) to be set.'], 'choices': ['attribute', 'text']}",
    "count": "{'description': ['Search for a given C(xpath) and provide the count of any matches.', 'This parameter requires C(xpath) to be set.'], 'type': 'bool', 'default': False}",
    "input_type": "{'description': ['Type of input for C(add_children) and C(set_children).'], 'choices': ['xml', 'yaml'], 'default': 'yaml'}",
    "namespaces": "{'description': ['The namespace C(prefix:uri) mapping for the XPath expression.', 'Needs to be a C(dict), not a C(list) of items.']}",
    "path": "{'description': ['Path to the file to operate on. File must exist ahead of time.', 'This parameter is required, unless C(xmlstring) is given.'], 'required': True, 'aliases': ['dest', 'file']}",
    "pretty_print": "{'description': ['Pretty print XML output.'], 'type': 'bool', 'default': False}",
    "print_match": "{'description': ['Search for a given C(xpath) and print out any matches.', 'This parameter requires C(xpath) to be set.'], 'type': 'bool', 'default': False}",
    "set_children": "{'description': ['Set the child-element(s) of a selected element for a given C(xpath).', 'Removes any existing children.', 'Child elements must be specified as in C(add_children).', 'This parameter requires C(xpath) to be set.']}",
    "state": "{'description': ['Set or remove an xpath selection (node(s), attribute(s)).'], 'default': 'present', 'choices': ['absent', 'present'], 'aliases': ['ensure']}",
    "strip_cdata_tags": "{'description': ['Remove CDATA tags surrounding text values.', 'Note that this might break your XML file if text values contain characters that could be interpreted as XML.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "value": "{'description': ['Desired state of the selected attribute.', 'Either a string, or to unset a value, the Python C(None) keyword (YAML Equivalent, C(null)).', 'Elements default to no value (but present).', 'Attributes default to an empty string.']}",
    "xmlstring": "{'description': ['A string containing XML on which to operate.', 'This parameter is required, unless C(path) is given.'], 'required': True}",
    "xpath": "{'description': ['A valid XPath expression describing the item(s) you want to manipulate.', 'Operates on the document root, C(/), by default.']}",
}
```

## Examples


``` yaml

- name: Remove the subjective attribute of the rating element
  xml:
    path: /foo/bar.xml
    xpath: /business/rating/@subjective
    state: absent

- name: Set the rating to 11
  xml:
    path: /foo/bar.xml
    xpath: /business/rating
    value: 11

# Retrieve and display the number of nodes
- name: Get count of beers nodes
  xml:
    path: /foo/bar.xml
    xpath: /business/beers/beer
    count: yes
  register: hits

- debug:
    var: hits.count

- name: Add a phonenumber element to the business element
  xml:
    path: /foo/bar.xml
    xpath: /business/phonenumber
    value: 555-555-1234

- name: Add several more beers to the beers element
  xml:
    path: /foo/bar.xml
    xpath: /business/beers
    add_children:
    - beer: Old Rasputin
    - beer: Old Motor Oil
    - beer: Old Curmudgeon

- name: Add a validxhtml element to the website element
  xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml

- name: Add an empty validatedon attribute to the validxhtml element
  xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml/@validatedon

- name: Add or modify an attribute, add element if needed
  xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml
    attribute: validatedon
    value: 1976-08-05

# How to read an attribute value and access it in Ansible
- name: Read attribute value
  xml:
    path: /foo/bar.xml
    xpath: /business/website/validxhtml
    content: attribute
    attribute: validatedon
  register: xmlresp

- name: Show attribute value
  debug:
    var: xmlresp.matches[0].validxhtml.validatedon

- name: Remove all children from the website element (option 1)
  xml:
    path: /foo/bar.xml
    xpath: /business/website/*
    state: absent

- name: Remove all children from the website element (option 2)
  xml:
    path: /foo/bar.xml
    xpath: /business/website
    children: []

# In case of namespaces, like in below XML, they have to be explicitely stated
# NOTE: there's the prefix "x" in front of the "bar", too
#<?xml version='1.0' encoding='UTF-8'?>
#<foo xmlns="http://x.test" xmlns:attr="http://z.test">
#  <bar>
#    <baz xmlns="http://y.test" attr:my_namespaced_attribute="true" />
#  </bar>
#</foo>

- name: Set namespaced '/x:foo/x:bar/y:baz/@z:my_namespaced_attribute' to 'false'
  xml:
    path: foo.xml
    xpath: /x:foo/x:bar/y:baz
    namespaces:
      x: http://x.test
      y: http://y.test
      z: http://z.test
    attribute: z:my_namespaced_attribute
    value: 'false'

```

## License

TODO

## Author Information
  - ['Tim Bielawa (@tbielawa)', 'Magnus Hedemark (@magnus919)', 'Dag Wieers (@dagwieers)']
  - ['Tim Bielawa (@tbielawa)', 'Magnus Hedemark (@magnus919)', 'Dag Wieers (@dagwieers)']
  - ['Tim Bielawa (@tbielawa)', 'Magnus Hedemark (@magnus919)', 'Dag Wieers (@dagwieers)']
