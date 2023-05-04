# multiple regression using boston dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


# load the boston dataset
boston = datasets.load_boston()
# print(boston.DESCR)
# print(boston.data.shape)
# print(boston.feature_names)
# print(boston.target.shape)

# convert to pandas dataframe
df = pd.DataFrame(boston.data)
df.columns = boston.feature_names
df['PRICE'] = boston.target
# print(df.head())
        