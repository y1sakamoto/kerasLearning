import numpy as np

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
    _arrB=np.empty((0,3), int)
    _arrB=np.append(_arrB, np.array([[2, 3, 4]]), axis=0)
    return _arrA,_arrB

a,b=back()
print(a)
print(b)
