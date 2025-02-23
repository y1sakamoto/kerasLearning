from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers

import numpy as np
import sys
import readCsvData as csv


import os

path=os.path.exists("./examples/weight_100000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
model=load_model("./singleMouseArrayOut/0606weight/weight_24000.h5")
#model=load_model("../../examples/weight_50000.h5")




data_dim=2
inputSteps = 200
outputSteps = 50

epoch=5000
Interval_prediction=0


###########################################
##############Making Data##################
#X,Y=csv.makeData()
X,Y=csv.getShuffleData(inputSteps,outputSteps,Interval_prediction)


while(True):

    x,y=csv.getRandom(X,Y)
    prediction=model.predict(x,batch_size=64)
    #print('x')

    #print(x)
    #print('prediction')

    #print(prediction)
    #print('y-prediction')

    print(y-prediction)
