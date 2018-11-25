import csv

# with open('data.csv','w') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['id','name','age'])
#   writer.writerow(['1001','mike',12])

with open('data.csv','w') as csvfile:
  filenames = ['id','name','age']
  writer = csv.DictWriter(csvfile,filenames=filenames)
  writer.writeheader()
  writer.writerow(['id','name','age'])
  writer.writerow(['1001','mike',12])


## 读取

with open('data.csv','r',encoding='utf-8') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(row)