# ajax 模拟 获取微博数据
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
  'Host': 'm.weibo.cn',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
  'Referer': 'https://m.weibo.cn/u/2830678474',
  'A-Requested-With': 'XMLHttpRequest'
}

# 
def get_pages(page):
  params = {
    'type': 'uid',
    'value': '2830678474',
    'containerid': '1076032830678474',
    'page': page
  }

  url = base_url + urlencode(params)
  try:
    response = requests.get(url,headers=headers)
     # print('ok:',response.json())
    if response.status_code == 200:
      # print('ok:',response.json())
      return response.json()
  except requests.ConnectionError as e:
    print('Error', e.args)

# 
def parse_page(json):
  if json:
    items = json.get('data').get('cards')
    for itemb in items:
      item = itemb.get('mblog')
      if item:
        weibo = {}
        # print('666:',item)
        weibo['id'] = item.get('id')
        weibo['text'] = pq(item.get('text')).text()
        weibo['attitudes'] = item.get('attitudes_count')
        weibo['comments'] = item.get('comments_count')
        weibo['reposts'] = item.get('reposts_count')
        yield weibo

# 保存数据库

client = MongoClient()
db = client['weibo']
collection = db['weibo']

def save_to_mongo(result):
  if collection.insert(result):
    print('save to Mongo')

if __name__ == '__main__':
  for page in range(1):
    json = get_pages(1)
    # print(json)
    results = parse_page(json)
    for result in results:
      print(result)
      # save_to_mongo(result)