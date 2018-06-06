import os

a=os.path.exists("./singleMouseTest/csv/MyRecordedMouseData.csv")

#a=os.path.exists("MyRecordedMouseData.csv")

print(a)



import numpy as np
import random



def getListFromCsv():
    data = np.loadtxt('./singleMouseTest/csv/MyRecordedMouseData.csv', delimiter=',', dtype='float')
    #data = np.array(range(200)).reshape(100,2)

    print('datasahpe:[%d][%d]' % (data.shape[0],data.shape[1]))
    list = data.tolist()
    dataSize0=data.shape[0]
    return list,data.shape[0]



def makeData(inputSteps=30,outputSteps=30,Interval_prediction=20):
    input=[]
    output=[]
    list,dataShape=getListFromCsv()
    _MaxNum=dataShape-inputSteps-Interval_prediction-outputSteps
    #_MaxNum=10
    for i in range(_MaxNum):
        list_input=[]
        list_output=[]

        for j in range(inputSteps):
            list_input.append(list[i+j])
        input.append(list_input)

        for j in range(outputSteps):
            list_output.append(list[i+j+inputSteps+Interval_prediction])
        output.append(list_output)


    np_Input=np.array(input)
    np_Outpuy=np.array(output)
    return np_Input,np_Outpuy
    pass

def getShuffleData(inputSteps=30,outputSteps=30,Interval_prediction=20):
    input,output=makeData(inputSteps,outputSteps,Interval_prediction)
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


#a,b=makeData(inputSteps=5,outputSteps=5,Interval_prediction=5)

#a,b=getShuffleData(inputSteps=5,outputSteps=5,Interval_prediction=1)

#print(a[0])
#print(b[0])

#print(a.shape)
#print(b.shape)

#print(type(a))
#print(type(b))
