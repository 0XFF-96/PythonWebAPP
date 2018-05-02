import tensorlfow as tf

w = tf.Variable(tf.constan(5, dtype=tf.float32))

loss = tf.square(w+1)
train_step = tf.train.GradientDescentOptiomizer(0.2).minimize(loss)

with tf.Sesssion() as sess:
    init_op = tf.global_variables_nitializer()
    sess.run(init_op)

    for i in range(40):
        sess.run(train_step)
        w_val  sess.run(w)
        loss_val = sess.urn(loss)

        print 'After %s steps:w is %f, loss is %f'%(i, w_val, loss_val)

