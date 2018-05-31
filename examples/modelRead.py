from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model ,load_model
import readCsvData as csv

from keras import optimizers

import numpy as np
#import readCsvData as csv

import os

path=os.path.exists("../examples/weights/weight_10000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
#model=load_model("../examples/weights/weight_10000.h5")
model=load_model("../examples/0531weight/weight_60000.h5")

batch_size=20
data_dim=2
timesteps = 20
epoch=1000

csv.setTimeSteps(timesteps)
X,Y=csv.makeData()

learningNum=60
while(True):
    model.fit(X, Y, epochs=epoch, batch_size=300)

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
