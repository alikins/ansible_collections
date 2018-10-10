# Ansible module: ansible.module_win_xml


Add XML fragment to an XML parent

## Description

Adds XML fragments formatted as strings to existing XML on remote servers.

## Requirements

TODO

## Arguments

``` json
{
    "attribute": "{'description': ["The attribute name if the type is 'attribute'. Required if C(type=attribute)."]}",
    "backup": "{'description': ["Whether to backup the remote server's XML before applying the change."], 'type': 'bool', 'default': False}",
    "fragment": "{'description': ['The string representation of the XML fragment to be added.'], 'required': True, 'aliases': ['xmlstring']}",
    "path": "{'description': ['The path of remote servers XML.'], 'required': True, 'aliases': ['dest', 'file']}",
    "type": "{'description': ['The type of XML you are working with.'], 'required': True, 'default': 'element', 'choices': ['element', 'attribute', 'text']}",
    "xpath": "{'description': ['The node of the remote server XML where the fragment will go.'], 'required': True}",
}
```

## Examples


``` yaml

# Apply our filter to Tomcat web.xml
- win_xml:
   path: C:\apache-tomcat\webapps\myapp\WEB-INF\web.xml
   fragment: '<filter><filter-name>MyFilter</filter-name><filter-class>com.example.MyFilter</filter-class></filter>'
   xpath: '/*'

# Apply sslEnabledProtocols to Tomcat's server.xml
- win_xml:
   path: C:\Tomcat\conf\server.xml
   xpath: '//Server/Service[@name="Catalina"]/Connector[@port="9443"]'
   attribute: 'sslEnabledProtocols'
   fragment: 'TLSv1,TLSv1.1,TLSv1.2'
   type: attribute

```

## License

TODO

## Author Information
  - ['Richard Levenberg (@richardcs)']
