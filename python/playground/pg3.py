# Author: Issam H. Laradji
# License: BSD 3 clause

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
import pymysql

import decimal
decimals = [
  decimal.Decimal('0.0008'),
  decimal.Decimal('11.1111'),
  decimal.Decimal('222.2222'),
  decimal.Decimal('3333.3333'),
  decimal.Decimal('1234.5678'),
]
for dec in decimals:
  print(str(dec))