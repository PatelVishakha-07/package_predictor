import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"D:\MCA\Sem_3\Machine Learning\Practicals\placement.csv")

x = df["cgpa"]
y = df["package"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)

m = lr.coef_
b = lr.intercept_

a