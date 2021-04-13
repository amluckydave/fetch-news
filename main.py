import requests
import re

msgList_School = ['No Updates']
msgList_Department = ['No Updates']
schSign = 0
departSign = 0

timeStr_School = "03-27"
timeStr_Department = "2021-03-31"
key = input()

headers0 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'referer': r'https://aerospace.xmu.edu.cn/index.htm',
    'Upgrade-Insecure-Requests': '1'}

url0 = 'https://aerospace.xmu.edu.cn/jwxx/yjsjw.htm'
data0 = requests.get(url0, headers=headers0).content.decode('utf-8')

pattern0 = re.compile(r'<span>(.*)</span>')
result0 = (re.findall(pattern0, data0))[1]

if result0 != timeStr_School:
    schSign = 1
    pattern_title0 = re.compile(r'<span>' + result0 + '</span>.*>(.+)</a>')
    msgList_School = (re.findall(pattern_title0, data0))

# -----------------------------------------------------------------
url1 = 'https://jdx.xmu.edu.cn/xwgg/tzgg.htm'
data1 = (requests.get(url1, headers=headers0).content.decode('utf-8'))

pattern1 = re.compile(r'\w{4}-\w{2}-\w{2}')
result1 = (re.findall(pattern1, data1))
newsNum = result1.count(result1[0])

if result1[0] != timeStr_Department:
    departSign = 1
    pattern_title1 = re.compile('<a.*?href=.*?>(.{5,})(?=</a>\r\n)')
    msgList_Department = (re.findall(pattern_title1, data1))[:newsNum]

# --------------------------------------------

desp = f"""
------
### ✨学院新闻：
```
{msgList_School}
```
### 🚀系新闻:
```
{msgList_Department}
```
"""

if schSign or departSign:
    requests.post('https://sc.ftqq.com/' + key + '.send', data={
        'text': 'News Updates',
        'desp': desp
    })
