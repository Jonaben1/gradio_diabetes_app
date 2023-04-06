import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


df = pd.read_csv('diabetes.csv')

# defining the target variable
X = df.drop(['outcome'], axis=True)
y = df.outcome


# spliting the data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)

model = LogisticRegression(max_iter=1000)
model.fit(x_train.values, y_train.values)

preds = model.predict(x_test.values)

joblib.dump(model, 'lg_model.pkl')


