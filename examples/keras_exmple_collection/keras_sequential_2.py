from keras.layers import Input, Dense
from keras.models import Model
import numpy as np

# This returns a tensor
inputs = Input(shape=(64,))

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(1, activation='softmax')(x)

# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              #loss='categorical_crossentropy',
              metrics=['accuracy'])
#model.fit(data, labels)  # starts training

batch_size=64
data_dim = 64
timesteps = 8
num_classes = 1

# Generate dummy training data
x_train = np.random.random((10,64))
y_train = np.random.random((10))
print(type(x_train))
print(x_train.size)

# Generate dummy validation data
#x_val = np.random.random((batch_size * 3, timesteps, data_dim))
#y_val = np.random.random((3, num_classes))

model.fit(x_train, y_train)  # starts training


#model.fit(x_train, y_train,
#          batch_size=batch_size, epochs=5, shuffle=False,
#          validation_data=(x_val, y_val))
