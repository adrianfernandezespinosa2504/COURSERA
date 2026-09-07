# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:53:15 2026

@author: Adrian
"""


import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# generamos dataset
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# creamos el modelo
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# entrenamos el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# evaluamos el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# guardamos el modelo
model.save('my_cifar10_model.h5')

# cargamos modelo
# oaded_model = tf.keras.models.load_model('my_cifar10_model.h5')