# -*- coding: utf-8 -*-
"""T20 World cup circket score predictor.ipyb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xu5M_nCtqJzSh5PwUQSpikdOx14Wlf-0
"""

# Commented out IPython magic to ensure Python compatibility.

import warnings
# %matplotlib inline 
warnings.filterwarnings('ignore')
import pickle

final_df = pickle.load(open('E:\\germany\\final ML end to end project\\T20 World cup Score Predictor\\python code for web application\\final_df.pkl','rb'))

X = final_df.drop(columns = ['runs_x'])
y = final_df['runs_x']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 1)

#X_train

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score,mean_absolute_error

trf = ColumnTransformer([
    ('trf',OneHotEncoder(sparse = False,drop = 'first'),['batting_team','bowling_team','city'])
]
,remainder = 'passthrough')

# Randomforest gives good but XGB is more good
pipe = Pipeline(steps = [
    ('step1',trf),
    ('step2',StandardScaler()),
    ('step3',XGBRegressor(n_estimators=1000,learning_rate=0.2,max_depth = 12,random_state=1))
])

# it will take almost 6 mins to run
pipe.fit(X_train,y_train)
y_pred = pipe.predict(X_test)
print(r2_score(y_test,y_pred))
print(mean_absolute_error(y_test,y_pred))

pickle.dump(pipe,open('pipe.pkl','wb'))



