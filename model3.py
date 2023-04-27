import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


df = pd.read_csv('cardio_train.csv',sep=";")
x_data = df.iloc[:, 1:12]
y = df.iloc[:, -1]

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_data,y)

pickle.dump(rf, open('model3.pkl','wb'))
