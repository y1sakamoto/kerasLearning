from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers

import numpy as np
import sys
import readCsvData as csv


import os

path=os.path.exists("../examples/weight_10000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
model=load_model("../examples/weight_10000.h5")


data_dim=2
timesteps = 50
epoch=5000
Interval_prediction=30


csv.setIntervalPrediction(Interval_prediction)

csv.setTimeSteps(timesteps)
X,Y=csv.makeData()

while(True):

    x,y=csv.getRandom(X,Y)
    prediction=model.predict(x,batch_size=64)
    print(y)
    print(prediction)
    print(y-prediction)
