from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model ,load_model
import readCsvData as csv

from keras import optimizers

import numpy as np
#import readCsvData as csv

import os

path=os.path.exists("./singleMouseTest/weight/0530weight/weight_4000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")

model=load_model("./singleMouseArrayOut/0606weight/weight_10000.h5")


data_dim=2
inputSteps = 200
outputSteps = 50

epoch=2000
Interval_prediction=0


###########################################
##############Making Data##################
#X,Y=csv.makeData()
X,Y=csv.getShuffleData(inputSteps,outputSteps,Interval_prediction)

learningNum=6
print(model.summary())
while(True):
    model.fit(X, Y, epochs=epoch, batch_size=500)




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
