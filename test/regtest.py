import re

content = 'hello 123456 word'

res = re.match('^hello\s(\d+)',content)
print(res)
print(res.group())
print(res.group(1))


res1 = re.sub('\d+', '',content)
print(res1)