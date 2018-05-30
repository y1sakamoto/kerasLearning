import numpy as np
import random

arr = np.empty((0,3), int)
arr = np.append(arr, np.array([[1, 2, 3]]), axis=0)
arr = np.append(arr, np.array([[4, 5, 0]]), axis=0)
print(arr)


def f (_arr:np.empty((0,3), int)):
    _arr=np.append(_arr, np.array([[1, 2, 3]]), axis=0)
    print(_arr)
    print(np.may_share_memory(_arr,arr))
f(arr)
print(arr)


def back ():
    _arrA=np.empty((0,3), int)
    _arrA=np.append(_arrA, np.array([[1, 2, 3]]), axis=0)
    _arrA=np.append(_arrA, np.array([[4, 5, 6]]), axis=0)
    _arrA=np.append(_arrA, np.array([[7, 8, 9]]), axis=0)

    _arrB=np.empty((0,2), int)
    _arrB=np.append(_arrB, np.array([[1, 2]]), axis=0)
    _arrB=np.append(_arrB, np.array([[3, 4]]), axis=0)
    _arrB=np.append(_arrB, np.array([[5, 6]]), axis=0)

    return _arrA,_arrB

a,b=back()
print(a)
print(b)


batch_size=20
data_dim=2
timesteps = 20

a=np.arange(50)
#print(a)
b = np.resize(a, (10, 2))
#print(b)
b[np.newaxis,:,:]
#print(b)

x=np.arange(15).reshape(3,5)
_x=x[np.newaxis,:,:]
print(_x)

def getRandom(x,y):
    numRandom=random.randrange(y.shape[0])
    rand_x=x[numRandom]
    rand_y=y[numRandom]
    print(numRandom)
    return rand_x,rand_y

i,j=back()
s,t=getRandom(i,j)
print (i)
print (s)
print (j)
print (t)


arr = np.empty((0,3), int)
arr = np.append(arr, np.array([[1, 2, 3]]), axis=0)
arr = np.append(arr, np.array([[4, 5, 0]]), axis=0)

arr2 = np.empty((0,3), int)
arr2 = np.append(arr2, np.array([[1, 1, 1]]), axis=0)
arr2 = np.append(arr2, np.array([[2, 2, 2]]), axis=0)
print(arr-arr2)

X=np.random.random((batch_size,timesteps,data_dim))
Y=np.random.random((batch_size,data_dim))




print('datasahpe:[%d][%d]' % (X.shape[0],Y.shape[1]))
