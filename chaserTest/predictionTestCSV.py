from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers
import numpy as np
import sys
import readCsvData as csv


import os

path=os.path.exists("./examples/weight_140000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
model=load_model("./weight_150000.h5")
#model=load_model("../../examples/weight_50000.h5")
import config as c

input_data_dim=c.inputDataDim
output_data_dim=c.outputDataDim

inputSteps = c.inputSteps
outputSteps = c.outputSteps
epoch=c.epoch
Interval_prediction=c.Interval_prediction
Interval_steps=c.Interval_steps
getDataRatio=c.getDataRatio




###########################################
##############Making Data##################
#X,Y=csv.makeData()
X,Y=csv.getShuffleData(inputSteps,outputSteps,Interval_prediction,Interval_steps,getDataRatio)

while(True):

    x,y=csv.getRandom(X,Y)
    prediction=model.predict(x,batch_size=64)
    #print('x')

    #print(x)

    #print('y')

    #print(y)
    #print('prediction')
    #print(prediction)

    print(y-prediction)
