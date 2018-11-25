# mongodb 数据库存储
# 
# 链接数据库

import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# db= client['test']

# 指定集合
collection = db.students
# collection = db['students']

# 插入数据
student = {
  'id': '2018111801',
  'name': 'johns',
  'age': 23,
  'gender': 'male'
}

# insert is deprecated. Use insert_one or insert_many instead.
result = collection.insert_one(student)
print(result)



## 查询

# result = collection.find_one({'name':'john'})
result = collection.find({'name':'john'})

# 年龄大于 20 
result = collection.find({'age':{'$gt':20}})

# 正则匹配,查询名字以 M 开头的数据
result = collection.find({'name':{'$regex': '^M.*'}})

# 计数
result = collection.find({'name':'john'}).count()

# 排序 sort
result = collection.find().sort('name',pymongo.ASCENDING)

# 偏移  skip() 偏移几个位置
result = collection.find().sort('name',pymongo.ASCENDING).skip(2)

# 还可以用 limit() 指定要取的结果个数
result = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)

print(type(result))
print(result)


# 更新

condition = {'name': 'johns'}
student = collection.find_one(condition)

student['age'] = 42

# Use replace_one, update_one or update_many instead.
# result = collection.update_one(condition,student)

# 使用 $set 更新
result = collection.update_one(condition,{'$set': student})
print(result)


# 删除
#  remove is deprecated. Use delete_one or delete_many instead.
result = collection.remove({'name': 'john'})
print(result)