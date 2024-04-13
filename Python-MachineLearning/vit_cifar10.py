import tensorflow as tf
import keras
from keras import layers
from keras.losses import SparseCategoricalCrossentropy
from keras.optimizers import Adam

(x_train, y_train), (x_train, y_test) = keras.datasets.cifar10.load_data()

n_class = 10
img_size = (32, 32, 3)

patch_size = 4
p2=(img_size[0]//patch_size)**2

d_model = 64
h, N = 8, 6

class Patches(layers.Layer):
    def __init__(self, patch_size):
        super(Patches, self).__init__()
        self.p_siz = patch_size


    def call(self, img):
        batch_size = tf.shape(img)[0]
        patches = tf.image.extract_patches(images=img, 
                                           sizes=[1, self.p_siz, self.p_siz, 1], 
                                           strides=[1, self.p_siz, self.p_siz, 1],
                                           rates=[1, 1, 1, 1],
                                           padding="VALID")
        patch_dims=patches.shape[-1]
        patches=tf.reshape(patches, [batch_size, -1, patch_dims])
        return patches


class PatchEncoder(layers.Layer):
    def __init__(self, p2, d_model):