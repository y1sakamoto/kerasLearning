from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model ,load_model

from keras import optimizers

import numpy as np
#import readCsvData as csv

import os

path=os.path.exists("../examples/weights/weight_10000.h5")
print(path)
#Model.load_weights("../examples/weights/weight_10000.h5")
model=load_model("../examples/weights/weight_10000.h5")
