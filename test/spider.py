import requests
import re
 
def get_one_page(url):
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
        }
    response = requests.get(url,headers = headers)
    if response.status_code ==200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
      yield {
        'index':item[0],
        'image':item[1],
        'title':item[2],
        'actor':item[3].strip()[3:],
        'time':item[4].strip()[5:],
        'score':item[5] + item[6]
      }
 
def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
      print(item)
    
main()
