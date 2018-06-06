from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np

data = np.array([[i] for i in range(50)])
targets = np.array([[i] for i in range(50)])



data_gen = TimeseriesGenerator(data, targets,
                               length=2, sampling_rate=1,
                               batch_size=10)


#assert len(data_gen) == 20

batch_0 = data_gen[0]
x, y = batch_0


print(x)
print(y)


#assert np.array_equal(x,
#                      np.array([[[0], [2], [4], [6], [8]],
#                                [[1], [3], [5], [7], [9]]]))
##                    np.array([[10], [11]]))
