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
X = np.array(X_list)
Y = np.array(Y_list)

# モデルを生成する
model = Sequential()
# 全結合層(2層->10層)
model.add(Dense(input_dim=2, output_dim=10))
# 活性化関数(tanh関数)
model.add(Activation("relu"))

model.add(Dense(input_dim=10, output_dim=100))
model.add(Activation("relu"))
model.add(Dense(input_dim=100, output_dim=100))
model.add(Activation("relu"))
model.add(Dense(input_dim=100, output_dim=10))
model.add(Activation("relu"))
model.add(Dense(input_dim=10, output_dim=10))
model.add(Activation("relu"))

# 全結合層(10層->2層)
model.add(Dense(output_dim=1))
# 活性化関数(sigmoid関数)
model.add(Activation("sigmoid"))

# モデルをコンパイル
model.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])
# 学習を実行
model.fit(X, Y, nb_epoch=3000, batch_size=32)

# 学習したモデルで予測する。
# [1,1]=> 1
# [0,0]=> 0
# という予測になるはず...
results = model.predict_proba(np.array([[1, 1], [0, 0]]))
# 結果を表示
print("Predict:\n", results)
