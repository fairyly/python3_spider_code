import pymysql

db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor = db.cursor()

# 创建数据库
# cursor.execute('select version()')
# data = cursor.fetchone()
# print('database version:',data)
# cursor.execute('create database spiders default character set utf8')
# db.close()


# 创建表
# sql = 'create table if not exists students(id varchar(255) not null,name varchar(255) not null,age int not null,primary key (id))'

# 插入数据
# id="20181118"
# name="fairy"
# age= 27
# sql = 'insert into students(id,name,age) values(%s, %s ,%s)'

# try:
#   cursor.execute(sql,(id, name, age))
#   db.commit()
# except:
#   db.rollback()
# db.close()


# data = {
#   'id': '20181116',
#   'name': 'fairy123',
#   'age': 2999
# }

# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)

# try:
#   if cursor.execute(sql,tuple(data.values())):
#     print('ok')
#     db.commit()
# except:
#   print('fail')
#   db.rollback()
# db.close()
# 
# 
# 

#更新数据
# sql = 'update students set age = %s where name = %s'

# try:
#   if cursor.execute(sql,(25,'fairy')):
#     print('ok')
#     db.commit()
# except:
#   print('fail')
#   db.rollback()
# db.close()




# 重复数据去重
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(table=table, keys=keys, values=values)

# update = ', '.join([" {key} = %s".format(key=key) for key in data])

# sql += update

# try:
#   if cursor.execute(sql,tuple(data.values())*2):
#     print('ok')
#     db.commit()
# except:
#   print('fail')
#   db.rollback()
# db.close()

# 删除数据

# table = 'students'
# condition = 'age > 27'

# sql = 'delete from {table} where {condition}'.format(table=table,condition=condition)

# try:
#   cursor.execute(sql)
#   print('ok')
#   db.commit()
# except:
#   print('fail')
#   db.rollback()
# db.close()


# 查询数据

sql = 'select * from students where age > 20'

try:
  cursor.execute(sql)
  print('ok',cursor.rowcount)

  one = cursor.fetchone()
  print('one',one)

  all = cursor.fetchall()
  print('all',all,type(all))
  # db.commit()  # 不需要 commit() 方法
except:
  print('fail')
  db.rollback()
db.close()
