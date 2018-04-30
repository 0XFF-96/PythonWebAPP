
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

w = tf.Variable(tf.zeros[784, 10])
b = tf.Variable(tf.zeros[10])
prediction = tf.nn.softmax(tf.matmul(x, W)+b)

loss = tf.reduce_mean(tf.square(y-predition))
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.global_variables_initialzer()

correct_prediction = 
                tf.equal(tf.argmx(y, 1).tf.argmax(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predciton, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(train_step, feed_dict={x:batch_xs, y:batch_ys})
    acc = sess.run(accuracy, feed_dict={x:mnist.test.images, y:mnist.test.labels})
    print('Iter', +str(epoch) + 'Testing Accuract' + str(acccC))



