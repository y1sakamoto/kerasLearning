import os

a=os.path.exists("./examples/csv/MyRecordedMouseData.csv")
#a=os.path.exists("MyRecordedMouseData.csv")

print(a)



import numpy as np
import random

Timesteps=30
Interval_prediction=20

def getListFromCsv():
    data = np.loadtxt('../examples/csv/MyRecordedMouseData.csv', delimiter=',', dtype='float')
    print('datasahpe:[%d][%d]' % (data.shape[0],data.shape[1]))
    list = data.tolist()
    dataSize0=data.shape[0]
    return list,data.shape[0]


def setTimeSteps(_time):
    global Timesteps
    Timesteps=_time
    print(Timesteps)
    pass

def makeData():
    input=[]
    output=[]
    list,dataShape=getListFromCsv()
    _MaxNum=dataShape-Timesteps-Interval_prediction
    #_MaxNum=10
    for i in range(_MaxNum):
        array_data=[]
        output.append(list[i+Interval_prediction])
        for j in range(Timesteps):
            array_data.append(list[i+j])
        input.append(array_data)

    np_Input=np.array(input)
    np_Outpuy=np.array(output)
    return np_Input,np_Outpuy
    pass

def getShuffleData():
    input,output=makeData()
    size=input.shape[0]
    print(size)
    numArray=np.arange(size)
    size=(int)(size*0.5)
    numArray=np.random.permutation(numArray)
    numArray=np.random.choice(numArray,size,replace=False)
    #print(input[numArray])
    return input[numArray],output[numArray]



def getRandom(x,y):
    numRandom=random.randrange(y.shape[0])
    rand_x=x[numRandom][np.newaxis,:]
    rand_y=y[numRandom][np.newaxis,:]
    print(numRandom)
    return rand_x,rand_y


a,b=getShuffleData()
#a,b=makeData()
print(a)
print(b)

print(a.shape)
print(b.shape)

print(type(a))
print(type(b))
