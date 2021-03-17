import requests
import re
import datetime

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

msgList_School = ['No Updates']
msgList_Department = ['No Updates']
schSign = 0
departSign = 0
key = input()  # server酱推送

# ----------------------------------------------------------------
timeStr_School = bj_time.strftime("%m-%d")

headers0 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'referer': r'https://aerospace.xmu.edu.cn/index.htm',
    'Upgrade-Insecure-Requests': '1'}

url = 'https://aerospace.xmu.edu.cn/jwxx/yjsjw.htm'
data = requests.get(url, headers=headers0).content.decode('utf-8')

pattern0 = re.compile(r'<span>(.*)</span>')
result = (re.findall(pattern0, data))

if timeStr_School in result:
    schSign = 1
    pattern_title0 = re.compile(r'<span>' + timeStr_School + '</span>.*>(.+)</a>')
    msgList_School = (re.findall(pattern_title0, data))

# ----------------------------------------------------------------

timeStr_Department = bj_time.strftime("%Y-%m-%d")

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'referer': r'https://jdx.xmu.edu.cn/',
    'Upgrade-Insecure-Requests': '1'}

url = 'https://jdx.xmu.edu.cn/xwgg/tzgg.htm'
data = (requests.get(url, headers=headers1).content.decode('utf-8'))

pattern1 = re.compile(r'\w{4}-\w{2}-\w{2}')
result = (re.findall(pattern1, data))

cnt = result.count(timeStr_Department)
if cnt:
    departSign = 1
    pattern_title1 = re.compile('<a.*?href=.*?>(.{5,})(?=</a>\r\n)')
    # 此处不认 $, 只认 \r\n <linux下换行>
    result_title = (re.findall(pattern_title1, data))

    msgList_Department = result_title[:cnt]

# --------------------------------------------

desp = f"""
------
### 🚁Now：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### ✨学院新闻：
```
 New_Msg:{msgList_School}
```
### 🚀系新闻:
```
 New_Msg:{msgList_Department}
```
"""

if schSign or departSign:
    requests.post('https://sc.ftqq.com/' + key + '.send', data={
        'text': bj_time.strftime("%Y-%m-%d %H:%M:%S %p") + ' 航院 Updates',
        'desp': desp
    })
