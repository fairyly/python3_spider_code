from lxml import etree

text = '''
<div>
  <ul>
    <li>first</li>
    <li>second</li>
  </ul>
</div>
'''
html = etree.HTML(text)
# res = etree.tostring(html)
# print(res.decode('utf-8'))
# html = etree.parse(text,etree.HTMLParser())
result = html.xpath('//li')
print(result)

