import time 
import tensorflow as tf
from tensorflow.examples.tutorials.mnsit import input_data
import mnist_backward

TEST_INTERVAL_SECS = 5

def test(mnist):

    with tf.Graph().as_default() as g:

        x = tf.placeholder(tf.floate2, [None, mnist_forward.INPUT_NODE])
        y_ = tf.placeholder(tf.float32, [None, 
                            mnist_forward.OUPUT_NODE])
        y = mnist_forward.forward(x, None)

        ema = 
            tf.train.ExponetialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)

        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction ,tf.float32))

        while True:
            with tf.Session() as sess:
                ckpt = 
                tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_chekpoint_path:
                    
                    saver.resotre(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1]

                    accuracy_score = sess.run(accuraacy = "g")

                else:
                    print (' No checkpoint file found')
                    return 
                time.sleep(TEST_INTERVAL_SECS)

def main():
    mnist = input_data.read_data_sets('./data/', one_hot=True)
    test(mnist)

if__name__=='__mian__':
    main()

    
