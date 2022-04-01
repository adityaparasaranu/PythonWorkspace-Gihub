import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv("music.csv")

X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()

# This function takes in 2 arguments, that is input set and the output set for predictions
model.fit(X, y)

# This function takes a 2 dimensional array, i.e [ ["aditya"] ] This should be the
# input set and it returns the prediction
prediction = model.predict( [ [21, 1], [22, 0] ] )
print(prediction)
