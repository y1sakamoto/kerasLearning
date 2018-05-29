###https://qiita.com/anafou/items/7c4d57a70efb42d105a5

import numpy as np
from keras.models import Model, Sequential
from keras.layers import Dense, Activation, Flatten, Conv1D, Input
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from keras.optimizers import Adam

def make_model(shape):
    input_layer = Input(batch_shape=shape)
    conv_1d_output_layer = Conv1D(FILTERS, KERNEL_SIZE, padding='same')(input_layer)
    flatten_output_layer = Flatten()(conv_1d_output_layer)
    prediction_result = Dense(1)(flatten_output_layer)

    model = Model(inputs=input_layer, outputs=prediction_result)
    return model



DATA_SAMPLES = 20
CHANNELS = 1
DATA_LENGTH = 10
KERNEL_SIZE = 3
FILTERS = 50

data = np.arange(DATA_SAMPLES * CHANNELS * DATA_LENGTH) * 10
data_channels_first = data.reshape(DATA_SAMPLES, CHANNELS, DATA_LENGTH)
data_channels_last = data_channels_first.transpose(0,2,1)

seikai = np.arange(DATA_SAMPLES).reshape(-1, 1)

print(data_channels_first.shape, data_channels_last.shape)


model_channels_first = make_model(shape=(None, CHANNELS, DATA_LENGTH))
model_channels_last  = make_model(shape=(None, DATA_LENGTH, CHANNELS))


model_channels_first.compile(optimizer="adam", loss='mse', metrics=['accuracy'])
print('channels first model')
print(model_channels_first.summary())

print('\n\n')

model_channels_last.compile(optimizer="adam", loss='mse', metrics=['accuracy'])
print('channels last model')
print(model_channels_last.summary())
