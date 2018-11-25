# ajax 模拟 获取搜素结果的数据
# -*- coding: UTF-8 -*-
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

from multiprocessing.pool import Pool

import os
from hashlib import md5

base_url = 'https://www.toutiao.com/search_content/?'

headers = {
  'Host': 'www.toutiao.com',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
  'Referer': 'https://www.toutiao.com/search/',
  'A-Requested-With': 'XMLHttpRequest'
}

# 
def get_pages():
  params = {
    'offset': 0,
    'format': 'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': 20,
    'cur_tab': 1,
    'from': 'search_tab'
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

def parse_page(json):
  if json:
    items = json.get('data')
    for item in items:
      if item.get('open_url'):
        articel = {}
        # print('666:',item)
        articel['tag_id'] = item.get('tag_id')
        articel['title'] = item.get('title')
        articel['media_name'] = item.get('media_name')
        articel['source_url'] = item.get('source_url')
        articel['read_count'] = item.get('read_count')
        yield articel

def get_image(json):
  if json:
    items = json.get('data')
    for item in items:
      if item.get('image_list'):
        title = item.get('title')
        images = item.get('image_list')
        for img in images:
          yield {
            'image': 'https:' + img.get('url'),
            'title': title
          }
      elif item.get('display'):
        # print(item.get('display').get('results'))
        title = item.get('id_str')
        images = item.get('display').get('results')
        itemss = item.get('display').get('items')
        if images:
          print('1')
          for img in images:
            yield {
              'image': img.get('img_url'),
              'title': title
            }
        elif itemss:
          print('2')
          for img in itemss:
            yield {
              'image': img.get('img'),
              'title': img.get('name'),
            }

# 保存图片到本地
def save_image(item):
  # 生成目录
  if not os.path.exists(item.get('title')):
    os.mkdir(item.get('title'))

  try:
    print(item.get('image'))
    response = requests.get(item.get('image'))
    if response.status_code == 200:
      # 保存图片
      file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
      if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
          f.write(response.content)
      else:
       print('already download:',file_path)
  except requests.ConnectionError as e:
    print('Error', e.args)

def main(offset):
  json = get_pages()
  for item in get_image(json):
    # print(item)
    save_image(item)


GROUP_START = 1
GROUP_END = 20
 
if __name__ == '__main__':

  # json = get_pages()
  # print(type(json),len(json))
  # results = parse_page(json)
  # for result in results:
  #   print(result)

  # for item in get_image(json):
  #   print(item)
  #   save_image(item)
  # 加入多线程
  pool = Pool()
  groups = ([x * 20 for x in range(GROUP_START,GROUP_END+1)])
  pool.map(main,groups)
  pool.close()
  pool.join()
 



