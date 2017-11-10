import xml.etree.ElementTree as ET

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''


# The find function searches through the XML tree and retrieves a node that
# matches the specified tag. Each node can have some text, some attributes (like
# hide), and some “child” nodes. Each node can be the top of a tree of nodes

tree=ET.fromstring(data)
print('Name:', tree.find('name').text )
print('Attr:', tree.find('email').get('hide') )

multipleTag = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''


stuff=ET.fromstring(multipleTag)
lst=stuff.findall('users/user')
print("User Count: ", len(lst))

for item in lst:
    print("Name:", item.find('name').text)
    print("ID:", item.find('id').text)
    print("Attribute:", item.get('x'))