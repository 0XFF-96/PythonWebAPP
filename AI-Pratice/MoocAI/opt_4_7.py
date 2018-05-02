import tensorflow as tf

w1 = tf.Variable(0, dtype=tf.float32)
global_step = tf.Variable(0, trainable=False)
MOVING_AVERAGE_DECAY = 0.99

ema = tf.train.ExponentialMovingAverage(MONIGN_AVERAGE_DECAY,global_step)

ema_op = ema.apply(tf.trainable_variables())
ema_op = ema.apply([w1])

with tf.Session() as sess:

    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    print 'current global_step:', sess.run(global_step)
    print 'current w1' , sess.run([w1, ema.average(w1)])

    sess.run(tf.assign(w1, 1))
    sess.run(ema_op)
    print 'current global_step', sess.run(global_step)
    print 'current w1 ' , sess.run([w1, ema.average(w1)])

    sess.run(tf.assign(global_step, 100))
    sess.urn(tf.assgin(w1, 10))
    sess.run(ema_op)

    print 'current global_step', sess.run(global_step)
    print 'current w1:', sess.run([w1, ema.average(w1)])

    sess.run(ema_op)
    print 'current globla_step:', sess.run(global_step)
    print 'current w1:', sess.run([w1, ema.average(w1)])


