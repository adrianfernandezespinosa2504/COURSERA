# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:00:24 2026

@author: Adrian
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:00:24 2026
@author: Adrian
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import missingno as msno
from scipy import stats

df = pd.read_csv('C:/Users/Adrian/Desktop/SPYDER/COURSERA/dataset_practica.csv')
#Comprobamos dataset correcto
print(df.head())

##MISSING DATA
msno.matrix(df)
msno.heatmap(df)
df_cleaned = df.dropna()
df_filled = df.fillna(df.mean(numeric_only=True))  

##OUTLIERS 
cols_numericas = df_cleaned.select_dtypes(include=[np.number]).columns  #(solo columnas numéricas)
z_scores = np.abs(stats.zscore(df_cleaned[cols_numericas]))
df_no_outliers = df_cleaned[(z_scores < 3).all(axis=1)] # any rows with Z-scores greater than three are considered outliers

##NORMALISING (solo columnas numéricas, guardando 'departamento' aparte)
scaler = MinMaxScaler()
df_scaled = df_no_outliers.copy()  # <-- FIX 3: partimos de una copia con todas las columnas
df_scaled[cols_numericas] = scaler.fit_transform(df_no_outliers[cols_numericas])

scaler = StandardScaler()
df_standardized = df_no_outliers.copy()
df_standardized[cols_numericas] = scaler.fit_transform(df_no_outliers[cols_numericas])

##TRANSFORMING
df_encoded = pd.get_dummies(df_scaled, columns=['departamento'])

##SAVING
df_encoded.to_csv('C:/Users/Adrian/Desktop/SPYDER/COURSERA/cleaned_preprocessed_data.csv', index=False)
print('Data cleaning and preprocessing complete. File saved as cleaned_preprocessed_data.csv')


'''
Para automatizar;

def load_data(filepath):
    return pd.read_csv(filepath)

def handle_missing_values(df):
    return df.fillna(df.mean())

def remove_outliers(df):
    z_scores = np.abs(stats.zscore(df))
    return df[(z_scores < 3).all(axis=1)]

def scale_data(df):
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

def encode_categorical(df, categorical_columns):
    return pd.get_dummies(df, columns=categorical_columns)

def save_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)

# Example usage:
df = load_data('your_dataset.csv')
df = handle_missing_values(df)
df = remove_outliers(df)
df = scale_data(df)
df = encode_categorical(df, ['categorical_column_name'])
save_data(df, 'cleaned_preprocessed_data.csv')

'''
