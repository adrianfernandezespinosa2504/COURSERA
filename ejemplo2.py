# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:58:17 2026

@author: Adrian
"""

import pandas as pd
import numpy as np
import funciones as fn

# Create a dummy dataset
np.random.seed(0)
dummy_data = {
    'Feature1': np.random.normal(100, 10, 100).tolist() + [np.nan, 200],  # Normally distributed with an outlier
    'Feature2': np.random.randint(0, 100, 102).tolist(),  # Random integers
    'Category': ['A', 'B', 'C', 'D'] * 25 + [np.nan, 'A'],  # Categorical with some missing values
    'Target': np.random.choice([0, 1], 102).tolist()  # Binary target variable
}

# Convert the dictionary to a pandas DataFrame
df_dummy = pd.DataFrame(dummy_data)

# Display the first few rows of the dummy dataset
print(df_dummy.head())


# Load the data
df_preprocessed = df_dummy.copy()

# Handle missing values
df_preprocessed = fn.handle_missing_values(df_preprocessed)
print('Missing values:\n', df_preprocessed.isnull().sum())


# Remove outliers
df_preprocessed = fn.remove_outliers(df_preprocessed)
print('Outliers:\n', df_preprocessed.describe())

# Scale the data
df_preprocessed = fn.scale_data(df_preprocessed)
print('Scaled data:\n', df_preprocessed.head())

# Encode categorical variables
df_preprocessed = fn.encode_categorical(df_preprocessed, ['Category'])
print('Encoded data:\n', df_preprocessed.columns)


# Display the preprocessed data, miramos como esta el dataset
print('\nFinal dataset:\n', df_preprocessed.head())


# Save the cleaned and preprocessed DataFrame to a CSV file
fn.save_data(df_preprocessed, 'preprocessed_dummy_data_ejemplo_2.csv')

print('Preprocessing complete. Preprocessed data saved as preprocessed_dummy_data_ejemplo_2.csv')