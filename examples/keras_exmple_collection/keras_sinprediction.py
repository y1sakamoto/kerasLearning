import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense, Activation

def sin2p(x, t=100):
    return np.sin(2.0 * np.pi * x / t) # sin(2πx/t) t = 周期

def sindata(t=100, cycle=2):
    x = np.arange(0, cycle*t) # 0 から cycle * t 未満の数
    return sin2p(x)


def noisy(Y, noise_range=(-0.05, 0.05)):
    noise = np.random.uniform(noise_range[0], noise_range[1], size=Y.shape)
    return Y + noise



# データ準備

np.random.seed(0)

rawdata = noisy(sindata(100,2), (-0.05, 0.05))
inputlen = 20

input=[]
target=[]
for i in range(0, len(rawdata) - inputlen):
    input.append( rawdata[i:i+inputlen] )
    target.append( rawdata[i+inputlen] )

X = np.array(input).reshape(len(input), inputlen, 1)
Y = np.array(target).reshape(len(input), 1)
x, val_x, y, val_y = train_test_split(X, Y, test_size=int(len(X) * 0.2), shuffle=False)

# トレーニング

n_in = 1
n_hidden = 20
n_out = 1
epochs = 10
batch_size = 10

model=Sequential()
model.add(SimpleRNN(n_hidden, input_shape=(inputlen, n_in), kernel_initializer='random_normal'))
model.add(Dense(n_out, kernel_initializer='random_normal'))
model.add(Activation('linear'))
model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.01, beta_1=0.9, beta_2=0.999))
model.fit(x, y, batch_size=batch_size, epochs=epochs, validation_data=(val_x, val_y))

# 予測

in_ = x[:1] # x の先頭 (1,20,1) 配列
predicted = [None for _ in range(inputlen)]
for _ in range(len(rawdata) - inputlen):
    out_ = model.predict(in_) # 予測した値 out_ は (1,1) 配列
    in_ = np.concatenate( (in_.reshape(inputlen, n_in)[1:], out_), axis=0 ).reshape(1, inputlen, n_in)
    predicted.append(out_.reshape(-1))
print(predicted)
