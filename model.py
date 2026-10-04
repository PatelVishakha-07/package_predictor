import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

df = pd.read_csv("placement.csv")

x = df[["cgpa"]]
y = df[["package"]]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)

m = lr.coef_[0][0]
b = lr.intercept_[0]

print("Slope (m):", round(m, 3))
print("Intercept (b):", round(b, 3))
print("R2_Score:", round(r2_score(y_test, y_predict), 3))
print("Mean Absolute Error:", round(mean_absolute_error(y_test, y_predict), 3))

with open("model.pkl", "wb") as f:
    pickle.dump(lr, f)
print("model.pkl saved")