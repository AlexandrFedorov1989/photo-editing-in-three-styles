import os

import hub as hub
import tensorflow as tf
import tensorflow_hub as hub

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
import numpy as np
from PIL import Image
import random


def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return Image.fromarray(tensor)


def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim
    new_shape = tf.cast(shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img





# Это функция, в которую передаётся только путь к файлу пользователя(в нашем случае - переменная content_image), возвращает обработанное фото
# Simpsons
def magic_S(path):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(tf.constant(path), tf.constant(
        load_img('/home/alexandr/bot_risovach/Simpsons/' + str(random.randint(1, 50)) + '.jpg')))[0]
    stylized_image = tensor_to_image(stylized_image)
    stylized_image.save('result.png')
    return stylized_image


# Dali
def magic_D(path):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(tf.constant(path), tf.constant(
        load_img('/home/alexandr/bot_risovach/Dali/' + str(random.randint(1, 50)) + '.jpg')))[0]
    stylized_image = tensor_to_image(stylized_image)
    stylized_image.save('result.png')
    return stylized_image


# VanGogh
def magic_V(path):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(tf.constant(path), tf.constant(
        load_img('/home/alexandr/bot_risovach/VanGogh/' + str(random.randint(1, 50)) + '.jpg')))[0]
    stylized_image = tensor_to_image(stylized_image)
    stylized_image.save('result.png')
    return stylized_image


