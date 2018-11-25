from pyquery import PyQuery as pq


html = """
<html>
<head>
  <title>test</title>
  <body>
    <div class="contain">
      <ul class="list>
        <li>first</li>
        <li>second</li>
      </ul>
    </div>
  </body>
</head>
</html>

"""

#### 字符串初始化

# doc = pq(html)
# print(doc('li'))


### URL初始化

# doc = pq(url='https://cuiqingcai.com') #首先会请求 url,然后得到 HTML 内容完成初始化
# print(doc('title'))

# h和下面代码功能相同

# from pyquery import PyQuery as pq
# import requests

# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))


### 文件初始化
# doc = pq(filename='deml.html')
# print(doc('li'))





## css 选择器
doc = pq(html)
print(doc('.contain .list li'))
print(type(doc('.contain .list li')))


