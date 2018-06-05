import os

a=os.path.exists("./examples/csv/test.csv")
print(a)

'''
import csv

f=open('./examples/MyRecordedMouseData.csv','r')
#f = open('./examples/test.csv', 'r')

reader = csv.reader(f)
header = next(reader)
for row in reader:
    print (row)

f.close()

'''
import numpy as np

data = np.loadtxt('./examples/csv/test.csv', delimiter=',', dtype='int')
list=data.tolist()
print(type(data))
print(type(list))

for i in range(len(list)):
    print (list[i])
