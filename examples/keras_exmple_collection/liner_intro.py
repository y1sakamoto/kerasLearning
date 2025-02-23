##https://qiita.com/jkkch/items/70fc223f2871ca5e691c

import tensorflow as tf
import numpy as np

# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32)
#print('x_data:',end=' ')
#print(x_data)
y_data = x_data * 10 + 0.3

#y_data = np.random.rand(100).astype(np.float32)
#print('y_data:',end=' ')
#print(y_data)

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but Tensorflow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
for i in range(y.shape[0]):
    print(y[i])

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(2000):
    if step % 20 == 0:
        print((step, sess.run(W), sess.run(b)))
        print(loss)

    sess.run(train)
