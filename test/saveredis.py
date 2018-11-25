# redis 储存

from redis import StrictRedis

# 连接 redis
redis = StrictRedis(host='localhost', port=6379, db=0, password='')

redis.set('name','test')
print(redis.get('name'))

# 使用 ConnectionPool 连接
# from redis import StrictRedis, ConnectionPool

# pool = ConnectionPool(host='localhost', port=6379, db=0, password='')
# redis = StrictRedis(connection_pool=pool)