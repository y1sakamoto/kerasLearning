from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model ,load_model
import readCsvData as csv

from keras import optimizers

import numpy as np
#import readCsvData as csv
import config as c

import os

path=os.path.exists("../kerasTest/weight_14000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")

model=load_model("./weight_130000.h5")



inputDataDim=c.inputDataDim
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

learningNum=25
print(model.summary())
while(True):
    model.fit(X, Y, epochs=epoch, batch_size=1000)




    fileName='weight_%i.h5' % (learningNum*epoch)
    print(fileName)
    learningNum+=1
    model.save(fileName)
    x,y=csv.getRandom(X,Y)
    prediction=model.predict(x)
    print(y)
    print(prediction)

    print(y-prediction)

#model.fit(Data_X, Data_Y)  # starts training
print(model.summary())
