from keras.layers import Input, Dense,Flatten,Conv2D,Conv1D
from keras.models import Model
from keras import optimizers

import numpy as np
import readCsvData as csv

batch_size=10
data_dim=2
timesteps = 20

set()

csv.setTimeSteps(timesteps)
X,Y=csv.makeData()


#X=np.random.random((batch_size,timesteps,data_dim))

#Y=np.random.random((batch_size,data_dim))

print(X.shape)
print(Y.shape)



# This returns a tensor
inputs = Input(shape=(timesteps,data_dim))
#inputs = Input(shape=(data_dim,))

# a layer instance is callable on a tensor, and returns a tensor
#x = Dense(10, activation='relu')(inputs)
#x = Conv1D(64, 2)(inputs)
#x = Conv1D(64, 2)(x)
x = Dense(10, activation='relu')(inputs)
x = Flatten()(x)
x = Dense(64, activation='relu')(x)
x = Dense(64, activation='relu')(x)
x = Dense(64, activation='relu')(x)
x = Dense(10, activation='relu')(x)
out = Dense(2, activation='relu')(x)

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

model.fit(X, Y, epochs=3000, batch_size=32)

#model.fit(Data_X, Data_Y)  # starts training
print(model.summary())
