from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers

import numpy as np
import sys
import readCsvData as csv


import os

path=os.path.exists("./singleMouseTest/weight/0604weight/weight_5000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
model=load_model("./singleMouseArrayOut/0606weight/weight_50000.h5")




data_dim=2
inputSteps = 50
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
    #print(y)
    #print(prediction)
    print(y-prediction)
