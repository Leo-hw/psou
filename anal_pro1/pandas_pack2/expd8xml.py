# XML 자료 읽기
import xml.etree.ElementTree as etree

#파이썬 방식으로 읽기
xml_f = open('my.xml', 'r', encoding='utf8').read()
print(xml_f, type(xml_f)) # <class 'str'>
root = etree.fromstring(xml_f)
print(root, type(root))     #<class 'xml.etree.ElementTree.Element'>
print(len(root))


print('----------------------------------------------')
# ElementTree 로 file 오픈
xmlFile = etree.parse('my.xml')
print(xmlFile, type(xmlFile))

root = xmlFile.getroot()
print(root.tag) # items
print(root[0].tag)  #item                 0 번째 요소명 (node name)
print(root[0][0].tag) #name
print(root[0][1].tag) #tel
print(root[0][0].attrib)
print(root[0][2].attrib)
print(root[0][2].attrib.keys())
print(root[0][2].attrib.values())
print()
myname = root.find("item").find("name").text
print(myname)

mytel = root.find("item").find("tel").text
print(myname + " " + mytel)

print()
for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, ' ', child2.attrib)
    print()
print()
for e in root.iter('exam'):
    print(e.attrib)

print()
#children = root.findall('item')
children = root.findall('.//item')              # './/item[1]'      './/item[last()]' ...
print(len(children))
for aa in children:
    re_id =aa.find('name').get('id')            # 해당 요소의 속성값 읽기
    re_name = aa.find('name').text
    re_tel = aa.find('tel').text
    print(re_id, re_name, re_tel)

    
    
    
