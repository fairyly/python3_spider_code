from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
   'Referer': 'http://httpbin.org',
   'Connection': 'keep-alive'
}
dict = {
  'name': 'grame'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url, data=data, headers=headers,method='POST')
page = request.urlopen(req).read()
page = page.decode('utf-8')
print(page)