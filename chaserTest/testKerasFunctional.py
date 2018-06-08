from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation,LSTM,Reshape,MaxPooling1D,Cropping1D
from keras.models import Model
from keras import optimizers

import numpy as np
import readCsvData as csv
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
#X,Y=csv.makeData(inputSteps,outputSteps,Interval_prediction,Interval_steps)
X,Y=csv.getShuffleData(inputSteps,outputSteps,Interval_prediction,Interval_steps,getDataRatio)

#X,Y=csv.getShuffleData()
###########################################
#batch_size=20
#X=np.random.random((batch_size,timesteps,data_dim))
#Y=np.random.random((batch_size,data_dim))

print(X.shape)
print(Y.shape)



# This returns a tensor
inputs = Input(shape=(inputSteps,input_data_dim))
#inputs = Input(shape=(data_dim,))
# a layer instance is callable on a tensor, and returns a tensor

#x = Dense(10, activation='relu')(inputs)

#x = Conv1D(10,kernel_size=20,activation='relu')(inputs)
#x = Dense(30, activation='relu')(x)

#x = Conv1D(10,kernel_size=20,activation='relu')(x)
#x = Dense(30, activation='relu')(x)
x = Conv1D(4,kernel_size=3,activation='relu')(inputs)
x = Conv1D(4,kernel_size=3,activation='relu')(x)
x = MaxPooling1D(pool_size=2)(x)
x = Conv1D(4,kernel_size=3,activation='relu')(x)
x = Conv1D(4,kernel_size=3,activation='relu')(x)
x = MaxPooling1D(pool_size=2)(x)
x = Conv1D(2,kernel_size=3,activation='relu')(x)
x = Conv1D(2,kernel_size=3,activation='relu')(x)
x = MaxPooling1D(pool_size=2)(x)


#x = Conv1D(100,kernel_size=1,activation='relu')(inputs)

#x = Dense(120, activation='relu')(inputs)

#x = Reshape((50, 2))(inputs)

#x = Conv1D(64, 2)(x)

#x = Dense(120, activation='relu')(inputs)
x = Flatten()(x)
#x = Dense(160, activation='relu')(x)
#x = Dense(160, activation='relu')(x)
x = Dense(32, activation='relu')(x)
x = Dense(32, activation='relu')(x)
x = Dense(32, activation='relu')(x)
x = Dense(32, activation='relu')(x)

x = Dense(2, activation='relu')(x)

out = Reshape((outputSteps, output_data_dim))(x)


predictions = Dense(output_data_dim, activation='sigmoid')(out)

# This creates a model that includes

# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=predictions)
#model.compile(optimizer='rmsprop',
#              loss='categorical_crossentropy',
#              metrics=['accuracy'])
print(model.summary())
#opt=optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
#model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])

model.compile(loss="mean_absolute_percentage_error", optimizer="adam", metrics=["accuracy"])




learningNum=1
while(True):
    model.fit(X, Y, epochs=epoch, batch_size=10,validation_split=0.1)

    fileName='weight_%i.h5' % (learningNum*epoch)
    print(fileName)
    learningNum+=1
    model.save(fileName)
    x,y=csv.getRandom(X,Y)
    prediction=model.predict(x)
    #print(y)
    #print(prediction)

    print(y-prediction)

#model.fit(Data_X, Data_Y)  # starts training
print(model.summary())
