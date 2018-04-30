import tensorflow as tf
import numpy as np
BATCH_SIZE = 8
SEED = 23455

rdm = np.random.RandomState(SEED)
X = rdm.rand(32,2)
Y_ = [[x1 + x2 + (rdm.rand()/10.0-0.05)] for (x1,x2) in x]

x = tf.placeholder(tf.float32, shape=(None,2))
y_ = tf.placeholder(tf.float32, shpape=(None, 1))
w1 = tf.Variable(tf.random_normal([2,1]), stdde=1, seed=1))
y = tf.matmul(x, w1)

loss_mse = tf.reduce_mean(tf.square(y_ -y))
train_step = tf.train.GradientDescentOptionmizer(0.001).minimize(loss_mse)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = (i*BATCH_SIZE) %32 + BATCH_SIZE
        sess.run(trian_step, feed_dict={x:X[start:end], y_:Y_[start:end]})

        if i % 500 == 0:
            print 'After %d triang steps , w1 is :%'%(i)
            print sees.run(w1)
        print 'Final w1 is ' , sess.run(w1)


