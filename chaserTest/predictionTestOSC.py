from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model,load_model
from keras import optimizers
from time import sleep

import numpy as np
import oscToKeras as osc
#import readCsvData as csv


import os
path=os.path.exists("./chaserTest/0612interval2/weight_3000000.h5")
model=load_model("./0619/weight_130000.h5")

#print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
import config as c

input_data_dim=c.inputDataDim
input_steps = c.inputSteps






osc.set()
osc.setInputSize(input_steps,input_data_dim)

counter=0
while(True):
    counter+=1
    x=osc.getInput()
    #print(x)
    if counter==3:
        counter=0
        prediction=model.predict(x,batch_size=64)
        #print('x')
        #print(x)
        #print('prediction')

        #print(prediction)

        osc.sendArray(prediction)
    osc.loop()
    #sleep(0.033)
    #print(y)
    #print(prediction)
    #print(y-prediction)
