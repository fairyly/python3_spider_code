import json

str = '''
[
  {
    "name": "jonh",
    "sex": "male"
  }
]
'''

data = json.loads(str)
print(data)
print(type(data))


## 从json 文本读取内容
with open('data.json','r') as file:
  str = file.read()
  data = json.loads(str)
  print(data)


with open('data.json','w') as file:
  file.write(json.dumps(str))