from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

browser = webdriver.Chrome()

wait = WebDriverWait(browser,10)
KETWORD = 'ipad'

# taobao 搜索页
def index_page(page):
  """
  抓取索引页
  ：page: 页码
  """
  print('正在爬取第', page , '页')
  try:
    browser.get('https://s.taobao.com/search?q=' + quote(KETWORD))
    if page > 1:
      input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form> input')))
      submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form >span.btn.J_Submit')))
      
      input.clear()
      input.send_keys(page)
      submit.click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
    get_products() 
      # print(browser.current_url)
      # print(browser.get_cookies())
      # print(browser.page_source)
  except TimeoutException:
    index_page(page)
  # finally:
  #   browser.close()

# 获取商品列表
def get_products():
  html = browser.page_source
  doc = pq(html)
  items = doc('#mainsrp-itemlist .items .item').items()
  for item in items:
    product = {
      'image': item.find('.pie .img').attr('data-src'),
      'price': item. find('.price').text(),
      'deal': item.find('.deal-cnt').text(),
      'title': item. ind('.title').text(),
      'shop': item.find('.shop').text(),
      'location': item.find('.location').text()
    }
    print(product)
    save_to_mongo(product)

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)

# 指定数据库
db = client[MONGO_DB]

def save_to_mongo(result):
  try:
    if db[MONGO_COLLECTION].insert(result):
      print('存储到 MongoDB 成功')
  except Exception: 
    print('存储量 MongoDB 失败')


MAX_PAGE = 2

def main():
  for i in range(1,MAX_PAGE):
    index_page(i)

if __name__ == '__main__':
  main()
