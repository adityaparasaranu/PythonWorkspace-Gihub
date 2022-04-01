import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

food_data = pd.read_csv("food_data.csv")

food_list = ["carbohydrate", "proteins", "fat", "vitaminsAndMinerals"]
input_set = ["age", "gender", "occupation"]
X = food_data.drop(columns=food_list)
y = food_data.drop(columns=input_set)

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "food_model.joblib")