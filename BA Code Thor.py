import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression

player_data = pd.read_csv('player_data.csv')
player_data.columns


h_data = pd.read_csv('hollingersStats.csv')
pd.set_option('display.max_columns', None)

m_data = h_data.merge(player_data, left_on = 'player', right_on = 'name')
m_data

m_data.drop('name',axis = 1, inplace = True)