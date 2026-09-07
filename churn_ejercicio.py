# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:39:28 2026

@author: Adrian
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# cargamos dataset
data = pd.read_csv('customer_churn.csv')

# ojeamos el dataset
print(data.head())
print(data.info())

# preprocesamos los datos
data = data.drop(columns=['CustomerID']) #Simplify the dataset
data = data.dropna()  # dropping missing values

data = pd.get_dummies(data, drop_first=True) # para codificar variables no numericas

# dividimos el dataset para entrenamiento y testing
X = data.drop('Churn', axis=1)
y = data['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# desarrollamos y entrenamos el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# validamos el modelo
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'Test accuracy: {test_acc}')

# NUEVO: optimizamos para el despliegue
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# guardamos el modelo
model.save('churn_model.h5')

'''
El resultado del modelo no es fiable — y es normal

Test accuracy: 0.0

Esto se debe a que tu dataset tiene solo 5 filas (RangeIndex: 5 entries, 0 to 4). Al dividir con test_size=0.2, te quedas con 4 filas para entrenar y 1 sola para test. Con esos números:

El modelo memoriza literalmente el training set (por eso accuracy: 1.0000 en el último epoch de entrenamiento).
Con una única muestra de test, el resultado (0% o 100%) es prácticamente una moneda al aire, no una medida real de rendimiento.
'''