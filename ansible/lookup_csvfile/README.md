# Ansible lookup: ansible.lookup_csvfile


read data from a TSV or CSV file

## Description

The csvfile lookup reads the contents of a file in CSV (comma-separated value) format. The lookup looks for the row where the first column matches keyname, and returns the value in the second column, unless a different column is specified.

## Requirements

TODO

## Arguments

``` json
{
    "col": "{'description': ['column to return (0 index).'], 'default': '1'}",
    "default": "{'description': ['what to return if the value is not found in the file.'], 'default': ''}",
    "delimiter": "{'description': ['field separator in the file, for a tab you can specify "TAB" or "t".'], 'default': 'TAB'}",
    "encoding": "{'description': ['Encoding (character set) of the used CSV file.'], 'default': 'utf-8', 'version_added': '2.1'}",
    "file": "{'description': ['name of the CSV/TSV file to open.'], 'default': 'ansible.csv'}",
}
```

## Examples


``` yaml

- name:  Match 'Li' on the first column, return the second column (0 based index)
  debug: msg="The atomic number of Lithium is {{ lookup('csvfile', 'Li file=elements.csv delimiter=,') }}"

- name: msg="Match 'Li' on the first column, but return the 3rd column (columns start counting after the match)"
  debug: msg="The atomic mass of Lithium is {{ lookup('csvfile', 'Li file=elements.csv delimiter=, col=2') }}"

- name: Define Values From CSV File
  set_fact:
    loop_ip: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=1') }}"
    int_ip: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=2') }}"
    int_mask: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=3') }}"
    int_name: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=4') }}"
    local_as: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=5') }}"
    neighbor_as: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=6') }}"
    neigh_int_ip: "{{ lookup('csvfile', bgp_neighbor_ip +' file=bgp_neighbors.csv delimiter=, col=7') }}"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>']
