import pandas as pd
import numpy as np
import xgboost
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

df = pd.read_csv("C:/python/predict/dataset.csv")


def clean_square(df, a):
    for j in range(len(a)):
        for i in range(len(df.index) - 1):
            try:
                df.iloc[i, a[j]] = float(df.iloc[i, a[j]])
            except ValueError:
                df.iloc[i, a[j]] = "0";
                df.iloc[i, a[j]] = float(df.iloc[i, a[j]])
        temp = df['square' + str(a[j])].astype(float)
        df['square' + str(a[j])] = temp
        temp = []


to_clean = [1, 2, 3]  # индексы столбцов, которые чистим ниже
clean_square(df, to_clean)
df['type_house'].fillna('no_info', inplace=True)
df.fillna(0, inplace=True)


le = LabelEncoder()
cat = ['type_house', 'state', 'dist']
for x in cat:
    df[x] = le.fit_transform(df[x].astype(str))
 


df_s = df.drop(['Unnamed: 0', 'currency', 'value'], axis=1)

X = []
temp = []
y = np.array(df['value'])
for x in range(len(df.index)):  # создаем матрицу на вход для модели
    for l in df_s.columns.values:
        temp.append(float(df_s.loc[x][l]))
    X.append(temp)
    temp = []

X = np.array(X)

xgb_r = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                             colsample_bytree=1, max_depth=7)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
xgb_r.fit(X_train, y_train)
pred = xgb_r.predict(X_test)



