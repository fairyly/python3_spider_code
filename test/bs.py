from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>hello</p>','lxml')
# print(soup.p.string)


html = """
<html>
<head>
  <title>test</title>
  <body>
    <div>
      <ul>
        <li>first</li>
        <li>second</li>
      </ul>
    </div>
  </body>
</head>
</html>

"""

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print("输出表签<title>及内部标签或内容:",soup.title)
print(soup.title.string)
print( "输出表签<body>及内部标签或内容:",soup.body)
print(soup.ul)