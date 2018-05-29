#####https://qiita.com/hiroeorz@github/items/33b85529be0829f34973

from keras.models import Sequential
from keras.layers import Activation, Dense
import numpy as np

# 学習のためのデータ。
# 今回、Xは[0,0]または[1,1]の2種類。
# Yは0または1の2種類
# X:[0,0] => Y:0
# X:[1,1] => Y:1
# という対応になっている
X_list = [[0, 0], [1, 1], [0, 0], [1, 1], [1, 1], [1, 1]]
Y_list = [   [0],    [1],    [0],    [1],    [1],    [1]]


# kerasのmodelに渡す前にX,Yをnumpyのarrayに変換する。
#X = np.array(X_list)
#Y = np.array(Y_list)

batch_size=64
data_dim=2
timesteps = 2


X=np.random.random((batch_size,data_dim))
Y=np.random.random((batch_size))
print(X.shape)
print(X)

print(Y.shape)

##random
##https://note.nkmk.me/python-numpy-random/
# モデルを生成する
model = Sequential()
# 全結合層(2層->10層)

#model.add(Conv1D(2, 2), activation='relu')
#model.add(Flatten())


model.add(Dense(input_shape=(2,), units=10))

#model.add(Dense(input_dim=2, output_dim=10))
# 活性化関数(tanh関数)
model.add(Activation("relu"))
model.add(Dense(input_dim=10, units=100))
model.add(Activation("relu"))
model.add(Dense(input_dim=100, units=100))
model.add(Activation("relu"))
model.add(Dense(input_dim=100, units=10))
model.add(Activation("relu"))
model.add(Dense(input_dim=10, units=10))
model.add(Activation("relu"))

# 全結合層(10層->2層)
model.add(Dense(units=1))
# 活性化関数(sigmoid関数)
model.add(Activation("sigmoid"))

# モデルをコンパイル
model.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])
# 学習を実行

model.fit(X, Y, epochs=30, batch_size=32)
print(model.summary())
# 学習したモデルで予測する。
# [1,1]=> 1
# [0,0]=> 0
# という予測になるはず...
results = model.predict_proba(np.array([[1, 1], [0, 0]]))
# 結果を表示
print("Predict:\n", results)
