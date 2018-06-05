from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers
from time import sleep

import numpy as np
import oscToKeras as osc
#import readCsvData as csv


import os
path=os.path.exists("./examples/weight_2000.h5")
model=load_model("../examples/weight_30000.h5")

#print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")

batch_size=20
data_dim=2
timesteps = 50
epoch=1000
osc.set()
osc.setTimeSteps(timesteps)

counter=0
while(True):
    counter+=1
    x=osc.getArrayInput()
    print(x)
    if counter==3:
        counter=0
        prediction=model.predict(x,batch_size=64)
        osc.sendArray(prediction)
    osc.loop()
    #sleep(0.033)
    #print(y)
    #print(prediction)
    #print(y-prediction)
