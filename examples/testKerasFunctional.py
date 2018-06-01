from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D,Activation
from keras.models import Model
from keras import optimizers

import numpy as np
import readCsvData as csv



data_dim=2
timesteps = 20
epoch=5000
Interval_prediction=20


csv.setTimeSteps(timesteps)
csv.setIntervalPrediction(Interval_prediction)

###########################################
##############Making Data##################
#X,Y=csv.makeData()
X,Y=csv.getShuffleData()
###########################################
#batch_size=20
#X=np.random.random((batch_size,timesteps,data_dim))
#Y=np.random.random((batch_size,data_dim))

print(X.shape)
print(Y.shape)



# This returns a tensor
inputs = Input(shape=(timesteps,data_dim))
#inputs = Input(shape=(data_dim,))
# a layer instance is callable on a tensor, and returns a tensor
x = Dense(20, activation='relu')(inputs)
x = Dense(20, activation='relu')(x)

x = Flatten()(x)

#x = Conv1D(64, 2,activation='relu')(x)
#x = Conv1D(64, 2)(x)
x = Dense(500, activation='relu')(x)
x = Dense(500, activation='relu')(x)
x = Dense(500, activation='relu')(x)
out = Dense(500, activation='relu')(x)


predictions = Dense(data_dim, activation='sigmoid')(out)

# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=predictions)
#model.compile(optimizer='rmsprop',
#              loss='categorical_crossentropy',
#              metrics=['accuracy'])
print(model.summary())
#opt=optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
#model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])

model.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])




learningNum=1
while(True):
    model.fit(X, Y, epochs=epoch, batch_size=10000)

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
