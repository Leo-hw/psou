# 기상청 제공 XML 형식의 날씨 정보 읽기\
import urllib.request
import xml.etree.ElementTree as etree

# 방법 1 : 웹문서를 읽어 file 에 저장 후 처리
'''
try:
    webdata = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
    webxml = webdata.read()
    webxml = webxml.decode('utf-8')           # 디코딩
    print(webxml)
    webdata.close()
    
    with open('expd9wdata.xml', mode = 'w', encoding='utf-8') as f:
        f.write(webxml)
    print('저장성공')
except Exception as e:
    print('err :' + str(e))
'''
# 저장된 파일로 XML 문서 파싱
xmlFile = etree.parse('expd9wdata.xml')
root = xmlFile.getroot()
print(root.tag)
print(root[0].tag)

children = root.findall("{current}weather")         # root.findall(root[0].tag)
print(children)


for it in children:
    y = it.get('year')
    m = it.get('month')
    d = it.get('day')
    h = it.get('hour')
    print(y+'년'+m+'월'+d+'일'+h+'시 현재')
    
datas = []
for child in root:
    print(child.tag)        #{current}weather
    for it in child:
        print(it.tag)           #{current}local
        local_name = it.text
        re_ta = it.get('ta')
        re_desc = it.get('desc')
        #print(local_name, re_ta, re_desc)
        datas += [[local_name,re_ta,re_desc]]
        
#print(datas)
from pandas import DataFrame
df = DataFrame(datas, columns=['지역','온도','상태'])
print(df)
print(df.head())

print('-----------------------------------------------')
# 방법2 : 웹문서를 읽어 바로 파싱해서 처리
webdata2 = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')

xmlfile1 = etree.parse(webdata2)
root1 = xmlfile1.getroot()
ndate = list(root1[0].attrib.values())
print(ndate[0] + '년'+ndate[1]+'월'+ndate[2]+'일'+ndate[3]+'시  현재')

for child in root:
    for subchild in child:
        print(subchild.text +":", subchild.get('ta'))
    
    