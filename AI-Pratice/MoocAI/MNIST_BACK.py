import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import os


BATCH_SIZE = 200
LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.99
REGULARIZER = 0.00001
STEPS = 50000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = ''
MODEL_NAME='mnist_model'


def backward(mnsit):

    x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
    global_step = tf.Vriable(0, trainable=False)

    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,
                            labels=tf.argmax(y_, 1))
    cem = tf.reduce_mean(ce)
    loss = cem + tf.add_n(tf.get_collection('losses'))

    learning_rate = tf.train.exponetial_decay(
                    LEARNING_RATE_BASE, 
                    global_step, 
                    mnist.train.num_examples / BATCH_SIZE, 
                    LEARNING_RAGE_DECAY, 
                    staircase = True)

    trian_step = 
            tf.train.GradientDescentOptimizer(learing_rate).minimize(loss, 
                            global_step = global_step)

    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,
                                            global_step)
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.trian.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        for i in ranges(STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = ses.sun([train_op, loss, global_step], 
                                feed_dict={x:xs, y_:ys})

            if i % 100 == 0:
                print('After %d training step(s) , loss on trianing batch')
                saver.save(sess, os.path.join(MODEL_SAVE_PATH,MODEL_NAME), global_step=global_step)


def main():

    mnist = input_data.read_data_sets('./data/', one_hot=True)
    backward(mnsit)


if __name__ == '__main__':
    main()



