# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:42:16 2026

@author: Adrian
"""
from setuptools import setup, find_packages

setup(
    name='my_model_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.2',
        'pandas==1.3.3',
        'scikit-learn==0.24.2',
        'tensorflow==2.6.0'
    ],
    scripts=['scripts/preprocess.py', 'scripts/postprocess.py']
)