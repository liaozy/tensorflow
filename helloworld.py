import tensorflow as tf

# hello=tf.constant("hello, tensorflow")
# sess=tf.Session()
# print sess.run(hello)

import tensorflow.models.image.cifar10.cifar10 as cifar10
cifar10.maybe_download_and_extract()
images, labels = cifar10.distorted_inputs()
print images
print labels