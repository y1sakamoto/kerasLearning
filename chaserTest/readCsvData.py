import os

a=os.path.exists("./chaserTest/csv/MyRecordedMouseData.csv")

#a=os.path.exists("MyRecordedMouseData.csv")

print(a)



import numpy as np
import random



def getListFromCsv():
    data = np.loadtxt('./chaserTest/csv/MyRecordedMouseData.csv', delimiter=',', dtype='float')
    #data = np.array(range(200)).reshape(50,4)
    #data = np.linspace(0,1,20000).reshape(5000,4)
    print('datasahpe:[%d][%d]' % (data.shape[0],data.shape[1]))
    list = data.tolist()
    dataSize0=data.shape[0]
    return list,data.shape[0]



def makeData(inputSteps=20,outputSteps=1,Interval_prediction=20,Interval_steps=1):
    input=[]
    output=[]
    list,dataShape=getListFromCsv()
    _MaxNum=dataShape
    _MaxNum=_MaxNum-inputSteps*Interval_steps
    _MaxNum=_MaxNum-Interval_prediction
    _MaxNum=_MaxNum-outputSteps*Interval_steps

    #_MaxNum=10
    for i in range(_MaxNum):
        list_input=[]
        list_output=[]

        for j in range(inputSteps):
            _num=i+j*Interval_steps
            list_input.append(list[_num])
        input.append(list_input)

        for j in range(outputSteps):
            _num=i+j*Interval_steps+inputSteps*Interval_steps+Interval_prediction
            list_output.append(list[_num])
        output.append(list_output)


    np_Input=np.array(input)
    np_Output=np.array(output)

    ##############DELETE DIMENSION######################
    ##############DELETE DIMENSION######################
    #np_Input=np.delete(np_Input, [0,1], 2)
    #np_Output=np.delete(np_Output, [2,3], 2)
    np_Output=np.delete(np_Output, [2,3,4,5,6,7,8,9,10], 2)
    return np_Input,np_Output
    pass

def getShuffleData(inputSteps=20,outputSteps=1,Interval_prediction=20,Interval_steps=1,getDataRatio=0.5):
    input,output=makeData(inputSteps,outputSteps,Interval_prediction,Interval_steps)
    size=input.shape[0]
    print(size)
    numArray=np.arange(size)
    size=(int)(size*getDataRatio)
    numArray=np.random.permutation(numArray)
    numArray=np.random.choice(numArray,size,replace=False)
    #print(input[numArray])
    #_input=input[numArray]
    #_input=_input.transpose(0,2,1)
    #return input[numArray],output[numArray]
    return input[numArray],output[numArray]




def getRandom(x,y):
    numRandom=random.randrange(y.shape[0])
    rand_x=x[numRandom][np.newaxis,:]
    rand_y=y[numRandom][np.newaxis,:]
    print(numRandom)
    return rand_x,rand_y


#a,b=makeData(inputSteps=10,outputSteps=1,Interval_prediction=0,Interval_steps=1)

a,b=getShuffleData(inputSteps=5,outputSteps=5,Interval_prediction=1)

#date = np.linspace(0,1,20000).reshape(5000,4)
#print(date)
print(a.shape)
print(b.shape)

#a=a.transpose(0,2,1)
#print(a)
#print(b)

#print(a[0])
#print(b[0])

#print(a.shape)
#print(b.shape)

#print(type(a))
#print(type(b))
