###XML Basics
# <person>
#    <name> Chuck </name>
#    <phone type = "intl">
#        +1 734 303 4456
#    </phone>
#    <email hide = "yes" />
# </person>

###XSD Constraints (XML Schema)
# <xs: element name = "person">
#    <xs: complexType>
#        <xs:sequence>
#            <xs:element name="full_name" type="xs:string"
#                minOccurs="1" maxOccurs="10" />
#            <xs:element name="child_name" type="xs:string"
#                minOccurs="1" maxOccurs="10" />
#        </xs:sequence>
#    </xs: complexType>
# </xs:element>

###XSD Data Types
# <xs:element name = "customer" type="xs:string"/>
# <xs:element name = "start" type="xs:date"/>
# <xs:element name = "startdate" type="xs:dateTime"/>
# <xs:element name = "prize" type="xs:decimal"/>
# <xs:element name = "weeks" type="xs:integer"/>

# XML in Python
import xml.etree.ElementTree as ET

data = ''' <person>
<name>Chuck</name> <phone type="intl">
    +1 734 303 4456
  </phone>
<email hide="yes" /> </person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# List of Trees
import xml.etree.ElementTree as ET

input = '''<stuff>
    <users> Chuck 
        <user x = "2>
            <id> 001 </id>
            <name>Chuck </name>
        </user>
        <user x = "7>
            <id> 009 </id>
            <name>Brent </name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get("x"))

###
